#!/usr/bin/python
# -*- coding: utf-8 -*-

from util import has_any_word, has_every_word, php_rand


def generate_responses(status_text, morphemes, surfaces, orig_forms):
    responses = []

    # 天空の城ラピュタ
    if u'バルス' in status_text or u'ﾊﾞﾙｽ' in status_text:
        baluses = (
            u'＼バルス!!!／',
            u'＼ﾊﾞﾙｽ／',
            u'目が、目がぁ〜！',
            u'＼ポポポポ～ン／',
            u'あ〜がぁ〜!!あ〜あ〜目がぁ〜目がぁ〜!!あ〜あ〜目がぁ〜あ〜あ〜!!'
        )
        msg = my_choose(choices, False)
        responses.append( (msg, 99) )

    # 這いよれ！ニャル子さん
    if has_every_word(status_text, (u'うー', u'にゃー')):
        if php_rand(1, 10) < 7:
            msg = u'(」・ω・)」うー！ (／・ω・)／にゃー！'
        else:
            msg = u"Let's＼(・ω・)／にゃー！"
        responses.append( (msg, 98) )
    if has_any_word(status_text, (u'SAN値', u'ピンチ')) and u'パンチ' not in status_text:
        msg = u'＼(・ω・＼)SAN値!(／・ω・)／ピンチ!'
        responses.append( (msg, 98) )
    if u'ピンチにパンチ' in status_text:
        msg = u'＼(・ω・＼)PIN値!(／・ω・)／パンチ!'
        responses.append( (msg, 98) )
    if u'太陽曰く燃えよカオス' in status_text:
        if php_rand(1, 10) < 2:
            msg = u'(」・ω・)」うー！ (／・ω・)／にゃー！'
        else:
            msg = u"Let's＼(・ω・)／にゃー！"
        responses.append( (msg, 98) )
    if u'」うー' in status_text:
        msg = u'(／・ω・)／にゃー！'
        responses.append( (msg, 98) )
    if u'／にゃー' in status_text:
        msg = u'(」・ω・)」うー！'
        responses.append( (msg, 98) )

    # 花咲くいろは
    if has_any_word(status_text, (u'ほびろん', u'ホビロン')):
        msg = u'死ね! #hanairo'
        responses.append( (msg, 98) )
    if has_any_word(status_text, (u'なこち', u'押水', u'豊崎', u'愛生')):
        # '菜子'/non美奈子
        msg = u'なこち' + (u'！' * php_rand(1, 3)) + u' #hanairo'
        responses.append( (msg, 50) )
    if has_any_word(status_text, (u'松前', u'緒花')):
        msg = u'ふーん'
        responses.append( (msg, 50) )

    # ゆるゆり
    if u'いつもミラクル' in status_text:
        msg = u'ててってててって'
        responses.append( (msg, 99) )
    if u'ゆりゆららららゆるゆり' in status_text:
        msg = u'結衣せんぱーい！'
        responses.append( (msg, 99) )

    # 進撃の巨人
    if u'紅蓮の弓矢' in status_text:
        msg = u'＼ｲｪｪｪｪｶﾞｧｧｧー!!!!／'
        responses.append( (msg, 90) )

    # 魔法科高校の劣等生
    if u'Rising Hope' in status_text:
        msg = u'＼みかんでマッサージ／'
        responses.append( (msg, 98) )

    # ラブライブ
    #if has_any_word(status_text, (u'エリチカ', u'絢瀬絵里')):
    #    msg = u'おうちに帰る!!'
    #    responses.append( (msg, 10) )
    if has_any_word(status_text, (u'おうちに帰る', u'おうちかえる')):
        msg = u'こみみけ、おうちに帰る!!'
        responses.append( (msg, 50) )

    # 日常
    if u'じょーじょーゆーじょー' in status_text:
        msg = u'ててててててて'
        responses.append( (msg, 50) )

    # まどか☆マギカ
    if u'ほむ' in status_text:
        msg = (u'ほむ' * php_rand(1, 4)) + u' #homhom'
        responses.append( (msg, 50) )

    # のんのんびより
    if u'にゃんぱす' in status_text:
        msg = u'にゃんぱすー'
        responses.append( (msg, 99) )

    # 刀語
    if has_any_word(status_text, (u'刀語', u'とがめ')):
        msg = u'ちぇりおー!!'
        responses.append( (msg, 99) )

    # イナズマイレブンGO
    if u'たそがれない' in status_text:
        # 「かなり純情」
        msg = u'私そっと瞳閉じない'
        responses.append( (msg, 99) )

    # KT
    if u'こんいろ∞トキメキ' in status_text:
        msg = u'＼SU・KU・MI・ZU！／'
        responses.append( (msg, 99) )
    elif has_every_word(status_text, (u'海', u'水着')):
        msg = u'＼SU・KU・MI・ZU！／'
        responses.append( (msg, 99) )

    ## その他、声優ネタ
    if has_any_word(status_text, (u'くぎゅ', u'釘宮', u'ルイズ')):
        msg = u'くぎゅ' + (u'う' * php_rand(8, 20)) + u' http://t.co/tfMqkNq'
        responses.append( (msg, 99) )

    if has_any_word(status_text, (u'堀江', u'由衣', u'ほっちゃん', u'ほちゃ')):
        msg = u'ほ、ほーっ、ホアアーッ!! ホアーッ!!'
        responses.append( (msg, 99) )

    if has_any_word(status_text, (u'長門', u'有希')):
        msg = u'長門ぉーーー!!!'
        responses.append( (msg, 99) )

    if u'奈々' in status_text:
        msg = u'奈々様ーーー!!!'
        responses.append( (msg, 99) )
    if u'シャッス' in status_text:
        msg = u'シャッス!!!'
        responses.append( (msg, 99) )

    if has_any_word(status_text, (u'ERIN', u'えーりん')):
        msg = u'えーりん！えーりん！( ﾟ∀ﾟ)o彡゜'
        responses.append( (msg, 99) )


    return responses
