create TEMP view QUERY as
select * from frequency
union
select 'q' as docid, 'washington' as term, 1 as count 
union
select 'q' as docid, 'taxes' as term, 1 as count
union 
select 'q' as docid, 'treasury' as term, 1 as count;

select max(score)
from(
select d1, d2, sum(count) as score from
(select A.docid d1, B.docid d2, A.count * B.count as count
from QUERY A 
join QUERY B
ON A.term = B.term and A.docid='q')
group by d1, d2
order by score);