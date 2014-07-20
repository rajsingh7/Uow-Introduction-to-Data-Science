select row_num,col_num, sum(value) as value
from(
  select A.row_num, B.col_num, A.value*B.value as value
  from A join B
  on A.col_num=B.row_num)
group by row_num, col_num;