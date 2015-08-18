#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from db.thru_word import ThruWord

import util
import anime
import humanity
import zeitgeist
from langgen import *

my_user_id = 198824125

ignore_ids = frozenset((
    my_user_id,
    199688815, # @randomodai
    134681353, # @kiri_tori
    423309927, # @co33k_bot
    238613592, # @naoya_rin
    389367531, # @naoya_rin_auto
    # 4141001, # @teriyaki 一時
    # 259223861, # @teriyaki_past 一時
    1259908302, # @teriyaki_digest
))

# ここに含まれるscreen name以外は@を外す
friend_screennames = (
    'co33k',
    'teriyaki', 'teriyaki_past', 'teteteBGM',
    'lipovitan_rin', 'hanasaku_rin', 'balibali', 'matsukaze_rin', 'matsutake_rin', 'natsukaze_rin', 'nowplaying_rin', 'mamehijiki_rin', 'mayihelp_rin', 'karikarip_rin', 'teuga_rin', 'endless_rin',
    'kiwpon', 'tti_pon', 'nowplaying_pon',
    'nise_nabe',
    'poison_yade',
    # 'garin54',
    'picomu',
    'co3k', 'co3k_past', 'co3k_now', 'kanihara',
    'warau_oni',
    # 'kashiwasan',
    # 'uzura8',
    # 'fumicos',
    # 'chomochomo',
    # 'ooharabucyou',
    # 'naoya_rin',
    'kim_upsilon',
    'neko_ta',
    'takamimelon',
    'meshilogger',
    'uraburab',
)

def escape_unknown_persons(text):
    escaped = []
    curr = 0
    for match in re.finditer(r'(@)([_0-9A-Za-z]+)', text):
        if match.group(2) not in friend_screennames:
            span = match.span(1)
            assert text[span[0]:span[1]] == '@'
            escaped.append(text[curr:span[0]])
            curr = span[1]
    escaped.append(text[curr:])
    return u'$'.join(escaped)

teri_age_str = util.age_str(19790608, u'誕生日男子')
if util.p(50):
    teri_age_str = u'人間で言うとおよそ' + teri_age_str

nicknames_teri = (
    u'てりやき',
    u'テリー',
    u'ててて',
    u'うひひ',
    u'弁当男子',
    u'大人コミック',
    teri_age_str, teri_age_str, teri_age_str,
    u'терияки',
    u'越後製菓',
    u'ブラジル',
    u'ポンコツおじさん',
    u'おおひら村',
    u'「カレーはフォークで」派',
    u'カリスマブロガー',
    u'飲んだくれ',
    u'後で詰む人',
    u'お〜いお茶俳人',
    u'料理－愛情＝自炊',
    u'Ingressおじさん',
    u'ビア充',
    u'どこまでも自転車で行く',
    u'エリクサー余らす系男子',
    #u'サラリーマンのコスプレ',
    u'本体は自転車で、上に乗ってる飾りの男性',
    u'本体はスーツで、中に入ってる飾りの男性',
    u'青椒肉絲食べたいマン',
    u'夜雨予報の前日は自転車をオフィスに置いて帰るマン',
    u'さくら水産とかやよい軒で満腹なのにおかわりよそいに行っちゃうお子様',
    u'今でもいちばん右が「昭和」だと思っている30代',
    u'ヤキトリホームラン',
    u'暑い日にはサウナに入る系男子',
    u'休肝日のつもりなのにジョギングしちゃうマン',
)
nicknames_teri_digest = (
    u'てりやき',
    u'ダイジェスト版',
)
nicknames_rin = (
    u'手うが',
    u'かりかり',
    u'鈴',
    u'２組',
    u'酢豚',
    u'松茸',
    u'栄養ドリンク',
    u'コンビニおにぎり',
    u'今はなき豆ひじき',
    u'にわかスクフェス勢',
    u'西山陰県',
    u'だって終わらない',
    u'方眼紙',
)
nicknames_ebi = (
    u'えび',
    u'うめ',
    u'こみけ',
    u'ワンランク上の大人',
    u'磯辺焼',
    u'磯辺焼bot',
    u'脚本家さん',
    u'えびお★★★★',
    u'シャレオツ区民',
    u'I ♥︎ SHIBUYA',
    u'歌広場昂輔',
    u'元生徒会長',
    u'kokomade',
)
nicknames_oni = (
    u'鬼',
    u'笑う鬼',
)

userinfos = {
    7812092   : ( 15,  True, nicknames_ebi ), # @co3k
    285544941 : (  3, False, nicknames_ebi ), # @co3k_now
    198824125 : ( 99,  True, (u'こみみけ',) ), # @co33k
    284623708 : (  0,  True, nicknames_teri ), #/ @teteteBGM
    283105568 : (  3,  True, nicknames_rin ), # @nowplaying_rin
    14432798  : (  5,  True, (u'ばりばり', u'バカ犬',) ), # @balibali
    278079610 : ( 25,  True, nicknames_rin ), # @momoyama_taro == @hanasaku_rin
    4141001   : ( 30,  True, nicknames_teri ), # @teriyaki
    1259908302: (  0,  True, nicknames_teri_digest ), # @teriyaki_digest
    1562055122: (  5, False, (u'エリチカ',) ),
    212823737 : (  5,  True, nicknames_oni ), # @warau_oni

    46932814  : ( 10, False, (u'にせなべ', u'偽なべ', u'にせもの',) ), # @nise_nabe
    #288055722 : ( 20, False, (u'ぽん',u'ぽんぽん') ), # @tti_pon

    464490859 : (  5, False, () ),

    40480664  : (  0, False, (u'upsilon',) ), # @kim_upsilon
    39950821  : (  0, False, (u'bucyou',) ), # @ooharabucyou
    55247007  : (  7, False, (u'ねこた',) ), # @neko_ta
    266533405 : (  0, False, () ), # @tschun3 
    15026791  : (  0, False, () ), # @debiru
    66878662  : (  0, False, () ), # toranekoland
    238613592 : (  0, False, () ), # @naoya_rin
    459169581 : (  5, False, (u'メロン', u'果物',) ), # @takamimelon
    60834701  : (  3, False, (u'pnetan',) ), # @pnetan

    45138281  : (  3, False, (u'夏奈', u'南家次女', u'バカ野郎日本代表',) ), # @Minami_kana 南夏奈
    70330280  : (  3, False, (u'千秋', u'南家三女', u'カナヅチ', u'小学生',) ), # @MinamiChiaki 南千秋
}


thru_words = ThruWord.words()

allowed_hashtags = (u'kr_cvs', u'テストやで') #, u'#キョクナビ')

censor_words = ('co33k_bot', 'naoya_rin', 'naoya_t')


def is_to_ignore(status):
    # retweeted_status is set
    if getattr(status, 'retweeted_status', None):
        print '!!IGNORE: retweeted_status is set'
        return True

    # censor words
    for censor_word in censor_words:
        if censor_word in status.text:
            print '!!IGNORE: censor word (%s) detected' % censor_word
            return True

    # unallowed hashtag
    mo = re.search(ur'#(\S+)\s?', status.text)
    if mo:
        hashtag = mo.group(1)
        if hashtag not in allowed_hashtags:
            print '!!IGNORE: unallowed hashtag (%s)' % hashtag.encode('utf-8')
            return True

    # userid to be ignored
    if status.user.id in ignore_ids:
        print '!!IGNORE: (%s) in ignore_ids' % status.user.screen_name
        return True

    # thru-words
    for thru_word in thru_words: # unicode
        if thru_word in status.text:
            print '!!IGNORE: (%s) in status text' % thru_word.encode('utf-8')
            return True

    return False


def responses_for_status(user, status, dry_run=False):
    status_text = status.text

    res_rate = 12.5
    ozanari_p = False
    nickname = user.name

    if user.id in userinfos:
        res_rate, ozanari_p, nicknames = userinfos[user.id]
        # print res_rate, ozanari_p, nicknames
        if len(nicknames) > 0:
            nickname = util.my_choose(nicknames)

    # print '{ nickname=%s ozanari?=%s res_rate=%g }' % (nickname, ozanari_p, res_rate)

    if u'_music' in status_text:
        res_rate *= 0.333
    elif u'nowplaying' in status_text:
        res_rate *= 0.25
    else:
        res_rate *= 1.0


    status_text = re.sub(r'[QR]T @[_0-9A-Za-z]+', '', status_text)
    status_text = escape_unknown_persons(status_text)

    # print user.screenname, ">", status_text
    morphemes = util.split_into_morphemes(status_text)
    # print ' / '.join([' '.join(morpheme) for morpheme in morphemes])
    surfaces = [surface for surface, pos, orig_form in morphemes]
    orig_forms = [orig_form for surface, pos, orig_form in morphemes]


    responses = []
    def add_response(message, percent, with_rt=True):
        if isinstance(message, str):
            message = message.decode('utf-8')
        if with_rt:
            target_url = 'https://twitter.com/%s/status/%s' % (user.screenname, status.id_str)
            full_text = u'%s %s' % (message, target_url)
            # full_text = u'%s RT @%s: %s' % (message, user.screenname, status_text) ## unofficial RT
        else:
            full_text = u'@%s %s' % (user.screenname, message)

        responses.append( (full_text, percent * res_rate / 100) )


    # 宛先限定
    if u'雪' in status_text and 'teriyaki' in user.screenname:
        add_responses( u'nicejogging', 80 )


    # 適当な相槌
    add_response( generate_aizuchi(worse=ozanari_p), 18 )

    # 〜のくせに...
    add_response( generate_kuseni(nickname), 18 if ozanari_p else 9 )

    # モジュール
    for module in (humanity, anime, zeitgeist,):
        for response in module.generate_responses(status_text, morphemes, surfaces, orig_forms):
            if isinstance(response[0], str):
                response[0] = response[0].decode('utf-8')
            add_response(*response)

    # [(message, rate), ...]
    return responses


if __name__ == '__main__':
    text = '@abc@co33k@neko_ta@unknown@person'
    print escape_unknown_persons(text)
