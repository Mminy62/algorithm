-- 코드를 입력하세요
SELECT A.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(B.REVIEW_SCORE), 2) average
FROM REST_INFO A JOIN REST_REVIEW B
    ON A.REST_ID = B.REST_ID
WHERE ADDRESS LIKE "서울%" and REVIEW_SCORE IS NOT NULL
GROUP BY A.REST_ID
ORDER BY average DESC, FAVORITES DESC;