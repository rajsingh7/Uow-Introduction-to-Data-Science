/*find all documents that have more than 300 total terms, including duplicate terms. */

select count(*)
from (
select *
from frequency
group by docid
having sum(count) > 300);