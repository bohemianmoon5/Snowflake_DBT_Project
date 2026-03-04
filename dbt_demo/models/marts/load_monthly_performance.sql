SELECT
	  TO_CHAR(DATE_TRUNC('MONTH', c.START_DATE), 'YYYY-MM') AS MONTH
	, SUM(p.COST)    AS TOTAL_COST
	, SUM(p.REVENUE) AS TOTAL_REVENUE
FROM {{ ref('raw_campaign_performance') }} p
JOIN {{ ref('raw_campaigns') }} c
  ON p.CAMPAIGN_ID = c.CAMPAIGN_ID
GROUP BY 1
ORDER BY 1