--Seed values to insert into schema tables--

INSERT INTO Equipment (equipment_type, in_use, riid)
VALUES (1, 0, 1
);

INSERT INTO EmergencyContacts (name, phone_number)
VALUES ('Carl Mason', '5103975674'
);
INSERT INTO EmergencyContacts (name, phone_number)
VALUES ('Itzel Camarena', '5102377420'
);

INSERT INTO Clients (name, age, city, street_address, phone_number, ecid, gender)
VALUES ('Bradley Benedict', 23, 'New York', '61 Stalec Drive', '4043562278', 1, 'Male'
);
INSERT INTO Clients (name, age, city, street_address, phone_number, ecid)
VALUES ('Alex Hilfinger', 56, 'Seattle', '1560 Vernon Avenue', '2066153292', 2
);

INSERT INTO EquipmentTypes (name, description)
VALUES ('Fastchair 300', 'Wheelchair manufactured by Nanda Enterprises in 2013'
);

INSERT INTO RentalInfo (eid, rental_start, rental_end)
VALUES (1, '20141107', '20150324'
);

INSERT INTO Employees (emp_name)
VALUES ('Daniel Tahir'
);
INSERT INTO Employees (emp_name)
VALUES ('Sophia Godín'
);

INSERT INTO ServiceRequests (cid, attendant_id, service_type, gender_pref, address, start_time,
  end_time, client_notes, dispatch_notes, attendant_notes, emergency_level, riid, completed)
VALUES (1, 1, 2, 'No Preference', '61 Stalec Drive', '20141030', '20150324', 'Please deliver ASAP!',
  'Deliver wheelchair to client', 'Delivered wheelchair to client on 7th November', 'Urgent', 1, 1
);
INSERT INTO ServiceRequests (cid, attendant_id, service_type, gender_pref, address, start_time,
  end_time, client_notes, dispatch_notes, attendant_notes, emergency_level, completed)
VALUES (2, 2, 1, 'Female', '1560 Vernon Avenue', '20070617', '20070629', 'Help needed with removing clothes from wardrobe',
  'Go to the client\'s given address to assist', 'Assistance provided', 'Not Urgent', 1
);
