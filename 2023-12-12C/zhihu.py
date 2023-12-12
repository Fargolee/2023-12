#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/12 19:23
# @Author  : Lee
# @File    : zhihu.py
import requests

class Zhihu:
    """
    知乎热榜
    """

    def __init__(self):
        self.hot_lists_api = 'https://api.zhihu.com/topstory/hot-lists/total'  # 热榜api
        self.recommend_lists_api = 'https://api.zhihu.com/topstory/recommend'  # 推荐api
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }
        self.hot = self.get_hot_lists()  # 热榜未处理数据
        self.recommend = self.get_recommend_lists()  # 推荐未处理数据
        self.hot_data = self.wash_hot_lists()  # 热榜处理后数据
        self.recommend_data = self.wash_recommend_lists()  # 推荐处理后数据

    def get_hot_lists(self):
        """
        获取知乎热榜
        :return: json
        """
        params = {'limit': '10',
                  'is_browser_model': '0'}
        response = requests.get(url=self.hot_lists_api, headers=self.headers, params=params)
        return response.json()

    def get_recommend_lists(self):
        """
        获取随机推荐
        :return:
        """
        params = {
            "action": "down",
            "ad_interval": "-10",
            "after_id": '1',  # TODO:
            "page_number": '1',  # TODO:
            "session_token": "99872c210b53364be1ede4bf459e8005", }
        response = requests.get(url=self.recommend_lists_api, headers=self.headers, params=params)
        return response.json()

    def wash_hot_lists(self):
        """
        清洗热榜数据
        :return:['[title](url)',....]
        """
        hot_lists = []
        for data in self.hot['data']:
            title = data['target']['title']
            url = data['target']['url'].replace('api.zhihu.com/questions', 'zhihu.com/question')
            hot_lists.append(f'[{title}]({url})')
        return hot_lists

    def wash_recommend_lists(self):
        """
        清洗推荐数据
        :return:
        """
        hot_lists = []
        for data in self.recommend['data']:
            try:
                title = data['target']['question']['title']
                url = data['target']['question']['url'].replace('api.zhihu.com/questions', 'zhihu.com/question')
            except KeyError:
                title = data['target']['title']
                url = data['target']['url'].replace('api.zhihu.com/questions', 'zhihu.com/question')
            hot_lists.append(f'[{title}]({url})')
        return hot_lists

zhihu = Zhihu()
# print(zhihu.hot_data)
print(zhihu.recommend_data)