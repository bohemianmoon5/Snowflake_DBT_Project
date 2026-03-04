{{ config(materialized='view') }}

SELECT *
FROM {{ source('p_source', 'P_CAMPAIGNS') }}
