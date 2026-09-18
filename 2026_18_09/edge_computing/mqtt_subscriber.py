"""Subscriber MQTT - recebe a telemetria enviada pelo ESP32 (Wokwi).

Atividade de Edge Computing: Wokwi -> Broker MQTT -> Python (Paho MQTT).

Grupo (1ESPI):
    Bruno Carreiro Dos Santos            - RM 569423
    Eduardo Bechara Medeiros Craveiro    - RM 571081
    Gustavo Moita de Lima                - RM 569180
    Daniel Graciano dos Santos Ferreira  - RM 568886

Como usar (Colab ou local):
    pip install paho-mqtt
    python mqtt_subscriber.py

O ESP32 publica a telemetria no formato "t|<temperatura>|h|<umidade>"
(ex.: "t|24.0|h|40.0") no topico /TEF/device018/attrs.
"""

from datetime import datetime

import paho.mqtt.client as mqtt

# --------------------------------------------------------------- Configuracao
BROKER = "54.91.80.136"
PORT = 1883
KEEPALIVE = 60
DEVICE_ID = "device018"  # computador N18 do laboratorio
CLIENT_ID = f"python_subscriber_{DEVICE_ID}"

TOPICO_TELEMETRIA = f"/TEF/{DEVICE_ID}/attrs"


def parse_telemetria(payload):
    """Converte "t|24.0|h|40.0" em {"t": "24.0", "h": "40.0"}."""
    partes = payload.split("|")
    return dict(zip(partes[0::2], partes[1::2]))


# ------------------------------------------------------------------- Callbacks
def on_connect(client, userdata, flags, reason_code, properties=None):
    if reason_code == 0:
        print(f"[SUCESSO] Conectado ao Broker {BROKER}:{PORT}")
        client.subscribe(TOPICO_TELEMETRIA)
        print(f"[SUCESSO] Inscrito em {TOPICO_TELEMETRIA}. Aguardando leituras...")
        print("-" * 60)
    else:
        print(f"[FALHA] Nao foi possivel conectar. Codigo: {reason_code}")


def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8", errors="replace").strip()
    horario = datetime.now().strftime("%H:%M:%S")
    leitura = parse_telemetria(payload)

    if "t" in leitura and "h" in leitura:
        print(f"[NOVA LEITURA {horario}] Temperatura: {leitura['t']} C | "
              f"Umidade: {leitura['h']} %")
    else:
        print(f"[NOVA LEITURA {horario}] {payload}")


def on_disconnect(client, userdata, reason_code, properties=None):
    print(f"[INFO] Desconectado do broker (codigo {reason_code})")


# ----------------------------------------------------------------------- Main
def criar_cliente():
    """Cria o cliente compativel com paho-mqtt 1.x e 2.x."""
    try:  # paho-mqtt >= 2.0
        return mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=CLIENT_ID)
    except AttributeError:  # paho-mqtt 1.x
        return mqtt.Client(client_id=CLIENT_ID)


def main():
    client = criar_cliente()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect

    print(f"[INICIO] Conectando ao broker {BROKER}:{PORT}...")
    client.connect(BROKER, PORT, keepalive=KEEPALIVE)

    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("\n[FIM] Leitura interrompida pelo usuario.")
    finally:
        client.disconnect()


if __name__ == "__main__":
    main()
