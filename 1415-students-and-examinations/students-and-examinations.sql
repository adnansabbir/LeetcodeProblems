select S.student_id, S.student_name, Sub.subject_name, count(e.student_id) as attended_exams
from Students S
join Subjects Sub
left join Examinations E on S.student_id = E.student_id and Sub.subject_name = E.subject_name
group by S.student_id, S.student_name, Sub.subject_name
order by S.student_id, Sub.subject_name
