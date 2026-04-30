CREATE OR REPLACE FUNCTION func_minimum(arr NUMERIC[]) RETURNS NUMERIC AS $$
DECLARE
    min_val NUMERIC := NULL;
    val NUMERIC;
BEGIN
    FOREACH val IN ARRAY arr
    LOOP
        IF val IS NOT NULL AND (min_val IS NULL OR val < min_val) THEN 
            min_val := val; 
        END IF;
    END LOOP;
    RETURN min_val;
END;
$$ LANGUAGE plpgsql;


SELECT func_minimum(VARIADIC arr => ARRAY[10.0, -1.0, 5.0, 4.4]);