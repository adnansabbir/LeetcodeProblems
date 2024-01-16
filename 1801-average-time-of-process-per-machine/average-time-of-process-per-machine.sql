select a1.machine_id, round(avg((a2.timestamp - a1.timestamp)::numeric), 3) as processing_time
from Activity a1
inner join Activity as a2 on (a1.machine_id = a2.machine_id and a1.process_id = a2.process_id and a2.activity_type = 'end')
where a1.activity_type = 'start'
group by a1.machine_id