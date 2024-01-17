select 
    contest_id,
    round((count(contest_id)::decimal / (select count(*) from Users)) * 100, 2) as percentage
from Register
group by contest_id
order by percentage desc, contest_id