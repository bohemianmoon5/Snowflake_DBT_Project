
  create or replace   view p_mart.p_mart_schema.raw_campaigns
  
   as (
    SELECT *
FROM p_source_db.p_source_schema.P_CAMPAIGNS
  );

