SELECT ROUND(AVG(B.player_id IS NOT NULL) * 1.0, 2) AS fraction
FROM (
    SELECT player_id, MIN(event_date) AS first_day
    FROM Activity
    GROUP BY player_id
) A
LEFT JOIN Activity B
  ON A.player_id = B.player_id
 AND B.event_date = DATE_ADD(A.first_day, INTERVAL 1 DAY)