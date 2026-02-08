SELECT product_name, year, price
FROM Sales A
JOIN Product B ON A.product_id  = B.product_id