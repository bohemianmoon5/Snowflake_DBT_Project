SELECT
    traffic_source,
    SUM(total_revenue) AS revenue
FROM {{ source('p_source', 'first_touch') }}
GROUP BY traffic_source
