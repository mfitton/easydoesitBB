CREATE TABLE Clients (
	cid INT NOT NULL PRIMARY KEY,
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
	name TEXT,
	phone_number TEXT
)

CREATE TABLE ServiceRequests (
	rid INT NOT NULL PRIMARY KEY,
	cid INT REFERENCES Clients,
	attendant_id INT REFERENCES Employees,
	service_type INT REFERENCES Services,
	latitude INT,
	longitude INT,
	start_time DATETIME,
	end_time DATETIME,
	dispatch_notes TEXT,
	attendant_notes TEXT
)

CREATE TABLE Equipment (
	eid INT NOT NULL PRIMARY KEY,
	equipment_type REFERENCES EquipmentTypes,
	in_use INT,
	borrower_id REFERENCES Clients
)

CREATE TABLE EquipmentTypes (
	etid INT NOT NULL PRIMARY KEY,
	name TEXT,
	description TEXT
)
