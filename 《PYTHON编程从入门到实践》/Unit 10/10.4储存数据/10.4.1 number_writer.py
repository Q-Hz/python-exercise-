# 存入数据 json
import json
number = [1,2,3,4]
file_name = 'number.json'
with open(file_name,'w') as f_obj:
    json.dump(number,f_obj)