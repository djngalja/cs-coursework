SELECT address, pizzeria.name, COUNT(*) AS count_of_orders
FROM person_order LEFT JOIN person ON person_id = person.id
    LEFT JOIN menu ON menu_id = menu.id
    LEFT JOIN pizzeria On pizzeria_id = pizzeria.id
GROUP BY 1, 2
ORDER BY 1, 2;