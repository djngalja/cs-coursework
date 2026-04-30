WITH stats AS (
    SELECT pizzeria.name AS pizzeria_name, 
        COUNT(CASE WHEN gender = 'female' THEN 1 END) AS female,
        COUNT(CASE WHEN gender = 'male' THEN 1 END) AS male
    FROM person_order LEFT JOIN person ON person_id = person.id
        LEFT JOIN menu ON menu_id = menu.id
        LEFT JOIN pizzeria ON pizzeria_id = pizzeria.id
    GROUP BY 1
)
SELECT pizzeria_name FROM stats
WHERE male = 0
    UNION ALL
SELECT pizzeria_name FROM stats
WHERE female = 0 
ORDER BY 1; 