import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# LOAD DATA
logger.info("Step 1: Loading raw data...")
orders = pd.read_csv("data/raw/orders.csv")
customers = pd.read_csv("data/raw/customers.csv")
inventory = pd.read_csv("data/raw/inventory.csv")

# VALIDATE
logger.info("Step 2: Validating data...")
orders = orders.drop_duplicates(subset=['order_id'])
customers = customers.drop_duplicates(subset=['customer_id'])
inventory = inventory.drop_duplicates(subset=['product_id'])

# TRANSFORM
logger.info("Step 3: Transforming data...")
orders['order_date'] = pd.to_datetime(orders['order_date'])
orders['amount'] = orders['amount'].astype(float)
customers['signup_date'] = pd.to_datetime(customers['signup_date'])
inventory['stock_quantity'] = inventory['stock_quantity'].astype(int)
inventory['last_updated'] = pd.to_datetime(inventory['last_updated'])

# CREATE METRICS
logger.info("Step 4: Creating metrics...")
merged = orders.merge(inventory[['product_id', 'product_name', 'category']], on='product_id')
metrics = merged.groupby(['order_date', 'product_id', 'product_name', 'category']).agg(
    order_count=('order_id', 'count'),
    total_revenue=('amount', 'sum'),
    avg_order_value=('amount', 'mean')
).reset_index()
metrics.columns = ['metric_date', 'product_id', 'product_name', 'category', 'order_count', 'total_revenue', 'avg_order_value']

# SAVE
logger.info("Step 5: Saving to CSV...")
orders.to_csv("data/processed/orders_transformed.csv", index=False)
customers.to_csv("data/processed/customers_transformed.csv", index=False)
inventory.to_csv("data/processed/inventory_transformed.csv", index=False)
metrics.to_csv("data/processed/order_metrics.csv", index=False)

logger.info("=== PIPELINE COMPLETE ===")
logger.info(f"Orders: {len(orders)}, Customers: {len(customers)}, Products: {len(inventory)}")
logger.info(f"Metrics: {len(metrics)} rows")
