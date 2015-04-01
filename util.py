#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import datetime
import random
import MeCab

# string
def has_any_word(text, words):
    for word in words:
        if word in text:
            return True
    return False

def has_every_word(text, words):
    for word in words:
        if word not in text:
            return False
    return True


# PHP互換
def php_rand(lo=None, hi=None):
    if lo and hi:
        return random.randint(lo, hi)
    else:
        return random.randint(0, 32767)


def php_idate(fmt):
    return int(time.strftime('%' + fmt))


# unix time <-> datetime
def unixtime_to_datetime(ut):
    datetime.datetime.fromtimespamp(ut)


def datetime_to_unixtime(dt):
    return int(time.mktime(dt.timetuple()))


# MeCab
mecab_tagger = MeCab.Tagger("-Ochasen")

def split_into_morphemes(text_uc):
    text_utf8 = text_uc.encode('utf-8')
    bag = []
    node = mecab_tagger.parseToNode(text_utf8)
    while node:
        if node.posid != 0:
            ar = node.feature.split(',')

            surface = node.surface.decode('utf-8')
            pos = ar[0].decode('utf-8')
            orig_form = ar[6].decode('utf-8')
            bag.append( (surface, pos, orig_form) )
        node = node.next
    return bag


# birthday
def age_str(birthday, on_the_day_str):
    ymd = int(time.strftime('%Y%m%d'))
    age = int((ymd - birthday) / 10000)

    md = ymd % 10000
    birth_md = birthday % 10000
    month_ago = birth_md - 200
    if month_ago < 0:
        month_ago += 1200

    if md == birth_md:
        age_str = on_the_day_str
    elif month_ago <= md < birth_md:
        age_str = u'もうすぐ%d歳' % (age + 1)
    else:
        age_str = u'%d歳' % age

    return age_str

#
# 確率とか分布とか
#
def p(true_rate):
    return random.randint(1, 100) <= true_rate

# なんちゃって正規分布
def my_rand(lo, hi):
    mu = (lo + hi + 1) / 2
    d = hi - lo

    x = 0
    for i in range(6):
        x += random.randint(lo - d, hi + d)
    x = int((x + 3)/6)

    if x < lo:
        x = lo
    elif x > hi:
        x = hi

    return x


def my_choose(candidates, use_gaussian=True):
    # 要素の入った配列から、なんちゃって分布に従ってランダムに１つ選んで返す
    def _choose(candidates, randfn):
        return candidates[ randfn(0, len(candidates)-1) ]

    if use_gaussian:
        return _choose(candidates, my_rand)
    else:
        return _choose(candidates, random.randint)
