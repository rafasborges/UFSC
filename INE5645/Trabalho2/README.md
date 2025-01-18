# Trabalho2p

Para compilar:
# Navegar até a pasta onde está o código
cd /caminho/para/Trabalho2p

# Compilar manualmente 
gcc -o servidor servidor.c -lpthread
gcc -o cliente cliente.c


# Iniciar o servidor
./servidor --port 8080 --max_clients 3 --buffer_size 256

# Iniciar o cliente
 ./cliente arquivo.txt 127.0.0.1 novo_local/arquivo.txt
 
 ./cliente arquivo1.txt 127.0.0.1 novo_local/arquivo1.txt
 
 ./cliente arquivo2.txt 127.0.0.1 novo_local/arquivo2.txt
 
 ./cliente arquivo3.txt 127.0.0.1 novo_local/arquivo3.txt
