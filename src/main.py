#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from storybuilder.assets import common_rubi
from config import ASSET
# import scenes
from scenes import Apart
from scenes import Bridge


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Structure    - 1/8: 1K
#   4. Spec
#   5. Plot         - 1/4: 2.5K
#   6. Scenes
#   7. Conte        - 1/2: 5K
#   8. Layout
#   9. Draft        - 1/1: 10K
#
################################################################

# Constant
TITLE = "夕暮れの笑顔が描けない"
MAJOR, MINOR, MICRO = 2, 0, 0
COPY = "口にしなければ壊れなかったのだろうか"
ONELINE = "仲良し三人組を崩して恋人になった二人だったが"
OUTLINE = "約一万字の恋愛短編。付き合っている彼を呼び出して別れようと切り出す。何故そこに至ったのかを彼女は語り始めた。"
THEME = "真実を知ることで壊れてしまった"
GENRE = "恋愛"
TARGET = "20-30years(woman)"
SIZE = "25から30枚相当"
CONTEST_INFO = "コバルト短編小説新人賞209回"
CAUTION = ""
NOTE = "以前イラストコンテストに出したものの焼き直し"
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
TAGS = ["恋愛",]
RELEASED = (8, 9, 2020)


# Episodes
def ep_main(w: World):
    return w.episode('別れ話',
            Bridge.reunion(w),
            Apart.her_truth(w),
            w.symbol("（了）"),
            )


def ch_main(w: World):
    return w.chapter('main',
            ep_main(w),
            )


def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(common_rubi.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_taginfos(*TAGS)
    w.config.set_released(*RELEASED)
    return w.run(
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

