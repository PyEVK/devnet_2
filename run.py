import argparse
from main import main
#
NETWORK_ADDR = "192.168.100.0/24"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--mac', type=str, required=True, help='MAC address for search')

    mac = parser.parse_args()

    main(mac, NETWORK_ADDR)
