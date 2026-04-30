WITH stats AS (
    (SELECT pizzeria_id, COUNT(*) AS count, 'visit' AS action_type
    FROM person_visits
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 3)
        UNION
    (SELECT pizzeria_id, COUNT(*), 'order'
    FROM person_order LEFT JOIN menu ON menu_id = menu.id
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 3)
)
SELECT name, count, action_type
FROM stats LEFT JOIN pizzeria ON pizzeria_id = pizzeria.id
ORDER BY 3, 2 DESC, 1;