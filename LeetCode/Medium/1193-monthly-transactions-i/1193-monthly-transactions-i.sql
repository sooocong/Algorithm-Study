SELECT
    DATE_FORMAT(A.trans_date, '%Y-%m') AS month,
    A.country,
    COUNT(*) AS trans_count,
    MAX(IFNULL(B.approved_count, 0)) AS approved_count,
    SUM(A.amount) AS trans_total_amount,
    MAX(IFNULL(B.approved_total_amount, 0)) AS approved_total_amount
FROM Transactions A
LEFT JOIN (
    SELECT
        DATE_FORMAT(trans_date, '%Y-%m') AS month,
        country,
        SUM(amount) AS approved_total_amount,
        COUNT(*) AS approved_count
    FROM Transactions
    WHERE state = 'approved'
    GROUP BY 1, 2
) B ON DATE_FORMAT(A.trans_date, '%Y-%m') = B.month AND A.country <=> B.country
GROUP BY 1, 2;