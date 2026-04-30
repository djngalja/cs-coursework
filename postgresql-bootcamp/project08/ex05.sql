COMMENT ON TABLE person_discounts IS 'Discount calculated based on number of orders';
COMMENT ON COLUMN person_discounts.id IS 'The primary key of the table, a counter';
COMMENT ON COLUMN person_discounts.person_id IS 'A foreign key that identifies a person from person table, a link between tables';
COMMENT ON COLUMN person_discounts.pizzeria_id IS 'A foreign key that identifies a pizzeria from pizzeria table, a link between tables';
COMMENT ON COLUMN person_discounts.discount IS 'Discount of a person (person_id) in a pizzeria (pizzeria_id), percent';