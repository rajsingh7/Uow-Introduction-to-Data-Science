SELECT row_num,col_num, SUM(value) AS value
FROM(
  SELECT A.row_num, B.col_num, A.value*B.value AS value
  FROM A JOIN B
  ON A.col_num=B.row_num)
GROUP BY row_num, col_num;