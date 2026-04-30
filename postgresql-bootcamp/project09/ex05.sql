SELECT DISTINCT name
FROM person_order LEFT JOIN person ON person.id = person_id
ORDER BY 1;