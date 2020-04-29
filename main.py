from nornir import InitNornir


def main(mac, network):
    # Инициализация Nornir
    try:
        nr = InitNornir(config_file="nornir_config.yaml")
    except FileNotFoundError as err:
        print("Nornir init error: ", err)
        return None
