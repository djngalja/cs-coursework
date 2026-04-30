CREATE MATERIALIZED VIEW mv_dmitriy_visits_and_eats AS
WITH visits AS (
    SELECT pizzeria_id FROM person_visits
    WHERE visit_date = '2022-01-08' AND person_id 
        IN (SELECT id FROM person WHERE name = 'Dmitriy')
)
SELECT name AS pizzeria_name
FROM pizzeria RIGHT JOIN (SELECT pizzeria_id FROM menu WHERE price < 800) AS cheap_menu
    ON pizzeria.id = cheap_menu.pizzeria_id
    RIGHT JOIN visits ON pizzeria.id = visits.pizzeria_id
WITH DATA;