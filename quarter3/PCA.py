"""
PCA Analysis: UN Population Growth & Health Indicators
=======================================================
Dataset: Population growth and indicators of fertility and mortality
Source:  United Nations (264 countries/areas, years 2010–2022)

Features analysed (7 indicators):
  - Population annual rate of increase (%)
  - Total fertility rate (children per woman)
  - Infant mortality for both sexes (per 1,000 live births)
  - Maternal mortality ratio (deaths per 100,000 population)
  - Life expectancy at birth – both sexes, males, females (years)
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer

# ── Configuration ──────────────────────────────────────────────────────────────
DATA_PATH = "T03.csv"  # path to the uploaded CSV
YEAR_FOCUS = 2020  # year used for the main PCA snapshot

FEATURES = [
    "Population annual rate of increase (percent)",
    "Total fertility rate (children per women)",
    "Infant mortality for both sexes (per 1,000 live births)",
    "Maternal mortality ratio (deaths per 100,000 population)",
    "Life expectancy at birth for both sexes (years)",
    "Life expectancy at birth for males (years)",
    "Life expectancy at birth for females (years)",
]

SHORT_LABELS = [
    "Pop. growth",
    "Fertility rate",
    "Infant mortality",
    "Maternal mortality",
    "Life exp. (both)",
    "Life exp. (male)",
    "Life exp. (female)",
]

# ── 1. Load & reshape ──────────────────────────────────────────────────────────
raw = pd.read_csv(DATA_PATH, header=1)
raw.columns = ["ID", "Country", "Year", "Series", "Value", "Footnotes", "Source"]
raw["Value"] = pd.to_numeric(raw["Value"], errors="coerce")


# Pivot: rows = country, columns = Series (for a given year)
def make_pivot(df, year):
    subset = df[df["Year"] == year]
    pivot = subset.pivot_table(
        index=["ID", "Country"], columns="Series", values="Value", aggfunc="mean"
    ).reset_index()
    pivot.columns.name = None
    return pivot


pivot_all = make_pivot(raw, YEAR_FOCUS)

# Keep only the 7 feature columns that are present
available = [f for f in FEATURES if f in pivot_all.columns]
meta = pivot_all[["ID", "Country"]].copy()
data = pivot_all[available].copy()

# ── 2. Impute & scale ─────────────────────────────────────────────────────────
imputer = SimpleImputer(strategy="median")
X_imp = imputer.fit_transform(data)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imp)

# ── 3. PCA – full (all components) ────────────────────────────────────────────
pca_full = PCA()
pca_full.fit(X_scaled)

explained = pca_full.explained_variance_ratio_
cumulative = np.cumsum(explained)
n_components = len(explained)

for i, (ev, cum) in enumerate(zip(explained, cumulative), 1):
    bar = "█" * int(ev * 40)

# Determine how many PCs explain ≥90 % variance
n_90 = int(np.argmax(cumulative >= 0.90)) + 1

# ── 4. PCA – reduced (2 components for visualisation) ─────────────────────────
pca2 = PCA(n_components=2)
X_pca = pca2.fit_transform(X_scaled)

scores = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
scores["Country"] = meta["Country"].values

# ── 5. Loadings ───────────────────────────────────────────────────────────────
loadings = pd.DataFrame(
    pca2.components_.T,
    index=SHORT_LABELS[:len(available)],
    columns=["PC1", "PC2"]
)
# ── 6. Top / bottom countries on PC1 ──────────────────────────────────────────
top_n = 8
top_pc1 = scores.nlargest(top_n, "PC1")[["Country", "PC1", "PC2"]]
bottom_pc1 = scores.nsmallest(top_n, "PC1")[["Country", "PC1", "PC2"]]

# ── 7. Visualisation ──────────────────────────────────────────────────────────
fig = plt.figure(figsize=(18, 13))
fig.patch.set_facecolor("#0f1117")

gs = GridSpec(2, 3, figure=fig, hspace=0.40, wspace=0.38)
ax2 = fig.add_subplot(gs[0, 1:])  # biplot / scatter
ax3 = fig.add_subplot(gs[1, :2])  # loading heatmap
ax4 = fig.add_subplot(gs[1, 2])  # top/bottom bar chart

BG = "#0f1117"
CARD = "#1a1d27"
ACC1 = "#7c6af7"  # purple
ACC2 = "#4eadf5"  # blue
ACC3 = "#f7706a"  # red/salmon
GOLD = "#f5c842"
GREY = "#8b90a0"
WHITE = "#e8eaf0"

for ax in [ax2, ax3, ax4]:
    ax.set_facecolor(CARD)
    for spine in ax.spines.values():
        spine.set_color("#2e3248")


def title(ax, text):
    ax.set_title(text, color=WHITE, fontsize=12, fontweight="bold", pad=10)

# — 7b. Biplot (scatter + loading arrows) ──────────────────────────────────────
sc = ax2.scatter(scores["PC1"], scores["PC2"],
                 alpha=0.55, s=22, c=scores["PC1"],
                 cmap="coolwarm", edgecolors="none", zorder=2)

# Overlay top/bottom extreme countries
highlight = pd.concat([top_pc1.head(3), bottom_pc1.head(3)])
for _, row in highlight.iterrows():
    ax2.scatter(row["PC1"], row["PC2"], s=60, color=GOLD,
                edgecolors=WHITE, linewidths=0.6, zorder=4)
    ax2.text(row["PC1"] + 0.08, row["PC2"], row["Country"],
             color=GOLD, fontsize=7, va="center", zorder=5)

# Loading arrows (scaled)
scale = 3.5
for (feat, row_l), short in zip(loadings.iterrows(), SHORT_LABELS):
    x, y = row_l["PC1"] * scale, row_l["PC2"] * scale
    ax2.annotate("", xy=(x, y), xytext=(0, 0),
                 arrowprops=dict(arrowstyle="->", color=ACC2, lw=1.5), zorder=3)
    ax2.text(x * 1.08, y * 1.08, short, color=ACC2, fontsize=7.5,
             ha="center", va="center", zorder=3)

ax2.axhline(0, color="#2e3248", linewidth=0.8)
ax2.axvline(0, color="#2e3248", linewidth=0.8)
ax2.set_xlabel(f"PC1  ({pca2.explained_variance_ratio_[0] * 100:.1f}%)", color=GREY, fontsize=9)
ax2.set_ylabel(f"PC2  ({pca2.explained_variance_ratio_[1] * 100:.1f}%)", color=GREY, fontsize=9)
ax2.tick_params(colors=GREY, labelsize=8)
cbar = fig.colorbar(sc, ax=ax2, pad=0.01)
cbar.ax.yaxis.set_tick_params(color=GREY, labelsize=7)
plt.setp(cbar.ax.yaxis.get_ticklabels(), color=GREY)
cbar.set_label("PC1 score", color=GREY, fontsize=8)
title(ax2, f"Biplot — PC1 vs PC2  (year {YEAR_FOCUS})")

# — 7c. Loading heatmap ────────────────────────────────────────────────────────
load_arr = loadings.values
im = ax3.imshow(load_arr.T, cmap="RdBu_r", vmin=-1, vmax=1, aspect="auto")

ax3.set_xticks(range(len(SHORT_LABELS[:len(available)])))
ax3.set_xticklabels(SHORT_LABELS[:len(available)], rotation=30, ha="right",
                    color=WHITE, fontsize=8)
ax3.set_yticks([0, 1])
ax3.set_yticklabels(["PC1", "PC2"], color=WHITE, fontsize=9)
for i in range(load_arr.shape[0]):
    for j in range(load_arr.shape[1]):
        ax3.text(i, j, f"{load_arr[i, j]:+.2f}", ha="center", va="center",
                 color="white" if abs(load_arr[i, j]) > 0.5 else BG, fontsize=8)
fig.colorbar(im, ax=ax3, orientation="horizontal", pad=0.22, fraction=0.04,
             label="Loading").ax.xaxis.label.set_color(GREY)
title(ax3, "Feature Loadings Heatmap")

# — 7d. Top/Bottom countries bar ───────────────────────────────────────────────
n_show = 6
combined = pd.concat([
    top_pc1.head(n_show).assign(group="High PC1"),
    bottom_pc1.head(n_show).assign(group="Low PC1")
])
colors = [ACC1] * n_show + [ACC3] * n_show
y_pos = range(len(combined))
h_bars = ax4.barh(list(y_pos), combined["PC1"].values,
                  color=colors, alpha=0.85, edgecolor="none", height=0.65)
ax4.set_yticks(list(y_pos))
ax4.set_yticklabels(combined["Country"].values, color=WHITE, fontsize=7.5)
ax4.axvline(0, color=GREY, linewidth=0.8)
ax4.set_xlabel("PC1 Score", color=GREY, fontsize=9)
ax4.tick_params(colors=GREY, labelsize=8)

patch_hi = mpatches.Patch(color=ACC1, label="High PC1")
patch_lo = mpatches.Patch(color=ACC3, label="Low PC1")
ax4.legend(handles=[patch_hi, patch_lo], fontsize=8, labelcolor=WHITE,
           facecolor=CARD, edgecolor=CARD)
title(ax4, f"Extreme Countries on PC1")

# — Main title ─────────────────────────────────────────────────────────────────
fig.suptitle(
    "PCA of UN Demographic Indicators  ·  264 Countries",
    color=WHITE, fontsize=15, fontweight="bold", y=0.98
)
plt.show()