# coding: utf-8
# Your code here!
""" jsonの形式はあくまでString型としか認識できないため、
    dictonary型にエンコードする
    エンコード　　　　　：json.loads
    デコード（toString）：json.dumps
"""

import json

'''どちらで定義してもDictionary型'''
dict = {"name": "tarou", "age": 23, "gender": "man"}
json_str = {
    "name":"hitomi",
    "age": 22,
    "gender": "woman"
}

print(type(dict))
print(type(json_str))
# <class 'dict'>
# <class 'dict'>

''' インデントありで出力__'''
enc = json.dumps(dict, indent=2)

print(enc)
print(type(enc))
# {
#   "name": "tarou",
#   "age": 23,
#   "gender": "man"
# }
# <class 'str'>
