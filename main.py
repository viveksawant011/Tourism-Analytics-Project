from src.data_loader import load_data
from src.visualizations import (
    line_chart,
    bar_chart,
    heatmap,
    scatter_tiktok,
    scatter_instagram,
    combo_co2,
    scatter_google
)
from src.analysis import print_kpis

# Load dataset
df = load_data("data/Tourism_Impact_Analytics_Dataset.csv")

# KPIs
print_kpis(df)

# Charts
line_chart(df)
bar_chart(df)
heatmap(df)
scatter_tiktok(df)
scatter_instagram(df)
combo_co2(df)
scatter_google(df)