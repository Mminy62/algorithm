# -- 코드를 입력하세요
select convert(DATE_FORMAT(A.start_date, "%m"), unsigned) MONTH, A.CAR_ID CAR_ID, COUNT(*)
from CAR_RENTAL_COMPANY_RENTAL_HISTORY A 
where A.CAR_ID IN
    (SELECT CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where DATE_FORMAT(start_date, "%m") >= 8 and DATE_FORMAT(start_date, "%m") <= 10
    group by CAR_ID
    having COUNT(*) >= 5)
    # and 
 and DATE_FORMAT(A.start_date, "%m") >= 8 and DATE_FORMAT(A.start_date, "%m") <= 10
group by DATE_FORMAT(A.start_date, "%m"), A.car_id
having COUNT(*) != 0
order by MONTH, CAR_ID DESC



# '''
# SELECT MONTH(START_DATE) AS MONTH, R.CAR_ID, COUNT(*) AS RECORDS
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY R
# WHERE R.CAR_ID IN (
#     SELECT CAR_ID
#     FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
#     WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
#     GROUP BY CAR_ID
#     HAVING COUNT(*) >= 5
# )
# AND R.START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
# GROUP BY MONTH(START_DATE), R.CAR_ID
# HAVING COUNT(*) > 0
# ORDER BY MONTH(START_DATE), R.CAR_ID DESC;'''

-- 자동차 아이디별로 8월에 몇번 빌렸는지