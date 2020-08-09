# -*- cofing: utf-8 -*-
'''
Stage: Bridge
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def reunion(w: World):
    akina, senba, miharu = w.get('akina'), w.get('senba'), w.get('miharu')
    who = w.get("who")
    return w.scene("夕暮れ時の再会",
            akina.be(),
            akina.do("すう、と左から右に茜色を含んだ絵筆を走らせると上手い具合にかすれた夕暮れの空が描ける",
                "油系の絵の具だとどうしてもあの淡い切なさが表現できない気がして、いつも水彩絵の具にしてしまう",
                "けれど水彩では油絵の具のように塗り重ねてリアルを表現するような力強さは得られない",
                "人物画のときはその強さが欲しいのだけれど、上手くいかないものだ",
                "この橋の上から川面に夕陽が映り込む自然が見せる圧倒的なアートを目にする度に$Mは溜息を落としてしまう"),
            akina.do("チョコレート色のぺらぺらな生地のコートのポケットからスマートフォンを取り出す",
                "明るくなった液晶には$full_senbaの文字が並んだ",
                "『もうすぐ着くから』という余計なものを排除した文面に彼の必死さが伺える気がしたけれど、",
                "長文で書いてきたことなんか一度しかなかったと思い直し、",
                "結局$Mの気分がそれに向かっているだけなんだと自嘲した"),
            akina.do("折角の日に、あの頃は履けなかった踵のある靴で、あの頃憧れた背中に掛かる長さになった髪は少しだけ色を抜いた",
                "コートの下には$Mにしては丈の短いワンピースのスカートが膝上で風に揺られている",
                "後ろ姿くらいならあの子に間違えてくれるだろうか",
                "そんな悪戯をしたかった訳じゃないけれど、今までと同じではなくなる心地が自分を浮つかせているのが分かった"),
            akina.do("まだ$Mは一人だった",
                "時刻は十七時を少し過ぎたところで、橋の上を通り過ぎていく車の数も増えた",
                "向こう岸から来るバスには学生服がたくさん詰まっていて、それが嫌だから三人でいつもここまで歩いて帰ってきたことを思い出す",
                "思い出はいつも綺麗だと彼女なら言うのだろうけれど$Mにとってはご飯に混ざった砂利を噛んでしまった時のような気まずさがそこにつきまとう"),
            akina.do("カップルだろうか",
                "二人横並びで歩いてきた学生服の男女の女子側が肩をとんとんと叩いて、",
                "彼にスマートフォンを向ける",
                "びっくりしたようになった顔にシャッター音が走り、やめろよ、と照れ笑いの声で相手の女子の髪の毛を上からなでつける",
                "まだ付き合い始めたところだろう",
                "平日のこの時間帯によくここを通り掛かるけれど一度も見たことがない二人だ",
                "これが休日ならカップルや学生たちが橋の上から河を見やり、思い思いにインスタに写真を上げては笑顔を浮かべている光景が見られる",
                "でも今この橋の上にいる通行人Ａはママチャリの前カゴに膨らんだエコバッグを載せて通り抜けていくおばさんと、その初々しいカップルらしき学生二人と、",
                "$Mだけだ"),
            akina.do("日が落ちてくる",
                "右手側の山から川面に夕暮れの茜空と紫雲が長く伸びながら写し取られ、昼間の熱が冷めた空気と相まって物憂げな気持ちに寄り添ってくれる",
                "このしんみりした空気がやはり今の気分には似つかわしい",
                "いつだってさよならは胸の中をすう、と何かが吹き抜ける"),
            senba.talk("おう"),
            akina.do("手を上げなくてもよく分かる",
                "$Mを見つけた瞬間に「あ、いた」という表情になる",
                "目の前に急ブレーキで止まった自転車は学生時代から使い込んだカゴのない、ライトが右側しか残っていない、サドルの下に斜めにビニール傘が突っ込まれたひと目で彼のと分かる代物だった",
                "スタンドも無くしてハンドルを握ったまま降りた彼は頭一つか二つ分は平均より大きい",
                "ラフなシャツにジーンズ姿で、足元は爪先が薄くなったスニーカーだ",
                "きっと今日も後ろのポケットに液晶がひび割れたスマートフォンを突っ込んでいる"),
            senba.talk("$meバイトまでしか付き合えないけど、時間足りる？"),
            akina.do("二十センチ上からこちらを伺うように訊いて、その睫毛の多い涼し気な目元を細め口角を上げる",
                "小学三年の頃から慣れ親しんできた$full_senbaの作り笑いだ",
                "それが作り笑いだと気づいたのは小学校の修学旅行でみんなとはぐれて$Mと彼と$miharuの三人になった時だった",
                "彼女を安心させたい",
                "一緒にいる大切な人間への心遣いが夕暮れみたいな作り笑顔にさせる",
                "何となくそういうものだと分かってはいたけれど、その本当の意味に気づいたのは最近になってアルバムやスマートフォンの写真を見返していた時だった",
                "もっと早く気づいていたら何かが変わったのだろうか",
                "それともその程度のことでは変わらない未来に続く一本道のレールの上を歩き続けるしかないのだろうか"),
            senba.talk("あれか",
                "ひょっとして今夜仕事の相手と会うとか？",
                "$meは絵のことは分からないけど、でも$akinaなら絶対うまくいく",
                "中学の頃からずっとクラスで一番上手い絵描いてたからな"),
            akina.talk("別れよう"),
            akina.do("何度も心の中で練習した短い言葉が、彼の表情を凍りつかせた"),
            akina.think("予想外？　それとも１％くらいは覚悟があったのだろうか",
                    "$full_senbaはそれを悟られないようにといつもの作り笑顔に切り替える",
                    "彼の隙きはいつも一瞬だ",
                    "じっと注意していないと見逃してしまう、その本音が滲んだ表情を、",
                    "今日の$Mは一度も見逃さないつもりだ"),
            senba.talk("な、何言い出すんだよ急に",
                    "来月一緒に紅葉見に行こうって約束してたよな？"),
            akina.do("そういえばそんな約束を取り付けられたんだった、と思い出して苦笑する",
                    "$senbaは「な？」と$Mに今の言葉が冗談の類であることを求めてくるけれど、明け方までずっと考えて出した結論だった",
                    "今日の目元の化粧が濃いのは隈を隠す為で、それを彼は感づけない",
                    "よく見ているようで自分の見たい$full_akinaを見ているだけなのだ",
                    "かつての$Mが、そして$full_miharuがそうであったように、",
                    "いつだって自分に都合の良い世界が真っ先に目に入る",
                    "だったら思い描いた通りの世界だけ存在してくれればいいのに、と星に願ってみても、現実は無情にも時間とともにただ流れていく"),
            akina.do("夕陽の傾きが、二人の影をアスファルトの上に引き伸ばして、それが何度も車に踏みつけられていった",
                    "$Mがそれを八ほど数えたところで「冗談、だよな？」という間の抜けた声が響いた"),
            akina.talk("冗談なら良かったね、って思ってる"),
            akina.do("いきなり突きつけられた本当に流石に笑顔が引き攣った$senbaの目の前に、$Mは自分のスマートフォンの画面を突きつける"),
            senba.talk("何だよ"),
            akina.do("そこには$Mがこの二週間ばかり睡眠不足な日々を費やして描いたイラストが二枚、並べて映してあった"),
            akina.talk("これ、何の絵か分かる？"),
            akina.do("二枚とも同じ構図だ",
                    "橋の上で背の高い男性が女性を自分に引き寄せるようにして両腕を背中に回し抱き締めている",
                    "背景には遠くにうっすら青くなった山の稜線があり、そこに半分だけ顔を出した太陽の光、赤みがかった空にはグレィの雲が浮かぶ",
                    "橋の下を流れる川の水面にもその色が反射し、きらきらとした光の上にはシャボンのような様々な色の空気玉が漂っていた", "&"),
            akina.do("もう一枚はほぼ同じように橋の上で抱き合う男女だが空は一枚目より少し明るく薄っすらと青い部分も見え、より明るさに満ちている",
                    "中でも一番の違いは男の顔だ",
                    "片方は胸元に頭を埋める女性を見守るように優しい笑顔で相手の髪を撫で付けている",
                    "もう片方は背中に腕を回しつつ一体何を考えているのか分からないのっぺらぼうで、顔には何も描かれていない"),
            senba.talk("ほとんど同じみたいだけど、これが？"),
            akina.talk("こっちの夕暮れが$meで、朝明けの方が$miharu"),
            akina.do("その言葉だけではまだ意味が全然伝わらないらしい"),
            akina.talk("そういえばさ、$senbaも招待状もらってるよね"),
            senba.talk("もらった、けどさ"),
            akina.do("口ごもった彼は目線をそっと川の方に投げてしまう",
                    "さっきから$Mが何度も$full_miharuの名前を出しているのが気になるのだろう",
                    "彼の心の中の表情を読み取ろうと$Mはじっと顔を覗くようにして見上げている",
                    "いつもはここまで相手の顔なんて見ないし、見ようとも思わないけれど、",
                    "今日は、いや、今この数分間だけはどうしても彼の表情の機微を自分の網膜に刻みつけておきたい"),
            akina.talk("行くの？"),
            akina.do("何も言わずただ彼は首を横に振る"),
            akina.talk("行けばいいのに"),
            akina.do("$Mの言葉に眉を顰めると、小さな溜息をついてから彼はこう返した"),
            senba.talk("ひょっとしてあいつのこと気にしてそんなこと言い出したのか？",
                    "だったらもう俺は美春とは終わってるし、結婚式にだって出ない。卒業式でちゃんと約束しただろ？　一人しか選べないなら俺は日下部秋奈を選ぶって"),
            akina.do("あの日と同じで真っ直ぐに$Mだけを射抜く鋭さだった",
                    "そこには作られた笑みは微塵もなく、ただただ大切な一人の女性だけに熱意が向けられている"),
            akina.talk("そういえばそんなこと、言ってたね"),
            akina.do("わざとらしさでカモフラージュして視線を夕暮れと青空の狭間に投げる",
                    "あれはキャンパスの桜並木がいくつもの蕾を抱え込んで少し重そうだな、と思いながら木漏れ日に眩しそうに彼が目を細め、",
                    "$miharuはいつものようにひらひらの服を着ていてそれに蝶が止まったと大げさなくらいに喜んでいた時だった",
                    "いつもと違って妙に口数が少ないし具合でも悪いのだろうかと心配するくらいの顔色をしていた彼が大きく息を吸い込み、地響きみたいな声を発した",
                    "「あの」というそれに直感した$Mは内心で「やっとか」と期待したのに、",
                    "彼の眼差しは何故か$Mへと向けられたのだ",
                    "確かに彼が決断をするように仕向けたのは$Mだった",
                    "けれどそれは大学を出てそれぞれが別々の進路に就くことが決まり、",
                    "もうあの三人で毎日を過ごすことも、そこにいつも存在していた彼の笑顔を覗き見して満足できていた時間も失われてしまうことを考えた時に、",
                    "どういう選択をすることが$Mたちにとっての一番なのかを考えた結果だった",
                    "ただ$Mの一番と彼の一番が異なっていただけで、あの決断自体は間違ったものではなかったと今でも思っている"),
            akina.talk("で、その選んだ結果のことはどう思ってるの？"),
            akina.do("結果、と彼は小さく声に出し、二秒ほど逡巡した後で再び$Mを見て口を開いた"),
            senba.talk("$meが後悔してる、とでも言いたいのか？",
                    "$miharuとならもっと$meの人生が上手く転がってたかもなんて今更思わないよ",
                    "そもそも$meはお前と一緒にいられて幸せだし、音楽の夢だってずっと追いかけられてて、",
                    "結果こそ出てないけどさ来週の日曜には$meたちの演奏を聞きにどっかのプロデューサーが来てくれることになってるんだ",
                    "これが順調なのかどうかは分からない",
                    "けど捨てた方の人生が良かったかも知れないとかそんなこと考える方がどうかしてるよ",
                    "人生なんて常に一方通行だろ？",
                    "後戻りなんてできない",
                    "だから、$meは$meの信じた道を前に進むだけだ",
                    "それが、気に食わないのか？"),
            akina.do("口数の多い方ではない彼の舌が、熱を帯びる",
                    "こういう顔を$miharuには見せたことあるのだろうか",
                    "付き合ってみるまでこんなに内側に熱いものを抱えていた人だとは知らなかったけれど、",
                    "どうしてそれを$Mに向けてしまったのだろう"),
            senba.talk("$meじゃ、駄目なのか？"),
            akina.do("彼の瞳が$Mを射抜く",
                    "『俺は$full_akinaを選ぶ』と$miharuのいる前で宣言したあの日と同じ熱さで、",
                    "その逞しい眉を真っ直ぐにしている",
                    "それは小さなステージの上でスポットライトを浴びながら間違えないようにと必死にベースの弦を弾いている彼の生真面目な表情だった",
                    "普段から言葉にするのは苦手だっていう彼が、唯一これなら何か伝えられる気がするんだと得意げに弾いて見せてくれるベースやギター",
                    "話している時よりずっと活き活きとして楽しそうで、たった一メートルほどの距離がその何倍にも感じられるほど別の世界にいる$full_senbaがそこにはいた",
                    "ああ、本当の彼は$Mの前にはいないんだ",
                    "そう確信するに足るくらいには、別の表情を見せてくれたことを思い出す"),
            senba.talk("どうしても今すぐじゃなきゃ駄目なのか？"),
            akina.do("$Mが答えを返せずに黙り込んでしまうと、彼はその間を埋めようと必死に言葉を繋いでくる",
                    "でももう手遅れなの、と口を開こうとするけれどそれすら彼の目には入らず「なあ」とお腹に響く強い声で続ける"),
            senba.talk("$meに悪いところがあれば直す",
                    "気に入らないことや許せない癖とか、考え方とか、なんでもいい",
                    "そもそも急になのか？",
                    "それとも今までもずっと感じてた違和感なのか？",
                    "$meの前じゃそんな素振りなかったじゃないか",
                    "ひょっとしてあれか？",
                    "経済的な話か？",
                    "この先ずっと結婚できそうにないからとか、そういうやつ？　だったら"),
            akina.do("際限なく饒舌になる彼の口を右の人差し指と中指で押さえつけて黙らせた"),
            akina.talk("ねえ、覚えてるかな",
                    "$meがあの日、なんて言ったか"),
            senba.talk("あの日？"),
            akina.do("一瞬だけ思い出すように右上を見て、彼は懐かしそうに柔らかい表情で瞬きをする"),
            senba.talk("ああ、忘れてない"),
            akina.do("彼の目が真っ直ぐ向けられる",
                    "二十センチほど高い目線があの日と同じ威圧感を$Mの前で再現していた",
                    "彼はそのまま$Mの両肩に手を置くと、一歩、距離を詰めた",
                    "その後ろで支えを失った自転車が横倒しになって耳障りな音を立てたが彼は構わずに口を開く"),
            senba.talk("卒業式の前の日だ",
                    "お前は$meにずっと三人で一緒にいられないとしたらどちらを選ぶのか訊いた",
                    "$miharuとお前とは小学校からの腐れ縁で、たとえバラバラになったってその絆は一生もんだと考えてた$meにとってそんな選択は有り得ないって言ったよな"),
            akina.talk("なら翌日、どうして$meに告白なんてことしたの？",
                    "なぜ私を選んだの？",
                    "あの子は、$miharuは、いつもの下校の別れ際みたく涙を浮かべて声を殺していたじゃない",
                    "$senbaなら、ずっとあの子を妹のように守ってきたあなたなら、あんな酷いことしないと思ってた"),
            akina.think("そもそも二人を恋人というステップに踏み出させる為に身を引こうとしたのにあんなことになって、",
                    "$Mは酷く混乱してしまったことを思い出す",
                    "両肩に置かれた彼の手が熱くて、あの時とそっくりで、",
                    "胸の動悸が始まってしまった",
                    "$Mはそれを隠そうと目線を下げるけれど、彼の手はそうさせまいと力が入った"),
            akina.talk("痛いよ"),
            senba.talk("悪い", "けど$meはお前があんなこと言い出さなければ今だってきっとあの頃の三人のままで楽しく旅行の計画練ってたと思うんだ",
                    "ずっと聞かないでおこうと思ってた",
                    "けどこんな時だから聞いておきたいんだ",
                    "どうしてあんなことを言い出したんだ？",
                    "$meが$miharuと付き合うと言い出すって、そう思ったのか？"),
            akina.talk("そうよ",
                    "$meはね、いつか三人じゃなくて$senbaと$miharuの二人になるってずっと思ってた",
                    "だから卒業してみんなバラバラになっちゃう前にどうしても確かめたかったのよ",
                    "ちゃんと$miharuを幸せにしてあげられる$full_senbaかどうか", "ただそれが確かめたかったの"),
            akina.do("$Mの本音に彼は目を細くして、肩に置いていた手を下ろした",
                    "倒れてしまった自転車を引き起こすとどうしていいのか分からない視線を青く滲む山へと投げて、何か考え込むように口元をすぼめる"),
            senba.talk("最初から、さ"),
            akina.talk("え？"),
            senba.talk("最初から決まっていたんだ、$meの中では",
                    "$miharuは誰が見ても可愛くてその人懐こさと愛嬌から周囲の人間に大切にされる人生が待っているんだろうって思ってた",
                    "$akinaは逆に周囲とはあまり馴染まずに一人でも立派に立って歩いていける、そんな強さを見せながらも心の奥には誰かが付いててやらないといけない脆さみたいなものがあるなって感じてて、",
                    "だから$meにとって$miharuは妹みたいな存在で、$meが本当に男として守ってやるべき存在は$akinaだった",
                    "付き合うようになってから何度も言ったと思うけどさ、$meの本当の初恋が、$full_akinaなんだ",
                    "お前なんだよ"),
            akina.do("この三年間、彼の口から何度も聞いた言葉だ",
                    "そこに嘘偽りはなく、冗談でもなく、額に汗をきらめかせてベースを弾いている時のじっとりと熱いその生真面目さが込められた言葉だ",
                    "それを最後にどうしても聞いておきたかった"),
            akina.think("――うん、ありがとう"),
            akina.do("心の中でお礼を言うと、すう、と夕暮れ時の少し冷めた空気を吸い込んで、練習してきた言葉を口にする"),
            akina.talk("ごめん",
                    "$meの初恋はね、間違ってたの"),
            senba.do("$full_senbaは「え？」という文字を貼り付けた表情で固まっていた", "&"),
            akina.do("言葉の意味が理解できないのか、それとも理解したくてもそういう思考にならないのか、",
                    "とにかく彼は見せたことのないような寂しさと切なさの混ざった目で$Mを見つめて「え」とだけ声に漏らした"),
            akina.talk("$meの初恋は$senbaだと言ったけど、間違いだってことに気づいたのよ",
                    "$senbaじゃなかった", "それを思い出しただけ"),
            senba.talk("今更そんなこと言われてもな、$meはもうお前の恋人になったんだぞ？",
                    "$miharuを泣かせて大切な幼馴染を失ってまでお前を選んだ",
                    "それなのに間違いだったとか……何だよ", "何なんだよ！"),
            akina.do("彼は唇を噛む",
                    "何かといえばいつもそうやって我慢をする",
                    "今すぐにでも自分自身を殴りつけたいのかも知れない",
                    "本当は心の中に獣を飼っている男性だと最近になって理解してきた"),
            akina.talk("$miharuのとこに行きなよ", "まだ間に合うんじゃないかな"),
            akina.do("そんな彼を更に痛めつけるような言葉を突き出す"),
            senba.talk("今更行けるかよ", "行ってどうなるんだよ", "どうしろって言うんだ"),
            akina.talk("結婚相手から奪っちゃえばいいじゃない",
                    "だってあの子、一切連絡をくれなくなったのにわざわざ招待状送りつけてきたんだよ？",
                    "まだ$senbaのこと信じてるんだよ",
                    "諦めてないんだよ",
                    "裏切られても、まだ自分に優しかった$senbaが戻ってきてくれるって信じてるんだよ",
                    "$miharuはずっとそういう子だから"),
            senba.talk("もう、無理だよ"),
            akina.do("嗚咽にも思える「無理」という吐き出しだった",
                    "$miharuのことだけじゃない", "$Mのことも、今の別れ話も、最初から間違ってたと言ったことも、何もかもがごっちゃになって、",
                    "初めて彼から「タスケテ」という心の声が聞こえた気がした"),
            akina.do("それでも$Mは手を出さない", "どんなに酷い表情をさせてしまっても変えないと決めた決断だったから"),
            akina.talk("なんで？"),
            akina.do("言葉は無責任だと思う"),
            akina.talk("人生は一方通行だから？"),
            akina.do("思えば$Mは小さい頃から言葉や発言よりも自分で目にしたことや見て感じ取ったことの方をより大切にしてきた",
                    "それはあまり構ってくれなかった両親がスケッチブックと色鉛筆を与えて勝手に遊ばせていたという選択の結果なのかも知れないけれど、",
                    "$Mはこの結果に満足しているし、今ではこの生き方が馴染んでいると思っている",
                    "ただそれが$full_senbaにとってはあまり良い結果にならなかったというだけだ",
                    "いや、二人にとって、か"),
            akina.do("彼は$Mの言葉に首を横に振る",
                    "それから視線を$Mの右手へと向けた",
                    "けれどごめんなさい",
                    "その薬指に二人揃いにしたシルバーリングはもう嵌まっていない",
                    "質入れして画材に変わってしまった"),
            senba.talk("なんで、いつも一人で決めちまうんだ"),
            akina.talk("ごめんなさい"),
            akina.do("小さくそう呟き、$Mはそこではじめて$senbaに両腕を伸ばして彼を抱き寄せた",
                    "いつもなら彼が$Mか$miharuを抱きしめる側だけれど最後くらいは逆になってもいいだろう",
                    "背の高い彼の胸元に顔を埋めるようにして近づける",
                    "$Mが上げた柔軟剤の匂いがするシャツと胸板の逞しさが少しだけ甘い誘惑をしてきた",
                    "それに抗うように更に頭を押し付け、自分の表情を隠す"),
            akina.think("そう",
                    "そうなのだ",
                    "目の前の相手に自分の本音を知られないようにこうして相手の顔を自分の胸元で隠して誤魔化してきたのだ",
                    "そうやって彼が本当に見ていたのは$miharuではなく$Mだった",
                    "あの優しく見守るような笑顔の先にいたのは$full_akinaだったのだ"),
            senba.talk("あ……"),
            akina.do("彼のズボンのポケットでスマートフォンが鳴り出した",
                    "タイムアップの合図なのかも知れない",
                    "流れてきたのは彼がやっているバンドの激しいパンク調ではなく、$miharuが好んで聞いていた男性アイドルのポップミュージックだ"),
            akina.talk("出ないの？"),
            senba.talk("悪い"),
            akina.do("彼に回した腕を解いて離れると、背中を向けてから電話に出た"),
            senba.talk("あ、はい……ええ、早めに入れるか、ですか"),
            akina.do("どうやらバイト先かららしい",
                    "彼が大学時代から継続して働かせてもらっている中華料理屋で大将とは$Mも顔なじみだ",
                    "天津飯と蒸し鶏の香味野菜添えをいつも頼むのだけれど特別にアイスを付けてくれる",
                    "彼の周囲にはいい人が集まっていて、ただそれを彼自身は自覚していない",
                    "バンドのメンバーも口は悪いけれど$Mのことを決して悪く言ったりはしないし、イラストについては意外と真剣に意見をくれたりする"),
            senba.talk("えっと、それって今すぐですか？"),
            akina.do("漏れ聞こえた内容から察すると、早めに来て仕込みを手伝って欲しいということらしい"),
            akina.talk("行きなよ"),
            senba.talk("けどまだ話が"),
            akina.talk("もう話すことはないわよ"),
            akina.do("彼は「折り返し掛け直します」と慌ただしく口にして電話を切ると、一瞬思い切り唇を噛み締め、こう言い放った"),
            senba.talk("$meはまだ何も言ってない"),
            akina.do("あれだけ色々と言葉を並べても結局何も変わらない",
                    "これは理解しようとか話し合おうということではないのだと、彼には分からないのだ",
                    "だから$Mは力なく首を横に振ると、今一度自分のスマートフォンに映る二枚のイラストを見せた"),
            senba.talk("だからこれが何なんだよ？"),
            akina.talk("分からない？",
                    "片方はね、顔が描けないの",
                    "$meといる時のあなたはね、$miharuといた時のような笑顔を見せてはくれないのよ",
                    "だから描けない"),
            senba.do("え、という言葉を発したまま口が動かなくなってしまった彼はゆっくりと自分の右頬に指を当てて、それをつねったり、引っ張ったりしてみる",
                    "それから無理やり口角を上げて笑みを作ろうとしたが眉毛が凹んで目元に涙が滲んでしまった"),
            akina.do("$meは背を向け、一歩、彼から離れる"),
            akina.think("たぶん最初から分かってたんだと思う",
                    "三人から二人になった時に気づくべきだった",
                    "だから、さよなら、大好きだった$miharuの$full_senba"),
            senba.talk("……なあ", "$me、笑ってなかったか"),
            akina.do("笑ってたよ",
                    "それだけ答えて、どんどん足を進める",
                    "なあ、という彼の声は遠ざかり、それでも走ってまで追いかけてこようとしないことが分かって、",
                    "$Mは小指の先に小さなトゲが刺さったみたいな気持ちになりかけたけれど、",
                    "そんな痛みを本当はずっと誤魔化しながら二人で並んで歩いていただけだったんだという事実を思い出しただけで、そのトゲは今、すう、と抜けてどこかに落ちてしまった",
                    "そういえば学生時代はいつも最後まで泣いて彼に慰められている$miharuを見ながら苦笑を見せる彼に先に帰るねとアイコンタクトをして、",
                    "三人から一人になったものだった",
                    "それなのにどうしてこんなことになったのだろう",
                    "どうして$Mを、選んでしまったのだろう",
                    "どうして選ばせてしまったのだろう",
                    "その間違いに、どうして気づけなかったのだろう"),
            akina.think("たくさんの「どうして」が夕暮れに溶けていく",
                    "首筋をひやりとした生まれたての夜風が抜けていった"),
            akina.think("全然、寂しくないんてない",
                    "一人が少し肌寒いだけだ"),
            )

