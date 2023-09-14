# 测试如何获取存档ID
import wget  # 下载库
import os # 操控文件
import tempfile # 临时文件
import json # 解析JSON
import jsonpath
import requests


IGN = str(input("请输入正确的玩家ID: "))   
apiurl = "https://sky.shiiyu.moe/api/v2/profile/"+IGN
player_data_json = requests.get(apiurl)
player_data = json.loads(player_data_json.text)
playerprofilesid = []
playerprofilesid.append(jsonpath.jsonpath(player_data,'$..profile_id')[0])
print(playerprofilesid)
# profiles_data = player_data["profiles"][playerprofilesid]  #进入存档JSON
# data_profiles_data = profiles_data["data"]