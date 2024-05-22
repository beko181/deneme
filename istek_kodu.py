import requests
import json

# Değişkenleri doldurun
measurement_id = "G-XMP1NCZ10X"
api_secret = "XVujbPOuQS6WYdLGK7E7jQ"
client_id = "5153568.1704207090"
event_name = "test_event"

# İstek verisini oluşturun
data = {
    "client_id": client_id,
    "events": [
        {
            "name": event_name,

        }
    ]
}

# JSON verisini oluşturun ve uzunluğunu hesaplayın
json_data = json.dumps(data)
content_length = len(json_data)

# HTTP isteği başlığını oluşturun
headers = {
    "Content-Type": "application/json",
    "Content-Length": str(content_length)
}

# URL'yi oluşturun
url = f"https://www.google-analytics.com/mp/collect?measurement_id=G-XMP1NCZ10X&api_secret=XVujbPOuQS6WYdLGK7E7jQ"

# POST isteğini gönderin
response = requests.post(url, headers=headers, data=json_data)

# Yanıtı kontrol edin
if response.status_code == 200:
    print("İstek başarıyla gönderildi.")
else:
    print(f"Hata kodu: {response.status_code}")
    print(f"Hata mesajı: {response.text}")

