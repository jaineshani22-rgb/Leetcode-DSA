# Write your MySQL query statement below
WITH AllProducts AS (
    SELECT DISTINCT product_id
    FROM Products
),
LatestPrice AS (
    SELECT 
        product_id,
        new_price,
        ROW_NUMBER() OVER (
            PARTITION BY product_id 
            ORDER BY change_date DESC
        ) AS rn
    FROM Products
    WHERE change_date <= '2019-08-16'
)
SELECT 
    ap.product_id,
    COALESCE(lp.new_price, 10) AS price
FROM AllProducts ap
LEFT JOIN LatestPrice lp
    ON ap.product_id = lp.product_id
   AND lp.rn = 1;