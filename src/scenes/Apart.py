# -*- cofing: utf-8 -*-
'''
Stage: Apart
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def her_truth(w: World):
    who = w.get("who")
    return w.scene("彼女の真実",
            w.symbol("　　　　◆"),
            who.do("アトリエとして借りているアパートに戻ると、強烈な西日が差し込んでいた。そこに立てたイーゼルに掛かる夕暮れの方の絵には、男の顔が描かれていない"),
            who.do("秋奈は画材を取り出すと、ナイフの先で男の頭の部分を少しずつ削ぎ取る。そちらが終われば女の方も"),
            who.do("日が落ちてすっかり暗くなった頃、秋奈は部屋を出た"),
            who.do("差し込んだ月明かりが照らすイーゼルの絵には男だけが描かれ、その彼は寂しげに笑みを浮かべていた"),
            )

