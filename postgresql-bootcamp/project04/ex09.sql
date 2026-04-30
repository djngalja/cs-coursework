WITH temp AS (    
    SELECT MAX(id) + 1 AS id,
        (SELECT id FROM person WHERE name = 'Denis') AS person_id,
        (SELECT id FROM pizzeria WHERE name = 'Dominos') AS pizzeria_id,
        '2022-02-24'::date AS visit_date
    FROM person_visits
    UNION ALL
    SELECT 
        MAX(id) + 2 AS id,
        (SELECT id FROM person WHERE name = 'Irina'),
        (SELECT id FROM pizzeria WHERE name = 'Dominos'),
        '2022-02-24'::date
    FROM person_visits
)
INSERT INTO person_visits (id, person_id, pizzeria_id, visit_date)
SELECT *
FROM temp;
