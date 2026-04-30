SELECT order_date, name || ' (age:' || age || ')' AS person_information
FROM person_order LEFT JOIN person ON person_id = person.id
ORDER BY 1, 2;