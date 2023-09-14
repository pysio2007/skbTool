# 测试如何处理得到一个正确的UUID
import json
import requests
IGN = str(input("请输入正确ID: "))
mojangurl = "https://api.mojang.com/users/profiles/minecraft/"
mojangapi = (mojangurl+IGN)
uuid_data_json = requests.get(mojangapi)
uuid_json = uuid_data_json.text
uuid_data = json.loads(uuid_json)
get_uuid = uuid_data["id"]
uuid_list = list(get_uuid)
uuid_list.insert(8,"-")
uuid_list.insert(13,"-")
uuid_list.insert(18,"-")
uuid_list.insert(23,"-")
uuid = ''.join(uuid_list)
print(uuid)