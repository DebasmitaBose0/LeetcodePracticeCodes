SELECT Department, Employee, Salary
FROM (
    SELECT d.name AS Department,
           e.name AS Employee,
           e.salary AS Salary,
           DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS r
    FROM Employee e
    JOIN Department d
    ON e.departmentId = d.id
) t
WHERE r = 1;