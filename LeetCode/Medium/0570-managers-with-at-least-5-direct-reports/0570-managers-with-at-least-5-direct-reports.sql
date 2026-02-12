WITH SS AS (
    SELECT id, name, managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(*) >= 5
)

SELECT B.name
FROM SS A
JOIN Employee B ON A.managerId = B.id