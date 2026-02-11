WITH SS AS (
    SELECT *
    FROM Students
    CROSS JOIN Subjects
)

SELECT
    A.student_id,
    A.student_name,
    A.subject_name,
    COUNT(B.subject_name) AS attended_exams
FROM SS A
LEFT JOIN Examinations B
ON A.student_id = B.student_id AND A.subject_name = B.subject_name
GROUP BY 1, 2, 3
ORDER BY 1, 3;