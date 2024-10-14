import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth


# password = getpass()

# headers = {'Authorization': f'Bearer b17fc6498e63a93751e8e1db66d7711a589bc00f'}
# headers = {'Authorization': f'Token b17fc6498e63a93751e8e1db66d7711a589bc00f'}
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/128.0 Mobile/15E148 Safari/605.1.15',
    'Content-Type': 'application/json',
    # 'Authorization': f'Token b17fc6498e63a93751e8e1db66d7711a589bc00f'
}
cookies = {'sessionid': 'cik74arx1c08rmqlkvl3mr8o0446rmzq'}
endpoint = 'http://127.0.0.1:8000/all/'

r = requests.get(endpoint, headers=headers, cookies=cookies)

print(r.headers)