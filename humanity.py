#!/usr/bin/python
# -*- coding: utf-8 -*-

from util import has_any_word, has_every_word, php_rand, my_choose
import re

def generate_responses(status_text, morphemes, surfaces, orig_forms):
    responses = []

    # bot
    bot_words = (u'bot', u'にせもの',
                 u'ボ　　ッ　　ト', u'ボ　ッ　ト', u'ボ  ッ  ト',
                 u'ボ ッ ト', u'ボット')
    if has_any_word(status_text, bot_words):
        # msg = u'ほんものやで http://t.co/3e3ZCox'
        # msg = u'botですがなにか'
        msg = u'いつからbotだと錯覚していた？'
        responses.append( (msg, 85) )

    # tejimaya
    if u'#kr_cvs' in status_text:
        if u'梅' in status_text:
            msg = u'ブドウ糖 #kr_cvs'
            # msg = 'しおミルキー #kr_cvs'
        else:
            msg = u'梅 #kr_cvs'
        responses.append( (msg, 80, False) )
    if u'手うが' in status_text:
        msg = u'NT'
        responses.append( (msg, 95) )
    if u' FF ' in status_text:
        msg = u'255'
        responses.append( (msg, 95) )

    # co３k
    if u'co３k' in status_text:
        msg = u'co３３k'
        responses.append( (msg, 95) )

    # えび
    if has_any_word(status_text, (u'CD-ROM', u'YU-NO')):
        msg = u'というわけで先にデバッガで追いかけてディスクチェックっぽいところを２箇所ほど無効化しましたやで'
        responses.append( (msg, 20) )

    if has_any_word(orig_forms, (u'蟹', u'かに')):
        msg = u'かにー'
        responses.append( (msg, 15) )

    # てりやき
    if u'ごはん、何食べた？' in status_text and u'@teriyaki' not in status_text:
        choices = (
            u'ブドウ糖',
            u'梅', u'梅', u'梅',
            u'磯辺焼',
            u'電球',
            u'寿司',
            u'ハッピーターン'
        )
        msg = my_choose(choices, False)
        responses.append( (msg, 99) )


#    if u'雪' in status_text and u'@teriyaki' in status_text:
#        msg = u'nicejogging'
#        responses.append( (msg, 80) )

    # nicebeer (ビア充爆発しろ)
    beer_related_words = (
        u'ビール', u'beer', u'ビアー', u'ルービー',
        u'ビアガーデン', u'オクトーバーフェスト'
        u'サッポロ', u'アサヒ', u'キリン', u'エビス',
        u'ジョギング', u'km run',
        u'ぷしゅ',
        # u'飲む',
        # '浴衣', '花火', '祭り',
    )
    if has_any_word(status_text, beer_related_words):
        responses.append( (u'nicebeer', 50) )
    if has_any_word(status_text, (u'ホッピー', u'hoppy')):
        responses.append( (u'happyhoppy', 50) )

    # nicecurry
    curry_related_words = (
        u'カレー', u'カリー', u'curry', u'Curry',
    )
    if has_any_word(status_text, curry_related_words):
        responses.append( (u'nicecurry', 50) )

    # ｶﾞﾀｯ
    gatatt_words = (
        u'ログイン', # u'ﾛｸﾞｲﾝ',
        # u'海',
        u'狩り',
        u'花澤', # '花澤香菜',
        u'海未',
        # u'いちご',
        u'穂乃果',
        u'にこ',
        u'豆ひじき',
        u'枝豆',
    )
    if has_any_word(orig_forms, gatatt_words):
        responses.append( (u'ｶﾞﾀｯ', 80) )

    # ただいま→おかえり
    okaerip = False
    if has_any_word(status_text, (u'ただいま', u'帰宅', u'バネリー', u'ﾊﾞﾈﾘｰ')):
        okaerip = True
    elif u'きたく' in status_text and (u'たく', u'助動詞', u'たい') not in morphemes:
        okaerip = True
    if okaerip:
        responses.append( (u'おかえりやで', 80) )

    # 在処
    arika_dic = (
        ((u'鍵',), u'鞄の中'),
        ((u'財布', u'さいふ', u'サイフ'), u'家'),
        ((u'鞄', u'かばん'), u'会社'),
        ((u'携帯',), u'会社'),
    )
    for objs, where in arika_dic:
        for obj in objs:
            if obj in status_text:
                msg = u'%sなら%sやで' % (obj, where)
                responses.append( (msg, 95) )
                break

    # 梅
    ume_dic = (
        ((u'風邪',), u'風邪をひいたら', u'梅'),
        ((u'夜道',), u'暗い夜道には', u'梅'),
        ((u'緊急事態',), u'緊急事態には', u'梅'),
        ((u'文系',), u'文系には', u'梅'),
        ((u'筋肉痛',), u'筋肉痛には', u'梅'),
        ((u'日焼',), u'日焼けには', u'梅'),
        ((u'腹痛', u'ぽんぺ', u'ponponpain',), u'腹痛には', u'梅'),
        ((u'磯辺焼', u'磯部焼',), u'磯辺焼には', u'梅'),
        ((u'鼻血',), u'鼻血には', u'苺'),
        ((u'気圧の変化',), u'気圧の変化には', u'梅'),
        ((u'疲れる', u'疲れた',), u'疲れたら', u'ブドウ糖'),
        ((u'泣', u'涙',), u'泣きたい時には', u'梅'),
        ((u'つらい', u'つらぽよ',), u'つらい時には', u'梅'),
        ((u'嬉', u'うれし',), u'嬉しい時には', u'梅'),
    )
    for words, when, recipe in ume_dic:
        for word in words:
            if word in status_text:
                msg = u'%s%sやで' % (when, recipe)
                responses.append( (msg, 88, False) )
    if (u'頭' in status_text or u'あたま' in status_text) and (u'痛' in status_text or u'いた' in status_text):
        msg = u'頭痛には梅やで'
        responses.append( (msg, 88, False) )

    # 北海道ネタ
    if has_any_word(status_text, (u'ユキムシ', u'ゆきむし', u'雪虫')):
        msg = u'秋に自転車乗ってると口の中はいるよねー'
        responses.append( (msg, 99) )
    if u'七夕' in status_text:
        msg = u'お菓子もロウソクももらえない七夕は意味ないで'
        responses.append( (msg, 80) )
    if u'うまいっしょ' in status_text:
        msg = u'うまいっしょは2007年に販売終了したで'
        responses.append( (msg, 80) )
    if has_any_word(status_text, (u'やきそば弁当', u'やき弁', u'焼きそば弁当')):
        msg = u'やきそば弁当の弁当じゃない感は異常やで'
        responses.append( (msg, 80) )
    if u'コンビニ' in status_text:
        msg = u'コンビニといえばセイコマやで'
        responses.append( (msg, 33) )

    # それは・・・やで
    def in_fact_message(actual_obj):
        return u'それは %s やで' % actual_obj

    if has_any_word(status_text, (u'コーヒー', u'珈琲')):
        msg = in_fact_message( my_choose((u'みろ', u'めんつゆ',), False) )
        responses.append( (msg, 66) )
    if u'アイス' in orig_forms:
        msg = in_fact_message(u'せっけん')
        responses.append( (msg, 66) )

    if has_any_word(orig_forms, (u'水', u'ウォーター')):
        msg = in_fact_message(u'いろはすみかん')
        responses.append( (msg, 66) )
    elif u'いろはす' in status_text and not has_any_word(status_text, (u'オレンジ', u'みかん')):
        msg = in_fact_message(u'いろはすみかん')
        responses.append( (msg, 66) )

    # RFC
    obsoleted_rfcs = (
        15, 114, 172, 196, 265, 354, 675, 760, 765,
        772, 783, 790, 821, 822, 850,
        918, 966, 977, 988, 1054, 1067, 1071, 1081,
        1094, 1098, 1112, 1131, 1225, 1247, 1294,
        1388, 1460, 1487, 1490, 1508, 1509,
        1531, 1541, 1583, 1631, 1723, 1725, 1774,
        1813, 1883, 1889, 1991, 2058, 2059, 2060,
        2078, 2109, 2117, 2138, 2139, 2168, 2178,
        2222, 2236, 2373, 2440, 2445, 2616, 2915,
        2960, 2965, 3010, 3174, 3513
    )
    mo = re.search('[Rr][Ff][Cc] *([0-9]+)', status_text)
    if mo:
        rfc_num = int(mo.group(1))
        if rfc_num in obsoleted_rfcs:
            msg = u'そのRFC (%d)、Obsoleted だよ。知らないのかい？' % rfc_num
            responses.append( (msg, 100) )

    # その他
    if u'海' in orig_forms:
        msg = u'ｶﾞﾀｯ'
        responses.append( (msg, 99) )
    if u'今日どこ行く' in status_text:
        msg = u'海'
        responses.append( (msg, 99) )

    if u'傘' in status_text and u'傘とか甘え' not in status_text:
        msg = u'傘とか甘え'
        responses.append( (msg, 50) )

    if u'sqlite3' in status_text:
        msg = u'sqlite33やで'
        responses.append( (msg, 98) )

    if u'ぬるぽ' in status_text:
        msg = u'ｶﾞｯ はセルフサービスやで'
        responses.append( (msg, 85) )

    if u'人生オワタ' in status_text:
        msg = u'＼(^o^)／'
        responses.append( (msg, 85) )

    if u'死' in status_text:
        msg = u'しんでしまうとはなさけないで'
        responses.append( (msg, 85) )

    if has_any_word(status_text, (u'ヒャッハー', u'ﾋｬｯﾊｰ')):
        msg = u'ﾋｬｯﾊｰ'
        responses.append( (msg, 80) )

    if has_any_word(status_text, (u'うざ', u'うぜ')):
        msg = u'///'
        responses.append( (msg, 80) )

    if u'」はい' in status_text:
        msg = u'はい'
        responses.append( (msg, 99) )

    if u'うひ' in status_text:
        msg = u'う' + (u'ひ' * util.php_rand(2, 4))
        responses.append( (msg, 50) )


    #if u'30分' in status_text:
    #    msg = u'金曜日以外は390円／30分'
    #    responses.append( (msg, 85, False) )

    painful_words = (
        u'痛',
        u'寝違',
        u'吊り天井',
        u'かみきる', u'噛み切',
        u'イテ'
    )
    if has_any_word(status_text, painful_words):
        msg = u'＞＜'
        responses.append( (msg, 85) )

    return responses
