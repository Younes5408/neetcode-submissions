-- Write your query below
SELECT employee_id , (Case when employee_id % 2 = 1 AND name NOT LIKE 'M%' Then salary ELSE 0 END) As bonus FROM employees Order by employee_id ASC ;