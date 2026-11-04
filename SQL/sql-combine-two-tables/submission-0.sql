-- Write your query below
select first_name,last_name,city,state

from address a right JOIN  person p USING(person_id)