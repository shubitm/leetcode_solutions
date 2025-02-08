SELECT M.name
FROM Employee E
JOIN Employee M ON E.managerId = M.id
GROUP BY M.id
HAVING COUNT(E.id) >= 5;