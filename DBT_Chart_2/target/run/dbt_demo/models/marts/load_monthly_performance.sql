
  
    

        create or replace transient table p_mart.p_mart_schema.load_monthly_performance
         as
        (SELECT
	  TO_CHAR(DATE_TRUNC('MONTH', c.START_DATE), 'YYYY-MM') AS MONTH
	, SUM(p.COST)    AS TOTAL_COST
	, SUM(p.REVENUE) AS TOTAL_REVENUE
FROM p_mart.p_mart_schema.raw_campaign_performance p
JOIN p_mart.p_mart_schema.raw_campaigns c
  ON p.CAMPAIGN_ID = c.CAMPAIGN_ID
GROUP BY 1
ORDER BY 1
        );
      
  