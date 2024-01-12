select Product.product_name as product_name, Sales.year as year, Sales.price as price
from Sales
left join Product on Sales.product_id = Product.product_id