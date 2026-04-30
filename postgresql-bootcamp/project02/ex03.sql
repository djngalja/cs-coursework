(SELECT order_date AS action_date, person_id
    FROM person_order)
INTERSECT
(SELECT visit_date, person_id FROM person_visits)
ORDER BY 1 ASC, 2 DESC;