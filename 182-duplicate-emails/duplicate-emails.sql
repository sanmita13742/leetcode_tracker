with cte as (
    select email, dense_rank() over(partition by email order by id) as denserank from Person
)
select distinct(email) from cte where denserank <> 1;