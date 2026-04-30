INSERT INTO currency VALUES (100, 'EUR', 0.85, '2022-01-01 13:29');
INSERT INTO currency VALUES (100, 'EUR', 0.79, '2022-01-08 13:29');

WITH src AS (
    SELECT user_id, money, currency_id, updated
    FROM balance
    WHERE currency_id IN (SELECT DISTINCT id FROM currency)
),
updated_tab AS (
    SELECT user_id, currency_id, money, 
        (SELECT MAX(currency.updated)
        FROM currency
        WHERE currency.updated < src.updated
            AND currency.id = currency_id) AS t1,
        (SELECT MIN(currency.updated)
        FROM currency
        WHERE currency.updated > src.updated
            AND currency.id = currency_id) AS t2 
    FROM src 
),
final_time AS (
    SELECT user_id, currency_id, money, COALESCE(t1, t2) AS t
    FROM updated_tab
)
SELECT COALESCE("user".name, 'not defined') AS name, 
    COALESCE(lastname, 'not defined') AS lastname, 
    currency.name AS currency_name,
    money * currency.rate_to_usd AS currency_in_usd
FROM final_time LEFT JOIN "user" ON "user".id = user_id
    LEFT JOIN currency ON currency.id = currency_id 
        AND currency.updated = t
ORDER BY 1 DESC, 2, 3;





