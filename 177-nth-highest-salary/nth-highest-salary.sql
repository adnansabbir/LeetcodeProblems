CREATE FUNCTION getNthHighestSalary(N int) RETURNS int
    BEGIN
        DECLARE offset_value int DEFAULT N - 1;
        DECLARE result int;
        
        select distinct salary into result
        from employee
        order by salary desc
        limit 1 offset offset_value;
        
        RETURN result;
    END