-- ID가 홀수이고 설명이 비어 있지 않은 영화를 보고하는 솔루션을 작성하세요 "boring".
-- 결과 테이블을 rating 내림차순
SELECT *
FROM Cinema
WHERE MOD(id , 2) = 1 AND description NOT IN ('boring')
ORDER BY rating DESC