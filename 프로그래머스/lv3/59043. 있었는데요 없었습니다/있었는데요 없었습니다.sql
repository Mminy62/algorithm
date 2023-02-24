# 입양일이 잘못 입력되었다. 보호 시작일보다 입양일이 더 빠른 것 찾기
# 아이디, 이름 출력, 보호 시작일이 빠른순으로 
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.DATETIME > B.DATETIME
ORDER BY A.DATETIME

