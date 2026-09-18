"""Publisher MQTT - envia comandos de liga/desliga do LED para o ESP32 (Wokwi).

Atividade de Edge Computing: Python (Paho MQTT) -> Broker MQTT -> Wokwi.

Grupo (1ESPI):
    Bruno Carreiro Dos Santos            - RM 569423
    Eduardo Bechara Medeiros Craveiro    - RM 571081
    Gustavo Moita de Lima                - RM 569180
    Daniel Graciano dos Santos Ferreira  - RM 568886

Como usar (Colab ou local):
    pip install paho-mqtt
    python mqtt_publisher.py

Antes de executar, troque DEVICE_ID pelo numero do seu computador (ex.: "device015").
"""

import time

import paho.mqtt.client as mqtt

# --------------------------------------------------------------- Configuracao
BROKER = "54.91.80.136"
PORT = 1883
DEVICE_ID = "deviceXXX"  # <-- troque pelo numero do seu computador (ex.: device015)
CLIENT_ID = f"python_publisher_{DEVICE_ID}"

TOPICO_COMANDO = f"/TEF/{DEVICE_ID}/cmd"

COMANDO_LIGAR = f"{DEVICE_ID}@on|"
COMANDO_DESLIGAR = f"{DEVICE_ID}@off|"

INTERVALO = 5  # segundos entre um comando e outro
CICLOS = 5     # quantas vezes liga/desliga (use None para repetir sem parar)


def criar_cliente():
    """Cria o cliente compativel com paho-mqtt 1.x e 2.x."""
    try:  # paho-mqtt >= 2.0
        return mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=CLIENT_ID)
    except AttributeError:  # paho-mqtt 1.x
        return mqtt.Client(client_id=CLIENT_ID)


def enviar(client, comando):
    resultado = client.publish(TOPICO_COMANDO, comando)
    status = "OK" if resultado.rc == mqtt.MQTT_ERR_SUCCESS else f"ERRO ({resultado.rc})"
    print(f"[{status}] {TOPICO_COMANDO} <- {comando}")


def main():
    client = criar_cliente()

    print(f"Conectando ao broker {BROKER}:{PORT} como '{CLIENT_ID}'...")
    client.connect(BROKER, PORT, keepalive=60)
    client.loop_start()
    print(f"[OK] Conectado. Publicando em {TOPICO_COMANDO}")
    print("-" * 60)

    ciclo = 0
    try:
        while CICLOS is None or ciclo < CICLOS:
            ciclo += 1
            print(f"\nCiclo {ciclo}")
            enviar(client, COMANDO_LIGAR)
            time.sleep(INTERVALO)
            enviar(client, COMANDO_DESLIGAR)
            time.sleep(INTERVALO)
    except KeyboardInterrupt:
        print("\n[INFO] Encerrando o publisher...")
    finally:
        client.loop_stop()
        client.disconnect()
        print("[INFO] Desconectado do broker.")


if __name__ == "__main__":
    main()
