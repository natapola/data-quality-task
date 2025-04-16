select *
from customers c 
where customer_id is null;


select email 
from customers c 
where email not like '%@%.%';


select count(*) as duplicates
from customers c 
group by customer_id
having count(*) >1;


select email, count(email) as duplicates
from customers c 
group by email
having count(*) >1;


select count(distinct email) as uniq_email,
		count(distinct concat(first_name, last_name)) as uniq_full_name
from customers c ;


select customer_id
from customers c 
where customer_id < 0;


select *
from products p 
where product_id is null or product_name is null or category is null or price is null;


select count(*) as duplicates
from products p 
group by product_id, product_name, category, price
having count(*) > 1;


select price 
from products p
where price < 0;


select p.category, count(t.transaction_id) as count_items
from products p 
right join transactions t on t.product_id = p.product_id
group by p.category;


select p.product_id, count(p.product_id) as count_product_id, p.category
from products p
join transactions t on t.product_id = p.product_id
group by p.product_id
order by count_product_id;


select *
from transactions t 
where transaction_id is null or transaction_date is null or product_id is null or amount is null;


select count(*) as duplocates
from transactions t 
group by transaction_id, transaction_date, product_id, amount
having count(*) > 1;


select *
from transactions t 
where amount < 0;


select count(amount) as count_null_amount
from transactions t 
where amount <0;


select p.product_id, p.price, t.amount,
case 
	when p.price = t.amount then 'correct'
	when p.price <> t.amount then 'incorrect'
end
from products p 
right join transactions t on t.product_id = p.product_id;


select count(*) as count_incorrect
from (select p.product_id, p.price, t.amount,
case 
	when p.price = t.amount then 'correct'
	when p.price <> t.amount then 'incorrect'
end as status
from products p 
right join transactions t on t.product_id = p.product_id)
where status = 'incorrect';







