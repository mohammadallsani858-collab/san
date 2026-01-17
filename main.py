import urllib.request
import json

print("আসসালামু আলাইকুম সানি ভাই! আপনার এআই এখন তৈরি।")
surah = input("সূরা নম্বর দিন: ")
ayah = input("আয়াত নম্বর দিন: ")

url = f"https://api.alquran.cloud/v1/ayah/{surah}:{ayah}/bn.bengali"
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())
    print("আয়াত: ", data['data']['text'])
