-- SELECT machine_id, () AS processing_time
-- FROM Activity
-- WHERE 


SELECT A.machine_id, ROUND(AVG(B.timestamp - A.timestamp), 3) AS processing_time
FROM Activity A
JOIN Activity B
WHERE A.machine_id = B.machine_id AND A.process_id = B.process_id AND B.activity_type = 'end' AND A.activity_type = 'start'
GROUP BY 1