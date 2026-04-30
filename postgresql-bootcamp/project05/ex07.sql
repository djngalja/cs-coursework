WITH cheap_pizzeria AS (
    SELECT pizzeria_id 
    FROM menu LEFT JOIN pizzeria ON pizzeria_id = pizzeria.id
    WHERE price < 800 AND name NOT IN 
        (SELECT * FROM mv_dmitriy_visits_and_eats)
    LIMIT 1
),
temp AS (
    SELECT MAX(id) + 1 AS id,
        (SELECT id FROM person WHERE name = 'Dmitriy') AS person_id,
        (SELECT * FROM cheap_pizzeria) AS pizzeria_id,
        '2022-01-08'::date AS visit_date
    FROM person_visits
)
INSERT INTO person_visits (id, person_id, pizzeria_id, visit_date)
SELECT * FROM temp;

REFRESH MATERIALIZED VIEW mv_dmitriy_visits_and_eats;