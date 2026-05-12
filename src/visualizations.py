import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

PALETTE = "viridis"
SEASON_PALETTE = {
    "Winter": "#4C78A8",
    "Spring": "#F58518",
    "Summer": "#54A24B",
    "Autumn": "#E45756"
}

# Global font styling
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.labelsize"] = 12
plt.rcParams["figure.titlesize"] = 16

def line_chart(df):
    plt.figure(figsize=(10,5))
    plt.plot(df["month_year"], df["visitors_total"])
    plt.title("Visitors Trend")
    plt.xticks(rotation=45)
    plt.savefig("outputs/charts/line_chart.png", dpi=300, bbox_inches="tight")
    plt.show()
    
def bar_chart(df):
    season_data = df.groupby("Season")["visitors_total"].sum().reset_index()
    season_data = season_data.sort_values("visitors_total", ascending=False)

    plt.figure(figsize=(8,5))

    sns.barplot(
        data=season_data,
        x="Season",
        y="visitors_total",
        palette=[SEASON_PALETTE[s] for s in season_data["Season"]]
    )

    plt.title("Total Visitors by Season")
    plt.xlabel("Season")
    plt.ylabel("Visitors")
    plt.savefig("outputs/charts/bar_chart.png", dpi=300, bbox_inches="tight")
    plt.show()
    
def heatmap(df):
    pivot = df.pivot_table(
        values="visitors_total",
        index="Season",
        columns=df["month_year"].dt.year,
        aggfunc="sum"
    )

    plt.figure(figsize=(8,5))

    sns.heatmap(
        pivot,
        cmap="YlOrRd",
        annot=True,
        fmt=".0f",
        linewidths=0.5
    )

    plt.title("Seasonality Heatmap")
    plt.savefig("outputs/charts/heatmap.png", dpi=300, bbox_inches="tight")
    plt.show()
    
def scatter_tiktok(df):
    plt.figure(figsize=(7,5))

    sns.scatterplot(
        data=df,
        x="tiktok_views_millions",
        y="visitors_total",
        hue="Season",
        palette=SEASON_PALETTE,
        alpha=0.7,
        edgecolor="black"
    )

    sns.regplot(
        data=df,
        x="tiktok_views_millions",
        y="visitors_total",
        scatter=False,
        color="black"
    )

    plt.title("TikTok Views vs Visitors")
    plt.xlabel("TikTok Views (Millions)")
    plt.ylabel("Visitors")

    plt.legend(title="Season")
    plt.savefig("outputs/charts/scatter_tiktok.png", dpi=300, bbox_inches="tight")
    plt.show()
    
def scatter_instagram(df):
    sns.scatterplot(
        x=df["ig_posts_count"],
        y=df["visitors_total"],
        hue=df["Season"]
    )

    sns.regplot(
        x=df["ig_posts_count"],
        y=df["visitors_total"],
        scatter=False,
        color="black"
    )

    plt.title("Instagram vs Visitors")
    plt.savefig("outputs/charts/scatter_instagram.png", dpi=300, bbox_inches="tight")
    plt.show()
    
def combo_co2(df):
    fig, ax1 = plt.subplots(figsize=(10,5))

    ax1.bar(
        df["month_year"],
        df["visitors_total"],
        color="#4C78A8",
        alpha=0.7
    )
    ax1.set_ylabel("Visitors")

    ax2 = ax1.twinx()
    ax2.plot(
        df["month_year"],
        df["total_co2_tons"],
        color="#E45756",
        marker="o",
        linewidth=2
    )
    ax2.set_ylabel("CO₂ Emissions")

    plt.title("Visitors vs CO₂ Emissions")
    plt.xticks(rotation=45)
    plt.savefig("outputs/charts/combo_co2.png", dpi=300, bbox_inches="tight")
    plt.show()

def scatter_google(df):
    sns.scatterplot(
        x=df["google_trends_index"],
        y=df["visitors_total"],
        hue=df["Season"]
    )

    sns.regplot(
        x=df["google_trends_index"],
        y=df["visitors_total"],
        scatter=False,
        color="black"
    )

    plt.title("Google Trends vs Visitors")
    plt.savefig("outputs/charts/scatter_google.png", dpi=300, bbox_inches="tight")
    plt.show()