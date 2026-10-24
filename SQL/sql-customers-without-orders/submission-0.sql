-- Write your query below
SELECT name from customers WHere id not in (Select customer_id from orders);