SELECT
    A.product_id,
    IFNULL(ROUND(SUM(A.price * B.units) / NULLIF(SUM(B.units), 0), 2), 0) AS average_price
FROM Prices A
LEFT JOIN UnitsSold B
ON A.product_id = B.product_id AND B.purchase_date BETWEEN A.start_date AND A.end_date
GROUP BY 1;