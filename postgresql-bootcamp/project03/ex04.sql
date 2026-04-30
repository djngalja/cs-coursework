WITH my_pizza AS (
    SELECT * FROM menu
    WHERE pizza_name LIKE 'pepperoni%' OR pizza_name LIKE 'mushroom%'
)
SELECT pizza_name, pizzeria.name AS pizzeria_name, price
FROM my_pizza LEFT JOIN pizzeria ON pizzeria_id = pizzeria.id
ORDER BY 1, 2;