import requests

try:
    response = requests.post("https://httpbin.org/post", json={"name":"Mykola", "profession":"AI Engineer"})
    # response = requests.get("https://httpbin.org/get", params={"name":"Mykola", "age":"50"})
    # response = requests.get("https://api.github.com")
    response.raise_for_status()
    data = response.json()
    print(data["json"])
    
except requests.JSONDecodeError:
    print("Ошибка! Тело ответа пусто или это не JSON.")
    
except requests.HTTPError:
    print("HTTP ошибка")
    
except requests.RequestException:
    print("Сбой соединения")