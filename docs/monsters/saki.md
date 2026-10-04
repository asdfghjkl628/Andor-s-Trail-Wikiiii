# ![](../assets/icons/monsters/monsters_newb_1_122.png){ .sprite } Saki

| Stat | Value |
|---|---|
| Class | ghost |
| HP | 498 |
| Max AP | 12 |
| Attack cost | 4 |
| Move cost | 10 |
| Damage | 5 to 7 |
| Attack chance | 230 |
| Block chance | 233 |
| Damage resistance | 14 |
| Critical skill | 0 |
| Critical multiplier | 0 |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons can't be critically hit. Your crit build will have to sit this one out.

## On hit

- **On target:** Deathtouch (magnitude 1, 3 rounds, 50% chance)

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Soul pearl](../items/soul_pearl.md) | 100% | 5 |
| [Kazaul bonemeal](../items/pot_bm_kazaul.md) | 100% | 2 to 4 |
| [Gold coins](../items/gold.md) | 100% | 650 to 699 |

## Found on

- [undertell_1_1](../maps/undertell_1_1.md)
- [undertell_exit](../maps/undertell_exit.md)

## Quests

- [Dominion](../quests/dominion.md): stages 20, 30, 70

??? quote "Dialogue (25 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-saki_selector"></span>**`saki_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if latest stage of [Dominion](../quests/dominion.md#stage-10) is 10)* → [saki_meet_10](#d-saki_meet_10)
    - branch 2 *(if reached stage 20 of [Dominion](../quests/dominion.md#stage-20); NOT reached stage 30 of [Dominion](../quests/dominion.md#stage-30))* → [saki_pearls_10](#d-saki_pearls_10)
    - branch 3 *(if reached stage 60 of [Dominion](../quests/dominion.md#stage-60))* → [saki_trapped_10](#d-saki_trapped_10)

    <span id="d-saki_meet_10"></span>**`saki_meet_10`** Saki: “Hello, $playername.”

    - “[freaking out] Who are you? Where did you come from?” → [saki_meet_20](#d-saki_meet_20)

    <span id="d-saki_pearls_10"></span>**`saki_pearls_10`** Saki: “Are you returning because you were successful in retrieving the pearls?”

    - “Yeah, here they are.” *(if hand over 5× [Soul pearl](../items/soul_pearl.md))* → [saki_pearls_20](#d-saki_pearls_20)
    - “[lie] Yes. Here you go, all five of them.” *(if NOT carry 5× [Soul pearl](../items/soul_pearl.md))* → [saki_not_5_pearls](#d-saki_not_5_pearls)

    <span id="d-saki_trapped_10"></span>**`saki_trapped_10`** Saki: “I'm not able to get out!”

    - Next → [saki_trapped_20](#d-saki_trapped_20)

    <span id="d-saki_meet_20"></span>**`saki_meet_20`** Saki: “Saki, my name is. Haunt this area is all I do.”

    - “Pleased to meet you...I think.” → [saki_devotion_selector](#d-saki_devotion_selector)

    <span id="d-saki_pearls_20"></span>**`saki_pearls_20`** Saki: “Thank you for these powerful artifacts!” — **effects:** sets stage 30 of [Dominion](../quests/dominion.md#stage-30), removes monsters from undertell_1_1


    <span id="d-saki_not_5_pearls"></span>**`saki_not_5_pearls`** Saki: “You still have to find all of them. Now go.”

    - “Right, I need to find five of them.” → *conversation ends*

    <span id="d-saki_trapped_20"></span>**`saki_trapped_20`** [Voice of Shannal](../monsters/voice_shannal.md): “My barriers are not just physical, but magical. No one can enter or leave Undertell without my say so. $playername, get this guy!” — **effects:** sets stage 70 of [Dominion](../quests/dominion.md#stage-70)

    - Next → [saki_fight](#d-saki_fight)

    <span id="d-saki_devotion_selector"></span>**`saki_devotion_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 450 of [Devotion](../quests/devotion.md#stage-450))* → [saki_devotion_450_10](#d-saki_devotion_450_10)
    - branch 2 *(if reached stage 480 of [Devotion](../quests/devotion.md#stage-480))* → [saki_devotion_480_10](#d-saki_devotion_480_10)

    <span id="d-saki_fight"></span>**`saki_fight`** [Saki](../monsters/saki.md): “The kid can try!”

    - “It'll be my pleasure!” → [saki_fight_20](#d-saki_fight_20)

    <span id="d-saki_devotion_450_10"></span>**`saki_devotion_450_10`** Saki: “Kha'zaan are no more, thanks to you. Their spirits lingered, making us hide.”

    - Next → [saki_dominion_10](#d-saki_dominion_10)

    <span id="d-saki_devotion_480_10"></span>**`saki_devotion_480_10`** Saki: “Kha'zaan are no more. However, in the future, be wary, and learn not to get bamboozled. Hope you have learned your lesson.”

    - Next → [saki_devotion_480_ysrine_10](#d-saki_devotion_480_ysrine_10)

    <span id="d-saki_fight_20"></span>**`saki_fight_20`** Saki: “You can't have what is mine! I shall use this power to cleanse a corner of Dhayavar and make it my Dominion!”

    - “You followers of Kazaul - you want everything for yourself! Give them up!” → *fight starts*

    <span id="d-saki_dominion_10"></span>**`saki_dominion_10`** Saki: “Well, now you need to find more spirits in this place. Ours.”

    - “And you want me to liberate them. Why?” → [saki_dominion_20](#d-saki_dominion_20)

    <span id="d-saki_devotion_480_ysrine_10"></span>**`saki_devotion_480_ysrine_10`** [Ysrine](../monsters/ysrine.md): “Aye, little one. What were you thinking?”

    - Next → [saki_devotion_480_20](#d-saki_devotion_480_20)

    <span id="d-saki_dominion_20"></span>**`saki_dominion_20`** Saki: “Because while the light of Elythara may not be extinguished, it has dimmed here in Dhayavar.”

    - “Why would your colleagues be spirits? You won the war.” → [saki_dominion_30](#d-saki_dominion_30)

    <span id="d-saki_devotion_480_20"></span>**`saki_devotion_480_20`** [Saki](../monsters/saki.md): “Anyways, it was their spirits that lingered, making us hide.”

    - Next → [saki_dominion_10](#d-saki_dominion_10)

    <span id="d-saki_dominion_30"></span>**`saki_dominion_30`** Saki: “Did we win? Perhaps. Narrowly. And not decisively. The Shadow remains, and monsters from the other realm still roam freely.”

    - “They lost their bodies during the war?” → [saki_dominion_40](#d-saki_dominion_40)

    <span id="d-saki_dominion_40"></span>**`saki_dominion_40`** Saki: “Yes. Five of my closest colleagues lost their corporeal forms here. The magic was heavy, and Elythara's blessing caused their spirits to linger.”

    - “Like the Kha'zaan shades.” → [saki_dominion_50](#d-saki_dominion_50)

    <span id="d-saki_dominion_50"></span>**`saki_dominion_50`** Saki: “Er...yes. Similar. And now that the Kha'zaan are gone, they remain. Will you help them?”

    - “They will not attack me?” → [saki_dominion_60](#d-saki_dominion_60)

    <span id="d-saki_dominion_60"></span>**`saki_dominion_60`** [Lethgar miner ghost](../monsters/lethgar_miner_ghost.md): “They helped defend Dhayavar. They are not likely to harm any of us now.”

    - “Very well. What needs to be done?” → [saki_dominion_70](#d-saki_dominion_70)

    <span id="d-saki_dominion_70"></span>**`saki_dominion_70`** [Saki](../monsters/saki.md): “You are right to be wary. But I swear on Elythara, no harm will come from us.”

    - “Tell me what I must do.” → [saki_dominion_80](#d-saki_dominion_80)

    <span id="d-saki_dominion_80"></span>**`saki_dominion_80`** Saki: “When they fell, their souls condensed into pearls. Five in total.”

    - “Pearls?” → [saki_dominion_90](#d-saki_dominion_90)

    <span id="d-saki_dominion_90"></span>**`saki_dominion_90`** Saki: “Yes. Shimmering soul pearls. Liches gathered them, unaware of what they carried.”

    - “So I must destroy the liches and recover the pearls.” → [saki_dominion_100](#d-saki_dominion_100)

    <span id="d-saki_dominion_100"></span>**`saki_dominion_100`** Saki: “They will return again and again unless stopped. Kill them, reclaim the pearls, and bring them here.” — **effects:** sets stage 20 of [Dominion](../quests/dominion.md#stage-20), spawns monsters on undertell_21, spawns monsters on undertell_3_lava_01, spawns monsters on undertell_4_01, spawns monsters on undertell_7_10, spawns monsters on undertell_5

    - “I will return with the soul pearls.” → *conversation ends*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=saki.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=saki.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=saki.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=saki.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `saki` · Data from v0.8.18</small>
