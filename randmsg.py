#!/usr/bin/python
# -*- coding: utf-8 -*-
from langgen import *
from util import php_idate, php_rand


def msggen(pattern_id):
    h = php_idate('H')
    if not pattern_id:
        pattern_id = php_rand(1, 300)

    print pattern_id
    ## freq = 20/60 (cronjob per hour) * 1/100 (rand) * 7 = 7/300 (/hour) = 300/7 [= 40h+毎]
    ## freq = 60/60 (cronjob per hour) * 1/200 (rand) * 15 = 4.5/60 (/hour) = 300/7 [= 40h+毎]

    msg = None

    if pattern_id == 1:
        msg = tetete_gen.gen()
    elif pattern_id == 2:
        msg = tetete_ja_gen.gen()
    elif pattern_id in (3,4,5):
        msg = ebiebi_gen.gen()
    elif pattern_id == 6:
        msg = 'タイトルに「えび」'
    elif pattern_id == 7:
        msg = 'ｼｬｷｰﾝ'
    elif pattern_id == 8:
        msg = chomochomo_gen.gen()
#    elif pattern_id == 8:
#        if php_idate('d') == 24:
#            msg = '梅リー・クリスマス #kr_cvs'
    elif pattern_id in (9, 10):
        msg = poke_gen.gen(use_gaussian=False)
    elif pattern_id == 12:
        msg = 'おしりかじり虫〜♪'
    elif pattern_id == 13:
        msg = 'じつはボットやで♪'
    elif pattern_id == 14:
        if php_idate('w') == 0 or php_idate('w') >= 5:
            msg = 'バネリー'
    elif pattern_id == 15:
        msg = '(」・ω・)」うー！ (／・ω・)／にゃー！'
#    elif pattern_id == 14:
#        msg = '＼ポポポポ〜ン!／'
#    elif pattern_id == 15:
#        if h >= 15:
#            msg = 'ドライジンジャー #kr_cvs'
#        else fall thru
    elif pattern_id == 16:
        if h >= 16:
            msg = '梅 #kr_cvs'
    elif pattern_id == 17:
        if h >= 17:
            msg = 'うちわ #kr_cvs'
    elif pattern_id == 18:
        if h >= 19:
            msg = '100m×%d本' % php_rand(3, 15)
    elif pattern_id == 19:
        if 11 <= h <= 21:
            msg = generate_marukame()
    elif pattern_id == 20:
        if h <= 3 or 22 <= h:
            msg = '@teriyaki 寿司 #kr_cvs'
    else:
        msg = None

    return msg
