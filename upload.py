# Author: justin0u0<mail@justin0u0.com>

import requests
import getpass

url = 'https://acm.cs.nthu.edu.tw/users/login/'
username = input('Username: ')
password = getpass.getpass('Password: ')

headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

session = requests.session()
r = session.get(url, headers=headers)

payload = {
  'username': username,
  'password': password,
  'csrfmiddlewaretoken': session.cookies['csrftoken']
}

headers = {
  'Referer': url,
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

res = session.post(url, headers=headers, data=payload)

if res.status_code == 200:
  print('Login successfully')

problem_id = input('Problem ID: ')
upload_url = f'https://acm.cs.nthu.edu.tw/problem/{problem_id}/testcase/'

headers = {
  'Referer': f'https://acm.cs.nthu.edu.tw/problem/{problem_id}/edit/',
  'X-CSRFToken': session.cookies['csrftoken'],
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

testcases = int(input('Number of testcases: '))

for testcase in range(testcases):
  file_name = f'./data/{problem_id}_{str(testcase).zfill(2)}'
  print(f'Uploading {file_name}.in, {file_name}.out ...')

  files = {
    't_in': open(f'{file_name}.in', 'rb'),
    't_out': open(f'{file_name}.out', 'rb')
  }

  payload = {
    'time_limit': 1,
    'memory_limit': 32
  }

  res = session.post(upload_url, headers=headers, files=files, data=payload)

  if res.status_code == 200:
    print(f'Upload {file_name}.in, {file_name}.out successfully')

