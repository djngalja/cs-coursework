SELECT COALESCE(person.name, '-') AS person_name, 
    visit_date, COALESCE(pizzeria.name, '-') AS pizzeria_name
FROM (SELECT * FROM person_visits 
    WHERE visit_date >= '2022-01-01' AND visit_date <= '2022-01-03') AS visits
    FULL JOIN person ON person.id = person_id
    FULL JOIN pizzeria ON pizzeria.id = pizzeria_id
ORDER BY 1, 2, 3;