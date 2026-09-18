# Atividade de Edge Computing — Wokwi → Broker MQTT → Python (Paho MQTT)

Validação do fluxo completo de comunicação entre o **ESP32 no Wokwi**, o **broker MQTT**
e o **backend em Python** usando a biblioteca **Paho MQTT**.

- **Turma:** 1ESPI
- **Data da entrega:** 18/09/2026

## Integrantes do grupo

| Nome | RM |
| --- | --- |
| Bruno Carreiro Dos Santos | 569423 |
| Eduardo Bechara Medeiros Craveiro | 571081 |
| Gustavo Moita de Lima | 569180 |
| Daniel Graciano dos Santos Ferreira | 568886 |

## Infraestrutura

| Item | Valor |
| --- | --- |
| Broker MQTT | `54.91.80.136` |
| Porta | `1883` |
| Device | `device018` (computador **N18** do laboratório) |

### Tópicos MQTT

| Tópico | Direção | Conteúdo |
| --- | --- | --- |
| `/TEF/device018/attrs` | ESP32 → Python | Estado do LED (`s\|on` / `s\|off`) |
| `/TEF/device018/attrs/t` | ESP32 → Python | Temperatura (°C) lida no DHT22 |
| `/TEF/device018/attrs/h` | ESP32 → Python | Umidade (%) lida no DHT22 |
| `/TEF/device018/cmd` | Python → ESP32 | Comandos `device018@on\|` e `device018@off\|` |

## Arquivos

| Arquivo | Descrição |
| --- | --- |
| `esp32_dht22_mqtt.ino` | Código do ESP32 (Wokwi): conecta no Wi-Fi/broker, publica temperatura e umidade e liga/desliga o LED conforme os comandos recebidos |
| `mqtt_subscriber.py` | Backend Python que **recebe** a telemetria enviada pelo ESP32 |
| `mqtt_publisher.py` | Backend Python que **envia** os comandos de ligar/desligar o LED |
| `colab_mqtt.ipynb` | Mesmo código organizado em células, para rodar no Google Colab |
| `requirements.txt` | Dependência (`paho-mqtt`) |
| `diagram.json` | Circuito do Wokwi (ESP32 + DHT22 no GPIO4 + LED no GPIO2) — só é necessário se o projeto for montado do zero |
| `libraries.txt` | Bibliotecas do Wokwi (`PubSubClient`, `DHT sensor library`, `Adafruit Unified Sensor`) |

## Número do computador (`device018`)

A máquina usada é a **N18** do laboratório, então o device é `device018` e o
`ID_MQTT` é `fiware_018`. Cada aluno usa um número diferente para não colidir nos
tópicos do broker compartilhado.

Para rodar em outra máquina, o valor precisa ser trocado (e ser **o mesmo**) em dois lugares:

| Onde | Linha |
| --- | --- |
| `esp32_dht22_mqtt.ino` | `#define DEVICE_ID "device018"` |
| `mqtt_subscriber.py` / `mqtt_publisher.py` / notebook | `DEVICE_ID = "device018"` |

## Passo a passo — Wokwi (ESP32)

1. Abrir o projeto **Wokwi_ESP32_DHT22** (link enviado pelo professor), fazer login e
   clicar em **Save a copy** (não editar o original).
   Se precisar montar do zero: criar um projeto ESP32 novo e colar o conteúdo de
   `esp32_dht22_mqtt.ino`, `diagram.json` e `libraries.txt` nas abas correspondentes.
2. Conferir o `#define DEVICE_ID "device018"` (computador N18). Os tópicos e o
   `ID_MQTT` são montados a partir dele.
3. Executar o simulador (**Play**).
4. Verificar no Serial Monitor:
   - `WiFi conectado com sucesso: Wokwi-GUEST`
   - `Conectado com sucesso ao broker MQTT!`
   - `- Publicado -> Temperatura: ... C | Umidade: ... %`

## Passo a passo — Python (Colab ou local)

Executar na seguinte ordem:

1. Instalar a dependência:
   ```bash
   pip install paho-mqtt
   ```
2. Conferir que o `DEVICE_ID` é o mesmo usado no Wokwi — `device018` — em
   `mqtt_subscriber.py`, `mqtt_publisher.py` ou na célula de configuração do notebook.
3. Rodar o **subscriber** para receber a telemetria enviada pelo ESP32:
   ```bash
   python mqtt_subscriber.py
   ```
4. Rodar o **publisher** (em outra execução/célula) para enviar os comandos de LED:
   ```bash
   python mqtt_publisher.py
   ```

> **Importante:** sempre interrompa as execuções anteriores antes de rodar novamente,
> evitando múltiplas threads conectadas ao broker.

## Evidências da entrega (prints)

1. **Recebimento dos dados no Python (Subscriber)** — saída com temperatura e umidade chegando.
2. **Recebimento dos comandos no Wokwi (LED ligado/desligado)** — Serial Monitor com
   `- Mensagem recebida: device018@on|` e o LED aceso no simulador.
