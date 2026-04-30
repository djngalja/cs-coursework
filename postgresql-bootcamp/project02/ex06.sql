SELECT action_date, name AS person_name
FROM 
    ((SELECT order_date AS action_date, person_id
        FROM person_order)
    INTERSECT
    (SELECT visit_date, person_id FROM person_visits)) AS table1 
        LEFT JOIN person ON person_id = id
ORDER BY 1 ASC, 2 DESC;