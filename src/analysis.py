def print_kpis(df):
    print("Total Visitors:", df["visitors_total"].sum())
    print("Total Revenue:", df["hotel_revenue_eur"].sum())
    print("Total CO2:", df["total_co2_tons"].sum())
    print("Avg Occupancy:", df["hotel_occupancy_rate"].mean())