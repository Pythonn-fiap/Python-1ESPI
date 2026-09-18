/*
 * Atividade de Edge Computing - Wokwi (ESP32) -> Broker MQTT -> Python (Paho MQTT)
 *
 * Fluxo:
 *   ESP32 le o DHT22 e publica temperatura/umidade no broker MQTT.
 *   O backend em Python (subscriber) recebe a telemetria.
 *   O backend em Python (publisher) envia comandos de liga/desliga do LED.
 *
 * Device: device018 (computador N18 do laboratorio). Os topicos e o
 * ID_MQTT sao montados a partir do #define DEVICE_ID, entao para usar
 * outra maquina basta alterar aquela linha.
 *
 * Grupo (1ESPI):
 *   Bruno Carreiro Dos Santos               - RM 569423
 *   Eduardo Bechara Medeiros Craveiro       - RM 571081
 *   Gustavo Moita de Lima                   - RM 569180
 *   Daniel Graciano dos Santos Ferreira     - RM 568886
 */

#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

// ---------------------------------------------------------------- Wi-Fi (Wokwi)
const char* SSID     = "Wokwi-GUEST";
const char* PASSWORD = "";

// ---------------------------------------------------------------- Broker MQTT
const char* BROKER_MQTT  = "54.91.80.136";
const int   BROKER_PORT  = 1883;

// ---------------------------------------------------------------- Topicos
// Numero do computador do laboratorio (N18). O mesmo valor precisa estar
// no DEVICE_ID do codigo Python.
#define DEVICE_ID "device018"

const char* ID_MQTT           = "fiware_" DEVICE_ID;      // id unico no broker
const char* TOPICO_SUBSCRIBE  = "/TEF/" DEVICE_ID "/cmd";     // comandos recebidos
const char* TOPICO_PUBLISH_1  = "/TEF/" DEVICE_ID "/attrs";   // estado do LED
const char* TOPICO_PUBLISH_2  = "/TEF/" DEVICE_ID "/attrs/t"; // temperatura
const char* TOPICO_PUBLISH_3  = "/TEF/" DEVICE_ID "/attrs/h"; // umidade
const char* PREFIXO_COMANDO   = DEVICE_ID "@";                // prefixo dos comandos

// ---------------------------------------------------------------- Hardware
#define PINO_LED  2
#define PINO_DHT  4
#define TIPO_DHT  DHT22

DHT dht(PINO_DHT, TIPO_DHT);
WiFiClient espClient;
PubSubClient MQTT(espClient);

char estadoSaida = '0';                 // '0' = LED desligado, '1' = LED ligado
unsigned long publishUpdate = 0;
const unsigned long INTERVALO_PUBLISH = 2000;  // ms

// ---------------------------------------------------------------- Prototipos
void initSerial();
void initWiFi();
void initMQTT();
void reconectWiFi();
void reconnectMQTT();
void VerificaConexoesWiFIEMQTT();
void mqtt_callback(char* topic, byte* payload, unsigned int length);
void EnviaEstadoOutputMQTT();
void EnviaTelemetriaMQTT();
void InitOutput();

void setup() {
  InitOutput();
  initSerial();
  initWiFi();
  initMQTT();
  dht.begin();
  delay(3000);
  MQTT.publish(TOPICO_PUBLISH_1, "s|on");
}

void loop() {
  VerificaConexoesWiFIEMQTT();
  EnviaEstadoOutputMQTT();

  if (millis() - publishUpdate >= INTERVALO_PUBLISH) {
    publishUpdate = millis();
    EnviaTelemetriaMQTT();
  }

  MQTT.loop();
}

// ---------------------------------------------------------------- Implementacao
void initSerial() {
  Serial.begin(115200);
}

void initWiFi() {
  delay(10);
  Serial.println("------ Conexao WI-FI ------");
  Serial.print("Conectando-se na rede: ");
  Serial.println(SSID);
  reconectWiFi();
}

void initMQTT() {
  MQTT.setServer(BROKER_MQTT, BROKER_PORT);
  MQTT.setCallback(mqtt_callback);
}

void reconectWiFi() {
  if (WiFi.status() == WL_CONNECTED) return;

  WiFi.begin(SSID, PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
    Serial.print(".");
  }
  Serial.println();
  Serial.print("WiFi conectado com sucesso: ");
  Serial.println(SSID);
  Serial.print("IP obtido: ");
  Serial.println(WiFi.localIP());

  // Garante que o LED comeca desligado
  digitalWrite(PINO_LED, LOW);
}

void reconnectMQTT() {
  while (!MQTT.connected()) {
    Serial.print("* Tentando se conectar ao Broker MQTT: ");
    Serial.println(BROKER_MQTT);
    if (MQTT.connect(ID_MQTT)) {
      Serial.println("Conectado com sucesso ao broker MQTT!");
      MQTT.subscribe(TOPICO_SUBSCRIBE);
    } else {
      Serial.println("Falha ao reconectar no broker.");
      Serial.println("Nova tentativa de conexao em 2s");
      delay(2000);
    }
  }
}

void VerificaConexoesWiFIEMQTT() {
  if (!MQTT.connected()) reconnectMQTT();
  reconectWiFi();
}

void mqtt_callback(char* topic, byte* payload, unsigned int length) {
  String msg;
  for (unsigned int i = 0; i < length; i++) {
    msg += (char)payload[i];
  }
  Serial.print("- Mensagem recebida: ");
  Serial.println(msg);

  String onCommand  = String(PREFIXO_COMANDO) + "on|";
  String offCommand = String(PREFIXO_COMANDO) + "off|";

  if (msg.equals(onCommand)) {
    digitalWrite(PINO_LED, HIGH);
    estadoSaida = '1';
  }

  if (msg.equals(offCommand)) {
    digitalWrite(PINO_LED, LOW);
    estadoSaida = '0';
  }
}

void EnviaEstadoOutputMQTT() {
  if (estadoSaida == '1') {
    MQTT.publish(TOPICO_PUBLISH_1, "s|on");
    Serial.println("- Led Ligado");
  } else {
    MQTT.publish(TOPICO_PUBLISH_1, "s|off");
    Serial.println("- Led Desligado");
  }
  Serial.println("- Estado do LED enviado ao broker!");
  delay(1000);
}

void EnviaTelemetriaMQTT() {
  float umidade    = dht.readHumidity();
  float temperatura = dht.readTemperature();

  if (isnan(umidade) || isnan(temperatura)) {
    Serial.println("- Falha na leitura do DHT22!");
    return;
  }

  char bufferTemp[10];
  char bufferUmid[10];
  dtostrf(temperatura, 4, 2, bufferTemp);
  dtostrf(umidade, 4, 2, bufferUmid);

  MQTT.publish(TOPICO_PUBLISH_2, bufferTemp);
  MQTT.publish(TOPICO_PUBLISH_3, bufferUmid);

  Serial.print("- Publicado -> Temperatura: ");
  Serial.print(bufferTemp);
  Serial.print(" C | Umidade: ");
  Serial.print(bufferUmid);
  Serial.println(" %");
}

void InitOutput() {
  pinMode(PINO_LED, OUTPUT);
  digitalWrite(PINO_LED, LOW);
}
