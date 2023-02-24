# 보호소에 들어올땐 중성화가 안됨 -> 입양될 땐 중성화 된 친구들
# id, type, name 출력 id asc 순으로 
SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_INS A JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.SEX_UPON_INTAKE IN ("Intact Male", "Intact Female") AND B.SEX_UPON_OUTCOME IN ("Spayed Female", "Neutered Male")
ORDER BY A.ANIMAL_ID ASC