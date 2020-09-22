
You have to create one more column in predefined table with Name, Id,Department, and Salary.Now you have to create new column with Rank in it partition by Department

SELECT Name, Id, Department, Salary,
(SELECT COUNT(*) + 1 FROM Emp A
WHERE A.Department = B.Department AND A.Salary > B.Salary) As Rank
FROM Emp B
ORDER BY Department, Salary DESC