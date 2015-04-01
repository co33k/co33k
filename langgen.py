#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# A random sentence generator
#
import random

from util import p, my_rand, my_choose, has_any_word


def arg_to_gen(arg):
    if isinstance(arg, str):
        if len(arg) == 0 or arg[0] == ' ':
            return lambda use_gaussian: arg
        else:
            candidates = arg.split(' ')
            return lambda use_gaussian: my_choose(candidates, use_gaussian=use_gaussian)
    elif isinstance(arg, unicode):
        return lambda use_gaussian: arg.encode('utf-8')
    elif isinstance(arg, tuple) or isinstance(arg, list):
        return lambda use_gaussian: my_choose(arg, use_gaussian=use_gaussian)
    elif isinstance(arg, LanguageGenerator):
        return arg.gen
    else:
        return arg


class LanguageGenerator():
    def __init__(self, letter_gen, len_range, joint='', end=''):
        self.letter_gen = arg_to_gen(letter_gen)
        self.len_gen = lambda: my_rand(*len_range)
        self.joint_gen = arg_to_gen(joint)
        self.end_gen = arg_to_gen(end)

    def gen(self, use_gaussian=True):
        components = []
        length = self.len_gen()
        for i in range(length):
            components.append(self.letter_gen(use_gaussian))
            if i < length-1:
                components.append(self.joint_gen(use_gaussian))
            else:
                components.append(self.end_gen(use_gaussian))
        return ''.join(components)


tetete_gen = LanguageGenerator(
    LanguageGenerator('te', (1,7)),
    (1,6), ' ', 'he!! ! . ? !?')

tetete_ja_gen = LanguageGenerator(
    LanguageGenerator('て', (1,6)),
    (1,4), '　', 'へ☆ ！ 。 ？ へ＞＜')

chomochomo_gen = LanguageGenerator(
    LanguageGenerator('chomo', (1,3)),
    (1,4), ' ', '!! ! . ? !?')

ebiebi_gen = LanguageGenerator(
    LanguageGenerator('こみみけ えび さそり かに はら うばー うべー', (1,6)),
    (1,4), '　', 'ー☆ だYO やで ＞＜')

morus_gen = LanguageGenerator(
    LanguageGenerator('- .', (1,5)),
    (1,12), ' ', '')

sansuu_gen = LanguageGenerator(
    LanguageGenerator('1 2 3 4 5 6 7 8 9', (1,5)),
    (3,6), (' × ', ' + ', ' - ', ' ÷ '), ' = ')

melody_gen = LanguageGenerator(
    LanguageGenerator('ふぁ＃ し♭ ど ら♭ れ み ふぁ そ ら し み♭ ど＃', (3,7)),
    (2,6), '　', '♪')


def generate_aizuchi(worse=False):
    candidates = [
        u'ｶﾞﾀｯ',
        u'ですよねー',
        u'なるほどやでー',
        u'ふむふむ',
        u'へぇー',
        u'φ(｀д´)ﾒﾓﾒﾓ...',
        u'ふーん',
        u'ほほー',
        u'＞＜',
    ] #, 'にゃんぱすー']
    if worse:
        # (ゝω・)vｷｬﾋﾟｯ
        # 'エイプリルフールおつ',
        candidates += [
            u'すみません',
            u'草不可避',
            u'うにー',
            u'(∩ﾟдﾟ)ｱｰｱｰきこえなーい',
            u'うわ' + (u'あ' * random.randint(0,3)),
            u'ぷんぷくり～ん（怒） http://bit.ly/qq66qg ',
            u'激おこぷんぷん丸',
            u'激おこスティックファイナリアリティぷんぷんドリーム',
            u'エターナルフォースブリザード',
            u'えー！ なにそれ!?　 知りたい知りたーい♪',
            u'私、気になります！',
            u'それすごいいいね！',
            u'＼(^o^)／',
            u'てへぺろ(・ω<)',
            u'あげぽよ',
            u'♡',
            u'＼どんまい／',
            u'kokomadeやで',
            u'ｼｬﾊﾞﾄﾞｩﾋﾞﾀｯﾁﾍｰﾝｼｰﾝ!!',
            u'ﾃｨｳﾝ' * random.randint(2, 5),
        ]

        if p(50):
            candidates.append(u'うそおつ')
            # if (p(50)) $choix[] = 'エイプリルフールおつ';
        if p(30):
            candidates.append(u'm9(^Д^)ﾌﾟｷﾞｬｰ')

    return my_choose(candidates, use_gaussian=False)


def generate_kuseni(nickname=''):
    if has_any_word(nickname, (u'だって終わらない',
                               u'どこまでも自転車で行く')):
        return u'%sくせに…' % nickname

    if p(15):
        return u'%sが未だにbotなのか人力なのか分からない…' % nickname
    elif p(15):
        if nickname[-2:] == u'さん':
            nickname = nickname[:-2]
        return u'「%sさんっていつもふざけてるよね」「いい意味で」' % nickname
    elif p(15):
        return u'「%sにゃん？あああの妖怪なんとかの」' % nickname
    elif p(15):
        return u'%sはキメ顔でそう言った。' % nickname
    else:
        return u'%sのくせに…' % nickname


def generate_marukame():
    udon = (
        '釜揚げうどん', '釜玉うどん', '明太釜玉うどん', 'ぶっかけうどん',
        'かけうどん', 'ざるうどん', 'おろし醤油うどん', 'とろ玉うどん', 'カレーうどん'
    )
    mori = ('大', '並', '並', '梅', '笑')
    order = '%s(%s)' % (my_choose(udon), my_choose(mori, use_gaussian=True))

    tempura_gen = LanguageGenerator(
        LanguageGenerator(
            ('野菜かき揚げ', '半熟玉子天', 'かしわ天', 'えび天', 'いか天', 'げそ天',
             'きす天', 'ちくわ天', 'さつまいも天', 'なす天', 'かぼちゃ天'), (1,1)),
        (0,3), ' + ', '')

    tempura = tempura_gen.gen()

    if tempura != '':
        order += ' + ' + tempura

    return order


_poke_letters = (
    'はじめまして', 'こんにちは', 'こんばんは',
    'どうも', 'たすけてくださーい！', 'だれか', 'たすけてー！',
    'おたすけください！', 'よろしく', 'きゅうじょ', 'もとむ！', 'たのむ！',
    'キンキューじたい', 'はっせい！', 'たよりにしてます！',
    'ううぅ。', 'はぁ。', 'やっちゃった…', 'トホホ。',
    'やられた…。', 'ミスしました。', 'おしいんです！', 'くやしい！！',
    'ＰＬＥＡＳＥ！', 'ＨＥＹ！', 'ＹＥＡＨ！', 'ＨＥＬＰ！', 'ＧＯ！', 'ＧＯＯＤ！',
    'イヤーン！', 'いっしょうの', 'おねがいです', 'おねがい！',
    'こんなのアリ？！', 'ショック！', 'もうちょいで', 'ということで',
    'それでは', 'つよい', 'よわい', 'わたしとしたことが', 'ムチャをしました',
    'クリアもくぜん', 'ユダンしました', 'ちからつきました',
    'できればすぐ！', 'これるものなら！', 'カンタンです', 'むずかしいです',
    'おれいに', 'どうぞ', 'いどうちゅう', 'たんけんちゅう', 'すみません',
    'おまたせしました', 'ジャジャーン！', 'とうじょう！', 'ときどき', 'また',
    'いつのひか', 'やはり', 'いつも', 'いつまでも', 'メリークリスマス', 'プレゼント',
    'さいきょうの', 'さいじゃくの', 'キズだらけの', 'さすらいの',
    'おひまな', 'おちゃめな', 'あぶない', 'まじめな', 'ふしぎな',
    'あやしい', 'いかした', 'たよれる', 'かみさま', 'みならい',
    'しょしんしゃ', 'ハイレベル', 'プロレベル', 'とも', 'どうし',
    'かぜがふきますよう', 'よろしくてよ！', 'ホントに', 'ます',
    'エヘヘ', 'やった！', 'よかった', 'いやあ', 'オホホ',
    'めでたしめでたし', 'おてをはいしゃく！', 'パパンパンパン！',
    'かんりょう！', 'パチパチパチ！', 'まかせなさい！', 'らくしょー！',
    '……てごわかった', '……やばかった', 'せいこうしました',
    'なんとか', 'おめでとー。', 'がんばってね', 'ガンバレ！', 'おだいじに',
    'たっしゃで！', 'こんごとも', 'ヨロシク', 'あとはよろしく！',
    'いつでも', 'つづきをどうぞ', 'いのちを', 'たいせつに',
    'フッ……（さる）', 'では！！', 'またね♪', 'ありがとう！', 'さようなら！',
    'たすかりました！', 'サンキューです！', 'カンシャです！', 'カンゲキです！',
    'なにかください', 'しょくりょう', 'どうぐ', 'きぼう', 'いりません', 'ふよう',
    'だいじな', 'きちょうな', 'ごほうび', 'きをつけて', 'ちゅうい',
    'あります', 'ありません', 'たくさん', 'すこし', 'はやい', 'おそい', 'すごい',
    'とても', 'ほしい', 'います', 'いません', 'おれい', 'よいおとしを',
    'あけまして', 'おめでとう', 'ことしもよろしく', 'これで', 'ひとまず',
    'ヒジョーに', 'こころぐるしいですが', 'ダンジョン',
    '１０かい', '２０かい', '３０かい', '４０かい', '５０かい', '６０かい', '７０かい', '８０かい', '９０かい', '９９かい',
    'むちゃをしました', 'しか', 'ポケモン', 'たんけんたい',
    'とにかく', 'こうかん', 'なんでもよいので', 'きゃー！',
    'おれいなんて', 'いらないさ', 'はやいものがち！', 'ほしければ',
    'もうしわけございません', 'さんじょう！', 'はいけい', 'けいぐ',
    'ぜんりゃく', 'そうそう', 'じゃあね～', 'おはよう', 'さらば！',
    'さあ！', 'つどえ！', 'あつまれ！', 'ゆうきあるもの！', 'きてください',
    'すばらしい', 'あなたの', 'きみの', 'ちから', 'ひつよう', 'むぼうでした',
    'たのむから', 'たいしたものは', 'あげれませんが', 'わたせませんが',
    'ものすごい', 'またいつか', 'あいましょう', 'ごめんなさい',
    'ボンジュール！', 'ヘイヘイ！',
    'ＨＥＬＬＯ！', 'ＴＨＡＮＫ ＹＯＵ！', 'ＧＯＯＤ ＢＹＥ！', 'ＳＥＥ ＹＯＵ！',
)

_poke_endings = (
    'おねがいします', '（ためいき）', '（ドキドキ）',
    'ください', 'あげます', 'にいます', 'です', 'のみなさーん！',
    'にきゅうじょのてを！', 'にあいのてを！', 'いじょう',
    'いか', 'まで', 'のもの', 'でゲス', 'でした',
    '。', '！', '？', '…', 'ー', '～', '♪', 'Ｃｈｕ', 'ｏｒｚ',
    '（＋Ｗ＋）', '（－ｏ－）', '（＋ｏ＋）', '（。。）', '（－。－）',
)

poke_gen = LanguageGenerator(
    LanguageGenerator(_poke_letters, (1,3)),
    (1,4), '　', _poke_endings)

#def generate_poke():
#    return poke_gen.gen(use_gaussian=False)


if __name__ == '__main__':
    print 'tetete>', tetete_gen.gen()
    print 'chomochomo>', chomochomo_gen.gen()
    print 'tetete_ja>', tetete_ja_gen.gen()
    print 'ebiebi>', ebiebi_gen.gen()
    print 'morus>', morus_gen.gen()
    print 'sansuu>', sansuu_gen.gen()
    print 'melody>', melody_gen.gen()

    print 'aizuchi>', generate_aizuchi(False)
    print 'aizuchi(worse)>', generate_aizuchi(True)
    print 'kuseni>', generate_kuseni()
    print 'marukame>', generate_marukame()
    print 'poke>', poke_gen.gen(use_gaussian=False)
