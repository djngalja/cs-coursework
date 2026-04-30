--Session #1
BEGIN;


--Session #2
BEGIN;


--Session #1
UPDATE pizzeria
SET rating = 4
WHERE id  = 1;


--Session #2
UPDATE pizzeria
SET rating = 4.5
WHERE id  = 2;


--Session #1
UPDATE pizzeria
SET rating = 4.7
WHERE id  = 2;


--Session #2
UPDATE pizzeria
SET rating = 4.2
WHERE id  = 1;


--Session #1
COMMIT;


--Session #2
COMMIT;
