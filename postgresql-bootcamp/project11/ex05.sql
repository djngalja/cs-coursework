DROP FUNCTION IF EXISTS fnc_persons_male();
DROP FUNCTION IF EXISTS fnc_persons_female();

CREATE OR REPLACE FUNCTION fnc_persons(pgender TEXT DEFAULT 'female') RETURNS SETOF person AS $$
    SELECT *
    FROM person
    WHERE gender = pgender;
$$ LANGUAGE sql;


select *
from fnc_persons(pgender := 'male');

select *
from fnc_persons();