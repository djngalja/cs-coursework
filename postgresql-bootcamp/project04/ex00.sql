SELECT pizza_name, price, name AS pizzeria_name, visit_date
FROM person_visits LEFT JOIN pizzeria ON pizzeria_id = pizzeria.id
    LEFT JOIN menu ON person_visits.pizzeria_id = menu.pizzeria_id
WHERE person_id IN (SELECT id FROM person WHERE name = 'Kate')
    AND price >= 800 AND price <= 1000
ORDER BY 1, 2, 3;