CREATE OR REPLACE FUNCTION fnc_person_visits_and_eats_on_date(
    pperson TEXT DEFAULT 'Dmitriy',
    pprice NUMERIC DEFAULT 500,
    pdate DATE DEFAULT '2022-01-08'
) RETURNS SETOF TEXT AS $$
BEGIN
    RETURN QUERY
    WITH visits AS (
        SELECT pizzeria_id FROM person_visits
        WHERE visit_date = pdate AND person_id 
            IN (SELECT id FROM person WHERE name = pperson)
    )
    SELECT DISTINCT name::TEXT AS pizzeria_name
    FROM pizzeria RIGHT JOIN (SELECT pizzeria_id FROM menu WHERE price < pprice) AS cheap_menu
        ON pizzeria.id = cheap_menu.pizzeria_id
        RIGHT JOIN visits ON pizzeria.id = visits.pizzeria_id;
END;
$$ LANGUAGE plpgsql; 


select *  
from fnc_person_visits_and_eats_on_date(pprice := 800);

select *  
from fnc_person_visits_and_eats_on_date(pperson := 'Anna',pprice := 1300,pdate := '2022-01-01'); 