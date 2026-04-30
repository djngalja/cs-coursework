WITH stats AS (
    SELECT person_id, COUNT(*) AS count_of_visits
    FROM person_visits
    GROUP BY person_id
    ORDER BY 2 DESC, 1 ASC
    LIMIT 4
)
SELECT name, count_of_visits
FROM stats LEFT JOIN person ON person_id = person.id
ORDER BY 2 DESC, 1 ASC;