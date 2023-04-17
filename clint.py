import requests

url = "http://127.0.0.1:8000/dafna_app/get_cart/"

payload={}
headers = {
  'Authorization': 'Token 5f0b15f35a679f02794d7da9912fafc7c2dd54a0',
  'Cookie': 'csrftoken=9zZVkUrbNqlxi3512iYE7XDFwDWHhSp7'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json())