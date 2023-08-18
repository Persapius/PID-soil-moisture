# Importando a Biblioteca do Python
import pandas as pd

def Leitura_Tratamento_Dados_Arduino():

 # Nome do arquivo csv com os dados do arduino
 arquivo = 'dados_do_arduino.csv'

 # DataFrame Pandas com os dados do arduino
 data = pd.read_csv(arquivo)

 # Transformando as leituras em inteiros (int)
 data = data['Sensor de Umidade'].astype(int)

 # Selecionando os dados de umidade do solo
 data_umidade = list(data)

 # Retornando a Umidade do Solo
 return data_umidade

# Biblioteca do Python para Plotagem Gráfica
import matplotlib.pyplot as plt

def PlotagemGraficaPID(Umidade_do_Solo, SetPoint, Tempo_decorrido):
  '''
    Args:

      Umidade_do_Solo (list): Vetor contendo os valores da Umidade do Solo.
      SetPoint (list): Valor do Setpoint (Umidade desejada)
      Tempo_decorrido (int): Valor referente ao intervalo de leitura do sensor de umidade do solo 

      Return:

        None
  '''
  # Vetor do Tempo de Leitura do Sensor de Umidade do Solo
  Tempo = [i for i in range(0,len(Umidade_do_Solo)*Tempo_decorrido,Tempo_decorrido)] 

  # Vetor do SetPoint
  Vetor_SetPoint = [SetPoint for i in range(0,len(Tempo)*Tempo_decorrido,Tempo_decorrido)]
  
  # Criando o gráfico usando Matplotlib
  plt.plot(Tempo, Umidade_do_Solo, label='Umidade do Solo')
  plt.plot(Tempo, Vetor_SetPoint, label='SetPoint')
  plt.title('Projeto de Controlador PID - Resultados')
  plt.xlabel('Tempo (s)')
  plt.ylabel('Umidade do Solo/SetPoint')
  plt.legend()

  # Exibir o gráfico (opcional)
  plt.show()
