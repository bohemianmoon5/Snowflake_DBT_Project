{{ config(materialized='view') }}

SELECT *
FROM {{ source('p_source', 'CAMPAIGN_PERFORMANCE') }}
