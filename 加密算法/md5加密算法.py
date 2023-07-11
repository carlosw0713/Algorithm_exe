#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: md5加密算法.py
@time: 2023/6/12  11:11
"""

import hashlib

def md5_encode(text):
    '''MD5 加密函数'''
    hash = hashlib.md5(text.encode())
    return hash.hexdigest()

def md5_decode(encoded_text):
    '''MD5 解密函数'''
    print('无法解密 MD5 加密结果。')

# 调用示例
text = 'hello, world!'
encoded_text = md5_encode(text)
print('原文：', text)
print('加密结果：', encoded_text)
print('解密结果：',md5_encode(text))
print('是否一致：', encoded_text == md5_encode(text))
md5_decode(encoded_text)
