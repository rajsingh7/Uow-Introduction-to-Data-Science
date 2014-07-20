/*  count the number of documents containing the word "parliament"*/
select count(docid)
from frequency
where term = "parliament";