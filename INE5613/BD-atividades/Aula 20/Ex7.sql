CREATE TRIGGER InsercaoFuncFlorianopolis
INSTEAD OF INSERT ON FuncFlorianopolis
FOR EACH ROW
BEGIN
    INSERT INTO Funcionarios (codf, nome, CPF, idade, cidade)
    VALUES (NEW.codf, NEW.nome, NEW.CPF, NEW.idade, 'Florianopolis');
END;
