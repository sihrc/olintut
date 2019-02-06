from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

REQUEST_POOL = ThreadPoolExecutor(1000)

BASE_URL="http://localhost:5000"


def get_magic_call():
    return requests.get(f"{BASE_URL}/magic").text


def get_boring_call():
    return requests.get(f"{BASE_URL}/boring").text


def main(num_magic, num_boring):
    calls = {REQUEST_POOL.submit(get_magic_call): 1 for _ in range(num_magic)}
    calls.update({REQUEST_POOL.submit(get_boring_call): 0 for _ in range(num_boring)})

    magics = 0
    borings = 0
    for call in as_completed(calls):
        if calls[call]:
            magics += 1
        else:
            borings += 1
        print(f"Magics: {magics} | Borings: {borings}")


if __name__ == "__main__":
    main(10, 1000)
