CREATE TABLE USERS 
( 
UserID INT PRIMARY KEY IDENTITY(1,1), 
UName VARCHAR (50) NOT NULL, 
);
 
CREATE TABLE EMPLOYEES 
( 
EmployeeID INT PRIMARY KEY IDENTITY(1,1), 
EName VARCHAR (50) NOT NULL, 
Salary FLOAT NOT NULL, 
);

CREATE TABLE SHOPS 
( 
SName VARCHAR (50) PRIMARY KEY, 
);

CREATE TABLE PRODUCTS 
( 
PName VARCHAR (50) PRIMARY KEY, 
Maker VARCHAR (50) NOT NULL, 
Category VARCHAR (50) NOT NULL, 
);
 
CREATE TABLE ORDERS 
( 
OrderID INT PRIMARY KEY IDENTITY(1,1), 
Date_time DATETIME NOT NULL, 
Shipping_address VARCHAR (256) NOT NULL, 
UserID INT NOT NULL, 
FOREIGN KEY (UserID) REFERENCES USERS(UserID),
);
 
CREATE TABLE COMPLAINTS 
( 
ComplaintID INT PRIMARY KEY IDENTITY(1,1), 
Complaint_status VARCHAR (50) NOT NULL, 
Complaint_text VARCHAR (256) NOT NULL, 
Filed_date_time DATETIME NOT NULL, 
UserID INT NOT NULL, 
EmployeeID INT,
FOREIGN KEY (UserID) REFERENCES USERS(UserID),
FOREIGN KEY (EmployeeID) REFERENCES EMPLOYEES(EmployeeID),
);

CREATE TABLE COMPLAINTS_ON_ORDERS 
( 
ComplaintID INT PRIMARY KEY, 
OrderID INT NOT NULL, 
FOREIGN KEY (ComplaintID) REFERENCES COMPLAINTS(ComplaintID),
FOREIGN KEY (OrderID) REFERENCES ORDERS(OrderID),
);

CREATE TABLE COMPLAINTS_ON_SHOPS 
( 
ComplaintID INT PRIMARY KEY, 
SName VARCHAR (50) NOT NULL, 
FOREIGN KEY (ComplaintID) REFERENCES COMPLAINTS(ComplaintID),
FOREIGN KEY (SName) REFERENCES SHOPS(SName),
);
 
CREATE TABLE PRODUCTS_IN_SHOPS_2 
( 
SPID INT PRIMARY KEY IDENTITY(1,1), 
SPrice FLOAT NOT NULL, 
SQuantity INT NOT NULL, 
);
 
CREATE TABLE PRODUCTS_IN_SHOPS_1 
( 
PName VARCHAR (50) NOT NULL, 
SName VARCHAR (50) NOT NULL, 
SPID INT NOT NULL, 
CONSTRAINT PIS1_key PRIMARY KEY (PName,SName), 
FOREIGN KEY (SPID) REFERENCES PRODUCTS_IN_SHOPS_2(SPID),
FOREIGN KEY (SName) REFERENCES SHOPS(SName),
FOREIGN KEY (PName) REFERENCES PRODUCTS(PName),
);
 
CREATE TABLE PRODUCTS_IN_ORDERS 
( 
OPID INT PRIMARY KEY IDENTITY(1,1), 
Order_status VARCHAR (50) NOT NULL, 
OPrice FLOAT NOT NULL, 
OQuantity INT NOT NULL, 
Delivery_date DATETIME, 
OrderID INT NOT NULL, 
PName VARCHAR (50) NOT NULL, 
SName VARCHAR (50) NOT NULL, 
FOREIGN KEY (OrderID) REFERENCES ORDERS(OrderID),
FOREIGN KEY (PName) REFERENCES PRODUCTS(PName),
FOREIGN KEY (SName) REFERENCES SHOPS(SName),
);

CREATE TABLE FEEDBACKS 
( 
UserID INT NOT NULL, 
PName VARCHAR (50) NOT NULL, 
SName VARCHAR (50) NOT NULL, 
OrderID INT NOT NULL, 
Rating INT NOT NULL, 
Date_time DATETIME NOT NULL, 
Comment VARCHAR (256) NOT NULL, 
CONSTRAINT Feedback_key PRIMARY KEY (UserID,PName,SName,OrderID),
FOREIGN KEY (UserID) REFERENCES USERS(UserID),
FOREIGN KEY (PName) REFERENCES PRODUCTS(PName),
FOREIGN KEY (SName) REFERENCES SHOPS(SName),
FOREIGN KEY (OrderID) REFERENCES ORDERS(OrderID),
);
 
CREATE TABLE HANDLED 
( 
ComplaintID INT PRIMARY KEY NOT NULL, 
EmployeeID INT NOT NULL, 
Handled_date_time DATETIME NOT NULL, 
FOREIGN KEY (EmployeeID) REFERENCES EMPLOYEES(EmployeeID),
FOREIGN KEY (ComplaintID) REFERENCES COMPLAINTS(ComplaintID),
);
 
CREATE TABLE PRICE_HISTORY 
( 
P_start_date DATETIME NOT NULL, 
P_end_date DATETIME,  
PName VARCHAR (50) NOT NULL, 
SName VARCHAR (50) NOT NULL, 
Price FLOAT NOT NULL, 
CONSTRAINT PH_key PRIMARY KEY (P_start_date, P_end_date, PName, SName), 
FOREIGN KEY (PName) REFERENCES PRODUCTS(PName),
FOREIGN KEY (SName) REFERENCES SHOPS(SName),
);