SELECT nroa, andar 
FROM ambulatorios 
WHERE capacidade > SOME(SELECT capacidade FROM ambulatorios WHERE andar = 1);