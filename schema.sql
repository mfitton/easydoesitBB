CREATE TABLE Clients (
	cid INT NOT NULL PRIMARY KEY,
	name TEXT,
	age INT,
	city TEXT,
	street_address TEXT,
	phone_number TEXT,
	ecid REFERENCES EmergencyContacts,
	gender TEXT
);

CREATE TABLE EmergencyContacts (
	ecid INT NOT NULL PRIMARY KEY,
	name TEXT,
	phone_number TEXT
);

CREATE TABLE ServiceRequests (
	rid INT NOT NULL PRIMARY KEY,
	cid INT REFERENCES Clients,
	attendant_id INT REFERENCES Employees,
	service_type INT REFERENCES Services,
	address TEXT,
	start_time DATETIME,
	end_time DATETIME,
	client_notes TEXT,
	dispatch_notes TEXT,
	attendant_notes TEXT,
	emergency_level INT,
	tiid INT REFERENCES TransportInfo,
	riid INT REFERENCES RentalInfo
);

CREATE TABLE Equipment (
	eid INT NOT NULL PRIMARY KEY,
	equipment_type REFERENCES EquipmentTypes,
	in_use INT,
	riid INT REFERENCES RentalInfo
);

CREATE TABLE EquipmentTypes (
	etid INT NOT NULL PRIMARY KEY,
	name TEXT,
	description TEXT
);

CREATE TABLE TransportInfo (
	tiid INT NOT NULL PRIMARY KEY,
	from_address TEXT NOT NULL,
	to_address TEXT,
	pickup_time DATETIME
);

CREATE TABLE RentalInfo (
	riid INT NOT NULL PRIMARY KEY,
	eid INT NOT NULL REFERENCES Equipment,
	rental_start DATETIME NOT NULL,
	rental_end DATETIME
);
