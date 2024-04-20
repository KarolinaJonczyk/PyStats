CREATE TABLE Property_type (
    property_ID INT PRIMARY KEY,
    property_name VARCHAR(255)
);

CREATE TABLE List_year (
    list_year_ID INT PRIMARY KEY,
    list_year VARCHAR(255)
);

CREATE TABLE Date_recorded (
    date_recorded_ID INT PRIMARY KEY,
    date_recorded VARCHAR(255)
);

CREATE TABLE Residential_type (
    residential_ID INT PRIMARY KEY,
    residential_name VARCHAR(255)
);

CREATE TABLE Town (
    town_ID INT PRIMARY KEY,
    serial_number INT,
    town_name VARCHAR(255),
    FOREIGN KEY (serial_number) REFERENCES Estates(serial_number)
);

CREATE TABLE Street (
    street_ID INT PRIMARY KEY,
    town_ID INT,
    address_name VARCHAR(255),
    FOREIGN KEY (town_ID) REFERENCES Town(town_ID)
);

CREATE TABLE Address_list(
    address_ID INT PRIMARY KEY,
    town_ID INT,
    street_ID INT,
    FOREIGN KEY (town_ID) REFERENCES Town(town_ID), 
    FOREIGN KEY (street_ID) REFERENCES Street(street_ID)
);

CREATE TABLE Estates (
    serial_number INT PRIMARY KEY,
    property_ID INT,
    date_recorded_ID INT,
    list_year_ID INT,
    residential_ID INT,
    address_ID INT,
    assessed_value VARCHAR(255),
    sale_amount VARCHAR(255),
    sales_ratio VARCHAR(255),
    FOREIGN KEY (property_ID) REFERENCES Property_type(property_ID),
    FOREIGN KEY (date_recorded_ID) REFERENCES Date_recorded(date_recorded_ID),
    FOREIGN KEY (list_year_ID) REFERENCES List_year(list_year_ID),
    FOREIGN KEY (residential_ID) REFERENCES Residential_type(residential_ID),
    FOREIGN KEY (address_ID) REFERENCES Address_list(address_ID)
);

SELECT * FROM Town; 
