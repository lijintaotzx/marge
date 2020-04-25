# coding=utf-8
import random
import re


def generate_code():
    """
    随机生成4位数验证码
    """
    seeds = "1234567890"
    random_num = []
    for i in range(4):
        random_num.append(random.choice(seeds))
    return "".join(random_num)


def match_pn(pn):
    """
    正则验证手机号码
    :param pn: 手机号码
    :return: True or False
    """
    return True if re.match(r"^1[3578]\d{9}$", pn) else False
