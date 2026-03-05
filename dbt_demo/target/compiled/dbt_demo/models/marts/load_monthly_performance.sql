SELECT
	  TO_CHAR(DATE_TRUNC('MONTH', c.START_DATE), 'YYYY-MM') AS MONTH
	, SUM(p.COST)    AS TOTAL_COST
	, SUM(p.REVENUE) AS TOTAL_REVENUE
FROM p_source_db.p_source_schema.raw_campaign_performance p
JOIN p_source_db.p_source_schema.raw_campaigns c
  ON p.CAMPAIGN_ID = c.CAMPAIGN_ID
GROUP BY 1
ORDER BY 1