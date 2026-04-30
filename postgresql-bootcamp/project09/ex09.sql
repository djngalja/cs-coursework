WITH stats AS (    
    SELECT address, 
        ROUND(MAX(age) - (MIN(age)::NUMERIC / MAX(age)), 2) AS formula,
        ROUND(AVG(age), 2) AS average
    FROM person
    GROUP BY 1
    ORDER BY 1
)
SELECT address, formula, average,
    CASE WHEN formula > average THEN true ELSE false END AS comparison
FROM stats;