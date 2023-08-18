import serial
import csv

# Bibliotecas para Leitura Serial e CSV

def salvar_dados_em_csv(dados, nome_arquivo):
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(['Tempo'])  # Cabeçalho das colunas, se necessário
        writer.writerows(dados) # Escrevendo os dados

def ler_dados_do_serial(porta_serial):
    dados = []
    with serial.Serial(porta_serial, 115200) as ser:
        while True:
            linha = ser.readline().decode().strip()  # Lê uma linha da porta serial e converte para string
            if linha:  # Verifica se a linha não está vazia
                valores = linha.split(',')  # Separa os valores usando a vírgula como delimitador (CSV)
                dados.append(valores) # Adicionando os valores dos sensores aos dados
                print(valores)  # Apenas para verificar os dados na saída do console
            if len(dados) >= 1000:  # Para o exemplo, vamos salvar 1000 linhas de dados em CSV
                break
    return dados

if __name__ == '__main__':
    porta_serial_arduino = '/dev/ttyUSB0'  # Substitua pelo nome da porta serial do Arduino no seu sistema
    dados_recebidos = ler_dados_do_serial(porta_serial_arduino) # Fazer a leitura dos dados seriais do arduino
    salvar_dados_em_csv(dados_recebidos, 'dados_do_arduino.csv') # Salvando os arquivos em CSV
