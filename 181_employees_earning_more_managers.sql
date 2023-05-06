SELECT
 a.Name as 'Employee'
FROM
 employee AS a,
 employee AS b
WHERE
 b.Id = a.managerId
 AND
 a.salary > b.salary;