# E-Commerce ETL Pipeline

A production-grade ETL (Extract, Transform, Load) pipeline that processes raw e-commerce data, validates for quality, and exports analytics-ready metrics.

## What It Does

This pipeline solves a real problem: **raw data is messy**. It implements a 5-step process:

1. **Load** — Read raw CSV files (orders, customers, inventory)
2. **Validate** — Remove duplicates, catch nulls, enforce data types
3. **Transform** — Convert strings to proper types (dates, floats, ints)
4. **Aggregate** — Create business metrics (order counts, revenue, averages)
5. **Export** — Save cleaned data to CSVs

## Key Features

- ✅ **Data Validation** — Catches quality issues before transformation
- ✅ **Type Safety** — Enforces correct data types at every step
- ✅ **Logging** — Every step is logged; failures are debuggable
- ✅ **Reproducibility** — Same input = same output, every time
- ✅ **Metrics Generation** — Produces analytics-ready aggregations

## Quick Start

### Prerequisites
- Python 3.8+
- pandas

### Installation

\\\ash
pip install pandas
\\\

### Run the Pipeline

\\\ash
python pipeline_simple.py
\\\

**Output:**
- \data/processed/orders_transformed.csv\
- \data/processed/customers_transformed.csv\
- \data/processed/inventory_transformed.csv\
- \data/processed/order_metrics.csv\

## Example Output

### Input Data
- 5 orders across 3 customers
- 3 products in inventory
- Multiple days of transactions

### Output Metrics
\\\
metric_date | product_id | product_name | category    | order_count | total_revenue | avg_order_value
2026-09-01  | P001       | Laptop       | Electronics | 1           | 1500.00       | 1500.00
2026-09-02  | P002       | Phone        | Electronics | 1           | 2500.50       | 2500.50
2026-09-03  | P003       | Keyboard     | Electronics | 1           | 800.00        | 800.00
2026-09-04  | P001       | Laptop       | Electronics | 1           | 1500.00       | 1500.00
2026-09-05  | P002       | Phone        | Electronics | 1           | 2500.50       | 2500.50
\\\

## Architecture

\\\
Raw Data (CSV)
    ↓
Load → Validate → Transform → Aggregate → Export
    ↓       ↓         ↓          ↓         ↓
  Logs  Quality   Types    Metrics   Clean CSVs
\\\

## Key Learnings

**80% of data engineering is validation and plumbing, not algorithms.**

- **Validation matters** — Catching bad data early prevents downstream failures
- **Logging is critical** — When pipelines fail at 3 AM, good logs save hours of debugging
- **Reproducibility is non-negotiable** — Systems must produce the same output given the same input
- **Business logic is in transformations** — Aggregations create value that analysts use

## What's Next?

**Project 2:** Add real-time streaming with Kafka
- Process events as they arrive
- Live metrics updates
- Handle failures gracefully

**Project 3:** Add database + orchestration
- PostgreSQL for persistent storage
- dbt for SQL transformations
- Airflow for scheduling and monitoring

## Technologies

- **Language:** Python 3.8+
- **Data Processing:** pandas
- **Data Format:** CSV
- **Logging:** Python built-in logging

## Author

Ariti Chawla

- LinkedIn: [linkedin.com/in/ariti-chawla](https://linkedin.com/in/ariti-chawla)
- GitHub: [github.com/ariti2110](https://github.com/ariti2110)
- Portfolio: [https://portfolio-theta-beryl-86.vercel.app/](https://portfolio-theta-beryl-86.vercel.app/)

## License

MIT
