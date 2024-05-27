import websocket
import json
import requests
import time
import os

email = os.environ['email']
password = os.environ['password']


def refresh_token(email, password):
    data = {
        "email": email,
        "password": password,
        "vars": {
            "client_version": "99999",
        },
    }

    headers = {
        "authorization": "Basic OTAyaXViZGFmOWgyZTlocXBldzBmYjlhZWIzOTo="
    }

    try:
        response = requests.post(
            "https://gooberroyale-api.winterpixel.io/v2/account/authenticate/email?create=false",
            data=json.dumps(data),
            headers=headers,
        )
        token = json.loads(response.content)["token"]
        return token
    except Exception:
        print("Invalid credentials!")


def auto_claim():
    while True:
        token = str(refresh_token(email, password))
        ws1 = websocket.create_connection(
            "wss://gooberroyale-api.winterpixel.io/ws?lang=en&status=true&token="
            + token)
        collect_coins = {
            "cid": "2",
            "rpc": {
                "id": "claim_rewarded",
                "payload": "{}"
            }
        }
        ws1.send(json.dumps(collect_coins).encode())
        ws1.recv()
        msg1 = ws1.recv()
        a = json.loads(msg1)
        # print(a)

        wallet_coins = json.loads(a["rpc"]["payload"])["wallet"]["coins"]

        while wallet_coins > 2000:
            ws2 = websocket.create_connection(
                "wss://gooberroyale-api.winterpixel.io/ws?lang=en&status=true&token="
                + token)
            collect_goal = {
                "cid": "3",
                "rpc": {
                    "id": "tankkings_refresh_goal",
                    "payload": '{"goal_index":0}'
                },
            }
            ws2.send(json.dumps(collect_goal).encode())
            ws2.recv()
            msg2 = ws2.recv()
            b = json.loads(msg2)
            # print(b)

            wallet_coins = json.loads(b["rpc"]["payload"])["wallet"]["coins"]

            time.sleep(1)
            ws2.close()

        ws1.close()
        #time.sleep(181)


auto_claim()
