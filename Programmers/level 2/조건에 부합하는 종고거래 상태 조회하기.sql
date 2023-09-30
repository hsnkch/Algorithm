SELECT BOARD_ID,WRITER_ID,TITLE,PRICE, 
    CASE WHEN status = 'SALE' THEN '판매중'
    WHEN status = 'RESERVED' THEN '예약중' 
    WHEN status = 'DONE' THEN '거래완료' END status 
from USED_GOODS_BOARD 
where CREATED_DATE = '2022-10-05' 
order by BOARD_ID desc;