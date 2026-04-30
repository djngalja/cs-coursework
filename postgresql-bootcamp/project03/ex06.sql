WITH orders AS (
    SELECT menu_id
    FROM person_order
    WHERE person_id IN (
        SELECT id FROM person WHERE name IN ('Denis', 'Anna')
    )
)
SELECT pizza_name, name AS pizzeria_name
FROM orders LEFT JOIN menu ON menu_id = menu.id
    LEFT JOIN pizzeria ON pizzeria_id = pizzeria.id
ORDER BY 1, 2;