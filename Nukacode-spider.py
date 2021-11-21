import requests
from bs4 import BeautifulSoup
import json


def get_nuke_code_nukacrypt():
    res = ''
    r = requests.get("https://nukacrypt.com/")
    soup = BeautifulSoup(r.text, 'html.parser')
    spot = ['A', 'B', 'C']
    a_td = soup.find_all('td', {'style': "text-align: center;"})
    bc_td = soup.find_all('td', {'style': "text-align:center;"})
    # 破nukacrypt连空格都漏打了，以至于我得写两行分别抓
    nuke_date = soup.find('th', {'colspan': "3"})
    total_td = a_td + bc_td
    res += ('  -----=====-----\n')
    res += (nuke_date.string+'\n')
    for i in range(0, 3):
        res += ('     {}点：'.format(spot[i])+total_td[i].string+'\n')
    res += ('  -----=====-----')
    return res


def get_nuke_code_rougetrader():
    url = 'https://a.roguetrader.com/graphql'
    headers = {
        'origin': 'https://roguetrader.com',
        'accept-encoding': 'gzip, deflate, br',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44'
    }

    payload_data = {
        "operationName": "dashboard",
        "variables": "{}",
        "query": "query dashboard {\n  dashboard {\n    id\n    results\n    __typename\n  }\n}\n"
    }

    r = requests.post(url=url, data=payload_data, headers=headers, timeout=30)
    data = json.loads(r.text)
    data_str = str(data)
    a, b, c, t = "'alpha': '", "'bravo': '", "'charlie': '", "'range'"
    a_code = data_str[data_str.find(a)+10:data_str.find(a)+18]
    b_code = data_str[data_str.find(b)+10:data_str.find(b)+18]
    c_code = data_str[data_str.find(c)+12:data_str.find(c)+20]
    time_start = data_str[data_str.find(t)+16:data_str.find(t)+21]
    time_end = data_str[data_str.find(t)+40:data_str.find(t)+45]
    res = time_start + '至' + time_end + \
        '\nA点：' + a_code + '\nB点：' + b_code + '\nC点：' + c_code
    return res


def main():
    # print(get_nuke_code_nukacrypt())
    print(get_nuke_code_rougetrader())


main()
