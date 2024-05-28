import websocket, json, requests, time, datetime, os, keep_alive
from replit import db
from threading import Thread


email = os.environ['email']
email_2 = os.environ['email2']
password = os.environ['password']


if "token_dict" not in db.keys():
    db["token_dict"] = {"token": None, "last_refresh": None}


def refresh_token(email, password):
    # Only refresh token if 9 minutes have passed
    if db["token_dict"]["token"] is not None and db["token_dict"]["last_refresh"] is not None:
        time_diff = time.time() - db["token_dict"]["last_refresh"]

        if time_diff < 540:
            token = db["token_dict"]["token"]
            return token

    data = {
        "email": email,
        "password": password,
        "vars": {
            "client_version": "99999",
        },
    }

    headers = {
        # Secret to initially access server.
        "authorization": "Basic OTAyaXViZGFmOWgyZTlocXBldzBmYjlhZWIzOTo="
    }

    # Get token
    try:
        response = requests.post(
            "https://gooberdash-api.winterpixel.io/v2/account/authenticate/email?create=false",
            data=json.dumps(data),
            headers=headers,
        )
        token = json.loads(response.content)["token"]
        db["token_dict"]["token"] = token
        db["token_dict"]["last_refresh"] = time.time()
        return token
    except Exception:
        print("Invalid credentials!")


def collect_free_spin_no_ads():
    while True:
        token = str(refresh_token(email, password))
        current_timestamp = f"{datetime.datetime.utcfromtimestamp(time.time()):%Y-%m-%d %H:%M:%S} UTC"
        try:
            ws1 = websocket.create_connection("wss://gooberdash-api.winterpixel.io/ws?lang=en&status=true&token="+token)
            free_spin_no_ads = {"cid": "990", "rpc": {"id": "free_spin", "payload": "{}"}}
            ws1.send(json.dumps(free_spin_no_ads).encode())
            ws1.recv()
            msg1 = ws1.recv()
            msg1_json_loads = json.loads(msg1)
            global print_1
            print_1 = f"1 {msg1_json_loads}"
            global state_1
            state_1 = 'FAIL'
            ws1.close()
            if 'status_presence_event' not in print_1:
                if 'error' not in msg1_json_loads:
                    state_1 = 'SUCCESS'
                    with open("collect_log.txt", "a") as f:
                        f.write(f"{'free_spin_no_ads':<25};{'SUCCESS':<14};{current_timestamp}\n")
                else:
                    state_1 = 'NOT AVAILABLE'
        except Exception:
            with open("collect_log.txt", "a") as f:
                f.write(f"{'free_spin_no_ads':<25};{'FAIL':<14};{current_timestamp}\n")
        if state_1 == 'SUCCESS':
            time.sleep(43201)
        elif state_1 == 'NOT AVAILABLE':
            time.sleep(3600)
        elif state_1 == 'FAIL':
            time.sleep(10)


def collect_free_coin_with_ads():
    while True:
        token = str(refresh_token(email, password))
        current_timestamp = f"{datetime.datetime.utcfromtimestamp(time.time()):%Y-%m-%d %H:%M:%S} UTC"
        try:
            ws2 = websocket.create_connection("wss://gooberdash-api.winterpixel.io/ws?lang=en&status=true&token="+token)
            free_coin_with_ads = {"cid": "991", "rpc": {"id": "claim_rewarded_ad",
                     "payload": "{\"ad_placement\":\"free_coin\"}"}}
            ws2.send(json.dumps(free_coin_with_ads).encode())
            ws2.recv()
            msg2 = ws2.recv()
            msg2_json_loads = json.loads(msg2)
            global print_2
            print_2 = f"2 {msg2_json_loads}"
            global state_2
            state_2 = 'FAIL'
            ws2.close()
            if 'status_presence_event' not in print_2:
                if 'error' not in msg2_json_loads:
                    state_2 = 'SUCCESS'
                    with open("collect_log.txt", "a") as f:
                        f.write(f"{'free_coin_with_ads':<25};{'SUCCESS':<14};{current_timestamp}\n")
                else:
                    state_2 = 'NOT AVAILABLE'
        except Exception:
            with open("collect_log.txt", "a") as f:
                f.write(f"{'free_coin_with_ads':<25};{'FAIL':<14};{current_timestamp}\n")
        if state_2 == 'SUCCESS':
            time.sleep(3601)
        elif state_2 == 'NOT AVAILABLE':
            time.sleep(720)
        elif state_2 == 'FAIL':
            time.sleep(10)


def collect_free_gem_with_ads():
    while True:
        token = str(refresh_token(email, password))
        current_timestamp = f"{datetime.datetime.utcfromtimestamp(time.time()):%Y-%m-%d %H:%M:%S} UTC"
        try:
            ws3 = websocket.create_connection("wss://gooberdash-api.winterpixel.io/ws?lang=en&status=true&token="+token)
            free_gem_with_ads = {"cid": "992", "rpc": {"id": "claim_rewarded_ad",
                     "payload": "{\"ad_placement\":\"free_gem\"}"}}
            ws3.send(json.dumps(free_gem_with_ads).encode())
            ws3.recv()
            msg3 = ws3.recv()
            msg3_json_loads = json.loads(msg3)
            global print_3
            print_3 = f"3 {msg3_json_loads}"
            global state_3
            state_3 = 'FAIL'
            ws3.close()
            if 'status_presence_event' not in print_3:
                if 'error' not in msg3_json_loads:
                    state_3 = 'SUCCESS'
                    with open("collect_log.txt", "a") as f:
                        f.write(f"{'free_gem_with_ads':<25};{'SUCCESS':<14};{current_timestamp}\n")
                else:
                    state_3 = 'NOT AVAILABLE'
        except Exception:
            with open("collect_log.txt", "a") as f:
                f.write(f"{'free_gem_with_ads':<25};{'FAIL':<14};{current_timestamp}\n")
        if state_3 == 'SUCCESS':
            time.sleep(86401)
        elif state_3 == 'NOT AVAILABLE':
            time.sleep(3600)
        elif state_3 == 'FAIL':
            time.sleep(10)


def collect_free_spin_with_ads():
    while True:
        token = str(refresh_token(email, password))
        current_timestamp = f"{datetime.datetime.utcfromtimestamp(time.time()):%Y-%m-%d %H:%M:%S} UTC"
        try:
            ws4a = websocket.create_connection("wss://gooberdash-api.winterpixel.io/ws?lang=en&status=true&token="+token)
            free_spin_with_ads = {"cid": "993", "rpc": {"id": "claim_rewarded_ad",
                     "payload": "{\"ad_placement\":\"free_spin\"}"}}
            ws4a.send(json.dumps(free_spin_with_ads).encode())
            ws4a.recv()
            msg4a = ws4a.recv()
            msg4a_json_loads = json.loads(msg4a)
            global print_4a
            print_4a = f"4a {msg4a_json_loads}"
            global state_4
            state_4 = 'FAIL'
            ws4a.close()

            time.sleep(5)
            
            ws4b = websocket.create_connection("wss://gooberdash-api.winterpixel.io/ws?lang=en&status=true&token="+token)
            free_spin_no_ads = {"rpc": {"id": "free_spin", "payload": "{}"}}
            ws4b.send(json.dumps(free_spin_no_ads).encode())
            ws4b.recv()
            msg4b = ws4b.recv()
            msg4b_json_loads = json.loads(msg4b)
            global print_4b
            print_4b = f"4b {msg4b_json_loads}"
            ws4b.close()

            if 'status_presence_event' not in print_4a and 'status_presence_event' not in print_4b:
                if 'error' not in msg4a_json_loads and 'error' not in msg4b_json_loads:
                    state_4 = 'SUCCESS'
                    with open("collect_log.txt", "a") as f:
                        f.write(f"{'free_spin_with_ads':<25};{'SUCCESS':<14};{current_timestamp}\n")
                else:
                    state_4 = 'NOT AVAILABLE'
        except Exception:
            with open("collect_log.txt", "a") as f:
                f.write(f"{'free_spin_with_ads':<25};{'FAIL':<14};{current_timestamp}\n")
        if state_4 == 'SUCCESS':
            time.sleep(21601)
        elif state_4 == 'NOT AVAILABLE':
            time.sleep(3600)
        elif state_4 == 'FAIL':
            time.sleep(10)


def collect_prize_round_with_ads():
    while True:
        token = str(refresh_token(email, password))
        current_timestamp = f"{datetime.datetime.utcfromtimestamp(time.time()):%Y-%m-%d %H:%M:%S} UTC"
        try:
            ws5 = websocket.create_connection("wss://gooberdash-api.winterpixel.io/ws?lang=en&status=true&token="+token)
            prize_round_with_ads = {"cid": "994", "rpc": {"id": "claim_rewarded_ad",
                     "payload": "{\"ad_placement\":\"prize_round\"}"}}
            ws5.send(json.dumps(prize_round_with_ads).encode())
            ws5.recv()
            msg5 = ws5.recv()
            msg5_json_loads = json.loads(msg5)
            global print_5
            print_5 = f"5 {msg5_json_loads}"
            global state_5
            state_5 = 'FAIL'
            ws5.close()
            if 'status_presence_event' not in print_5:
                if 'error' not in msg5_json_loads:
                    state_5 = 'SUCCESS'
                    with open("collect_log.txt", "a") as f:
                        f.write(f"{'prize_round_with_ads':<25};{'SUCCESS':<14};{current_timestamp}\n")
                else:
                    state_5 = 'NOT AVAILABLE'
        except Exception:
            with open("collect_log.txt", "a") as f:
                f.write(f"{'prize_round_with_ads':<25};{'FAIL':<14};{current_timestamp}\n")
        if state_5 == 'SUCCESS':
            time.sleep(43201)
        elif state_5 == 'NOT AVAILABLE':
            time.sleep(3600)
        elif state_5 == 'FAIL':
            time.sleep(10)

if "token_dict_2" not in db.keys():
  db["token_dict_2"] = {"token": None, "last_refresh": None}


def refresh_token_2(email, password):
  # Only refresh token if 9 minutes have passed
  if db["token_dict_2"]["token"] is not None and db["token_dict_2"]["last_refresh"] is not None:
      time_diff = time.time() - db["token_dict_2"]["last_refresh"]

      if time_diff < 540:
          token = db["token_dict_2"]["token"]
          return token

  data = {
      "email": email,
      "password": password,
      "vars": {
          "client_version": "99999",
      },
  }

  headers = {
      # Secret to initially access server.
      "authorization": "Basic OTAyaXViZGFmOWgyZTlocXBldzBmYjlhZWIzOTo="
  }

  # Get token
  try:
      response = requests.post(
          "https://gooberdash-api.winterpixel.io/v2/account/authenticate/email?create=false",
          data=json.dumps(data),
          headers=headers,
      )
      token = json.loads(response.content)["token"]
      db["token_dict_2"]["token"] = token
      db["token_dict_2"]["last_refresh"] = time.time()
      return token
  except Exception:
      print("Invalid credentials!")


def collect_free_spin_no_ads_2():
  while True:
      token = str(refresh_token(email_2, password))
      current_timestamp = f"{datetime.datetime.utcfromtimestamp(time.time()):%Y-%m-%d %H:%M:%S} UTC"
      try:
          ws1 = websocket.create_connection("wss://gooberdash-api.winterpixel.io/ws?lang=en&status=true&token="+token)
          free_spin_no_ads = {"cid": "990", "rpc": {"id": "free_spin", "payload": "{}"}}
          ws1.send(json.dumps(free_spin_no_ads).encode())
          ws1.recv()
          msg1 = ws1.recv()
          msg1_json_loads = json.loads(msg1)
          global print_1
          print_1 = f"1 {msg1_json_loads}"
          global state_1
          state_1 = 'FAIL'
          ws1.close()
          if 'status_presence_event' not in print_1:
              if 'error' not in msg1_json_loads:
                  state_1 = 'SUCCESS'
                  with open("collect_log.txt", "a") as f:
                      f.write(f"{'free_spin_no_ads':<25};{'SUCCESS':<14};{current_timestamp}\n")
              else:
                  state_1 = 'NOT AVAILABLE'
      except Exception:
          with open("collect_log.txt", "a") as f:
              f.write(f"{'free_spin_no_ads':<25};{'FAIL':<14};{current_timestamp}\n")
      if state_1 == 'SUCCESS':
          time.sleep(43201)
      elif state_1 == 'NOT AVAILABLE':
          time.sleep(3600)
      elif state_1 == 'FAIL':
          time.sleep(10)


def collect_free_coin_with_ads_2():
  while True:
      token = str(refresh_token(email_2, password))
      current_timestamp = f"{datetime.datetime.utcfromtimestamp(time.time()):%Y-%m-%d %H:%M:%S} UTC"
      try:
          ws2 = websocket.create_connection("wss://gooberdash-api.winterpixel.io/ws?lang=en&status=true&token="+token)
          free_coin_with_ads = {"cid": "991", "rpc": {"id": "claim_rewarded_ad",
                   "payload": "{\"ad_placement\":\"free_coin\"}"}}
          ws2.send(json.dumps(free_coin_with_ads).encode())
          ws2.recv()
          msg2 = ws2.recv()
          msg2_json_loads = json.loads(msg2)
          global print_2
          print_2 = f"2 {msg2_json_loads}"
          global state_2
          state_2 = 'FAIL'
          ws2.close()
          if 'status_presence_event' not in print_2:
              if 'error' not in msg2_json_loads:
                  state_2 = 'SUCCESS'
                  with open("collect_log.txt", "a") as f:
                      f.write(f"{'free_coin_with_ads':<25};{'SUCCESS':<14};{current_timestamp}\n")
              else:
                  state_2 = 'NOT AVAILABLE'
      except Exception:
          with open("collect_log.txt", "a") as f:
              f.write(f"{'free_coin_with_ads':<25};{'FAIL':<14};{current_timestamp}\n")
      if state_2 == 'SUCCESS':
          time.sleep(3601)
      elif state_2 == 'NOT AVAILABLE':
          time.sleep(720)
      elif state_2 == 'FAIL':
          time.sleep(10)


def collect_free_gem_with_ads_2():
  while True:
      token = str(refresh_token(email_2, password))
      current_timestamp = f"{datetime.datetime.utcfromtimestamp(time.time()):%Y-%m-%d %H:%M:%S} UTC"
      try:
          ws3 = websocket.create_connection("wss://gooberdash-api.winterpixel.io/ws?lang=en&status=true&token="+token)
          free_gem_with_ads = {"cid": "992", "rpc": {"id": "claim_rewarded_ad",
                   "payload": "{\"ad_placement\":\"free_gem\"}"}}
          ws3.send(json.dumps(free_gem_with_ads).encode())
          ws3.recv()
          msg3 = ws3.recv()
          msg3_json_loads = json.loads(msg3)
          global print_3
          print_3 = f"3 {msg3_json_loads}"
          global state_3
          state_3 = 'FAIL'
          ws3.close()
          if 'status_presence_event' not in print_3:
              if 'error' not in msg3_json_loads:
                  state_3 = 'SUCCESS'
                  with open("collect_log.txt", "a") as f:
                      f.write(f"{'free_gem_with_ads':<25};{'SUCCESS':<14};{current_timestamp}\n")
              else:
                  state_3 = 'NOT AVAILABLE'
      except Exception:
          with open("collect_log.txt", "a") as f:
              f.write(f"{'free_gem_with_ads':<25};{'FAIL':<14};{current_timestamp}\n")
      if state_3 == 'SUCCESS':
          time.sleep(86401)
      elif state_3 == 'NOT AVAILABLE':
          time.sleep(3600)
      elif state_3 == 'FAIL':
          time.sleep(10)


def collect_free_spin_with_ads_2():
  while True:
      token = str(refresh_token(email_2, password))
      current_timestamp = f"{datetime.datetime.utcfromtimestamp(time.time()):%Y-%m-%d %H:%M:%S} UTC"
      try:
          ws4a = websocket.create_connection("wss://gooberdash-api.winterpixel.io/ws?lang=en&status=true&token="+token)
          free_spin_with_ads = {"cid": "993", "rpc": {"id": "claim_rewarded_ad",
                   "payload": "{\"ad_placement\":\"free_spin\"}"}}
          ws4a.send(json.dumps(free_spin_with_ads).encode())
          ws4a.recv()
          msg4a = ws4a.recv()
          msg4a_json_loads = json.loads(msg4a)
          global print_4a
          print_4a = f"4a {msg4a_json_loads}"
          global state_4
          state_4 = 'FAIL'
          ws4a.close()

          time.sleep(5)

          ws4b = websocket.create_connection("wss://gooberdash-api.winterpixel.io/ws?lang=en&status=true&token="+token)
          free_spin_no_ads = {"rpc": {"id": "free_spin", "payload": "{}"}}
          ws4b.send(json.dumps(free_spin_no_ads).encode())
          ws4b.recv()
          msg4b = ws4b.recv()
          msg4b_json_loads = json.loads(msg4b)
          global print_4b
          print_4b = f"4b {msg4b_json_loads}"
          ws4b.close()

          if 'status_presence_event' not in print_4a and 'status_presence_event' not in print_4b:
              if 'error' not in msg4a_json_loads and 'error' not in msg4b_json_loads:
                  state_4 = 'SUCCESS'
                  with open("collect_log.txt", "a") as f:
                      f.write(f"{'free_spin_with_ads':<25};{'SUCCESS':<14};{current_timestamp}\n")
              else:
                  state_4 = 'NOT AVAILABLE'
      except Exception:
          with open("collect_log.txt", "a") as f:
              f.write(f"{'free_spin_with_ads':<25};{'FAIL':<14};{current_timestamp}\n")
      if state_4 == 'SUCCESS':
          time.sleep(21601)
      elif state_4 == 'NOT AVAILABLE':
          time.sleep(3600)
      elif state_4 == 'FAIL':
          time.sleep(10)


def collect_prize_round_with_ads_2():
  while True:
      token = str(refresh_token(email_2, password))
      current_timestamp = f"{datetime.datetime.utcfromtimestamp(time.time()):%Y-%m-%d %H:%M:%S} UTC"
      try:
          ws5 = websocket.create_connection("wss://gooberdash-api.winterpixel.io/ws?lang=en&status=true&token="+token)
          prize_round_with_ads = {"cid": "994", "rpc": {"id": "claim_rewarded_ad",
                   "payload": "{\"ad_placement\":\"prize_round\"}"}}
          ws5.send(json.dumps(prize_round_with_ads).encode())
          ws5.recv()
          msg5 = ws5.recv()
          msg5_json_loads = json.loads(msg5)
          global print_5
          print_5 = f"5 {msg5_json_loads}"
          global state_5
          state_5 = 'FAIL'
          ws5.close()
          if 'status_presence_event' not in print_5:
              if 'error' not in msg5_json_loads:
                  state_5 = 'SUCCESS'
                  with open("collect_log.txt", "a") as f:
                      f.write(f"{'prize_round_with_ads':<25};{'SUCCESS':<14};{current_timestamp}\n")
              else:
                  state_5 = 'NOT AVAILABLE'
      except Exception:
          with open("collect_log.txt", "a") as f:
              f.write(f"{'prize_round_with_ads':<25};{'FAIL':<14};{current_timestamp}\n")
      if state_5 == 'SUCCESS':
          time.sleep(43201)
      elif state_5 == 'NOT AVAILABLE':
          time.sleep(3600)
      elif state_5 == 'FAIL':
          time.sleep(10)

t1 = Thread(target=collect_free_spin_no_ads)
t2 = Thread(target=collect_free_coin_with_ads)
t3 = Thread(target=collect_free_gem_with_ads)
t4 = Thread(target=collect_free_spin_with_ads)
t5 = Thread(target=collect_prize_round_with_ads)
t6 = Thread(target=collect_free_spin_no_ads_2)
t7 = Thread(target=collect_free_coin_with_ads_2)
t8 = Thread(target=collect_free_gem_with_ads_2)
t9 = Thread(target=collect_free_spin_with_ads_2)
t10 = Thread(target=collect_prize_round_with_ads_2)
t11 = Thread(target=keep_alive.keep_alive())

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()
t11.join()
