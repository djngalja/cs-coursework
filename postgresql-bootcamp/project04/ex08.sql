WITH temp AS (
    SELECT MAX(id) + 1 AS id, 
        (SELECT id FROM pizzeria WHERE name = 'Dominos') AS pizzeria_id,
        'sicilian pizza' AS pizza_name,
        900 AS price
    FROM menu
)
INSERT INTO menu (id, pizzeria_id, pizza_name, price)
SELECT id, pizzeria_id, pizza_name, price
FROM temp;