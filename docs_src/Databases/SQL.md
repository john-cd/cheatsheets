---
title: SQL Cheatsheet
category: databases
tags: SQL RDBMS
---
# SQL Cheatsheet

## DML: SELECT

*Filter*:

```SQL
SELECT LastName, FirstName, Address FROM Persons
WHERE Address IS NULL
```

*Like*:

```SQL
SELECT * FROM Customers
WHERE City LIKE 's%';

SELECT * FROM Customers
WHERE Country LIKE '%land%';

SELECT * FROM Customers
WHERE Country NOT LIKE '%land%';
```

*Sort*:

```SQL
SELECT * FROM Customers
ORDER BY Country DESC;

SELECT * FROM Customers
ORDER BY Country, CustomerName;
```

*Limit*:

```SQL
SELECT TOP number|percent column_name(s)
FROM table_name;

-- Examples:
SELECT TOP 2 * FROM Customers;

SELECT TOP 50 PERCENT * FROM Customers;
```

*Oracle Syntax*:

```SQL
SELECT column_name(s)
FROM table_name
WHERE ROWNUM <= number;
```

*Joins*:

```SQL
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
FULL OUTER JOIN Orders
ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerName;
```

*Union*:

```SQL
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;

SELECT column_name(s) FROM table1
UNION ALL
SELECT column_name(s) FROM table2;
```

*Select Into*:

```SQL
SELECT column_name(s)
INTO newtable [IN externaldb]
FROM table1;
```

*Formula*:

```SQL
SELECT ProductName, UnitPrice*(UnitsInStock+ISNULL(UnitsOnOrder,0))
FROM Products
```

## DML: INSERT

```SQL
INSERT INTO table_name
VALUES (value1,value2,value3,...);

INSERT INTO table_name (column1,column2,column3,...)
VALUES (value1,value2,value3,...);

-- Example:

INSERT INTO Customers (CustomerName, City, Country)
VALUES ('Cardinal', 'Stavanger', 'Norway');
```

*Insert from select*:

```SQL
INSERT INTO table2(column_name(s))
SELECT column_name(s)
FROM table1;

-- Example:

INSERT INTO Customers (CustomerName, Country)
SELECT SupplierName, Country FROM Suppliers
WHERE Country='Germany';
```

## DML: UPDATE

```SQL
UPDATE table_name
SET column1=value1,column2=value2,...
WHERE some_column=some_value;

-- Example:

UPDATE Customers
SET ContactName='Alfred Schmidt', City='Hamburg'
WHERE CustomerName='Alfreds Futterkiste';
```

## DML: DELETE

```SQL
DELETE FROM table_name
WHERE some_column=some_value;

DELETE FROM Customers
WHERE CustomerName='Alfreds Futterkiste' AND ContactName='Maria Anders';
```

## Databases

```SQL
CREATE DATABASE my_db;

DROP DATABASE my_db;
```

## Tables

*Create*:

```SQL
CREATE TABLE table_name
(
column_name1 data_type(size),
column_name2 data_type(size),
column_name3 data_type(size),
....
);

CREATE TABLE table_name
(
column_name1 data_type(size) constraint_name,
column_name2 data_type(size) constraint_name,
column_name3 data_type(size) constraint_name,
....
);
```

-- Examples

```SQL
CREATE TABLE Persons
(
P_Id int NOT NULL UNIQUE,
LastName varchar(255) NOT NULL,
FirstName varchar(255),
Address varchar(255),
City varchar(255)
)

CREATE TABLE Persons
(
P_Id int NOT NULL,
LastName varchar(255) NOT NULL,
FirstName varchar(255),
Address varchar(255),
City varchar(255),
CONSTRAINT uc_PersonID UNIQUE (P_Id, LastName)
)
```

```SQL
ALTER TABLE Persons
ADD CONSTRAINT uc_PersonID UNIQUE (P_Id,LastName)

ALTER TABLE Persons
DROP CONSTRAINT uc_PersonID
```

*Temporary Table*:

```SQL
CREATE TABLE #MyTempTable (cola INT PRIMARY KEY);
INSERT INTO #MyTempTable VALUES (1);
```

*Drop / Truncate*:

```SQL
DROP TABLE table_name

TRUNCATE TABLE table_name
```

## PRIMARY KEY constraint

```SQL
CREATE TABLE Persons
(
P_Id int NOT NULL PRIMARY KEY,
LastName varchar(255) NOT NULL,
FirstName varchar(255),
Address varchar(255),
City varchar(255)
)

CREATE TABLE Persons
(
P_Id int NOT NULL,
LastName varchar(255) NOT NULL,
FirstName varchar(255),
Address varchar(255),
City varchar(255),
CONSTRAINT PK_PersonID PRIMARY KEY (P_Id,LastName)
)

ALTER TABLE Persons
ADD CONSTRAINT PK_PersonID PRIMARY KEY (P_Id,LastName)

ALTER TABLE Persons
DROP CONSTRAINT PK_PersonID
```

## FOREIGN KEY constraints

```SQL
CREATE TABLE Orders
(
O_Id int NOT NULL PRIMARY KEY,
OrderNo int NOT NULL,
P_Id int FOREIGN KEY REFERENCES Persons(P_Id)
)

CREATE TABLE Orders
(
O_Id int NOT NULL,
OrderNo int NOT NULL,
P_Id int,
PRIMARY KEY (O_Id),
CONSTRAINT FK_PerOrders FOREIGN KEY (P_Id)
REFERENCES Persons(P_Id)
)
```

```SQL
ALTER TABLE Orders
ADD FOREIGN KEY (P_Id)
REFERENCES Persons(P_Id)

ALTER TABLE Orders
ADD CONSTRAINT fk_PerOrders
FOREIGN KEY (P_Id)
REFERENCES Persons(P_Id)

ALTER TABLE Orders
DROP CONSTRAINT fk_PerOrders
```

## CHECK Constraints

```SQL
CREATE TABLE Persons
(
P_Id int NOT NULL CHECK (P_Id>0),
LastName varchar(255) NOT NULL,
FirstName varchar(255),
Address varchar(255),
City varchar(255)
)

CREATE TABLE Persons
(
P_Id int NOT NULL,
LastName varchar(255) NOT NULL,
FirstName varchar(255),
Address varchar(255),
City varchar(255),
CONSTRAINT chk_Person CHECK (P_Id>0 AND City='Sandnes')
)
```

```SQL
ALTER TABLE Persons
ADD CONSTRAINT CHK_Person CHECK (P_Id>0 AND City='Sandnes')

ALTER TABLE Persons
DROP CONSTRAINT CHK_Person
```

## DEFAULT Constraints

```SQL
CREATE TABLE Orders
(
O_Id int NOT NULL,
OrderNo int NOT NULL,
P_Id int,
OrderDate date DEFAULT GETDATE()
)
```

```SQL
ALTER TABLE Persons
ALTER COLUMN City SET DEFAULT 'SEATTLE'

ALTER TABLE Persons
ALTER COLUMN City DROP DEFAULT
```

## Index

```SQL
CREATE UNIQUE INDEX index_name
ON table_name (column_name)

CREATE INDEX index_name
ON table_name (column_name1, col_name2)

-- Example:

CREATE INDEX PIndex
ON Persons (LastName, FirstName)
```

```SQL
DROP INDEX table_name.index_name

-- Example:

DROP INDEX IX_ProductVendor_BusinessEntityID
    ON Purchasing.ProductVendor;
```

## Add / drop / alter column in table

```SQL
ALTER TABLE table_name
ADD column_name datatype

ALTER TABLE table_name
DROP COLUMN column_name

ALTER TABLE table_name
ALTER COLUMN column_name datatype
```

## Autoincrement

``` SQL
CREATE TABLE Persons
(
ID int IDENTITY(1,1) PRIMARY KEY,
LastName varchar(255) NOT NULL,
FirstName varchar(255),
Address varchar(255),
City varchar(255)
)
```

Example:

```SQL
CREATE TABLE dbo.PurchaseOrderDetail
(
    PurchaseOrderID int NOT NULL
        REFERENCES Purchasing.PurchaseOrderHeader(PurchaseOrderID),
    LineNumber smallint NOT NULL,
    ProductID int NULL
        REFERENCES Production.Product(ProductID),
    UnitPrice money NULL,
    OrderQty smallint NULL,
    ReceivedQty float NULL,
    RejectedQty float NULL,
    DueDate datetime NULL,
    rowguid uniqueidentifier ROWGUIDCOL  NOT NULL
        CONSTRAINT DF_PurchaseOrderDetail_rowguid DEFAULT (newid()),
    ModifiedDate datetime NOT NULL
        CONSTRAINT DF_PurchaseOrderDetail_ModifiedDate DEFAULT (getdate()),
    LineTotal  AS ((UnitPrice*OrderQty)),
    StockedQty  AS ((ReceivedQty-RejectedQty)),
    CONSTRAINT PK_PurchaseOrderDetail_PurchaseOrderID_LineNumber
              PRIMARY KEY CLUSTERED (PurchaseOrderID, LineNumber)
              WITH (IGNORE_DUP_KEY = OFF)
)
ON PRIMARY;
```

## Views

```SQL
CREATE VIEW view_name AS
SELECT column_name(s)
FROM table_name
WHERE condition
```

```SQL
CREATE OR REPLACE VIEW view_name AS
SELECT column_name(s)
FROM table_name
WHERE condition
```

```SQL
DROP VIEW view_name
```

*Examples*:

```SQL
CREATE VIEW [Products Above Average Price] AS
SELECT ProductName,UnitPrice
FROM Products
WHERE UnitPrice > (SELECT AVG(UnitPrice) FROM Products)

SELECT * FROM [Products Above Average Price]
```

```SQL
CREATE VIEW [Category Sales For 1997] AS
SELECT DISTINCT CategoryName, Sum(ProductSales) AS CategorySales
FROM [Product Sales for 1997]
GROUP BY CategoryName
```

## Dates

```SQL
GETDATE()  -- Returns the current date and time

DATEPART() -- Returns a single part of a date/time

DATEADD()  -- Adds or subtracts a specified time interval from a date

DATEDIFF() -- Returns the time between two dates

CONVERT()  -- Displays date/time data in different formats
```

*Example*:

```SQL
CREATE TABLE Orders
(
OrderId int NOT NULL PRIMARY KEY,
ProductName varchar(50) NOT NULL,
OrderDate datetime NOT NULL DEFAULT GETDATE()
)

SELECT DATEPART(yyyy,OrderDate) AS OrderYear,
DATEPART(mm,OrderDate) AS OrderMonth,
DATEPART(dd,OrderDate) AS OrderDay,
FROM Orders
WHERE OrderId=1

SELECT OrderId,DATEADD(day,45,OrderDate) AS OrderPayDate
FROM Orders

SELECT DATEDIFF(day,'2008-06-05','2008-08-05') AS DiffDate

CONVERT(VARCHAR(19),GETDATE())
CONVERT(VARCHAR(10),GETDATE(),10)
CONVERT(VARCHAR(10),GETDATE(),110)
```

## SQL Server Data Types

**Data type / Description / Storage**

`char(n)`
Fixed width character string. Maximum 8,000 characters
Defined width

`varchar(n)`
Variable width character string. Maximum 8,000 characters
2 bytes + number of chars

`varchar(max)`
Variable width character string. Maximum 1,073,741,824 characters
2 bytes + number of chars

`text`
Variable width character string. Maximum 2GB of text data
4 bytes + number of chars

`nchar`
Fixed width Unicode string. Maximum 4,000 characters
Defined width x 2

`nvarchar`
Variable width Unicode string. Maximum 4,000 characters

`nvarchar(max)`
Variable width Unicode string. Maximum 536,870,912 characters

`ntext`
Variable width Unicode string. Maximum 2GB of text data

`bit`
Allows 0, 1, or NULL

`binary(n)`
Fixed width binary string. Maximum 8,000 bytes

`varbinary`
Variable width binary string. Maximum 8,000 bytes

`varbinary(max)`
Variable width binary string. Maximum 2GB

`image`
Variable width binary string. Maximum 2GB

### Number types

`tinyint`
Allows whole numbers from 0 to 255
1 byte

`smallint`
Allows whole numbers between -32,768 and 32,767
2 bytes

`int`
Allows whole numbers between -2,147,483,648 and 2,147,483,647
4 bytes

`bigint`
Allows whole numbers between -9,223,372,036,854,775,808 and 9,223,372,036,854,775,807
8 bytes

`decimal(p,s)`
Fixed precision and scale numbers.
Allows numbers from -10^38 +1 to 10^38.

The p parameter indicates the maximum total number of digits that can be stored (both to the left and to the right of the decimal point). p must be a value from 1 to 38. Default is 18. The s parameter indicates the maximum number of digits stored to the right of the decimal point. s must be a value from 0 to p. Default value is 0.
5-17 bytes

`numeric(p,s)`
Fixed precision and scale numbers.
Allows numbers from -10^38 +1 to 10^38.

The p parameter indicates the maximum total number of digits that can be stored (both to the left and to the right of the decimal point). p must be a value from 1 to 38. Default is 18. The s parameter indicates the maximum number of digits stored to the right of the decimal point. s must be a value from 0 to p. Default value is 0.
5-17 bytes

`smallmoney`
Monetary data from -214,748.3648 to 214,748.3647
4 bytes

`money`
Monetary data from -922,337,203,685,477.5808 to 922,337,203,685,477.5807
8 bytes

`float(n)`
Floating precision number data from -1.79E + 308 to 1.79E + 308.
The n parameter indicates whether the field should hold 4 or 8 bytes. float(24) holds a 4-byte field and float(53) holds an 8-byte field. Default value of n is 53.
4 or 8 bytes

`real`
Floating precision number data from -3.40E + 38 to 3.40E + 38
4 bytes

### Date types

`datetime`
From January 1, 1753 to December 31, 9999 with an accuracy of 3.33 milliseconds
8 bytes

`datetime2`
From January 1, 0001 to December 31, 9999 with an accuracy of 100 nanoseconds
6-8 bytes

`smalldatetime`
From January 1, 1900 to June 6, 2079 with an accuracy of 1 minute
4 bytes

`date`
Store a date only. From January 1, 0001 to December 31, 9999
3 bytes

`time`
Store a time only to an accuracy of 100 nanoseconds
3-5 bytes

`datetimeoffset`
The same as datetime2 with the addition of a time zone offset
8-10 bytes

`timestamp`
Stores a unique number that gets updated every time a row gets created or modified. The timestamp value is based upon an internal clock and does not correspond to real time. Each table may have only one timestamp variable

### Other data types

`sql_variant`
Stores up to 8,000 bytes of data of various data types, except text, ntext, and timestamp

`uniqueidentifier`
Stores a globally unique identifier (GUID)

`xml`
Stores XML formatted data. Maximum 2GB

`cursor`
Stores a reference to a cursor used for database operations

`table`
Stores a result-set for later processing

## SQL Aggregate Functions

SQL aggregate functions return a single value, calculated from values in a column.

Useful aggregate functions:

* `AVG()`   - Returns the average value
* `COUNT()` - Returns the number of rows
* `TOP 1`   - Single sample
* `MAX()`   - Returns the largest value
* `MIN()`   - Returns the smallest value
* `SUM()`   - Returns the sum

Examples:

```SQL
SELECT COUNT(DISTINCT column_name) FROM table_name;

SELECT TOP 1 column_name FROM table_name
ORDER BY column_name DESC;

SELECT column_name, aggregate_function(column_name)
FROM table_name
WHERE column_name operator value
GROUP BY column_name;

SELECT Shippers.ShipperName, COUNT(Orders.OrderID) AS NumberOfOrders
FROM Orders
LEFT JOIN Shippers
ON Orders.ShipperID=Shippers.ShipperID
GROUP BY ShipperName;

SELECT column_name, aggregate_function(column_name)
FROM table_name
WHERE column_name operator value
GROUP BY column_name
HAVING aggregate_function(column_name) operator value;

SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders
FROM Orders
INNER JOIN Employees
ON Orders.EmployeeID=Employees.EmployeeID)
GROUP BY LastName
HAVING COUNT(Orders.OrderID) > 10;
```

## SQL Scalar functions

* Converts a field to upper case: SELECT UPPER(column_name) FROM table_name;
* Converts a field to lower case: SELECT LOWER(column_name) FROM table_name;
* MID() - Extract characters from a text field
* LEN() - Returns the length of a text field
* ROUND() - Rounds a numeric field to the number of decimals specified
* NOW() - Returns the current system date and time
* FORMAT() - Formats how a field is to be displayed

```SQL
SELECT ProductName, ROUND(Price,0) AS RoundedPrice
FROM Products;
```

## Variables

```SQL
DECLARE @myvar char(20);
SET @myvar = 'This is a test';
SELECT @myvar;
```

## Scalar Function

```SQL
CREATE FUNCTION FunctionName
(
-- Add the parameters for the function here
@p1 int
)
RETURNS int
AS
BEGIN
-- Declare the return variable here
DECLARE @Result int
-- Add the T-SQL statements to compute the return value here
SELECT @Result = @p1

-- Return the result of the function
RETURN @Result
END
```

## Table Value Function

```SQL
IF OBJECT_ID (N'dbo.EmployeeByID' ) IS NOT NULL
   DROP FUNCTION dbo.EmployeeByID
GO

CREATE FUNCTION dbo.EmployeeByID(@InEmpID int)
RETURNS @retFindReports TABLE
(
	-- columns returned by the function
	EmployeeID int NOT NULL,
	Name nvarchar(255 ) NOT NULL,
	Title nvarchar(50 ) NOT NULL,
	EmployeeLevel int NOT NULL
)
AS
-- body of the function
BEGIN
   WITH DirectReports(Name , Title , EmployeeID , EmployeeLevel , Sort ) AS
	(SELECT CONVERT( varchar(255 ), c .FirstName + ' ' + c.LastName ),
		e.Title ,
		e.EmployeeID ,
		1 ,
		CONVERT(varchar (255), c. FirstName + ' ' + c .LastName)
	 FROM HumanResources.Employee AS e
		  JOIN Person.Contact AS c ON e.ContactID = c.ContactID
	 WHERE e.EmployeeID = @InEmpID
   UNION ALL
	 SELECT CONVERT (varchar( 255), REPLICATE ( '| ' , EmployeeLevel) +
		c.FirstName + ' ' + c. LastName),
		e.Title ,
		e.EmployeeID ,
		EmployeeLevel + 1,
		CONVERT ( varchar(255 ), RTRIM (Sort) + '| ' + FirstName + ' ' +
				 LastName)
	 FROM HumanResources.Employee as e
		  JOIN Person.Contact AS c ON e.ContactID = c.ContactID
		  JOIN DirectReports AS d ON e. ManagerID = d. EmployeeID
	)
   -- copy the required columns to the result of the function

   INSERT @retFindReports
   SELECT EmployeeID, Name, Title, EmployeeLevel
	 FROM DirectReports
   ORDER BY Sort
   RETURN
END
GO
```

## Stored Procedure

```SQL
CREATE PROCEDURE ProcedureName
		-- Add the parameters for the stored procedure here
		@p1 int = 0 ,
		@p2 int = 0
AS
BEGIN
		-- SET NOCOUNT ON added to prevent extra result sets from
		-- interfering with SELECT statements.
		SET NOCOUNT ON;

	-- Insert statements for procedure here
		SELECT @p1 , @p2
END
GO
```

## Self-join

Q. Here's the data in a table 'orders'

	customer_id order_id order_day
	123        27424624    25Dec2011
	123        89690900    25Dec2010
	797        12131323    25Dec2010
	876        67145419    15Dec2011

Could you give me SQL for customers who placed orders on both the days, 25th Dec 2010 and 25th Dec 2011?

```SQL
	SELECT o.customer_id, o.order_day
	FROM orders AS o
	INNER JOIN orders AS o1
	ON o.customer_id = o1.customer_id
	WHERE ...
```
