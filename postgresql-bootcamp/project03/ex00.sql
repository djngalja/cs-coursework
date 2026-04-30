SELECT name, rating
FROM pizzeria LEFT JOIN person_visits 
    ON pizzeria.id = pizzeria_id
WHERE visit_date IS NULL;
