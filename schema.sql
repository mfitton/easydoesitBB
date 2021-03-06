CREATE TABLE Clients (
	cid INTEGER PRIMARY KEY,
	name TEXT,
	age INT,
	city TEXT,
	street_address TEXT,
	phone_number TEXT,
	ecid REFERENCES EmergencyContacts,
	gender TEXT
);

CREATE TABLE EmergencyContacts (
	ecid INTEGER PRIMARY KEY,
	name TEXT,
	phone_number TEXT
);

CREATE TABLE ServiceRequests (
	rid INTEGER PRIMARY KEY,
	cid INT REFERENCES Clients,
	attendant_id INT REFERENCES Employees,
	service_type INT REFERENCES Services,
	gender_pref TEXT,
	address TEXT,
	start_time DATETIME,
	end_time DATETIME,
	client_notes TEXT,
	dispatch_notes TEXT,
	attendant_notes TEXT,
	emergency_level TEXT,
	tiid INT REFERENCES TransportInfo,
	riid INT REFERENCES RentalInfo,
	completed INT
);

CREATE TABLE Equipment (
	eid INTEGER PRIMARY KEY,
	equipment_type REFERENCES EquipmentTypes,
	in_use INT,
	riid INT REFERENCES RentalInfo
);

CREATE TABLE EquipmentTypes (
	etid INTEGER PRIMARY KEY,
	name TEXT,
	description TEXT
);

CREATE TABLE TransportInfo (
	tiid INTEGER PRIMARY KEY,
	from_address TEXT NOT NULL,
	to_address TEXT,
	pickup_time DATETIME
);

CREATE TABLE RentalInfo (
	riid INTEGER PRIMARY KEY,
	eid INT NOT NULL REFERENCES Equipment,
	rental_start DATETIME NOT NULL,
	rental_end DATETIME
);

CREATE TABLE Services AS
	SELECT 1 AS stid, 'Personal Attendant Help' AS type UNION
	SELECT 2        , 'Rental'                          UNION
	SELECT 3        , 'Repair Service'                  UNION
	SELECT 4        , 'Transports';

CREATE TABLE Employees (
	empid INTEGER PRIMARY KEY,
	emp_name TEXT
);
