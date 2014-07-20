create TEMP view Subset as
select * from frequency
where docid='10080_txt_crude' or docid='17035_txt_earn';

select sum(count) from
(select A.docid da, B.docid db, A.count * B.count as count
from Subset A 
join Subset B
on A.term = B.term and A.docid < B.docid)
group by da, db;