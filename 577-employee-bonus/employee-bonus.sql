select Employee.name, Bonus.bonus
from Employee
left join Bonus on Employee.empId = Bonus.empId
where coalesce(Bonus.bonus, 0) < 1000