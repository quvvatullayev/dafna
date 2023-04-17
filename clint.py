import requests

url = "http://127.0.0.1:8000/dafna_app/logout_user/"

payload={}
headers = {
  'Authorization': 'Token bf8f5abaa6824126167dd1ca319cd0c7408c2544',
  'Cookie': 'csrftoken=9zZVkUrbNqlxi3512iYE7XDFwDWHhSp7'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)