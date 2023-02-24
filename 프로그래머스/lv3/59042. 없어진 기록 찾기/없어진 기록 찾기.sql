# ANIMAL_ID 는 외래키
# 입양 간 기록은 있지만, 보호소에 들어온 기록은 없는 id, 이름을 id 순으로 출력
# 왼쪽(animal_OUTS) outer join해서 있는 것만 # 즉, 왼쪽에서 오른쪽을 뺀것, 공통을 뺀 것
# 공통 부분도 어차피 왼쪽 부분의 일부 이므로 left join 하면 되지만, 공통분모를 뺄 경우 where B.key is null 을 작성해주면 된다.
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_OUTS A LEFT OUTER JOIN ANIMAL_INS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL
ORDER BY A.ANIMAL_ID ASC
