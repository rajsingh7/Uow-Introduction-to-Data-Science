/*count the number of unique documents that contain both the word 'transactions' and the word 'world'*/

select count(*)
from(
select distinct f1.docid
from frequency f1, frequency f2
where f1.docid = f2.docid 
    and f1.term = "transactions"
	and f2.term = "world");