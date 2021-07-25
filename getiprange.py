#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : RedTeamWing
# @CreateTime: 2021/7/25 下午11:49
# @FileName: getiprange.py
# @Blog：https://redteamwing.com
# !/usr/bin/python
# -*- coding:utf-8 -*-
import re


def patchip():
    ipList = set()
    ipdata = open('./ip.txt', 'r').readlines()
    for ip in ipdata:
        ipList.add(ip)

    ipdict = []
    for ip in ipList:
        ip = re.findall(r'\d+?\.\d+?\.\d+?\.', ip)[0]
        # print(ip)
        ipdict.append(ip + "1")
        # ipset.add(re.findall(r'\d+?\.\d+?\.\d+?\.', ip)[0] + '0/24')
    sorted_nums = ipdict
    num_dict = {}
    for num in sorted_nums:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    # print(num_dict)
    num_dict = sorted(num_dict.items(), key=lambda item: item[1], reverse=True)
    print(num_dict)
    return num_dict


def save(data):
    f = open('./result.txt', 'w')
    for i in data:
        print(i[0], i[1])
        f.write(str(i[0]) + "/24" + ' == {}\n'.format(i[1]))
    f.close()


if __name__ == '__main__':
    ipdata = patchip()
    save(ipdata)
