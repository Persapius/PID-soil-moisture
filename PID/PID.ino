// Definindo o Pino do Sensor de Umidade do Solo
#define Pino_Sensor_Umidade_do_Solo A1


// Pino para controlar a bomba de água
#define Pino_Bomba 8

// Configuração do controle PID
double setpoint = 40; // Valor desejado de umidade do solo
double erro; // Sinal de Erro
double input; // Sinal de Entrada do PID
double PID; // Armazenar o controlador PID
double TempoIrrigacao; // Sinal de Controle (Tempo de Irrigaçao)
double Kp = 50; // Constante proporcional
double Ki = 0.042857; // Constante integral
double Kd = 17010; // Constante derivativa
double P = 0; // Parte Proporcional
double I = 0; // Parte Integral
double D = 0; // Parte Derivativa
double UltimaLeituraSensor = 0; // Leitura anterior do sensor de umidade do solo
unsigned long contador = 0; // Contador que atua no calculo do PID

void setup() {
  // Inicialização do sensor de umidade do solo
  pinMode(Pino_Sensor_Umidade_do_Solo, INPUT);

  // Inicialização da bomba de água
  pinMode(Pino_Bomba, OUTPUT);
  
  // Bomba desligada
  digitalWrite(Pino_Bomba, LOW);
  
  
  Serial.begin(115200); // Leitura da porta serial do arduino
}

void loop() {
  
  // Leitura da Umidade
  int ValorUmidade = analogRead(Pino_Sensor_Umidade_do_Solo);
  
  // Convertendo a leitura do sensor para o valor de umidade (Porcentagem)
  input = map(ValorUmidade, 0, 1023, 0, 100);

  // Imprimindo o valor da Umidade do Solo
  Serial.print(input);

  
  // Controlador PID
  PID = CalculaPID(erro, input, setpoint, UltimaLeituraSensor, P, I, D);
  
  // Mapeando o tempo de irrigaçao (sinal de controle)
   TempoIrrigacao = map(PID, -255, 255, 0, 5000);
  
  if ((input>setpoint) && (contador==10)) {
    
  // Acionando a Bomba
  digitalWrite(Pino_Bomba, HIGH); // Liga a bomba
  delay(TempoIrrigacao); // Mantém a bomba ligada por 5 segundos
  digitalWrite(Pino_Bomba, LOW); // Desliga a bomba
  delay(1000); // Delay de 1 segundo
  
  }
  
  contador+=1;
  
  // O contador e resetado apos o periodo de 1 dia
  if (contador==8640) {
  
    contador=0;
  }
  
  delay(10000); // Delay de 10 segundos
  
}


// Funcao para calcular o PID
double CalculaPID(double ERRO, double ENTRADA,double SETPOINT,double ULTIMA_LEITURA_SENSOR, double Proporcional, double Derivativa, double Integral) {
  
    // Calcula o sinal de erro
  ERRO = ENTRADA - SETPOINT;

  // Termo proporcional
  Proporcional = ERRO * Kp;

  // Termo Integral
  Integral += ERRO * Ki;

  // Termo Derivativo
  Derivativa = (ULTIMA_LEITURA_SENSOR - ENTRADA) * Kd;
  
  return Proporcional + Integral + Derivativa;

}
