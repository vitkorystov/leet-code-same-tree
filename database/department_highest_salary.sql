-- https://leetcode.com/problems/department-highest-salary/description/

-- MySql

SELECT
    Department,
    Employee,
    Salary
FROM (
    SELECT
        e.name as 'Employee',
        salary as 'Salary',
        max(e.salary) OVER(PARTITION BY e.departmentId) AS max_salary,
        d.name as 'Department'
    FROM Employee e
    INNER JOIN Department d ON e.departmentId = d.id
) AS a
WHERE Salary=max_salary
