UPDATE orion_stores.order_fact
SET Total_Retail_Price = CAST(REPLACE(REPLACE(Total_Retail_Price, '$', ''), ',', '') AS DECIMAL(10, 2)),
    CostPrice_Per_Unit = CAST(REPLACE(REPLACE(CostPrice_Per_Unit, '$', ''), ',', '') AS DECIMAL(10, 2));
    
SELECT 
	b.Product_Category,
    SUM(a.Total_Retail_Price) AS Total_Sales,
    SUM(a.CostPrice_Per_Unit * a.Quantity) AS Total_Cost,
    SUM(a.Total_Retail_Price) - SUM(a.CostPrice_Per_Unit * a.Quantity) AS Profit
FROM 
    order_fact AS a
JOIN product_dim AS b
ON a.Product_ID = b.ï»¿Product_ID
GROUP BY 
    Product_Category;