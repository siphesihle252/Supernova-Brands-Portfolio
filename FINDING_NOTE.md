# Operational Finding Note: Regional Gateway Latency Anomaly

## Notice to Analyst
* **Disclaimer:** All numbers and metrics contained in this dataset are strictly synthetic and generated for portfolio modeling purposes only. They do not reflect real-world financial or operational figures of Supernova Brands.

---

## Hidden Finding Description
When slicing operational transactions by **Country (`dim_territory.country_name`)** and cross-referencing with **Day of Week (`dim_calendar.day_of_week`)** alongside **Integration Channel (`dim_channel.channel_name`)**, a distinct non-obvious anomaly emerges:

* **The Slice on Dashboard:** A multi-line time-series visual tracking average `api_latency_ms` grouped by Country across days of the week.
* **The Hidden Finding:** While established markets (South Africa, Namibia) maintain stable API response latency (~240ms) throughout the week, **Zambia** experiences a dramatic, isolated latency spike averaging over 1,000ms **every Thursday**. 
* **Root Cause Analysis (for the Analyst):** This occurs due to a regional third-party inventory reconciliation cron job overlapping with peak afternoon webhook batch processing from localized e-commerce partners on Thursdays. Because it only appears when slicing by territory and day of week simultaneously, top-level monthly summaries mask the issue.