import requests
import pandas as pd
import time
pd.set_option('max_rows', 500)

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}

url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=317236632633'  # 定义要访问的地址
r = requests.get(url, headers=headers)  # 使用requests发起请求

import json

data_json = json.loads(r.text)
data = data_json['data']  # 取出json中的数据
areaTree = data['areaTree']  # 取出areaTree

# 将提取数据的方法封装为函数
def get_data(data, info_list):
    info = pd.DataFrame(data)[info_list]  # 主要信息

    today_data = pd.DataFrame([i['today'] for i in data])  # 生成today的数据
    today_data.columns = ['today_' + i for i in today_data.columns]  # 修改列名

    total_data = pd.DataFrame([i['total'] for i in data])  # 生成total的数据
    total_data.columns = ['total_' + i for i in total_data.columns]  # 修改列名

    return pd.concat([info, total_data, today_data], axis=1)  # info、today和total横向合并最终得到汇总的数据


today_world = get_data(areaTree, ['id', 'name'])
today_world.head()


def save_data(data, name):  # 定义保存数据方法
    file_name = name + '_' + time.strftime('%Y_%m_%d', time.localtime(time.time())) + '.csv'
    data.to_csv(file_name, index=None, encoding='utf_8_sig')
    print(file_name + ' 保存成功！')


time.strftime('%Y_%m_%d', time.localtime(time.time()))
save_data(today_world, 'today_world')