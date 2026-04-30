WITH ids AS (
    SELECT pizzeria_id 
    FROM person_visits 
    WHERE person_id IN (SELECT id FROM person WHERE name = 'Andrey')
        EXCEPT
    SELECT pizzeria_id
    FROM person_order LEFT JOIN menu ON menu_id = menu.id
    WHERE person_id IN (SELECT id FROM person WHERE name = 'Andrey')
)
SELECT name AS pizzeria_name
FROM ids LEFT JOIN pizzeria ON pizzeria_id = pizzeria.id
ORDER BY 1;