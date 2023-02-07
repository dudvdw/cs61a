.read data.sql


CREATE TABLE average_prices AS
  SELECT category, ROUND(AVG(MSRP)) as average_price from products group by category;


CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price) as lowest_prices from inventory group by item;

CREATE TABLE  lowest_cost AS
  SELECT name, ROUND(MIN(MSRP/rating)) from products group by category;

CREATE TABLE shopping_list AS
  SELECT a.name, b.store from lowest_cost as a, lowest_prices as b
  WHERE a.name = b.item;



CREATE TABLE total_bandwidth AS
  SELECT SUM(b.Mbs) from shopping_list as a, stores as b
  WHERE a.store = b.store;

