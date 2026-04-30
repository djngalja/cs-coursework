CREATE OR REPLACE FUNCTION fnc_fibonacci(pstop INT DEFAULT 10) RETURNS TABLE(nums INT) AS $$
    WITH RECURSIVE fib(n, next) AS (
        SELECT 0, 1
        UNION ALL
        SELECT next, n + next
        FROM fib
        WHERE next < pstop
    )
    SELECT n FROM fib;
$$ LANGUAGE sql;


select * from fnc_fibonacci(100);

select * from fnc_fibonacci(); 