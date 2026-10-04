# ![](../assets/icons/monsters/monsters_ld1_164.png){ .sprite } Arlish

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_164.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `arlish` |
| **Type** | Shopkeeper |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Brimhaven |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Farmer's flail](../items/flail_farm.md) | 100% | 1 |
| [Salt pork](../items/salt_pork.md) | 100% | 1 to 3 |
| [Cloth shirt](../items/shirt1.md) | 100% | 1 to 2 |
| [Fine green hat](../items/hat2.md) | 100% | 1 |
| [Milk](../items/milk.md) | 100% | 1 to 2 |
| [Fancy gloves](../items/gloves_fancy.md) | 100% | 1 |
| [Fine iron axe](../items/axe_fine_iron.md) | 100% | 1 |
| [Scythe](../items/scythe.md) | 100% | 1 |
| [Stiletto](../items/stiletto.md) | 100% | 1 |
| [Kitchen knife](../items/kitchen_knife.md) | 100% | 1 to 2 |
| [Butter](../items/butter.md) | 100% | 1 to 2 |
| [Raw dough](../items/dough.md) | 100% | 1 to 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [brimhaven_general1](../maps/brimhaven_general1.md) | Brimhaven | 1 | – |


## Quests

- [A cat and mouse game](../quests/cat_and_mouse.md): stages 40
- [A strange looking dagger](../quests/brv_dagger.md): stages 115, 120, 130, 200, 230
- [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md): stages 42
- [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md): stages 50

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Arlish. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/arlish_0.json" data-npc="Arlish" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (23 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-arlish_0"></span>**`arlish_0`** Arlish: “Hello. I'm Arlish, the proprietor. This is a general store, so I sell some of this, some of that, and a little bit of the other. Would you like to see what I have?”

    - “Yes, please show me.” → *shop opens*
    - “No thanks.” → *conversation ends*
    - “The teacher said that you would give me a cake.” *(if reached stage 40 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-40); NOT reached stage 42 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-42))* → [arlish_10](#d-arlish_10)
    - “The teacher said that you would give me a cake.” *(if reached stage 42 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-42))* → [arlish_20](#d-arlish_20)
    - “What can you tell me about Lawellyn's dagger?” *(if reached stage 110 of [A strange looking dagger](../quests/brv_dagger.md#stage-110); NOT reached stage 115 of [A strange looking dagger](../quests/brv_dagger.md#stage-115); NOT reached stage 120 of [A strange looking dagger](../quests/brv_dagger.md#stage-120); NOT reached stage 200 of [A strange looking dagger](../quests/brv_dagger.md#stage-200); NOT reached stage 230 of [A strange looking dagger](../quests/brv_dagger.md#stage-230))* → [arlish_asd_0](#d-arlish_asd_0)
    - “I want to talk about the investigation.” *(if reached stage 130 of [A strange looking dagger](../quests/brv_dagger.md#stage-130); NOT reached stage 200 of [A strange looking dagger](../quests/brv_dagger.md#stage-200); NOT reached stage 230 of [A strange looking dagger](../quests/brv_dagger.md#stage-230))* → [arlish_asd_100](#d-arlish_asd_100)
    - “I need to find a large empty bottle. Do you have one?” *(if reached stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20); reached stage 30 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-30); NOT reached stage 40 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-40))* → [arlish_bottle_1](#d-arlish_bottle_1)

    <span id="d-arlish_10"></span>**`arlish_10`** Arlish: “Sure. You must have done something very good. Wait a second...”

    - Next → [arlish_12](#d-arlish_12)

    <span id="d-arlish_20"></span>**`arlish_20`** Arlish: “Yes, but only one.”

    - “One could try...” → *conversation ends*

    <span id="d-arlish_asd_0"></span>**`arlish_asd_0`** Arlish: “Why? What do you know about it?”

    - “Well, I have it right here.” *(if hand over 1× [Assassin's blade](../items/dagger_assassin.md))* → [arlish_asd_20](#d-arlish_asd_20)
    - “Well, I have it right here.” *(if wearing (and give up) [Assassin's blade](../items/dagger_assassin.md))* → [arlish_asd_20](#d-arlish_asd_20)
    - “You have looked at the dagger. Can you tell me more?” *(if reached stage 50 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-50))* → [arlish_asd_30](#d-arlish_asd_30)
    - “I was just curious, I was told that a dagger I had was Lawellyn's, but I no longer have it.” *(if NOT carry 1× [Assassin's blade](../items/dagger_assassin.md); NOT wearing [Assassin's blade](../items/dagger_assassin.md); NOT reached stage 50 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-50))* → [arlish_asd_15](#d-arlish_asd_15)
    - “Nothing. I was just curious. Bye.” → *conversation ends*

    <span id="d-arlish_asd_100"></span>**`arlish_asd_100`** Arlish: “What about it?”

    - “I'm sorry, but I was not able to find any new information that would determine what happened to your father.” *(if reached stage 190 of [A strange looking dagger](../quests/brv_dagger.md#stage-190); NOT reached stage 200 of [A strange looking dagger](../quests/brv_dagger.md#stage-200); NOT reached stage 230 of [A strange looking dagger](../quests/brv_dagger.md#stage-230))* → [arlish_asd_110](#d-arlish_asd_110)
    - “I'm still investigating. I'll come back when I have more information.” *(if NOT reached stage 190 of [A strange looking dagger](../quests/brv_dagger.md#stage-190); NOT reached stage 220 of [A strange looking dagger](../quests/brv_dagger.md#stage-220))* → *conversation ends*
    - “I have some good news for you.” *(if reached stage 220 of [A strange looking dagger](../quests/brv_dagger.md#stage-220))* → [arlish_asd_140](#d-arlish_asd_140)

    <span id="d-arlish_bottle_1"></span>**`arlish_bottle_1`** Arlish: “Well, that's an unusual request. What would you need such a thing for?”

    - “Seviron at the church needs it. I'm just helping out.” → [arlish_bottle_2](#d-arlish_bottle_2)
    - “Nevermind. If you don't have one you should just say so. I'll look elsewhere.” → *conversation ends*

    <span id="d-arlish_12"></span>**`arlish_12`** Arlish: “Shall I cut it for you?”

    - “Yes, please.” → [arlish_16](#d-arlish_16)
    - “No, thank you. I prefer the cake as a whole.” → [arlish_14](#d-arlish_14)

    <span id="d-arlish_asd_20"></span>**`arlish_asd_20`** [Dummy NPC](../monsters/none.md): “Arlish takes the dagger and examines it while you continue to talk.” — **effects:** sets stage 50 of [brv_nondisplay_multipurpose (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-50)

    - “I was able to acquire the dagger and its gem. Then Edrin repaired it for me.” → [arlish_asd_30](#d-arlish_asd_30)

    <span id="d-arlish_asd_30"></span>**`arlish_asd_30`** [Arlish](../monsters/arlish.md): “This can't be it. It looks like my father's dagger, but his dagger has been missing for a couple of years now. I believe this is stolen property!”

    - “Tell me more.” → [arlish_asd_40](#d-arlish_asd_40)
    - “So what. You said it has been missing for years, so how would you know?” → *conversation ends*

    <span id="d-arlish_asd_15"></span>**`arlish_asd_15`** Arlish: “Well, he did have a dagger, but I can't say if the one you had was his if I can't look at it.” — **effects:** sets stage 115 of [A strange looking dagger](../quests/brv_dagger.md#stage-115)


    <span id="d-arlish_asd_110"></span>**`arlish_asd_110`** Arlish: “I'm sorry too. Thank you for trying.” — **effects:** sets stage 200 of [A strange looking dagger](../quests/brv_dagger.md#stage-200)


    <span id="d-arlish_asd_140"></span>**`arlish_asd_140`** Arlish: “I know you do. I heard that you found my father's murderer.”

    - Next → [arlish_asd_120](#d-arlish_asd_120)

    <span id="d-arlish_bottle_2"></span>**`arlish_bottle_2`** Arlish: “Well, I do happen to have one. I don't display it as shop inventory because I've never been asked for such a thing before. Since it's for the church, you can have it for free.” — **effects:** sets stage 40 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-40), gives [Large empty bottle](../items/large_bottle.md)


    <span id="d-arlish_16"></span>**`arlish_16`** Arlish: “Well, I'm cutting the cake into 8 large pieces. I hope they taste good to you!” — **effects:** gives 8× [Piece of cake](../items/cake_piece.md), sets stage 42 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-42)

    - “Thank you.” → *conversation ends*

    <span id="d-arlish_14"></span>**`arlish_14`** Arlish: “I'm afraid you'll get a stomachache if you eat the whole cake at once. But well - here you have it.” — **effects:** gives 1× [Cake](../items/cake.md), sets stage 42 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-42)

    - “Thank you.” → *conversation ends*

    <span id="d-arlish_asd_40"></span>**`arlish_asd_40`** Arlish: “You see, this was my father Lawellyn's most prized possession. He kept it with him always.”

    - “Please go on.” → [arlish_asd_50](#d-arlish_asd_50)

    <span id="d-arlish_asd_120"></span>**`arlish_asd_120`** Arlish: “I should have known that it was Ogea! He never agreed with my father's decision about the land.”

    - Next → [arlish_asd_130](#d-arlish_asd_130)

    <span id="d-arlish_asd_50"></span>**`arlish_asd_50`** Arlish: “Then one night, father did not come to my place for dinner as was the custom. I quickly became worried that something terrible had happened to him. So I went to Mustura for help, but she quickly pushed it off as 'Lawellyn simply went on a…”

    - Next → [arlish_asd_60](#d-arlish_asd_60)

    <span id="d-arlish_asd_130"></span>**`arlish_asd_130`** Arlish: “It would be my honor if you take Lawellyn's dagger. He would want you to have it.” — **effects:** sets stage 230 of [A strange looking dagger](../quests/brv_dagger.md#stage-230), gives 1× [Assassin's blade](../items/dagger_assassin.md)

    - “Thank you, but it was my honor to help bring you closure and justice.” → *conversation ends*

    <span id="d-arlish_asd_60"></span>**`arlish_asd_60`** Arlish: “But I tried to explain to her that Lawellyn would not do so without telling me.”

    - “That sounds suspicious.” → [arlish_asd_70](#d-arlish_asd_70)

    <span id="d-arlish_asd_70"></span>**`arlish_asd_70`** Arlish: “Indeed it does. In fact, I fear he was murdered. Will you help?”

    - “Yes. Of course I will go investigate a little. You are in need.” → [arlish_asd_80](#d-arlish_asd_80)
    - “I'm sorry, but I just don't have the time.” *(if NOT reached stage 130 of [A strange looking dagger](../quests/brv_dagger.md#stage-130))* → [arlish_asd_90](#d-arlish_asd_90)

    <span id="d-arlish_asd_80"></span>**`arlish_asd_80`** Arlish: “Oh thank you so much.” — **effects:** sets stage 130 of [A strange looking dagger](../quests/brv_dagger.md#stage-130)


    <span id="d-arlish_asd_90"></span>**`arlish_asd_90`** Arlish: “I'm sorry to hear this.” — **effects:** sets stage 120 of [A strange looking dagger](../quests/brv_dagger.md#stage-120)




## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 6 lines added |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 17 lines added, 1 line changed |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 1 line changed<br>· text: “You see, this was my father Lawellyn's most prized possesion. He kept…” → “You see, this was my father Lawellyn's most prized possession. He kep…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arlish.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arlish.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arlish.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arlish.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `arlish` |
    | Spawn group | `arlish` |
    | Loot table | `arlish` |
    | Conversation | `arlish_0` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_ld1:164` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "arlish",
     "name": "Arlish",
     "iconID": "monsters_ld1:164",
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "spawnGroup": "arlish",
     "phraseID": "arlish_0",
     "droplistID": "arlish"
    }
    ```


<small>Data from v0.8.18</small>
