import os
import random
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

print("Starting synthetic data generation for Supernova Brands...")

# Seed for reproducibility
random.seed(42)
np.random.seed(42)

# Date Range: May 2025 to Oct 2026 (approx 549 days)
start_date = datetime(2025, 5, 1)
end_date = datetime(2026, 10, 31)
date_list = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]

# 1. Generate dim_calendar
calendar_data = []
for d in date_list:
    calendar_data.append({
        "date_key": int(d.strftime("%Y%m%d")),
        "date": d.strftime("%Y-%m-%d"),
        "day_of_week": d.strftime("%A"),
        "calendar_month": d.strftime("%B"),
        "calendar_quarter": f"Q{(d.month - 1) // 3 + 1} {d.year}",
        "calendar_year": d.year,
        "is_weekend": 1 if d.weekday() >= 5 else 0
    })
df_calendar = pd.DataFrame(calendar_data)
df_calendar.to_csv("data/dim_calendar.csv", index=False)

# 2. Generate dim_territory
territories = [
    {"territory_id": 1, "country_name": "South Africa", "region_code": "ZA-CPT", "distribution_hub": "Montague Gardens", "market_maturity": "Established"},
    {"territory_id": 2, "country_name": "Namibia", "region_code": "NA-WDH", "distribution_hub": "Windhoek Hub", "market_maturity": "Established"},
    {"territory_id": 3, "country_name": "Botswana", "region_code": "BW-GBE", "distribution_hub": "Gaborone Hub", "market_maturity": "Established"},
    {"territory_id": 4, "country_name": "Zambia", "region_code": "ZM-LUN", "distribution_hub": "Lusaka Hub", "market_maturity": "Expanding"},
    {"territory_id": 5, "country_name": "Mauritius", "region_code": "MU-PLU", "distribution_hub": "Port Louis Hub", "market_maturity": "Expanding"}
]
df_territory = pd.DataFrame(territories)
df_territory.to_csv("data/dim_territory.csv", index=False)

# 3. Generate dim_channel (7 source channels)
channels = [
    {"channel_id": 1, "channel_name": "B2B Enterprise Portal", "channel_category": "B2B Retail", "integration_type": "Direct EDI"},
    {"channel_id": 2, "channel_name": "Shopify Direct E-Com", "channel_category": "E-Commerce", "integration_type": "REST API"},
    {"channel_id": 3, "channel_name": "Takealot Marketplace", "channel_category": "Marketplace API", "integration_type": "Webhook"},
    {"channel_id": 4, "channel_name": "WooCommerce Retailer Hub", "channel_category": "E-Commerce", "integration_type": "REST API"},
    {"channel_id": 5, "channel_name": "Direct Wholesale Orders", "channel_category": "B2B Retail", "integration_type": "Manual Import"},
    {"channel_id": 6, "channel_name": "Regional Partner API", "channel_category": "Marketplace API", "integration_type": "GraphQL"},
    {"channel_id": 7, "channel_name": "Mobile App Storefront", "channel_category": "E-Commerce", "integration_type": "REST API"}
]
df_channel = pd.DataFrame(channels)
df_channel.to_csv("data/dim_channel.csv", index=False)

# 4. Generate dim_department
departments = [
    {"department_id": 1, "department_name": "Sales", "cost_center_code": "CC-SLS-100"},
    {"department_id": 2, "department_name": "Finance", "cost_center_code": "CC-FIN-200"},
    {"department_id": 3, "department_name": "Ops", "cost_center_code": "CC-OPS-300"},
    {"department_id": 4, "department_name": "Customer Support", "cost_center_code": "CC-SUP-400"}
]
df_department = pd.DataFrame(departments)
df_department.to_csv("data/dim_department.csv", index=False)

# 5. Generate fact_operational_transactions (~120,000 rows)
print("Generating operational transactions...")
trans_rows = []
trans_id = 1
for _ in range(120000):
    d = random.choice(date_list)
    territory = random.choice(territories)
    channel = random.choice(channels)
    department = random.choice(departments)
    
    # Injecting hidden finding: Zambia (territory_id=4) via Shopify/WooCommerce has hidden latency spikes on Thursdays
    base_latency = random.gauss(240, 45)
    if territory["territory_id"] == 4 and d.strftime("%A") == "Thursday":
        base_latency += random.gauss(850, 120) # Hidden finding anomaly
        
    error_flag = 1 if base_latency > 700 else 0
    
    trans_rows.append({
        "transaction_id": trans_id,
        "date_key": int(d.strftime("%Y%m%d")),
        "territory_id": territory["territory_id"],
        "channel_id": channel["channel_id"],
        "department_id": department["department_id"],
        "order_volume": random.randint(1, 15),
        "gross_order_value": round(random.uniform(150.0, 4500.0), 2),
        "api_latency_ms": max(50, int(base_latency)),
        "error_flag": error_flag
    })
    trans_id += 1

df_trans = pd.DataFrame(trans_rows)
df_trans.to_csv("data/fact_operational_transactions.csv", index=False)

# 6. Generate fact_workflow_automation (~30,000 rows)
print("Generating workflow automation logs...")
auto_rows = []
auto_id = 1
for _ in range(30000):
    d = random.choice(date_list)
    territory = random.choice(territories)
    department = random.choice(departments)
    
    auto_rows.append({
        "automation_log_id": auto_id,
        "date_key": int(d.strftime("%Y%m%d")),
        "territory_id": territory["territory_id"],
        "department_id": department["department_id"],
        "execution_count": random.randint(1, 5),
        "time_saved_minutes": random.randint(15, 120),
        "manual_intervention_required": random.choice([0, 0, 0, 1]) # 25% chance
    })
    auto_id += 1

df_auto = pd.DataFrame(auto_rows)
df_auto.to_csv("data/fact_workflow_automation.csv", index=False)

print(f"Data generation complete! Total rows generated: {len(df_trans) + len(df_auto):,} across tables.")