WITH women AS (
    SELECT person_id
    FROM person_order LEFT JOIN menu ON menu_id = menu.id
    WHERE pizza_name IN ('pepperoni pizza', 'cheese pizza')
        AND person_id IN (SELECT id FROM person WHERE gender = 'female')
    GROUP BY 1
    HAVING COUNT(person_id) = 2
)
SELECT name 
FROM women LEFT JOIN person ON person.id = women.person_id
ORDER BY 1;