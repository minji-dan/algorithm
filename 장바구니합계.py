-- 20221030 
-- 각 장바구니의 아이디 결제일 결제금액, order by cart_id
-- 83 139500
-- 195 49270

select a.id, a.payed_at, sum(b.price)
from carts a, cart_products b
where a.id=b.cart_id
group by a.id
order by a.id
