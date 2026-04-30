WITH temp AS (
    SELECT MAX(id) + 1 AS id,
        (SELECT id FROM person WHERE name = 'Denis') AS person_id,
        (SELECT id FROM menu WHERE pizza_name = 'sicilian pizza') AS menu_id,
        '2022-02-24'::date AS order_date
    FROM person_order
    UNION ALL
    SELECT MAX(id) + 2,
        (SELECT id FROM person WHERE name = 'Irina'),
        (SELECT id FROM menu WHERE pizza_name = 'sicilian pizza'),
        '2022-02-24'::date
    FROM person_order
)
INSERT INTO person_order(id, person_id, menu_id, order_date)
SELECT *
FROM temp;