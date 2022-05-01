/*
1.
Frequent shoppers are shoppers who have purchased more than 2 items per shop for at least 5 shops
in the last 30 days. Who are the top 3 frequent shoppers in terms of the total cost of the items
they have purchased?
*/
WITH USERS_SHOPS_NUM_ORDERS_PAST_MONTH AS (
    SELECT O.UserID, PO.SName, SUM(PO.OQuantity) AS ItemsBought
    FROM PRODUCTS_IN_ORDERS AS PO
        INNER JOIN ORDERS AS O
        ON O.OrderID = PO.OrderID
    WHERE O.Date_time >= DATEADD(DAY, -30, GETDATE())
    GROUP BY O.UserID, SName
    HAVING SUM(PO.OQuantity) > 2
),
FREQUENT_SHOPPERS AS (
    SELECT Sub.UserID, COUNT(Sub.SName) AS NumShops
    FROM USERS_SHOPS_NUM_ORDERS_PAST_MONTH AS Sub
    GROUP BY Sub.UserID
    HAVING COUNT(Sub.SName) >= 5
)
SELECT TOP 3 FQ.UserID, SUM(PO.OPrice * PO.OQuantity) AS TotalCost
FROM FREQUENT_SHOPPERS AS FQ
    INNER JOIN ORDERS AS O
    ON FQ.UserID = O.UserID
    INNER JOIN PRODUCTS_IN_ORDERS AS PO
    ON O.OrderID = PO.OrderID
GROUP BY FQ.UserID
ORDER BY SUM(PO.OPrice * PO.OQuantity) DESC

/*
2.
Popular shops are shops which have sold more than 3 items in the last 30 days. Who are the top 3
shoppers in these popular shops in terms of the number of items they have purchased?
*/
SELECT TOP 3 ORDERS.UserID, SUM(P2.OQuantity) AS items_bought
FROM PRODUCTS_IN_ORDERS AS P2
JOIN ORDERS ON P2.OrderID = ORDERS.OrderID
INNER JOIN (
    -- popular shops
    SELECT P1.SName, SUM(OQuantity) AS items_sold
    FROM PRODUCTS_IN_ORDERS AS P1
    JOIN ORDERS ON P1.OrderID = ORDERS.OrderID
    WHERE DATEDIFF(day, ORDERS.Date_time, GETDATE()) BETWEEN 0 AND 30
    GROUP BY P1.SName
    HAVING SUM(OQuantity) >= 3
) AS POP_SHOPS ON P2.SName = POP_SHOPS.SName
GROUP BY ORDERS.UserID
ORDER BY SUM(P2.OQuantity) DESC