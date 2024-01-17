select 
    r.contest_id,
    round((count(r.contest_id)::decimal / u.total) * 100, 2) as percentage
from Register r, (select count(*) as total from Users) u
group by r.contest_id, u.total
order by percentage desc, r.contest_id
