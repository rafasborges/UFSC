SELECT andar, SUM(capacidade) AS capacidade_total
FROM Ambulatorios
GROUP BY andar;
