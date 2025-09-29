import requests

#Function
def ApiRequest(): 
    URL = "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"
    response = requests.get(URL)
    if response.status_code == 200:
        print("Connected")
        data = response.json()   
        results = data['results']   
        pokemons = []    
        for pokemon in results:
            obj = {"Pokemon":pokemon['name'] , "Img": pokemon['url']}
            pokemons.append(obj)
        return pokemons
    else:
        print("Problems:", response.text)


