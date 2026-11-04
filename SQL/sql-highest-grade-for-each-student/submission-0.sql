-- Write your query below
with c as( 
    select distinct on (student_id) student_id, exam_id,max(score) score

    from exam_results
    group by student_id ,exam_id
    order by student_id,score desc , exam_id


) 

select *
from c

;