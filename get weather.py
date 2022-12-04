import requests

cities = ['sanfrancisco', 'london', 'svo', 'череповец']
payload = {'n': '', 'T': '', 'q': '', 'M': '', 'lang': 'ru'}

for city in cities:
  response = requests.get(f'https://wttr.in/{city}', params=payload)
  response.raise_for_status()
  print(response.text)