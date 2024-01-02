client_id = '9n2YgE8RNMhYnO7Jsm3jHw'
client_secret = 'U2_VWOcgqVmcE172DmSMT-TOJuSf3Q'

import requests
li=[]
li2=[]
auth=requests.auth.HTTPBasicAuth(client_id,client_secret)
data =  {
'grant_type': 'password',
'username':'BigDeccer',
'password': 'arvind2301'
}

headers = {'User-Agent' : 'MyAPI/0.0.1'}
res = requests.post('https://www.reddit.com/api/v1/access_token',auth=auth , data=data , headers=headers)
TOKEN= res.json()['access_token']
headers={**headers,**{'Authorization': f'bearer {TOKEN}'}}

res= requests.get('https://oauth.reddit.com/r/nosleep/hot',headers=headers)

for post in res.json()['data']['children']:
    li.append((post['data']['titl']:
    li2.append((post['data']['selftext']e']))
    
for post in res.json()['data']['children))
    

print(li[8])
h=((li2[8]))
file = open('D:\Coding Work\Codeforces\Python\Reddit.txt','w')
file.write(h)
file.close()