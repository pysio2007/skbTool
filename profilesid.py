# 测试如何获取存档ID
import wget  # 下载库
import os # 操控文件
import tempfile # 临时文件
import json # 解析JSON
import jsonpath
import requests

IGN = "DJZS"
# IGN = str(input("请输入正确的玩家ID: "))   
apiurl = "https://sky.shiiyu.moe/api/v2/profile/"+IGN
player_data_json = requests.get(apiurl)
player_data = json.loads(player_data_json.text)
playerprofilesid_list = jsonpath.jsonpath(player_data,'$..profile_id')
print(playerprofilesid_list)
pidlist = len(playerprofilesid_list)
msg = ("请输入要查询存档的存档ID编号(0-"+str(pidlist)+") 查询当前正在玩存档请直接输入0 :")
pid = input(msg)

profiles_data = player_data["profiles"][playerprofilesid_list[pid]]  #进入存档JSON
data_profiles_data = profiles_data["data"]