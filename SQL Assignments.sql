-- Question 1 ---> Retrieve customer data

-- 1. Retrive Customer Details

SELECT * 
FROM SalesLT.Customer;

--2. Retrieve customer name data
SELECT 
    Title,
    FirstName,
    MiddleName,
    LastName,
    Suffix
FROM SalesLT.Customer;


--3. Retrieve customer names and phone numbers

 SELECT Salesperson, ISNULL(Title,'') + ' ' + LastName AS CustomerName, Phone
 FROM SalesLT.Customer;



 -- Question 2 : Retrieve data for transportation reports

-- 1. Retrieve a list of cities
 SELECT DISTINCT City, StateProvince
 FROM SalesLT.Address
 
 --2. Retrieve the heaviest products
 SELECT TOP (10) PERCENT WITH TIES Name
 FROM SalesLT.Product
 ORDER BY Weight DESC;


 -- Quesion 3: Retrieve product data

 --1. Retrieve product details for product model 1
 SELECT Name, Color, Size
 FROM SalesLT.Product
 WHERE ProductModelID = 1;

 --2. Filter products by color and size
 SELECT ProductNumber, Name
 FROM SalesLT.Product
 WHERE Color IN ('Black','Red','White') AND Size IN ('S','M');

 --3.Filter products by product number
 SELECT ProductNumber, Name, ListPrice
 FROM SalesLT.Product
 WHERE ProductNumber LIKE 'BK-%';

 --4.Retrieve specific products by product number 
 SELECT ProductNumber, Name, ListPrice
 FROM SalesLT.Product
 WHERE ProductNumber LIKE 'BK-[^R]%-[0-9][0-9]';


--Question 4.Generate invoice reports

--1. Retrieve customer orders 
 SELECT c.CompanyName, oh.SalesOrderID, oh.TotalDue
 FROM SalesLT.Customer AS c
 JOIN SalesLT.SalesOrderHeader AS oh
     ON oh.CustomerID = c.CustomerID;


 -- Question 5: Retrieve customer data

	-- 1.	Retrieve a list of all customers and their orders

SELECT a.AddressType,a.CustomerID,so.AddressLine1,so.City,so.StateProvince,so.Postalcode,so.CountryRegion FROM SalesLT.CustomerAddress AS a
JOIN SalesLT.Address AS so ON a.AddressID = so.AddressID
WHERE a.AddressType = 'Main Office';

 -- 2.	Retrieve a list of customers with no address
SELECT CustomerID,CompanyName,FirstName,LastName,Phone FROM SalesLT.Customer
SELECT AddressType,AddressID FROM SalesLT.CustomerAddress
SELECT a.CustomerID,a.CompanyName,a.FirstName,a.LastName,a.Phone,so.AddressID,so.AddressType FROM SalesLT.Customer AS a
JOIN SalesLT.CustomerAddress AS so ON a.CustomerID = so.CustomerID WHERE so.AddressID IS NULL;


 -- Question 6 : Retrieve order shipping information

  --1. Retrieve the order ID and freight cost of each order.
SELECT[SalesOrderID] ,ROUND(Freight, 2) AS FreightCost FROM SalesLT.SalesOrderHeader;

 -- 2.	Add the shipping method.
SELECT [SalesOrderID],ROUND(Freight, 2) AS FreightCost,LOWER(ShipMethod) AS ShippingMethod FROM SalesLT.SalesOrderHeader;

  -- 3.	Add shipping date details.
SELECT [SalesOrderID], ROUND(Freight, 2) AS FreightCost,LOWER(ShipMethod) AS ShippingMethod,YEAR(ShipDate) AS ShipYear,DATENAME(MONTH, ShipDate) AS ShipMonth,DAY(ShipDate) AS ShipDay FROM SalesLT.SalesOrderHeader;

  -- Quesion 7 : Aggregate product sales

-- 1.	Retrieve total sales by product
SELECT  p.Name AS ProductName,SUM(sod.LineTotal) AS TotalRevenue
FROM SalesLT.Product AS p
JOIN SalesLT.SalesOrderDetail AS sod ON p.ProductID = sod.ProductID GROUP BY p.Name ORDER BY TotalRevenue DESC;

-- 2.	Filter the product sales list to include only products that cost over 1,000
SELECT p.Name AS ProductName,SUM(sod.LineTotal) AS TotalRevenue FROM SalesLT.Product AS p
JOIN SalesLT.SalesOrderDetail AS sod ON p.ProductID = sod.ProductID WHERE p.ListPrice > 1000 GROUP BY p.Name ORDER BY TotalRevenue DESC;

-- 3.	Filter the product sales groups to include only total sales over 20,000

SELECT p.Name AS ProductName,SUM(sod.LineTotal) AS TotalRevenue FROM SalesLT.Product AS p
JOIN SalesLT.SalesOrderDetail AS sod ON p.ProductID = sod.ProductID WHERE p.ListPrice > 1000 GROUP BY p.Name HAVING SUM(sod.LineTotal) > 20000 ORDER BY
    TotalRevenue DESC;
