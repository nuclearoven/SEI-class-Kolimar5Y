import openpyxl as xl
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
# Note: Ensure the file path is accessible in your environment
data = pd.read_csv(r"filtrovanie_maraton.csv")

def occurences(kat, val):
    """
    Counts the number of times a specific value appears in a dataframe column.

    Args:
        kat (str): The column name to search in.
        val: The specific value to count.

    Returns:
        int: Total number of occurrences.
    """
    return data[kat].value_counts().get(val, 0)

def umiestnenie(kat, um):
    """
    Filters the main dataset for rows where a specific category matches a value.

    Args:
        kat (str): The column name to filter by.
        um: The value to match (e.g., a specific category or surname).

    Returns:
        pd.DataFrame: A filtered subset of the data.
    """
    return data[data[kat] == um]

# Count entries with missing "Strata" (Gap) data
a = 0
for i in data["Strata"]:
    if i == "---":
        a += 1

def thelastthing(data):
    """
    Generates a scatter and line plot showing the progression of mean times
    at different race milestones for each runner category.

    Args:
        data (pd.DataFrame): The marathon dataset.
    """
    graph_data = data.copy()
    # Columns we want
    time_cols = ['10 km', '21,1 km', '31,1 km', 'Čas']

    # Convert time columns to minutes
    for col in time_cols:
        graph_data[col] = pd.to_timedelta(graph_data[col], errors="coerce").dt.total_seconds() / 60

    # Compute mean time per category
    mean_times = graph_data.groupby("Kategórie")[time_cols].mean().reset_index()

    # Reshape for seaborn
    mean_long = mean_times.melt(
        id_vars="Kategórie",
        value_vars=time_cols,
        var_name="Distance",
        value_name="Mean Time (minutes)"
    )

    # Keep correct order on x-axis
    order = ['10 km', '21,1 km', '31,1 km', 'Čas']
    mean_long["Distance"] = pd.Categorical(mean_long["Distance"], categories=order, ordered=True)

    # Plot
    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=mean_long,
        x="Distance",
        y="Mean Time (minutes)",
        hue="Kategórie",
        s=80
    )

    sns.lineplot(
        data=mean_long,
        x="Distance",
        y="Mean Time (minutes)",
        hue="Kategórie",
        legend=False
    )

    plt.xticks(rotation=45)
    plt.title("Average Intermediate Times per Category")
    plt.xlabel("Distance")
    plt.ylabel("Mean Time (minutes)")
    plt.tight_layout()
    plt.show()

def timetosec(kat_list):
    """
    Converts finishing times (Čas) into minutes for specific categories.

    Args:
        kat_list (list): A list of category names (e.g., ['M hlavná kategória']).

    Returns:
        dict: A dictionary where keys are category names and values are Series of times in minutes.
    """
    categories = {}
    for i in kat_list:
        filtered_cat = umiestnenie("Kategórie", i)
        minutes = pd.to_timedelta(filtered_cat["Čas"], errors="coerce").dt.total_seconds() / 60
        categories[i] = minutes
    return categories

# Main Execution
kat = data["Kategórie"].unique()

# Kernel Density Estimate (KDE) Plot with highlighting a specific runner
sns.kdeplot(data=pd.DataFrame(timetosec(kat)), fill=True, common_norm=False, alpha=0.1)
plt.xlabel("Time in minutes")
szekely_time = umiestnenie("Priezvisko", "SZÉKELY")["Čas"].apply(lambda x: pd.to_timedelta(x, errors="coerce").total_seconds() / 60).iloc[0]
plt.axvline(szekely_time, color="red", label="Ondro Szekeli", zorder=99)
plt.text(szekely_time, 0.02, "Ondro Szekeli", rotation=90, color="red")
plt.title("Time Distribution by Category")
plt.show()

# Boxplot with specific runner highlight
sns.boxplot(data=pd.DataFrame(timetosec(kat)), orient="h")
plt.scatter(szekely_time, "M hlavná kategória", s=100, color="red", label="Ondro Szekeli", zorder=99)
plt.title("Time Variance per Category")
plt.show()

# Violin plot with specific runner highlight
sns.violinplot(data=pd.DataFrame(timetosec(kat)), orient="h")
plt.xlabel("Time in minutes")
plt.ylabel("Category")
plt.scatter(szekely_time, "M hlavná kategória", s=100, color="red", label="Ondro Szekeli", zorder=99)
plt.title("Density and Distribution (Violin Plot)")
plt.show()