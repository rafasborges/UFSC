SELECT andar
FROM Ambulatorios
GROUP BY andar
HAVING AVG(capacidade) >= 40;
