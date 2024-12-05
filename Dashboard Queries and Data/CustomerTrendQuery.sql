SELECT 
    DATE_FORMAT(order_date, '%Y-%m-01') AS month,
    SUM(Total_Retail_Price) AS total_sales,
    COUNT(order_id) AS total_orders
FROM order_fact
GROUP BY DATE_FORMAT(Order_Date, '%Y-%m-01')
ORDER BY month;