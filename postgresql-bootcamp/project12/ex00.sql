WITH src AS (
    SELECT user_id, type, SUM(money) AS volume, currency_id
    FROM balance
    GROUP BY 1, 2, 4
),
current_rates AS (
    SELECT id, MAX(updated) AS date
    FROM currency
    GROUP BY 1
),
last_currency AS (
    SELECT current_rates.id AS id, name, rate_to_usd
    FROM current_rates LEFT JOIN currency 
        ON current_rates.id = currency.id AND date = updated
)
SELECT COALESCE("user".name, 'not defined') AS name,
    COALESCE(lastname, 'not defined') AS lastname,
    type, 
    volume, 
    COALESCE(last_currency.name, 'not defined') AS currency_name,
    COALESCE(rate_to_usd, 1) AS last_rate_to_usd,
    volume * COALESCE(rate_to_usd, 1) AS total_volume_in_usd
FROM src LEFT JOIN "user" ON user_id = "user".id
    LEFT JOIN last_currency ON currency_id = last_currency.id
ORDER BY 1 DESC, 2, 3;