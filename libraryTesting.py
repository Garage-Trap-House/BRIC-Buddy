import requests
from requests.exceptions import HTTPError

def requestsAttempt(): 
    
    response = requests.get('https://api.github.com')

    if response.status_code == 200: 
        return "it worked!"
    elif response.status_code == 404: 
        return "not found :("


    # for url in ['https://api.github.com', 'https://api.github.com/invalid']: 
    #     try: 
    #         response = requests.get(url)
        
    #     except HTTPError as http_err: 
    #         print(f'HTTP error occured: {http_err}')
    #     except Exception as err: 
    #         print(f'OTher error occured: {err}')
        
    #     else: 
    #         print('Success !!!')
