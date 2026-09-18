/*
 * Atividade de Edge Computing - Wokwi (ESP32) -> Broker MQTT -> Python (Paho MQTT)
 *
 * Fluxo:
 *   ESP32 le o DHT22 e publica "t|<temp>|h|<umid>" no topico de telemetria.
 *   O backend em Python (subscriber) recebe a telemetria.
 *   O backend em Python (publisher) envia "device018@on|" / "device018@off|"
 *   no topico de comando para ligar e desligar o LED.
 *
 * Device: device018 (computador N18 do laboratorio).
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

#define DHTPIN 4
#define DHTTYPE DHT22
#define LED_PIN 2

const char* ssid = "Wokwi-GUEST";
const char* password = "";
const char* mqtt_server = "54.91.80.136";

// Numero de identificacao (ID) do computador usado no laboratorio: N18 -> device018
const char* topico_telemetria = "/TEF/device018/attrs";
const char* topico_comando    = "/TEF/device018/cmd";

DHT dht(DHTPIN, DHTTYPE);
WiFiClient espClient;
PubSubClient client(espClient);

unsigned long lastMsg = 0;
const long interval = 2000;

void callback(char* topic, byte* payload, unsigned int length)
{
    // Alocacao dinamica segura na stack e terminacao da string
    char msg[length + 1];
    memcpy(msg, payload, length);
    msg[length] = '\0';

    Serial.printf("Comando recebido no topico %s: %s\n", topic, msg);

    if (strcmp(msg, "device018@on|") == 0)
    {
        digitalWrite(LED_PIN, HIGH);
        Serial.println("Acao: LED LIGADO");
    }
    else if (strcmp(msg, "device018@off|") == 0)
    {
        digitalWrite(LED_PIN, LOW);
        Serial.println("Acao: LED DESLIGADO");
    }
    else
    {
        // Tratamento de comando desconhecido, evitando falha silenciosa
        Serial.println("Acao: Comando nao reconhecido. Ignorado.");
    }
}

void setup()
{
    Serial.begin(115200);
    pinMode(LED_PIN, OUTPUT);
    digitalWrite(LED_PIN, LOW);

    dht.begin();

    WiFi.begin(ssid, password);
    Serial.print("Conectando WiFi");
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }
    Serial.println("\nWiFi Conectado!");

    client.setServer(mqtt_server, 1883);
    client.setCallback(callback);
}

void reconnect()
{
    while (!client.connected())
    {
        Serial.print("Conectando ao MQTT...");

        // O numero do device entra no clientId para nao colidir com outro aluno
        char clientId[30];
        snprintf(clientId, sizeof(clientId), "ESP32_018_%04X", random(0xffff));

        if (client.connect(clientId))
        {
            Serial.println("Conectado!");
            client.subscribe(topico_comando);
        }
        else
        {
            Serial.print("Falha, rc=");
            Serial.print(client.state());
            Serial.println(" Retentando em 5s...");
            delay(5000);
        }
    }
}

void loop()
{
    if (!client.connected()) reconnect();

    client.loop();

    unsigned long now = millis();
    if (now - lastMsg > interval)
    {
        lastMsg = now;

        float t = dht.readTemperature();
        float h = dht.readHumidity();

        if (isnan(t) || isnan(h))
        {
            Serial.println("Falha ao ler o DHT!");
            return;
        }

        char buffer[50];
        snprintf(buffer, sizeof(buffer), "t|%.1f|h|%.1f", t, h);

        client.publish(topico_telemetria, buffer);
        Serial.printf("Publicado: %s\n", buffer);
    }
}
