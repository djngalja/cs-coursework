WITH dates AS (
    SELECT generate_series('2022-01-01'::date, '2022-01-10'::date, '1 day'::interval)
)
SELECT date(generate_series) AS missing_date
FROM dates LEFT JOIN (SELECT * FROM person_visits WHERE person_id = 1 OR person_id = 2)
        ON generate_series::date = visit_date
WHERE visit_date IS NULL
ORDER BY 1;