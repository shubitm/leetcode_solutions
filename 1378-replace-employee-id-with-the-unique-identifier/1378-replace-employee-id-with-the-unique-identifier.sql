SELECT COALESCE(euni.unique_id, NULL) AS unique_id, e.name
FROM Employees e  
LEFT JOIN EmployeeUNI euni  
ON e.id = euni.id;