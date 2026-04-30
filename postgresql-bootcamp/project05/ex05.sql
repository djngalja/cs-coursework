CREATE VIEW v_price_with_discount AS
SELECT name, pizza_name, price, 
    ROUND(price - price * 0.1)::int AS discount_price
FROM person_order LEFT JOIN person ON person_id = person.id
    LEFT JOIN menu ON menu_id = menu.id
ORDER BY 1, 2;