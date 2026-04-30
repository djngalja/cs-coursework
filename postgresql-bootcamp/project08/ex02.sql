SELECT person.name, pizza_name, price, 
    ROUND(price - discount / 100 * price) AS discount_price,
    pizzeria.name AS pizzeria_name
FROM person_order LEFT JOIN person ON person_order.person_id = person.id
    LEFT JOIN menu ON menu_id = menu.id
    LEFT JOIN pizzeria ON menu.pizzeria_id = pizzeria.id
    LEFT JOIN person_discounts 
        ON person_discounts.person_id = person.id AND person_discounts.pizzeria_id = pizzeria.id
ORDER BY 1, 2;