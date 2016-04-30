CREATE TABLE Users (
	uid INT NOT NULL PRIMARY KEY,
	name TEXT,
	age INT,
	city TEXT,
	street_address TEXT,
	phone_number TEXT,
	ecid REFERENCES EmergencyContacts,
	gender TEXT,

)
CREATE TABLE EmergencyContacts (
	ecid INT NOT NULL PRIMARY KEY,
)
