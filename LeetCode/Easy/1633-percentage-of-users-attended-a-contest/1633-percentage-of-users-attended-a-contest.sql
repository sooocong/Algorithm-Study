SELECT
    R.contest_id,
    ROUND( R.reg_cnt / T.total * 100, 2 ) AS percentage
FROM
    (
        SELECT contest_id, COUNT(DISTINCT user_id) AS reg_cnt
        FROM Register
        GROUP BY contest_id
    ) R
CROSS JOIN
    (
        SELECT COUNT(*) AS total
        FROM Users
    ) T
ORDER BY 2 DESC, 1;