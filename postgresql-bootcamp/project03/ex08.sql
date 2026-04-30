WITH menus AS (
    SELECT id
    FROM menu
    WHERE pizza_name LIKE 'mushroom%' OR pizza_name LIKE 'pepperoni%'
)
SELECT DISTINCT name 
FROM person_order RIGHT JOIN menus ON menu_id = menus.id
    LEFT JOIN person ON person_id = person.id
WHERE person_id IN (
    SELECT id 
    FROM person 
    WHERE gender = 'male' AND (address = 'Moscow' OR address = 'Samara')
)
ORDER BY 1 DESC;