# Supernova Brands: Digital Operations Star Schema Data Model

## Overview
This star schema is engineered to support the analytical, reporting, and operational optimization needs of the **Digital Operations Associate** at [Supernova Brands](https://www.linkedin.com/jobs/search-results/?currentJobId=4485826083&eBP=NOT_ELIGIBLE_FOR_CHARGING&refId=udIRAYDq3pijzZPfmhOXEQ%3D%3D&trackingId=iqxkn5%2FZGPHrIeB%2BeKTZPA%3D%3D&keywords=Operations%20Analyst&origin=BYV_SIMILAR_JOBS_IN_APP_NOTIFICATION&originToLandingJobPostings=4480443603%2C4485826083%2C4480634895%2C4479863961%2C4465666070%2C4481675639%2C4437834848%2C4480859661%2C4435814595%2C4472515995&geoId=104231451). It tracks multi-channel retail distribution, SaaS/ERP workflow efficiencies, and regional supply chain throughput across EMEA markets from May 2025 through October 2026.

---

## Ad Lineage Mapping Table

| Table Name | Schema Type | Ad Lineage Reference (Exact Text from Job Ad) | Functional Rationale |
| :--- | :--- | :--- | :--- |
| `dim_calendar` | Dimension | *"Start Date 🗓️: As soon as possible"* / temporal tracking across quarters | Provides standardized date hierarchies for time-series operational and financial reporting. |
| `dim_territory` | Dimension | *"servicing key territories from established markets like South Africa to rapidly expanding regions across Africa 🌍"* | Captures regional segmentation and country-level distribution hubs. |
| `dim_channel` | Dimension | *"We partner with Africa’s leading retailers and e-commerce platforms"* / *"seven source channels"* | Segments intake channels (e.g., B2B Key Accounts, Direct E-Commerce, Marketplace API). |
| `dim_department` | Dimension | *"Analyze the needs of various business functions (Sales, Finance, Ops)"* | Aligns operational throughput and ticket resolution metrics with internal organizational units. |
| `fact_operational_transactions` | Fact | *"As the Digital Operations Associate, you will serve as the strategic 'right hand'... ensuring our tech stack connects seamlessly"* | Granular log of transactional throughput, API sync events, and system latency metrics. One row per transaction event. |
| `fact_workflow_automation` | Fact | *"Automate Everything: Identify repetitive manual tasks and use low-code tools (e.g., Zapier, Make, Power Automate)"* | Tracks automation executions, manual fallback interventions, and time saved. One row per workflow execution log. |

---

## Dimension & Fact Table Architecture

### 1. `dim_calendar`
* **Primary Key:** `date_key` (YYYYMMDD)
* **Attributes:** `date`, `day_of_week`, `calendar_month`, `calendar_quarter`, `calendar_year`, `is_weekend`

### 2. `dim_territory`
* **Primary Key:** `territory_id`
* **Attributes:** `country_name`, `region_code`, `distribution_hub`, `market_maturity` ('Established' vs 'Expanding')

### 3. `dim_channel`
* **Primary Key:** `channel_id`
* **Attributes:** `channel_name`, `channel_category` ('B2B Retail', 'E-Commerce', 'Marketplace API'), `integration_type`

### 4. `dim_department`
* **Primary Key:** `department_id`
* **Attributes:** `department_name` ('Sales', 'Finance', 'Ops', 'Customer Support'), `cost_center_code`

### 5. `fact_operational_transactions`
* **Granularity:** One row per digital order/system integration event.
* **Foreign Keys:** `date_key`, `territory_id`, `channel_id`, `department_id`
* **Measures:** `order_volume`, `gross_order_value`, `api_latency_ms`, `error_flag`

### 6. `fact_workflow_automation`
* **Granularity:** One row per automated workflow execution or manual fallback trigger.
* **Foreign Keys:** `date_key`, `territory_id`, `department_id`
* **Measures:** `execution_count`, `time_saved_minutes`, `manual_intervention_required`

---

## Metrics Supported by Department

### Sales
* Total Order Value and Gross Revenue Trends across EMEA markets.
* Channel-specific conversion velocity and order drop-off rates.

### Finance
* Integration discrepancy loss exposure and reconciliation turnaround time.
* Operational cost savings derived from low-code automation workflows.

### Operations (Ops)
* System Sync Latency and API Error Rates across enterprise software stacks.
* Workflow automation adoption rates and manual intervention bottlenecks.