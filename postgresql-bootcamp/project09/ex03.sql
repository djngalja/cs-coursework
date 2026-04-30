WITH stats AS (
    (SELECT pizzeria_id, COUNT(*) AS count
    FROM person_visits
    GROUP BY 1)
        UNION
    (SELECT pizzeria_id, COUNT(*)
    FROM person_order LEFT JOIN menu ON menu_id = menu.id
    GROUP BY 1)
)
SELECT name, SUM(count) AS total_count
FROM stats LEFT JOIN pizzeria ON pizzeria_id = pizzeria.id
GROUP BY 1
ORDER BY 2 DESC, 1; 