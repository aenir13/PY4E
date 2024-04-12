import requests

def get_plus_code(address):
    # Substitua YOUR_API_KEY pela sua chave da API do Google Maps
    api_key = "http://py4e-data.dr-chuck.net/opengeo?"
    base_url = "http://py4e-data.dr-chuck.net/opengeo?"
    params = {"address": address, "key": api_key}
    response = requests.get(base_url, params=params)
    data = response.json()

    if "plus_code" in data["results"][0]:
        return data["results"][0]["plus_code"]["compound_code"]
    else:
        return "Plus code not found"

address = "Universidad de Buenos Aires"
plus_code = get_plus_code(address)
print(f"Plus code for '{address}': {plus_code}")
