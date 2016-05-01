SELECT triple_join(
  'A multiple join on the Equipment, EquipmentTypes, and RentalInfo tables works effectively: ',
    CASE WHEN
      (SELECT name, e.riid, rental_start, in_use FROM Equipment AS e
        JOIN EquipmentTypes ON equipment_type = etid
        JOIN RentalInfo AS ri ON e.riid = ri.riid)
= ('Enabler 420', 1, '20141107', 1)
  THEN 'Passed' ELSE 'Failed' END
  );
