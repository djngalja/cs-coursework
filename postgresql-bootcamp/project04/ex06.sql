WITH full_menu AS (
    SELECT pizza_name, pizzeria_id, name, price, menu.id AS menu_id
    FROM menu LEFT JOIN pizzeria ON pizzeria_id = pizzeria.id
)
SELECT t1.pizza_name AS pizza_name, t1.name AS pizzeria_name_1, 
    t2.name AS pizzeria_name_2, t1.price AS price
FROM full_menu AS t1 INNER JOIN full_menu AS t2
    ON t1.pizza_name = t2.pizza_name AND t1.price = t2.price 
    AND t1.name <> t2.name AND t1.menu_id > t2.menu_id
ORDER BY 1; 