from os import walk, remove
from time import sleep
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


def send_to_server(name, path):
    mp_encoder = MultipartEncoder(
        fields={
            'file_name': str(name),
            'file_data': (str(name), open(str(path), 'rb'), 'text/plain'),
            'direction': 'UTD'
        }
    )

    url = "http://127.0.0.1:8000/traffic/footage"
    response = requests.post(url, data=mp_encoder, headers={'Content-Type': mp_encoder.content_type})
    print(response.json())


def main():
    files = []

    for (dirpath, dirnames, filenames) in walk("./outputs"):
        files = filenames

    for name in files:
        send_to_server(name, "./outputs/" + name)
        remove("./outputs/" + name)
        sleep(1000)

    if len(files) == 0:
        print("Nothing to send!")
        sleep(100)


while True:
    main()
