import requests
import json
from base64 import b64decode


def get_akash_txs(block_num: str) -> None:
    """Выводим информацию по транзакциям очередного блока"""

    akash_response = requests.get(url=f"https://akash-rest.publicnode.com/blocks/{block_num}")

    with open("block.json", "w") as file:
        json.dump(akash_response.json(), file, indent=4)

    with open("block.json", "r") as file:
        data = json.load(file)

    try:
        txs = data["block"]["data"]["txs"]
        if txs:
            for i_tx in txs:
                print(b64decode(i_tx))
        else:
            print("Not txs are found in the block")
    except KeyError:
        if data.get("error"):
            print(f"Error - {data['error']}")
        else:
            print("No txs are found or some other error occurred")


if __name__ == '__main__':
    user_block = input("Enter the block number: ")
    get_akash_txs(block_num=user_block)
