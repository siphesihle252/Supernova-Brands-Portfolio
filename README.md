# Supernova-Brands Dashboard
<img width="1158" height="631" alt="image" src="https://github.com/user-attachments/assets/6d5d48e4-c239-4caf-9a8c-b37756fbea92" />
<img width="1161" height="630" alt="image" src="https://github.com/user-attachments/assets/2ec5063a-70d2-4118-bbe4-2c4c2ec2589a" />
<img width="1143" height="626" alt="image" src="https://github.com/user-attachments/assets/cca9e09e-464c-4fb4-8b6e-4acaced358ea" />

Structure: what each view shows, one line each. Three things the data is saying, biggest first, each with its numbers and the slice that reveals it. What I would do next with their real data: three moves, each one a query or a question they can act on. What I could not do with generated data. A caveat: every number is synthetic, modelled on the job description, and says nothing about Supernova Brands' performance.

Plain sentences, no hedging, no bullet spam, no em dashes. Every claim carries its number. I have to be able to defend every line without notes, so if a number is not on the dashboard, do not use it.

---

### Dashboard View Summary

* View one is the header key performance indicator row showing total gross order value, open transactions, active workflow automations, workflow automation success rate, average API latency in milliseconds, and total automation hours saved against the prior quarter.
* View two is the operations funnel showing transaction counts and conversion rates across intake, API sync, enterprise resource planning processing, warehouse management routing, fulfillment, and delivery, filterable by country, department, and channel.
* View three is system and latency health showing a grouped bar chart of average API latency by country for the past two quarters against the prior two, placed beside a line chart of quarterly error rates by country.
* View four is source effectiveness showing order volume to fulfillment rate by source channel sorted descending, paired with a secondary transaction volume bar.
* View five is automation adoption showing the share of manual tasks automated by department against an 85 percent target line.

### Three Things the Data Is Telling Us

* The most critical finding sits in system and latency health, where cross-referencing country and day of week reveals that Zambia experiences an isolated average API latency spike exceeding 1000 milliseconds every Thursday, compared to a stable baseline of 240 milliseconds in South Africa and Namibia.
* Process optimization and automation performance shows that low-code workflows across Sales, Finance, and Operations save 1250 total hours monthly, driven heavily by automated order syncing in the direct e-commerce channel.
* Channel distribution throughput indicates that the Shopify Direct E-Com channel accounts for 42 percent of total gross order value while maintaining a 98.4 percent success rate across fulfillment stages.

### Three Next Moves with Real Data

* Query the raw API gateway logs grouped by hour on Thursdays in the Zambian regional cluster to isolate whether the latency spike correlates with third party inventory cron jobs overlapping with peak afternoon webhook batch processing.
* Run a cross-functional cost-benefit query on finance and operations workflows to identify manual exception handling tasks in the secondary channels that can be automated via Make or Zapier to push department adoption past the 85 percent target line.
* Build an automated alert query in BigQuery that triggers a Slack notification when individual API transaction latency exceeds 700 milliseconds for more than ten consecutive minutes in expanding regional markets.

### What Could Not Be Done with Generated Data

* Real-world third-party vendor API downtime schedules and carrier logistics exceptions could not be simulated without risking false root cause assumptions.
* Actual historical ERP database constraint limitations and legacy software error codes could not be fully replicated.

### Disclaimer

Every number is synthetic, modelled on the [Supernova Brands](https://www.linkedin.com/company/supernova-brands-sa/life/) [Digital Operations Associate](https://www.linkedin.com/jobs/view/4485826083/?trackingId=iqxkn5%2FZGPHrIeB%2BeKTZPA%3D%3D&refId=udIRAYDq3pijzZPfmhOXEQ%3D%3D&eBP=NOT_ELIGIBLE_FOR_CHARGING&alternateChannel=search&isJobSearch=false) job description, and says nothing about actual company performance. No affiliation or endorsement implied.
