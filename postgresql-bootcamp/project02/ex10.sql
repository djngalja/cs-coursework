SELECT person.name AS person_name, pizza_name, pizzeria.name AS pizzeria_name
FROM person_order LEFT JOIN menu ON menu_id = menu.id
    LEFT JOIN pizzeria ON pizzeria_id = pizzeria.id
    LEFT JOIN person ON person_id = person.id
ORDER BY 1, 2, 3;