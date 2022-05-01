
/*
Query 1
Find the average price of “iPhone Xs” on Shiokee from 1 August 2021 to 31 August 2021.
*/
SELECT AVG(Y.Price) AS ave_price_iphoneX
FROM PRODUCTS_IN_SHOPS_1 AS X, PRICE_HISTORY AS Y
WHERE X.PName = ‘iPhoneX’ AND  X.PName = Y.PName AND X.SName = Y.SName AND Y.P_start_date >= ‘2021-08-01 00:00:00’ AND Y.P_end_date <= ‘2021-08-31 23:59:59’

/*
Query 2
Find products that received at least 100 ratings of “5” in August 2021, and order them by
their average ratings.
*/
WITH all_ratings AS (
	SELECT PName, COUNT(Rating) as CntRatings
	FROM FEEDBACKS
	WHERE Rating = 5
	GROUP BY PName
    	HAVING COUNT(Rating) >=100)
SELECT FEEDBACKS.PName, AVG(Rating) as Average_rating
FROM FEEDBACKS
INNER JOIN all_ratings temp
ON temp.PName = FEEDBACKS.PName
GROUP BY FEEDBACKS.PName
ORDER BY Average_rating DESC

/*
Query 3
For all products purchased in June 2021 that have been delivered, find the average time
from the ordering date to the delivery date.
*/
SELECT PName, AVG(DATEDIFF(DAY, Date_time, Delivery_date)) AS  Average_time_taken
FROM PRODUCTS_IN_ORDERS, ORDERS  
WHERE Order_status = 'delivered'
AND MONTH(Date_time) = 6
AND YEAR(Date_time) = 2021
AND ORDERS.OrderID = PRODUCTS_IN_ORDERS.OrderID
GROUP BY PName

/*
Query 4
Let us define the “latency” of an employee by the average that he/she takes to process
a complaint. Find the employee with the smallest latency.
*/
-- (1) Find latency of each employee
WITH [EmployeeLatency] AS (
	SELECT H.EmployeeID, AVG(DATEDIFF(second, C.Filed_date_time, H.Handled_date_time)) AS Latency
	FROM COMPLAINTS AS C, HANDLED AS H
	WHERE C.Complaint_status = 'addressed' AND
	C.EmployeeID = H.EmployeeID
	GROUP BY H.EmployeeID)
-- (2) Actual query
SELECT E.EmployeeID, E.EName, EL.Latency
FROM [EmployeeLatency] AS EL
	INNER JOIN EMPLOYEES AS E
	ON EL.EmployeeID = E.EmployeeID
WHERE EL.Latency = (
	SELECT MIN(Latency)
	FROM [EmployeeLatency]
)

/*
Query 5
Produce a list that contains (i) all products made by Samsung, and (ii) for each of them,
the number of shops on Shiokee that sell the product.
*/
-- Q5 i)
SELECT DISTINCT PName
FROM PRODUCTS
WHERE Maker = ‘Samsung’
-- Q5 ii)
SELECT PS.PName, COUNT(*) AS Num_of_shops
FROM PRODUCTS_IN_SHOPS_1 AS PS, PRODUCTS AS P
WHERE Maker = ‘Samsung’ AND PS.PName = P.PName
GROUP BY PS.PName

/*
Query 6
Find shops that made the most revenue in August 2021.
*/
WITH ShopRevenue AS (
	SELECT SName, SUM(OPrice*OQuantity) AS Revenue
FROM PRODUCTS_IN_ORDERS
WHERE Delivery_date >= ‘2021-08-01 00:00:00’
AND Delivery_date <= ‘2021-08-31 23:59:59’
GROUP BY SName
)
SELECT SName, Revenue
FROM ShopRevenue
WHERE Revenue = (
SELECT MAX(Revenue)
FROM ShopRevenue
)

/*
Query 7
For users that made the most amount of complaints, find the most expensive products he/she
has ever purchased.
*/
-- (1) Counting number of complaints for each userID
WITH [NumComplaints] AS 
(
	SELECT UserID, COUNT(*) AS Cnt
	FROM COMPLAINTS
	GROUP BY UserID
),
-- (2) Finding UserID with most complaints
[UserMaxComplaints] AS 
(
	SELECT UserID
	FROM (
		SELECT MAX([NumComplaints].Cnt) AS maxCnt
		FROM [NumComplaints] 
		) AS MaxComplaints INNER JOIN [NumComplaints] ON [NumComplaints].Cnt = MaxComplaints.maxCnt
),
-- (3) Joining UserID, Pname, OPrice into 1 table
[UserProductPrice] AS 
(
	SELECT ORDERS.UserID, Pname, OPrice 
	FROM (
		[UserMaxComplaints] INNER JOIN ORDERS ON [UserMaxComplaints].UserID = ORDERS.UserID 
		INNER JOIN PRODUCTS_IN_ORDERS ON ORDERS.OrderID = PRODUCTS_IN_ORDERS.OrderID
		)
)
-- (4) Actual query
SELECT DISTINCT MaxPrice.UserID, UName, Pname AS Most_expensive_product, OPrice AS Price
FROM (
	SELECT UserID, MAX(OPrice) AS Max_price
	FROM [UserProductPrice]
	GROUP BY UserID
	) AS MaxPrice 
	INNER JOIN [UserProductPrice] ON Max_price = OPrice 
	INNER JOIN USERS ON MaxPrice.UserID = USERS.UserID;

/*
Query 8
Find products that have never been purchased by some users, but are the top 5 most purchased
products by other users in August 2021.
*/
-- products that are not purchased by everyone 
WITH R2 AS 
(
SELECT P.PName, COUNT(DISTINCT O.userID) AS Unique_buyers
FROM PRODUCTS_IN_ORDERS AS P, ORDERS AS O
WHERE O.orderID = P.orderID
GROUP BY P.PName --num of unique buyers for every product
HAVING COUNT(DISTINCT O.userID) < (SELECT COUNT(*) FROM USERS)
)
-- top 5 most purchased products in August 2021
SELECT TOP 5 R2.PName, SUM(P2.OQuantity) AS Num_of_Times_purchased
FROM PRODUCTS_IN_ORDERS AS P2
INNER JOIN R2 ON P2.PName = R2.PName
INNER JOIN ORDERS ON P2.OrderID = ORDERS.OrderID
WHERE YEAR(ORDERS.Date_time) = 2021 AND
	  MONTH(ORDERS.Date_time) = 8
GROUP BY R2.PName
ORDER BY Num_of_Times_purchased DESC;

/*
Query 9
Find products that are increasingly being purchased over at least 3 months.
*/
WITH PTSD AS (
    SELECT PO.PName, SUM(PO.OQuantity) AS Sum_quantity, MONTH(O.Date_time) AS Month, YEAR(O.Date_time) AS Year
    FROM PRODUCTS_IN_ORDERS AS PO
    INNER JOIN ORDERS AS O
    ON PO.OrderID = O.OrderId
    GROUP BY PO.PName, MONTH(O.Date_time), YEAR(O.Date_time)
)
SELECT DISTINCT PTSD1.PName
FROM PTSD AS PTSD1
INNER JOIN PTSD AS PTSD2
ON PTSD1.PName = PTSD2.PName
AND PTSD1.Sum_quantity > PTSD2.Sum_quantity
AND (
    (PTSD1.Year = PTSD2.Year
        AND PTSD1.Month = PTSD2.Month + 1
    ) OR (PTSD1.Year = PTSD2.Year + 1
        AND PTSD1.Month = 12
        AND PTSD2.Month = 1
    )
)
INNER JOIN PTSD AS PTSD3
ON PTSD2.PName = PTSD3.PName
AND PTSD2.Sum_quantity > PTSD3.Sum_quantity
AND (
    (PTSD2.Year = PTSD3.Year
        AND PTSD2.Month = PTSD3.Month + 1
    ) OR (PTSD2.Year = PTSD3.Year + 1
        AND PTSD2.Month = 12
        AND PTSD3.Month = 1
    )
)

-- Query 10 and onwards are additional queries.
/*
Query 10
Find the number of complaints each employee has addressed and select the top 3 employees
who have addressed the most number of complaints from most to least.
*/
SELECT TOP 3 E.EmployeeID,COUNT(*) AS Num_Complaints
FROM EMPLOYEES AS E, HANDLED AS H, COMPLAINTS AS C
WHERE H.EmployeeID = E.EmployeeID
AND C.ComplaintID = H.ComplaintID
AND C.Complaint_status = 'addressed'
GROUP BY E.EmployeeID
ORDER BY Num_Complaints DESC

/*
Query 11
Find the top 3 shops with the most number of customers who made revisits. Revisit = A user ordering
from the same shop more than once.
*/
-- Shops that have revisiting customers
WITH R1 AS
(
SELECT P.SName, O.userID
FROM USERS AS U, ORDERS AS O, PRODUCTS_IN_ORDERS AS P
WHERE U.userID = O.userID AND
	   O.orderID = P.orderID
GROUP BY P.SName, O.userID
HAVING COUNT(O.orderID) > 1 
)
-- Top 3 shops with the most number of revisiting customers
SELECT TOP 3 R1.SName, COUNT( DISTINCT R1.userID) AS Num_of_revisiting_customer
FROM R1
GROUP BY R1.SName
ORDER BY Num_of_revisiting_customer DESC;

/*
Query 12
Find products and its corresponding shop with an average rating that is higher than that
of similar products (same products from other shops).
*/
SELECT PSA.PName, PSA.SName, PSA.Avg_Rating AS Avg_Rating_From_Shop, PA.Avg_Rating Avg_Rating
FROM (
    SELECT F1.PName, F1.SName, AVG(F1.Rating) AS Avg_Rating
    FROM FEEDBACKS AS F1
    GROUP BY F1.PName, F1.SName
) AS PSA
INNER JOIN (
	SELECT F2.PName, AVG(F2.Rating) AS Avg_Rating
    FROM FEEDBACKS AS F2
    GROUP BY F2.PName
) AS PA
ON (PSA.PName = PA.PName
	AND PSA.Avg_Rating > PA.Avg_Rating
)

/*
Query 13
Find the average ratings given by users who did not file any complaints.
*/
SELECT U.UserID, AVG(F.Rating) AS ave_rating
FROM USERS AS U, FEEDBACKS AS F
WHERE U.UserID = F.UserID AND
NOT EXISTS
    (SELECT *
    FROM COMPLAINTS AS C
    WHERE U.UserID = C.UserID)	
GROUP BY U.UserID

/*
Query 14
Find the average price of the product that was purchased the most number of times.
*/
WITH ProductQty AS (
SELECT PO2.PName, SUM(OQuantity) AS Total_Qty
FROM PRODUCTS_IN_ORDERS AS PO2
GROUP BY PO2.PName
)
SELECT PS1.PName, AVG(PS2.SPrice) AS Avg_price
FROM PRODUCTS_IN_SHOPS_1 AS PS1
	INNER JOIN ProductQty AS PQ1
ON PS1.PName = PQ1.PName
INNER JOIN PRODUCTS_IN_SHOPS_2 AS PS2
ON PS1.SPID = PS2.SPID
WHERE PQ1.Total_Qty = (
SELECT MAX(PQ.Total_Qty)
FROM ProductQty AS PQ
) GROUP BY PS1.PName
