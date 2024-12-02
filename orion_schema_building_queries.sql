#Customer Table
ALTER TABLE customer 
ADD PRIMARY KEY (ï»¿Customer_ID);

#Customer and Orders Relationship
ALTER TABLE order_fact 
ADD FOREIGN KEY (ï»¿Customer_ID) REFERENCES customer(ï»¿Customer_ID) 
ON DELETE CASCADE 
ON UPDATE CASCADE;

#Product Dimension Table
ALTER TABLE product_dim 
ADD PRIMARY KEY (ï»¿Product_ID);

#Product Prices Relationship
ALTER TABLE prices 
ADD FOREIGN KEY (ï»¿Product_ID) REFERENCES product_dim(ï»¿Product_ID) 
ON DELETE CASCADE 
ON UPDATE CASCADE;

#Order Fact and Product Dimension Relationship
ALTER TABLE order_fact 
ADD FOREIGN KEY (Product_ID) REFERENCES product_dim(ï»¿Product_ID) 
ON DELETE CASCADE 
ON UPDATE CASCADE;

#Staff Table
ALTER TABLE staff 
ADD PRIMARY KEY (ï»¿Employee_ID);

##cleaning data inconsistencies 
DELETE FROM employee_addresses 
WHERE ï»¿Employee_ID NOT IN (SELECT ï»¿Employee_ID FROM staff);

#Employee Addresses
ALTER TABLE employee_addresses
ADD FOREIGN KEY (ï»¿Employee_ID) REFERENCES staff(ï»¿Employee_ID)
ON DELETE CASCADE
ON UPDATE CASCADE;

#cleaning data inconsistencies 
DELETE FROM employee_organization
WHERE Manager_ID NOT IN (SELECT ï»¿Employee_ID FROM staff);

#Employee Organization
ALTER TABLE employee_organization
ADD FOREIGN KEY (ï»¿Employee_ID) REFERENCES staff(ï»¿Employee_ID)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE employee_organization
ADD FOREIGN KEY (Manager_ID) REFERENCES staff(ï»¿Employee_ID)
ON DELETE CASCADE
ON UPDATE CASCADE;

##cleaning data inconsistencies 
DELETE FROM employee_payroll 
WHERE ï»¿Employee_ID NOT IN (SELECT ï»¿Employee_ID FROM staff);

#Employee Payroll
ALTER TABLE employee_payroll
ADD FOREIGN KEY (ï»¿Employee_ID) REFERENCES staff(ï»¿Employee_ID)
ON DELETE CASCADE
ON UPDATE CASCADE;

#Employee Donations
ALTER TABLE employee_donations
ADD FOREIGN KEY (ï»¿Employee_ID) REFERENCES staff(ï»¿Employee_ID)
ON DELETE CASCADE
ON UPDATE CASCADE;

#Sales and Employee Relationship
ALTER TABLE sales
ADD FOREIGN KEY (ï»¿Employee_ID) REFERENCES staff(ï»¿Employee_ID)
ON DELETE CASCADE
ON UPDATE CASCADE;


#Order Fact Table: Primary key for order_fact is composite (Order_ID + Product_ID):
ALTER TABLE order_fact
ADD PRIMARY KEY (Order_ID, Product_ID);


#Quarterly Sales: For qtr1_2007 and qtr2_2007, linked customer and order_fact tables
ALTER TABLE qtr1_2007
ADD FOREIGN KEY (Customer_ID) REFERENCES customer(ï»¿Customer_ID)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE qtr1_2007
ADD FOREIGN KEY (ï»¿Order_ID) REFERENCES order_fact(Order_ID)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE qtr2_2007
ADD FOREIGN KEY (Customer_ID) REFERENCES customer(ï»¿Customer_ID)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE qtr2_2007
ADD FOREIGN KEY (ï»¿Order_ID) REFERENCES order_fact(Order_ID)
ON DELETE CASCADE
ON UPDATE CASCADE;









