# import requests
def superhero_int(hero1 = 'Thanos', hero2 = 'Hulk', hero3 = 'Captain America'):
    res = (requests.get('https://akabab.github.io/superhero-api/api//all.json'))
    data = res.json()
    print("Cамый умный супергерой:", max(dict([((data[i]['name'],data[i]['powerstats']['intelligence'])) for i in range(len(data)) if data[i]['name'] in (hero1+hero2+hero3)])))
superhero_int()

### 2 exersise
import requests
token = ' ' # токен надо ввести
def upload_file(file_path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    headers = { 'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}
    params = {"path": file_path, "overwrite": "true"}
    response = requests.get(url,headers=headers, params=params)
    link = response.json().get('href')
    buff = requests.put(link, file_path)
    print(buff)
if __name__ == '__main__':
    upload_file('file_homework.txt')
    
### 3 exersise [Работает через раз, часто вылетает ошибка с соеденинем сервера]
import requests 
res = requests.get('https://api.stackexchange.com/2.3/questions?fromdate=1680566400&todate=1680825600&order=desc&sort=activity&tagged=python&site=stackoverflow')
data = res.json()
for res in data['items']:
    print(res['title'])
        