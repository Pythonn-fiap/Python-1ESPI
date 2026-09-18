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

Antes de executar, troque DEVICE_ID pelo numero do seu computador (ex.: "device015").
"""

import json
from datetime import datetime

import paho.mqtt.client as mqtt

# --------------------------------------------------------------- Configuracao
BROKER = "54.91.80.136"
PORT = 1883
DEVICE_ID = "device018"  # computador N18 do laboratorio
CLIENT_ID = f"python_subscriber_{DEVICE_ID}"

TOPICO_ESTADO = f"/TEF/{DEVICE_ID}/attrs"
TOPICO_TEMPERATURA = f"/TEF/{DEVICE_ID}/attrs/t"
TOPICO_UMIDADE = f"/TEF/{DEVICE_ID}/attrs/h"

TOPICOS = [
    (TOPICO_ESTADO, 0),
    (TOPICO_TEMPERATURA, 0),
    (TOPICO_UMIDADE, 0),
]

# Ultimas leituras recebidas (usado apenas para exibir um resumo)
telemetria = {"estado_led": None, "temperatura": None, "umidade": None}


# ------------------------------------------------------------------- Callbacks
def on_connect(client, userdata, flags, reason_code, properties=None):
    if reason_code == 0:
        print(f"[OK] Conectado ao broker {BROKER}:{PORT}")
        client.subscribe(TOPICOS)
        for topico, _ in TOPICOS:
            print(f"     inscrito em: {topico}")
        print("-" * 60)
    else:
        print(f"[ERRO] Falha na conexao. Codigo: {reason_code}")


def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8", errors="replace").strip()
    horario = datetime.now().strftime("%H:%M:%S")

    if msg.topic == TOPICO_TEMPERATURA:
        telemetria["temperatura"] = payload
        print(f"[{horario}] Temperatura: {payload} C")
    elif msg.topic == TOPICO_UMIDADE:
        telemetria["umidade"] = payload
        print(f"[{horario}] Umidade....: {payload} %")
    elif msg.topic == TOPICO_ESTADO:
        # O ESP32 publica "s|on" ou "s|off"
        estado = payload.split("|")[-1]
        telemetria["estado_led"] = estado
        print(f"[{horario}] LED........: {estado.upper()}")
    else:
        print(f"[{horario}] {msg.topic} -> {payload}")


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

    print(f"Conectando ao broker {BROKER}:{PORT} como '{CLIENT_ID}'...")
    client.connect(BROKER, PORT, keepalive=60)

    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("\n[INFO] Encerrando o subscriber...")
        print("Ultima telemetria recebida:")
        print(json.dumps(telemetria, indent=2, ensure_ascii=False))
    finally:
        client.disconnect()


if __name__ == "__main__":
    main()
