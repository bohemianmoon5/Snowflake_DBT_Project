SELECT *
FROM {{ source('p_source', 'campaign_performance') }}
