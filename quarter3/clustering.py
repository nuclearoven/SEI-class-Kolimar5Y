import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
from matplotlib.lines import Line2D

from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from scipy.spatial.distance import pdist

# ── Configuration ──────────────────────────────────────────────────────────────
DATA_PATH  = "T03.csv"
YEAR_FOCUS = 2020
N_CLUSTERS = 4          # override with None to auto-pick from dendrogram gap
RANDOM_STATE = 42

FEATURES = [
    "Population annual rate of increase (percent)",
    "Total fertility rate (children per women)",
    "Infant mortality for both sexes (per 1,000 live births)",
    "Maternal mortality ratio (deaths per 100,000 population)",
    "Life expectancy at birth for both sexes (years)",
    "Life expectancy at birth for males (years)",
    "Life expectancy at birth for females (years)",
]
SHORT = [
    "Pop. growth", "Fertility", "Infant mort.",
    "Maternal mort.", "Life exp. (all)",
    "Life exp. (M)", "Life exp. (F)",
]


raw = pd.read_csv(DATA_PATH, header=1)
raw.columns = ["ID", "Country", "Year", "Series", "Value", "Footnotes", "Source"]
raw["Value"] = pd.to_numeric(raw["Value"], errors="coerce")

subset = raw[raw["Year"] == YEAR_FOCUS]
pivot  = subset.pivot_table(
    index=["ID", "Country"], columns="Series", values="Value", aggfunc="mean"
).reset_index()
pivot.columns.name = None

available = [f for f in FEATURES if f in pivot.columns]
meta = pivot[["ID", "Country"]].copy()
data = pivot[available].copy()
# ── 2. Impute & scale ─────────────────────────────────────────────────────────
X = SimpleImputer(strategy="median").fit_transform(data)
X_scaled = StandardScaler().fit_transform(X)

# ── 3. Hierarchical clustering (Ward linkage) ──────────────────────────────────
Z = linkage(X_scaled, method="ward", metric="euclidean")

# Auto-detect k from largest dendrogram gap if N_CLUSTERS is None
last_merges   = Z[-20:, 2]          # last 20 merge distances
acceleration  = np.diff(last_merges, 2)
k_auto        = acceleration[::-1].argmax() + 2
k             = N_CLUSTERS if N_CLUSTERS else k_auto
hier_labels = fcluster(Z, k, criterion="maxclust") - 1   # 0-indexed

# ── 4. K-Means ────────────────────────────────────────────────────────────────
km = KMeans(n_clusters=k, random_state=RANDOM_STATE, n_init=20)
km_labels = km.fit_predict(X_scaled)

sil = silhouette_score(X_scaled, km_labels)
inertia = km.inertia_

inertias, sil_scores = [], []
K_range = range(2, 11)
for ki in K_range:
    km_i = KMeans(n_clusters=ki, random_state=RANDOM_STATE, n_init=10).fit(X_scaled)
    inertias.append(km_i.inertia_)
    sil_scores.append(silhouette_score(X_scaled, km_i.labels_))

# ── 5. PCA projection for visualisation ───────────────────────────────────────
pca2 = PCA(n_components=2, random_state=RANDOM_STATE)
X_pca = pca2.fit_transform(X_scaled)
var_explained = pca2.explained_variance_ratio_

scores = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
scores["Country"]   = meta["Country"].values
scores["KM_Cluster"] = km_labels
scores["H_Cluster"]  = hier_labels

# ── 6. Cluster profiles (mean feature values per cluster) ─────────────────────
scores_df = scores.copy()
feature_df = pd.DataFrame(X, columns=SHORT)   # unscaled, imputed
feature_df["KM_Cluster"] = km_labels
profiles = feature_df.groupby("KM_Cluster")[SHORT].mean()

# Country counts
counts = pd.Series(km_labels).value_counts().sort_index()

# Notable countries per cluster
for c in range(k):
    c_countries = scores[scores["KM_Cluster"] == c]["Country"].values
    sample = ", ".join(c_countries[:6])

# ── 7. Palette & figure ───────────────────────────────────────────────────────
BG, CARD = "#0f1117", "#1a1d27"
WHITE, GREY = "#e8eaf0", "#8b90a0"
CLUSTER_COLORS = ["#7c6af7", "#4eadf5", "#f7706a", "#4ecf8a",
                  "#f5c842", "#c77dff", "#ff9f40"][:k]

fig = plt.figure(figsize=(20, 16))
fig.patch.set_facecolor(BG)
gs = GridSpec(3, 3, figure=fig, hspace=0.45, wspace=0.38)

ax_dend  = fig.add_subplot(gs[0, :])    # full-width dendrogram
ax_pca   = fig.add_subplot(gs[1, 1:])  # PCA scatter
ax_bar   = fig.add_subplot(gs[2, :])   # cluster profile bar chart

def style(ax):
    ax.set_facecolor(CARD)
    for s in ax.spines.values():
        s.set_color("#2e3248")
    ax.tick_params(colors=GREY, labelsize=8)

for ax in [ax_dend, ax_pca, ax_bar]:
    style(ax)

def ftitle(ax, t):
    ax.set_title(t, color=WHITE, fontsize=11, fontweight="bold", pad=9)

# ── 7a. Dendrogram ────────────────────────────────────────────────────────────
# Use a colour threshold to highlight the chosen k clusters
color_threshold = Z[-(k-1), 2]

dend = dendrogram(
    Z,
    ax=ax_dend,
    truncate_mode="lastp",
    p=60,
    show_leaf_counts=True,
    leaf_rotation=90,
    leaf_font_size=6,
    color_threshold=color_threshold,
    above_threshold_color=GREY,
    no_labels=False,
)
ax_dend.axhline(color_threshold, color="#f5c842", linestyle="--",
                linewidth=1.5, label=f"Cut → k={k} clusters")
ax_dend.set_ylabel("Ward Distance", color=GREY, fontsize=9)
ax_dend.set_xlabel("Countries / merged groups  (leaf count in parentheses)",
                   color=GREY, fontsize=8)
ax_dend.legend(fontsize=9, labelcolor=WHITE, facecolor=CARD, edgecolor=CARD)
ftitle(ax_dend, f"Hierarchical Dendrogram  (Ward linkage, truncated to 60 leaves)")

# Recolour dendrogram lines to match cluster palette
leaf_colors = [CLUSTER_COLORS[l] for l in hier_labels]
for coll in ax_dend.collections:
    coll.set_color(GREY)

# ── 7c. PCA scatter coloured by K-Means cluster ───────────────────────────────
for ci in range(k):
    mask = scores["KM_Cluster"] == ci
    ax_pca.scatter(
        scores.loc[mask, "PC1"], scores.loc[mask, "PC2"],
        c=CLUSTER_COLORS[ci], s=30, alpha=0.75,
        edgecolors="none", label=f"Cluster {ci+1}  (n={mask.sum()})"
    )

# Annotate a handful of notable countries per cluster
notables = {0: 3, 1: 3, 2: 3, 3: 3}
for ci in range(k):
    sub = scores[scores["KM_Cluster"] == ci].nlargest(notables.get(ci, 3), "PC1")
    for _, row in sub.iterrows():
        ax_pca.annotate(row["Country"], (row["PC1"], row["PC2"]),
                        fontsize=6.5, color=CLUSTER_COLORS[ci],
                        xytext=(4, 2), textcoords="offset points")

ax_pca.axhline(0, color="#2e3248", linewidth=0.7)
ax_pca.axvline(0, color="#2e3248", linewidth=0.7)
ax_pca.set_xlabel(f"PC1  ({var_explained[0]*100:.1f}% variance)", color=GREY, fontsize=9)
ax_pca.set_ylabel(f"PC2  ({var_explained[1]*100:.1f}% variance)", color=GREY, fontsize=9)
ax_pca.legend(fontsize=8, labelcolor=WHITE, facecolor=CARD, edgecolor=CARD,
              loc="upper left")
ftitle(ax_pca, f"K-Means Clusters in PCA Space  (k={k}, sil={sil:.2f})")

# ── 7d. Cluster profile grouped bar chart ─────────────────────────────────────
n_feat  = len(SHORT)
x       = np.arange(n_feat)
width   = 0.8 / k

for ci in range(k):
    offset = (ci - k/2 + 0.5) * width
    vals   = profiles.loc[ci, SHORT].values
    bars   = ax_bar.bar(x + offset, vals, width * 0.9,
                        color=CLUSTER_COLORS[ci], alpha=0.85,
                        label=f"Cluster {ci+1}", edgecolor="none")

ax_bar.set_xticks(x)
ax_bar.set_xticklabels(SHORT, rotation=25, ha="right", color=WHITE, fontsize=8.5)
ax_bar.set_ylabel("Mean value (original units)", color=GREY, fontsize=9)
ax_bar.axhline(0, color="#2e3248", linewidth=0.7)
ax_bar.legend(fontsize=8, labelcolor=WHITE, facecolor=CARD, edgecolor=CARD,
              ncol=k)
ftitle(ax_bar, "Cluster Profiles — Mean Feature Values per Cluster")

# ── Main title ────────────────────────────────────────────────────────────────
fig.suptitle(
    f"Hierarchical & K-Means Clustering of UN Demographic Indicators  ·  {YEAR_FOCUS}",
    color=WHITE, fontsize=14, fontweight="bold", y=0.99
)
plt.show()