import pandas as pd
import numpy as np

# Products list (10 types)
products = [
 "Rose Serenity","Lavender Calm","Jasmine Bliss","Sandalwood Warm",
 "Amber Deep","Citrus Fresh","Vanilla Soft","Patchouli Mystic",
 "Mint Clear","Oud Royal"
]

# Create dates for full 12 months (daily or monthly aggregate). We will create monthly aggregate.
months = pd.date_range(start='2024-01-01', end='2024-12-31', freq='MS')  # start of each month

rows = []
np.random.seed(42)  # reproducible

for month in months:
    month_label = month.strftime('%Y-%m')  # e.g., '2024-01'
    for product in products:
        # random monthly units sold between 20 and 400 (you can tune)
        units = np.random.randint(20, 400)
        # price per bottle unique per product between 5 and 10 €
        price = round(np.random.uniform(5.0, 10.0), 2)
        revenue = round(units * price, 2)
        cost_per_unit = 3.00   # fixed cost rule
        profit = round((price - cost_per_unit) * units, 2)
        rows.append({
            'month': month_label,
            'product': product,
            'units_sold': units,
            'price_eur': price,
            'revenue_eur': revenue,
            'cost_eur': round(cost_per_unit * units, 2),
            'profit_eur': profit
        })

df = pd.DataFrame(rows)

# Make sure the folder exists and save CSV
out_path = 'data/processed/aromatic_oils_sales.csv'
df.to_csv(out_path, index=False)
print("Saved:", out_path)
print(df.head().to_string(index=False))
