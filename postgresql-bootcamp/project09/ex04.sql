WITH stats AS ( 
    SELECT person_id, COUNT(*) AS count_of_visits
    FROM person_visits
    GROUP BY person_id
    HAVING COUNT(*) > 3
)
SELECT name, count_of_visits
FROM stats LEFT JOIN person ON person_id = person.id;