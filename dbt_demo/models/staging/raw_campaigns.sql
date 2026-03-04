SELECT *
FROM {{ source('p_source', 'campaigns') }}
