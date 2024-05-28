import requests
import json
import pwinput
import time

email = input(f"Email   : ")
password = pwinput.pwinput(prompt=f"Password: ", mask="*")

response = requests.post("https://dev-nakama.winterpixel.io/v2/account/authenticate/email?create=false", data=json.dumps({"email": email, "password": password, "vars": {"client_version": "999"}}), headers={"Authorization": "Basic OTAyaXViZGFmOWgyZTlocXBldzBmYjlhZWIzOTo="})
token = json.loads(response.content)["token"]

response2 = requests.get("https://dev-nakama.winterpixel.io/v2/friend",
                         headers={"authorization": f"Bearer {token}"})
friends = json.loads(response2.content)['friends']

user_id = input("Enter the user id:")

# def friend_code_to_id(friend_code):
#     data = {"friend_code": friend_code}
#     headers = {"authorization": f"Bearer {token}"}
    
#     response = requests.post(
#             "https://dev-nakama.winterpixel.io/v2/rpc/winterpixel_query_user_id_for_friend_code",
#             data=json.dumps(data),
#             headers=headers,
#         )

#     a = json.loads(response.content)
#     print(a)
#     return a["payload"]["user_id"]

# id = friend_code_to_id(friend_code)
# # for friend in friends:
# #   if friend['state'] == 2:
# #       ids.append(friend['user']['id'])

confirm = input(f"Do you want to delete {user_id} ? (Y/N)")

if confirm.lower() in ["y", "yes"]:
    # for id in ids:
    requests.delete(f"https://dev-nakama.winterpixel.io/v2/friend?ids={user_id}", headers={"authorization": f"Bearer {token}"})
    time.sleep(1)
    
    print(f"Succesfully deleted")
