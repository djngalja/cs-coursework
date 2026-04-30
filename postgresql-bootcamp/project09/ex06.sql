WITH stats AS (
    SELECT pizzeria_id, COUNT(*) AS count_of_orders, 
        ROUND(AVG(price), 2) AS average_price,
        MAX(price) AS max_price, MIN(price) AS min_price
    FROM person_order LEFT JOIN menu ON menu_id = menu.id
    GROUP BY 1
)
SELECT name, count_of_orders, average_price, max_price, min_price
FROM stats LEFT JOIN pizzeria ON pizzeria_id = pizzeria.id
ORDER BY 1;