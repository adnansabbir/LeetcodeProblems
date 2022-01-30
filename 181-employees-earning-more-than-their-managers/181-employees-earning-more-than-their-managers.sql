SELECT
    emp.Name AS Employee
FROM Employee AS emp JOIN Employee AS man
    ON emp.managerId = man.id
    AND emp.salary > man.salary;
