# Biblioteca do Python para Plotagem Gráfica
import matplotlib.pyplot as plt

# lista_valores_tempo => Vetor que representa o tempo de coleta do dados
# lista_valores_umidade => Vetor com o valor da umidade do solo coletada
# setpoint => Vetor com o valor da umidade desejada (Linha laranjada)

# Criando o gráfico usando Matplotlib
plt.plot(lista_valores_tempo, lista_valores_umidade, label='Umidade do Solo')
plt.plot(lista_valores_tempo, setpoint, label='SetPoint')
plt.title('Projeto de Controlador PID - Resultados')
plt.xlabel('Tempo (s)')
plt.ylabel('Umidade do Solo/SetPoint')
plt.legend()

# Salvar o gráfico como uma imagem PNG
plt.savefig("grafico.png")

# Exibir o gráfico (opcional)
plt.show()
