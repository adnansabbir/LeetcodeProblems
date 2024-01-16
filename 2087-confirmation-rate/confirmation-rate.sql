select 
    S.user_id, 
    case count(C.action) filter(where C.action = 'confirmed')
        when 0 then 0
        else (count(C.action) filter(where C.action = 'confirmed') / count(C.action)::decimal)::numeric(10,2)
    end as confirmation_rate
from Signups as S
left join Confirmations as C on S.user_id = C.user_id
group by S.user_id