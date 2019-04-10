#!/usr/bin/env python3  # 保证可以直接Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-
__Author__: 'Lucifer'
__Date__: "2019/02/28  下午 6:59"
__Name__: 'douban_top250.py'
__IDE__: 'PyCharm'

import re
import requests
from functools import reduce
import time

# 输入输入单个电影信息块, 输出影名信息
def title(contents):
    res = re.search('(<span class="title">.*?)</a>', contents, re.S)  # 提取电影名信息所在代码块
    if res:
        contents1 = res.group(1)
        res = re.findall('<span.*?>(.*?)</span>', contents1, re.S)  # 提取电影所有名的信息
        tits = []
        for result in res:
            result = re.sub('  ', '', result)  # 结果清洗
            result = result.split(';')[-1]  # 多个名称分割
            tits.append(result)
        return tits

# 提取导演/主演/时间/国家/电影标签的信息 输入单个电影信息块 输出director_Actor_Time_Nation_Tag list
def dATNT(contents):
    res = re.search('<div class="bd">.*?>(.*?)</p>', contents, re.S)  # 匹配导演/主演/时间/国家/电影标签的信息所在的部分
    if not res:
        return '初步信息提取失败'
    res = res.group(1)
    result = res.strip().split('&nbsp;')  # 将初步提取的信息块分割
    last = []
    info = []
    for i in result:  # 将分割的list清洗, 除去 '' 和 '/'
        if i != '/' and i:
            last.append(i.strip())
    director = last[0].split(':')[-1]  # 提出导演姓名
    info.append(director.strip())
    time1 = re.search(r'\d{4}', last[1], re.S)  # 时间信息单独提取
    if not time1:
        return '时间信息提取失败'
    time1 = time1.group()
    actor = last[1].split('<br>')[0]
    info.append(actor.split(':')[-1].strip())
    info.append(time1)
    info.append(last[-2])  # 加入国籍
    info.append(last[-1])  # 加入电影标签
    return info

# 输入整个电影信息块, 输出list[score/num, rmk]
def score(contents):
    score = re.search('<span class="rating_num".*?>(.*?)</span>', contents, re.S)   # 匹配评分内容  re.S .也匹配换行符
    score = score.group(1)
    num = re.search('<span>(.*?)人评价</span>', contents, re.S)  # 匹配参评人数  re.S .也匹配换行符
    num = num.group(1)
    remarks = re.search('<span class="inq">(.*?)</span>', contents, re.S)  # 匹配影评  re.S .也匹配换行符
    remarks = remarks.group(1)
    if not score:
        score = '评分提取失败'
    if not num:
        num = '参评人数提取失败'
    if not remarks:
        remarks = '影评提取失败'
    s_n = '/'.join([score, num])  # join 参数时可迭代对象
    return [s_n, remarks]

def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }  # 设置头文件
    response = requests.get(url, headers=headers)
    if response.status_code == 200:  # 访问成功的状态码
        return response.text
    return None

def crawler(url):
    html = get_one_page(url)  # 获取所有html代码
    if not html:
        raise ('网页访问失败:' + url)
    segments = re.findall('<div class="pic">.*?</li>', html, re.S)  # 爬取每个电影信息所在的代码块 组成列表
    for contents in segments:
        name = reduce(lambda x, y: x + '/' + y, title(contents))  # 将多个名字用/连接在一起  reduce lambda表达式  用join也行
        with open('douban.txt', 'a+', encoding='utf8') as f:  # encoding='utf8'不加会乱码  a+以追加模式继续写入
            f.write(name)
            f.write('   ')
            for i in dATNT(contents):   # 循环将dATNT(contents)生成的列表写入文件
                f.write(i)
                f.write('   ')
            for i in score(contents):  # 循环将score(contents)生成的列表写入文件
                f.write(i)
                f.write('   ')
            f.write('\n')  # 写完一行后换行, 并关闭文件句柄, 下次打开会从下一行追加文本

def main(offset):  # 循环重构后续网页
    url = 'https://movie.douban.com/top250?start=' + str(offset) + '&filter='
    crawler(url)


if __name__ == '__main__':
    with open('douban.txt', 'w', encoding='utf8') as f:  # w 写模式, 会重写文档
        f.write('片名     导演      主演     时间    国籍     标签     评分/参评人数     影评\n')
    URL = 'https://movie.douban.com/top250'
    crawler(URL)
    for i in range(1, 10):
        main(i * 25)
        time.sleep(1)  # 每次访问时间间隔一秒


