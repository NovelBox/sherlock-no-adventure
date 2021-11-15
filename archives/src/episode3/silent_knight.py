# -*- coding: utf-8 -*-
'''
Episode 3-0
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "沈黙の騎士"


# NOTE: outlines
ABSTRACT = """
$maryが一緒に暮らすようになり、彼女が家事に関する全てを買って出てくれた。だが$maryは経験がなく、おまけに壊滅的に下手だった。
今日も料理を失敗し、落ち込んで市場に買い出しに行く$maryを見送りつつ、$sherlockは$wilsonからの依頼で記事を調査する。
謎の失踪事件についての記事はいくつかあったが、関連性が見えてこない。それとは別の最近猟奇的な殺され方をしている事件があった。そちらはまだ話題になっていなかったが気になるという$sherlock。
一方買い物に出かけた$maryは$ignesたちと面識ができ、少し喋れるようになっていた。彼らに色々と紹介してもらい、市場の人間たちとも馴染みつつあった。彼女が$animalということで最初は奇異に見られたが、それも今でもマスコット的な存在となっていた。
帰り道、$maryは真っ赤な鎧を着た騎士を見つける。彼は困惑した様子で、$maryは思わず声を掛けた。
$maryが謎の鎧騎士を連れてくる。しかしその鎧騎士は話すことができなかった。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            #   NOTE
            w.plot_setup("$maryが一緒に暮らすようになり家事全般を担当してくれるようになったが彼女は壊滅的に下手だった"),
            w.plot_turnpoint("失敗して落ち込む$maryは市場に買い出しに向かう"),
            w.plot_develop("$wilsonは$sherlockにもう少し$maryに対して優しく扱ってやればと進言するが$sherlockは興味がない。ただ$wilsonの依頼である第二王女失踪に関する記事を集めてくれていた"),
            w.plot_turnpoint("$maryは市場で困っている赤い鎧騎士を見つける"),
            w.plot_resolve("$maryが困っていた鎧騎士を拾って連れて帰ってくる"),
            w.plot_turnpoint("$maryが連れてきた鎧騎士は喋ることができなかった"),
            w.plot_note("$maryが一緒に暮らすようになった"),
            w.plot_note("彼女は起きてくると、リビングで新聞を広げている$sherlockを見て「おはよう」と挨拶する"),
            w.plot_note("返事のない$sherlockにきれながらもキッチンに向かう"),
            w.plot_note("顔を洗い、エプロンをする"),
            w.plot_note("朝食の準備をする"),
            w.plot_note("焦げた目玉焼きにベーコン、パンにミルク"),
            w.plot_note("$sherlockは何も言わずにそれを食べる"),
            w.plot_note("そこに$wilsonが訪れる。「おはよう。ずいぶんと香ばしい臭いだね」"),
            w.plot_note("相変わらず料理は下手なままで$wilsonにからかわれると、$maryは「うちかて必死にやってんねん」とむくれる"),
            w.plot_note("「食事なんてお腹が膨れればいいんだよ」とそっけない$sherlock"),
            w.plot_note("$wilsonにも出してくれて、そのプレートを食べるがまずい顔"),
            w.plot_note("$maryは怒りながらも自分でもまずいらしい"),
            w.plot_note("$maryはそれでも食べて、後片付けにキッチンに引っ込む"),
            w.plot_note("$wilsonは$sherlockに失踪事件について何か進捗があったか尋ねる"),
            w.plot_note("改めて$wilsonの依頼内容を整理する$sherlock"),
            w.plot_note("第二王女が失踪したのは一ヶ月前。既に亡くなっていてもおかしくない"),
            w.plot_note("謎の失踪事件については、普通の失踪事件と見分けがつかないから判断しようがないが、記事にはいくつも見つかる"),
            w.plot_note("記事に掲載されるものの発生はばらばらで、頻度もよく分からない"),
            w.plot_note("それとは別に女性の猟奇殺人が二件、近く発生している。このうちの一人が半月前に失踪していた"),
            w.plot_note("第二王女については$adelにも実は聞いていたが$wilsonには黙っていた"),
            w.plot_note("$maryは洗濯物に取り掛かる"),
            w.plot_note("「ずいぶんと馴染んだな」と苦笑する$wilson"),
            w.plot_note("「馴染んでもらうのも困るんだが」と$sherlock"),
            #
            w.plot_note("一段落し買い物に出かける$mary"),
            w.plot_note("$sherlockは研究室にこもって何かやっていた"),
            w.plot_note("$Boscombeとは違い、どこも人が多く、まだまだ慣れない"),
            w.plot_note("馬車がいきかい、たまに$carと呼ばれる不思議な乗り物が走っていく"),
            w.plot_note("街は$maryにとって目新しいものばかりだった"),
            #
            w.plot_note("市場にやってくる$mary"),
            w.plot_note("最初は恐る恐るだったが$sherlockのところに出入りしている$ignesなど顔見知りが少しできて、話せるようになっていた"),
            w.plot_note("「おう$mary。買い物か？」と$ignes"),
            w.plot_note("$ignesは配達の途中だった"),
            w.plot_note("「うん。$ignesさんはお仕事？」"),
            w.plot_note("$maryは$sherlockがどんな人なのか、思い切って聞いてみる"),
            w.plot_note("$ignesは確かに変わっているが盗みで生計を立てるしかなかった自分みたいな子供に仕事を紹介してくれたりして、助かっていると"),
            w.plot_note("本人は謎や不思議を解明するのが好きだと言っているが、本心は人助けをすることに何かしら価値を見出しているんじゃないかと"),
            w.plot_note("「お前、好きなのか？」と笑う$ignes"),
            w.plot_note("$maryは「$ignesは嫌い」と言って先に行く"),
            w.plot_note("市場は$Boscombeとは違い、かなり賑わっていて人も多いし、露店も沢山開かれている"),
            w.plot_note("花屋の手伝いをしている$refiに出会う"),
            w.plot_note("$refiとは気が合った"),
            w.plot_note("$refiも捨て子で、スラムの集団の中で育った"),
            w.plot_note("$ignesたちに助けられながら育ち、今は$sherlockのツテで花屋の手伝いなんかをしながら暮らしている"),
            w.plot_note("$refiは$sherlockが好きと語る"),
            w.plot_note("他の人は見た目や金銭の有無で人を差別するけれど、$sherlockにとってそれは意味がないと"),
            #
            w.plot_note("買い物を済ませた$maryは途中で真っ赤な鎧を着た騎士を見つける"),
            w.plot_note("$maryは彼に声をかけた"),
            #
            w.plot_note("$sherlockは$wilsonと$maryについて話し合っていた"),
            w.plot_note("今後ずっとこのまま置いておくという訳にもいかないだろう、と"),
            w.plot_note("$sherlockもいつ危険なことに巻き込まれて命を落とすとも限らない"),
            w.plot_note("そういう時に備えて大家の$lisaなんかに話しておこうと思っていると"),
            w.plot_note("そこに$maryが戻ってくる"),
            w.plot_note("彼女は真っ赤な鎧騎士を連れていた"),
            w.plot_note("「あの、この騎士さんが困ってはったから、拾ってきたんやけど」"),
            w.plot_note("鎧騎士は頭を下げた"),
            outline=ABSTRACT)

