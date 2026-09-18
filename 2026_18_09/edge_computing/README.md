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
| Device | `deviceXXX` (número do computador usado no laboratório) |

### Tópicos MQTT

| Tópico | Direção | Conteúdo |
| --- | --- | --- |
| `/TEF/deviceXXX/attrs` | ESP32 → Python | Estado do LED (`s\|on` / `s\|off`) |
| `/TEF/deviceXXX/attrs/t` | ESP32 → Python | Temperatura (°C) lida no DHT22 |
| `/TEF/deviceXXX/attrs/h` | ESP32 → Python | Umidade (%) lida no DHT22 |
| `/TEF/deviceXXX/cmd` | Python → ESP32 | Comandos `deviceXXX@on\|` e `deviceXXX@off\|` |

## Arquivos

| Arquivo | Descrição |
| --- | --- |
| `esp32_dht22_mqtt.ino` | Código do ESP32 (Wokwi): conecta no Wi-Fi/broker, publica temperatura e umidade e liga/desliga o LED conforme os comandos recebidos |
| `mqtt_subscriber.py` | Backend Python que **recebe** a telemetria enviada pelo ESP32 |
| `mqtt_publisher.py` | Backend Python que **envia** os comandos de ligar/desligar o LED |
| `colab_mqtt.ipynb` | Mesmo código organizado em células, para rodar no Google Colab |
| `requirements.txt` | Dependência (`paho-mqtt`) |

## Número do computador (`deviceXXX`)

É o número da máquina do laboratório, usado para que cada aluno publique em tópicos
diferentes no broker compartilhado. Onde encontrar:

- na **etiqueta** colada no gabinete/monitor da máquina do laboratório;
- ou pelo **nome do computador** no Windows: `Win + R` → `cmd` → digitar `hostname`
  (normalmente o nome termina com o número, ex.: `LAB...-015`);
- ou perguntando ao professor na aula.

Se não conseguir o número, use um valor **único** para não colidir com outro aluno —
por exemplo os três últimos dígitos do RM (`device423`) — e confirme depois com o professor.

O valor precisa ser **o mesmo** em dois lugares:

| Onde | Linha |
| --- | --- |
| `esp32_dht22_mqtt.ino` | `#define DEVICE_ID "deviceXXX"` |
| `mqtt_subscriber.py` / `mqtt_publisher.py` / notebook | `DEVICE_ID = "deviceXXX"` |

## Passo a passo — Wokwi (ESP32)

1. Abrir o projeto no Wokwi, fazer login e clicar em **Save a copy** (não editar o original).
2. No código, trocar o `#define DEVICE_ID "deviceXXX"` pelo número do computador
   (ex.: `"device015"`). Os tópicos e o `ID_MQTT` são montados a partir dele.
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
2. Trocar `DEVICE_ID` para o mesmo valor usado no Wokwi (`mqtt_subscriber.py`,
   `mqtt_publisher.py` ou a célula de configuração do notebook).
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
   `- Mensagem recebida: deviceXXX@on|` e o LED aceso no simulador.
