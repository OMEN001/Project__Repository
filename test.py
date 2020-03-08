#_*_conding:utf-8_*_
#@Time    :2020/3/818:20
#@Author  :xiaodong.wu
#@Email   :2586089125@qq.com

def func():
    with open("data.txt","r",encoding="utf8") as f:
        data = f.readlines()
        print(data)
    case = []
    for a in data:
        b = a.split(",")
        dict = {}
        for c in b:
            d = c.split(":")
            key = d[0]
            value = d[1].replace("\n","")
            dict[key] = value
        case.append(dict)
    return case
res = func()
print(res)