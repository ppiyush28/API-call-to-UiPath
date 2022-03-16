import requests

''' genrating bearer token while authentication'''

data ={
“tenancyName” : “**",
“usernameOrEmailAddress” : "**”,
“password” : “**”
}

headers = { “Content-Type” : “application/json” }

response = requests.post(“basic orchestrator url” + “api/Account/Authenticate”,json=data,headers=headers,verify=False)
print('auth status : ' req.status_code)

auth = "Bearer " + response.json()[‘result’]

''' data fetch using token '''

headers1 = { “Content-Type” : “application/json”,
          Authorization" : auth }
            
            
req = requests.get(“basic orchestrator url” + "odata/Jobs",json=data,headers=headers,verify=False)
print('data fetch status : ' req.status_code)
           


