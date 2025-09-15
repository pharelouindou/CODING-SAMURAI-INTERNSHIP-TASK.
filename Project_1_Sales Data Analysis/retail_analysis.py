import pandas as pd
import matplotlib.pyplot as plt

def load_and_clean_data(filepath):
    df = pd.read_excel(filepath)
    return df.dropna()

def display_sales_statistics(df):
    print("Résumé des ventes:")
    print(f"Ventes totales: {df['Revenue'].sum():,.2f}")
    print(f"Vente moyenne: {df['Revenue'].mean():,.2f}")
    print(f"Nombre total d'unités vendues: {df['Unit Sold'].sum():,.0f}")

def plot_sales_by_category(df):
    df.groupby('Category')['Revenue'].sum().plot(kind='bar', figsize=(10, 6), title='Ventes totales par catégorie')
    plt.xlabel('Catégorie')
    plt.ylabel('Ventes (Rs)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_units_by_state(df):
    df.groupby('State')['Unit Sold'].sum().plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8), title='Distribution des unités vendues par État')
    plt.axis('equal')
    plt.show()

def plot_monthly_sales(df):
    monthly_sales = df.groupby('Month')['Revenue'].mean()
    monthly_sales.plot(kind='line', marker='o', figsize=(10, 6), title='Moyenne des ventes mensuelles')
    plt.xlabel('Mois')
    plt.ylabel('Ventes moyennes (Rs)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def display_top_products(df):
    print("\nTop 5 des produits les plus vendus:")
    top_products = df.groupby('Product')['Unit Sold'].sum().sort_values(ascending=False).head()
    print(top_products)

if __name__ == "__main__":
    filepath = '/home/pharelouindou/interne/retail store data.xlsx'
    df = load_and_clean_data(filepath)
    
    display_sales_statistics(df)
    plot_sales_by_category(df)
    plot_units_by_state(df)
    plot_monthly_sales(df)
    display_top_products(df)