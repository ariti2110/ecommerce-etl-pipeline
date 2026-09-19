import logging
from src.loaders import load_csv, validate_orders, validate_customers, validate_inventory
from src.transforms import transform_orders, transform_customers, transform_inventory, create_order_metrics
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_pipeline():
    try:
        logger.info("=== STARTING ETL PIPELINE ===")
        
        logger.info("Step 1: Loading raw data...")
        orders_raw = load_csv("data/raw/orders.csv")
        customers_raw = load_csv("data/raw/customers.csv")
        inventory_raw = load_csv("data/raw/inventory.csv")
        
        logger.info("Step 2: Validating data...")
        orders_validated = validate_orders(orders_raw)
        customers_validated = validate_customers(customers_raw)
        inventory_validated = validate_inventory(inventory_raw)
        
        logger.info("Step 3: Transforming data...")
        orders_transformed = transform_orders(orders_validated)
        customers_transformed = transform_customers(customers_validated)
        inventory_transformed = transform_inventory(inventory_validated)
        
        logger.info("Step 4: Saving transformed data...")
        orders_transformed.to_csv("data/processed/orders_transformed.csv", index=False)
        customers_transformed.to_csv("data/processed/customers_transformed.csv", index=False)
        inventory_transformed.to_csv("data/processed/inventory_transformed.csv", index=False)
        
        logger.info("Step 5: Creating metrics...")
        order_metrics = create_order_metrics(orders_transformed, inventory_transformed)
        order_metrics.to_csv("data/processed/order_metrics.csv", index=False)
        
        logger.info("=== PIPELINE COMPLETE ===")
        logger.info(f"Orders: {len(orders_transformed)}, Customers: {len(customers_transformed)}, Products: {len(inventory_transformed)}")
        logger.info(f"Metrics rows: {len(order_metrics)}")
        
    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise

if __name__ == "__main__":
    run_pipeline()
