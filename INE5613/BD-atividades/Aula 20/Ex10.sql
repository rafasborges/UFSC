CREATE VIEW MedicosAmbulatorios2 AS
SELECT codm, nome, idade, CPF, nroa
FROM Medicos
WHERE nroa >= 2
WITH CHECK OPTION;
