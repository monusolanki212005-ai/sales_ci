import pandas as pd
def analyse_sales(file_path="data/sales.csv"):
    """load the sales data and calculate revenue metrics"""
    df = pd.read_csv(file_path)
    required_columns = {"Date", "Product", "Category", "Quantity", "Price"}

    if not required_columns.issubset(df.columns):
        raise ValueError(f"Missing required columns: {required_columns - set(df.columns)}")

    df["Date"] = pd.to_datetime(df["Date"], errors='raise')
    df["Revenue"] = df["Quantity"] * df["Price"]

    total_revenue = df["Revenue"].sum()
    product_revenue = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
    

    return df,total_revenue, product_revenue

if __name__ == "__main__":
    df, total_revenue, product_revenue = analyse_sales()
    print(f"Total Revenue: {total_revenue}")
    print("Revenue by Product:")
    print(product_revenue)