#!/usr/bin/python
# -*- coding: utf-8 -*-

from util import has_any_word, has_every_word, php_rand, my_choose

def generate_responses(status_text, morphemes, surfaces, orig_forms):
    responses = []

    if u'＼ポポポポ～ン／' in status_text:
        msg = u'＼ポポポポ～ン／'
        responses.append( (msg, 80) )

    # エルシャダイ
    if u'大丈夫か' in status_text:
        msg = u'大丈夫だ、問題ない。'
        responses.append( (msg, 90) )

    # Yo
    if has_any_word(status_text, (u'yo', u'Yo', u'YO')):
        msg = u'Yo'
        responses.append( (msg, 50) )

    # 妖怪ウォッチ
    if has_any_word(orig_forms, (u'どうして', u'なんで', u'なぜ', u'何故')):
        msg = u'よ う か い のせいやで'
        responses.append( (msg, 66) )

    #if u'悲しいときー' in status_text:
    #    msg = u'#悲しいときー'
    #    responses.append( (msg, 50) )

    # エイプリルフール

    #if u'エイプリルフール' in status_text:
    #    msg = u'うそおつ'
    #    responses.append( (msg, 99) )
    #if has_any_word(status_text, (u'嘘', u'うそ')):
    #    msg = u'エイプリルフールおつ'
    #    responses.append( (msg, 99) )

    return responses
