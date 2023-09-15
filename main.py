import wget  # 下载库
import os # 操控文件
import tempfile # 临时文件
import json # 解析JSON
import requests
import jsonpath

os.system("cls")
print("欢迎使用SkyBlock查询工具 当前工具版本V 0.0.2")
IGN = str(input("请输入正确的玩家ID: "))                       ##获取玩家数据部分
mojangurl = "https://api.mojang.com/users/profiles/minecraft/"
mojangapi = (mojangurl+IGN)
uuid_data_json = requests.get(mojangapi)
uuid_json = uuid_data_json.text
uuid_data = json.loads(uuid_json)
if "id" in uuid_data:
    get_uuid = uuid_data["id"]
    uuid_list = list(get_uuid)
    uuid_list.insert(8,"-")
    uuid_list.insert(13,"-")
    uuid_list.insert(18,"-")
    uuid_list.insert(23,"-")
    uuid = ''.join(uuid_list)
    name = uuid_data["name"]
else:
    print("无法获取对应ID的UUID 请检查输入")
    print()
    input("输入任意键退出")
    exit()

apiurl = "https://sky.shiiyu.moe/api/v2/profile/"+IGN
player_data_json = requests.get(apiurl)
player_data = json.loads(player_data_json.text)

# player_data_json = open("TEST.json","rb")
# player_data = json.load(player_data_json)

playerprofilesid_list = jsonpath.jsonpath(player_data,'$..profile_id')
print(playerprofilesid_list)
pidlist = len(playerprofilesid_list)
msg = ("请输入要查询存档的存档ID编号(0-"+str(pidlist)+") 查询当前正在玩存档请直接输入0 :")
pid = input(msg)

profiles_data = player_data["profiles"][playerprofilesid_list[int(pid)]]  #进入存档JSON
data_profiles_data = profiles_data["data"]
data_profiles_data = profiles_data["data"]      # 进入DATA
levels_profiles_data = data_profiles_data["levels"]    #进入等级



####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
# 玩家数据变量区 qwq 这玩意要存的变量有点多 一次性处理了在打印
cute_name = profiles_data["cute_name"] # 存档名称
trophy_status = ()
dungeons_status_code = ()
master_dungeons_status_code = ()


if profiles_data["game_mode"] == "normal":
    gamemod = "普通"
elif profiles_data["game_mode"] == "ironman":
    gamemod = "铁人"
elif profiles_data["game_mode"] == "bingo":
    gamemod = "Bingo"         ##游戏模式

fairy_souls_collected = data_profiles_data["fairy_souls"]["collected"] #仙女之魂获得数


coop = []
coop.append(jsonpath.jsonpath(data_profiles_data["members"], '$..display_name'))   
coop_str = ''.join(str(i) for i in coop) 
if coop_str == "False" :
    coop_str = "无Coop"           # Coop

taming = levels_profiles_data["taming"]["level"]     #驯养等级
farming = levels_profiles_data["farming"]["level"]    #农业等级
combat = levels_profiles_data["combat"]["level"]    #战斗等级
mining = levels_profiles_data["mining"]["level"]     #挖矿等级
foraging = levels_profiles_data["foraging"]["level"]   #伐木等级 
fishing = levels_profiles_data["fishing"]["level"]     #钓鱼等级
enchanting = levels_profiles_data["enchanting"]["level"]   #附魔等级
alchemy = levels_profiles_data["alchemy"]["level"]         #酿药等级
carpentry = levels_profiles_data["carpentry"]["level"]      #制造等级
if "runecrafting" in levels_profiles_data :
    runecrafting = levels_profiles_data["runecrafting"]["level"]   #符文等级
else:
    runecrafting = "无法查询"
if "social" in levels_profiles_data :
    social = levels_profiles_data["social"]["level"]      # 社交等级
else:
    social = "无法查询"
AVG = data_profiles_data["average_level"]         #技能AVG

first_join = data_profiles_data["first_join"]["text"]     #第一次加入时间

skyblock_level = data_profiles_data["skyblock_level"]["level"]    #SkyBlock Level


if "bank" in data_profiles_data :
    bank = data_profiles_data["bank"]   #银行
    bank = format(bank, ',')
else :
    bank = "无法获取银行数据"

if "purse" in data_profiles_data :
    purse = data_profiles_data["purse"]      #钱包
    purse = format(purse, ',')
else:
    purse = "无法获取钱包数据"

if "trophy_fish" in data_profiles_data :
    trophy_fish_profiles_data = data_profiles_data["trophy_fish"]   #奖杯鱼
    fish_trophy_fish_profiles_data = trophy_fish_profiles_data["fish"]    #奖杯鱼小类
    trophy_fish_total = trophy_fish_profiles_data["total_caught"]      #总计奖杯鱼
    trophy_fish_name = trophy_fish_profiles_data["stage"]["name"]    #当前称号
    if "stage" in trophy_fish_profiles_data :
        if "type" in trophy_fish_profiles_data["stage"] :
            trophy_fish_type = trophy_fish_profiles_data["stage"]["type"]    #当前等级
        else :
            trophy_fish_type = "无法获取"
    else:
        trophy_fish_type = "无法获取"
    trophy_fish_progress = trophy_fish_profiles_data["stage"]["progress"]    #当前进度
    trophy_total = jsonpath.jsonpath(fish_trophy_fish_profiles_data, '$..total')
    trophy_bronze = jsonpath.jsonpath(fish_trophy_fish_profiles_data, '$..bronze')
    trophy_silver = jsonpath.jsonpath(fish_trophy_fish_profiles_data, '$..silver')
    trophy_gold = jsonpath.jsonpath(fish_trophy_fish_profiles_data, '$..gold')
    trophy_diamond = jsonpath.jsonpath(fish_trophy_fish_profiles_data, '$..diamond')
    trophy_highestType = jsonpath.jsonpath(fish_trophy_fish_profiles_data, '$..highestType')
    trophy_name = jsonpath.jsonpath(fish_trophy_fish_profiles_data, '$..name')
    trophy_list = 0                                                                                          ##各种奖杯鱼
else :
    trophy_status = "false"
if "dungeons" in data_profiles_data :
    dungeons_data = data_profiles_data["dungeons"]                                        #地牢部分
    cata = dungeons_data["catacombs"]["level"]["level"]
    floors_dungeons = dungeons_data["catacombs"]["floors"]
    if "0" in floors_dungeons :
       entrance_total =  floors_dungeons["0"]["stats"]["milestone_completions"]             
    else: 
       entrance_total = "无法获取"                                                     #E0
    if "1" in floors_dungeons :
       F1_total =  floors_dungeons["1"]["stats"]["milestone_completions"]             
    else: 
       F1_total = "无法获取"                                                     #F1
    if "2" in floors_dungeons :
       F2_total =  floors_dungeons["2"]["stats"]["milestone_completions"]             
    else: 
       F2_total = "无法获取"                                                     #F2
    if "3" in floors_dungeons :
       F3_total =  floors_dungeons["3"]["stats"]["milestone_completions"]             
    else: 
       F3_total = "无法获取"                                                     #F3
    if "4" in floors_dungeons :
       F4_total =  floors_dungeons["4"]["stats"]["milestone_completions"]             
    else: 
       F4_total = "无法获取"                                                     #F4
    if "5" in floors_dungeons :
       F5_total =  floors_dungeons["5"]["stats"]["milestone_completions"]             
    else: 
       F5_total = "无法获取"                                                     #F5
    if "6" in floors_dungeons :
       F6_total =  floors_dungeons["6"]["stats"]["milestone_completions"]             
    else: 
       F6_total = "无法获取"                                                     #F6
    if "7" in floors_dungeons :
       F7_total =  floors_dungeons["7"]["stats"]["milestone_completions"]             
    else: 
       F7_total = "无法获取"                                                     #F7

    if "master_catacombs" in dungeons_data :             #大师地牢
        master_dungeons_data = dungeons_data["master_catacombs"]
        floors_dungeons_master = master_dungeons_data["floors"]
        if "1" in floors_dungeons_master :
          M1_total = floors_dungeons_master["1"]["stats"]["milestone_completions"]          #M1
        else:
          M1_total = "无法获取"
        if "2" in floors_dungeons_master :
          M2_total = floors_dungeons_master["2"]["stats"]["milestone_completions"]     #M2
        else:
          M2_total = "无法获取"
        if "3" in floors_dungeons_master :                                #M3
          M3_total = floors_dungeons_master["3"]["stats"]["milestone_completions"]
        else:
          M3_total = "无法获取"
        if "4" in floors_dungeons_master :
          M4_total = floors_dungeons_master["4"]["stats"]["milestone_completions"]                  #M4
        else:
          M4_total = "无法获取"
        if "5" in floors_dungeons_master :                                              #M5
          M5_total = floors_dungeons_master["5"]["stats"]["milestone_completions"] 
        else:
          M5_total = "无法获取"
        if "6" in floors_dungeons_master :                                  #M6
          M6_total = floors_dungeons_master["6"]["stats"]["milestone_completions"]
        else:
          M6_total = "无法获取"
        if "7" in floors_dungeons_master :                                      #M7
          M7_total = floors_dungeons_master["7"]["stats"]["milestone_completions"]
        else:
          M7_total = "无法获取"








    else:
        master_dungeons_status_code = "false"
else:
    dungeons_status_code = "false"




####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

os.system("cls")
print("玩家名称:",name)
print("存档名称:",cute_name,"游戏模式:",gamemod,"第一次加入:",first_join)
print("合作玩家(Coop): ",coop_str,"")
print("-------------------------------------------------")
print("银行内Coins:",bank)
print("钱包内Coins:",purse)
print("-------------------------------------------------")
print("SkyBlock Level:",skyblock_level) 
print("战斗等级:",combat,"挖矿等级:",mining,"伐木等级",foraging)
print("钓鱼等级:",fishing,"附魔等级:",enchanting,"酿药等级:",alchemy)
print("社交等级:",social,"符文等级:",runecrafting,"农业等级:",farming)
print("制作等级:",carpentry,"驯养等级:",taming)
print("技能AVG:",AVG)
print("-------------------------------------------------")
if dungeons_status_code == "false":
    print("无法查询地牢信息")
else:
    print("地牢等级:",cata)
    print("地牢入口总计完成:",entrance_total)
    print("F1总计完成:",F1_total,"| F2总计完成:",F2_total,"| F3总计完成:",F3_total)
    print("F4总计完成:",F4_total,"| F5总计完成:",F5_total,"| F6总计完成:",F6_total)
    print("F7总计完成:",F7_total)
if master_dungeons_status_code == "false":
    print("无法查询大师模式地牢信息")
else:
    print("-------------------------------------------------")
    print("M1总计完成:",M1_total,"| M2总计完成:",M2_total,"| M3总计完成:",M3_total)
    print("M4总计完成:",M4_total,"| M5总计完成:",M5_total,"| M6总计完成:",M6_total)
    print("M7总计完成:",M7_total)
print("-------------------------------------------------")
if trophy_status == "false":
    print("查询玩家不存在奖杯鱼数据")
else:
    print("当前奖杯鱼称号:",trophy_fish_name)
    print("当前等级:",trophy_fish_type,"当前进度:",trophy_fish_progress)
    print("总计钓上的奖杯鱼:",trophy_fish_total,"")
    print("奖杯鱼统计：")
    while trophy_list<len(trophy_gold):
        print(trophy_name[trophy_list],"|","总计:",trophy_total[trophy_list],"铜:",trophy_bronze[trophy_list],"银:",trophy_silver[trophy_list],"金:",trophy_gold[trophy_list],"钻石:",trophy_diamond[trophy_list],"最高等级:",trophy_highestType[trophy_list])
        trophy_list=trophy_list+1
print("-------------------------------------------------")
print("已收集仙女之魂:",fairy_souls_collected)




















print()
input("输入任意键退出")