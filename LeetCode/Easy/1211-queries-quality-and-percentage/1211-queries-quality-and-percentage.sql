SELECT
    Q.query_name,
    ROUND(SUM(Q.rating / Q.position) / COUNT(*), 2) AS quality,
    ROUND(IFNULL(P.poor_query, 0) / COUNT(*) * 100, 2) AS poor_query_percentage
FROM Queries Q
LEFT JOIN (SELECT query_name, COUNT(query_name) AS poor_query
            FROM Queries
            WHERE rating < 3
            GROUP BY 1) P
ON Q.query_name = P.query_name
GROUP BY 1;