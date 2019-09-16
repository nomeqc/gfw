#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests, base64


def gen_base64(s):
    b64_str = str(base64.b64encode(bytes(s, 'utf-8')), 'utf-8')
    # print(b64_str)
    ret_str = ""
    index = 0
    s_len = len(b64_str)
    # print("len:"+ str(s_len))
    
    while index < s_len:
        temp_s = b64_str[index: index + min(64, s_len - index)]
        # print("temp str:" + temp_s)
        ret_str = ret_str + temp_s + "\n"
        index = index + 64
    return ret_str


if __name__ == "__main__":
    try:
        with open("user_rule.txt", "r", encoding="utf-8") as f:
            user_rule = f.read()
            print("user_rule:\n" + user_rule)
    except FileNotFoundError:
        print("user_rule.txt不能存在")
        exit(0)

    print("正在下载gfwlist.txt ...")
    try:
        response = requests.get("https://pagure.io/gfwlist/raw/master/f/gfwlist.txt")
        gfwlist = base64.b64decode(response.text)
    except Exception:
        print("请求出错了")
    
    with open("list.txt", "w", encoding="utf-8") as f:
        result = '!################Fallrainy Start##################\n{}!################Fallrainy End##################\n\n{}'.format(user_rule, str(gfwlist, 'utf-8'))
        # print("result:" + result)
        content = gen_base64(result)
        f.write(content)
    print("list.txt已经生成成功。")


    
    


