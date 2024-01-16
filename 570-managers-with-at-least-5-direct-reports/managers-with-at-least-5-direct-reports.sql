select E1.name
from Employee E1, Employee E2
where E1.id = E2.managerId
group by E1.id
having count(*) > 4
