SELECT NULLIF(unique_id, "") AS unique_id, name
FROM Employees A
LEFT JOIN EmployeeUNI B ON A.id = B.id