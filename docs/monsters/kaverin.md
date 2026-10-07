---
description: "Kaverin is an NPC who can also be fought in Andor's Trail, found in Remgard. Starts Old friends?."
---

# ![](../assets/icons/monsters/monsters_ld1_100.png){ .sprite } Kaverin

**Where to find Kaverin:** Remgard: [Remgard tavern 1](../maps/remgard_tavern1.md#pin-npc-kaverin)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_100.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Role** | Starts [Old friends?](../quests/kaverin.md) |
| **Found in** | Remgard |
| **Class** | Giant |
| **HP** | 320 |
| **XP when defeated** | 491 |
| **Entry ID** | `kaverin` |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Giant |
| HP | 320 |
| XP when defeated | 491 |
| Damage | 1 to 20 |
| Attack chance | 65 |
| Block chance | 90 |
| Damage resistance | 6 |
| Max AP | 5 |
| Attack cost | 3 AP |
| Attacks per turn | 1 |
| Move cost | 5 AP |
| Critical skill | 30 |
| Critical multiplier | 3.0 |
| Critical hit chance | 19% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 100 |
| [Regular potion of health](../items/health.md) | 100% | 1 to 2 |
| [Weathered shirt](../items/shirt_weathered.md) | 100% | 1 |
| [Crude combat ring](../items/ring_crude_combat.md) | 100% | 1 |
| [Kaverin's sealed message](../items/kaverin_message.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Remgard tavern 1](../maps/remgard_tavern1.md) | Remgard | 1 | – |

## Quests

- [Old friends?](../quests/kaverin.md): stages 10, 20, 21, 22, 25, 40, 45, 60, 90

## Dialogue simulator

Set your quest stages and items, then talk to Kaverin. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/kaverin.json" data-npc="Kaverin" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (28 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-kaverin"></span>**`kaverin`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 21 of [Old friends?](../quests/kaverin.md#stage-21))* → [kaverin_decline2](#d-kaverin_decline2)
    - branch 2 *(if reached stage 60 of [Old friends?](../quests/kaverin.md#stage-60))* → [kaverin_fight_1](#d-kaverin_fight_1)
    - branch 3 *(if reached stage 90 of [Old friends?](../quests/kaverin.md#stage-90))* → [kaverin_done_ret](#d-kaverin_done_ret)
    - branch 4 *(if reached stage 45 of [Old friends?](../quests/kaverin.md#stage-45))* → [kaverin_done3](#d-kaverin_done3)
    - branch 5 *(if reached stage 40 of [Old friends?](../quests/kaverin.md#stage-40))* → [kaverin_done1](#d-kaverin_done1)
    - branch 6 *(if reached stage 25 of [Old friends?](../quests/kaverin.md#stage-25))* → [kaverin_return1](#d-kaverin_return1)
    - branch 7 *(if reached stage 22 of [Old friends?](../quests/kaverin.md#stage-22))* → [kaverin_accept2](#d-kaverin_accept2)
    - branch 8 *(if reached stage 20 of [Old friends?](../quests/kaverin.md#stage-20))* → [kaverin_8r](#d-kaverin_8r)
    - branch 9 → [kaverin_1](#d-kaverin_1)

    <span id="d-kaverin_decline2"></span>**`kaverin_decline2`** Kaverin: “The friend from Fallhaven returns. Please leave me be, I have things to do.”


    <span id="d-kaverin_fight_1"></span>**`kaverin_fight_1`** Kaverin: “Oh yes, I can feel it. You work for Vacor! He must be stopped!” — **effects:** sets stage 60 of [Old friends?](../quests/kaverin.md#stage-60)

    - “Fight!” → *fight starts*

    <span id="d-kaverin_done_ret"></span>**`kaverin_done_ret`** Kaverin: “Hello again. It's comforting to know that Unzel is still alive, and that you delivered my message to him.”

    - Next → [kaverin_done6](#d-kaverin_done6)

    <span id="d-kaverin_done3"></span>**`kaverin_done3`** Kaverin: “We've discovered one of Vacor's hideouts, far to the south.”

    - Next → [kaverin_done4](#d-kaverin_done4)

    <span id="d-kaverin_done1"></span>**`kaverin_done1`** Kaverin: “Thank you, my friend. May you walk in the glow of the Shadow.” — **effects:** sets stage 40 of [Old friends?](../quests/kaverin.md#stage-40)

    - Next → [kaverin_done2](#d-kaverin_done2)

    <span id="d-kaverin_return1"></span>**`kaverin_return1`** Kaverin: “It's good to see you again. Have you delivered my message to Unzel?”

    - “Yes, the message is delivered.” *(if reached stage 30 of [Old friends?](../quests/kaverin.md#stage-30))* → [kaverin_done1](#d-kaverin_done1)
    - “No, not yet.” → [kaverin_return2](#d-kaverin_return2)

    <span id="d-kaverin_accept2"></span>**`kaverin_accept2`** Kaverin: “Make sure this doesn't fall into the hands of Feygard, or her loyalists.”

    - Next → [kaverin_accept3](#d-kaverin_accept3)

    <span id="d-kaverin_8r"></span>**`kaverin_8r`** Kaverin: “My friend from Fallhaven returns. It's comforting to hear that Unzel is still alive.”

    - Next → [kaverin_8](#d-kaverin_8)

    <span id="d-kaverin_1"></span>**`kaverin_1`** Kaverin: “From the looks of you, you don't seem to be from around here. That makes two of us then. He he.”

    - “I'm from the village of Crossglen, far to the west of here.” → [kaverin_2](#d-kaverin_2)

    <span id="d-kaverin_done6"></span>**`kaverin_done6`** Kaverin: “Walk with the Shadow, my friend.”


    <span id="d-kaverin_done4"></span>**`kaverin_done4`** Kaverin: “Since you helped us stop him, it's fitting that you have this.”

    - Next → [kaverin_done5](#d-kaverin_done5)

    <span id="d-kaverin_done2"></span>**`kaverin_done2`** Kaverin: “Take this map as compensation for a job well done.” — **effects:** gives [Map to Vacor's old hideout](../items/vacor_map.md), sets stage 45 of [Old friends?](../quests/kaverin.md#stage-45)

    - Next → [kaverin_done3](#d-kaverin_done3)

    <span id="d-kaverin_return2"></span>**`kaverin_return2`** Kaverin: “Please don't take too long. Walk with the Shadow, my friend.”


    <span id="d-kaverin_accept3"></span>**`kaverin_accept3`** Kaverin: “[He gives you a sealed message]” — **effects:** gives [Kaverin's sealed message](../items/kaverin_message.md), sets stage 25 of [Old friends?](../quests/kaverin.md#stage-25)

    - “You can count on me, Kaverin.” → [kaverin_accept4](#d-kaverin_accept4)

    <span id="d-kaverin_8"></span>**`kaverin_8`** Kaverin: “Would you be willing to deliver a message to him?” — **effects:** sets stage 20 of [Old friends?](../quests/kaverin.md#stage-20)

    - Next → [kaverin_9](#d-kaverin_9)

    <span id="d-kaverin_2"></span>**`kaverin_2`** Kaverin: “Crossglen! I know that place, it's not far from Fallhaven, right?”

    - Next → [kaverin_3](#d-kaverin_3)

    <span id="d-kaverin_done5"></span>**`kaverin_done5`** Kaverin: “According to the map, the hideout should be just to the northwest of the former prison of Flagstone. Feel free to take whatever is left in there.” — **effects:** sets stage 90 of [Old friends?](../quests/kaverin.md#stage-90)

    - Next → [kaverin_done6](#d-kaverin_done6)

    <span id="d-kaverin_accept4"></span>**`kaverin_accept4`** Kaverin: “Good. Now go deliver that message to Unzel.”


    <span id="d-kaverin_9"></span>**`kaverin_9`** Kaverin: “You'd be well compensated for your efforts.”

    - “Anything for the sake of the Shadow.” → [kaverin_accept1](#d-kaverin_accept1)
    - “Sure.” → [kaverin_accept1](#d-kaverin_accept1)
    - “No, I am done helping you people.” → [kaverin_decline1](#d-kaverin_decline1)

    <span id="d-kaverin_3"></span>**`kaverin_3`** Kaverin: “I have an old ... shall we say ... friend ... from Fallhaven. Goes by the name of Unzel.”

    - Next → [kaverin_4](#d-kaverin_4)

    <span id="d-kaverin_accept1"></span>**`kaverin_accept1`** Kaverin: “Good, that's exactly what I wanted to hear.” — **effects:** sets stage 22 of [Old friends?](../quests/kaverin.md#stage-22)

    - Next → [kaverin_accept2](#d-kaverin_accept2)

    <span id="d-kaverin_decline1"></span>**`kaverin_decline1`** Kaverin: “That is unfortunate, you seemed like such a bright boy too.” — **effects:** sets stage 21 of [Old friends?](../quests/kaverin.md#stage-21)


    <span id="d-kaverin_4"></span>**`kaverin_4`** Kaverin: “You wouldn't by any chance have met him, would you?” — **effects:** sets stage 10 of [Old friends?](../quests/kaverin.md#stage-10)

    - “No, I've never met him.” → [kaverin_5](#d-kaverin_5)
    - “Yes, I've met that fool. He was an easy kill.” *(if reached stage 60 of [Missing pieces](../quests/vacor.md#stage-60))* → [kaverin_6](#d-kaverin_6)
    - “Yes, I have met him. I still have some of his blood on my boots.” *(if reached stage 60 of [Missing pieces](../quests/vacor.md#stage-60))* → [kaverin_6](#d-kaverin_6)
    - “Yes, I even helped him defeat a scoundrel named Vacor.” *(if reached stage 61 of [Missing pieces](../quests/vacor.md#stage-61))* → [kaverin_7](#d-kaverin_7)

    <span id="d-kaverin_5"></span>**`kaverin_5`** Kaverin: “I guess he keeps to himself. I sure hope he is OK. If you ever run into him, please say hi to him for me.”

    - “I'm trying to find my brother Andor, have you seen him?” → [kaverin_5b](#d-kaverin_5b)

    <span id="d-kaverin_6"></span>**`kaverin_6`** Kaverin: “You?! But ... but ... this is terrible! I bet you are one of the goons of that Vacor fellow.”

    - Next → [kaverin_fight_1](#d-kaverin_fight_1)

    <span id="d-kaverin_7"></span>**`kaverin_7`** Kaverin: “Excellent, that is good news indeed! May you walk with the Shadow, my friend!”

    - Next → [kaverin_8](#d-kaverin_8)

    <span id="d-kaverin_5b"></span>**`kaverin_5b`** Kaverin: “Andor? No, I'm sorry. I've never heard of him.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect)<br>Dialogue: 7 lines changed<br>· text: “I have an old .. shall we say .. friend .. from Fallhaven. Goes by th…” → “I have an old ... shall we say ... friend ... from Fallhaven. Goes by…”<br>· text: “(He gives you a sealed message.)” → “[He gives you a sealed message]” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `kaverin` |
    | Spawn group | `kaverin` |
    | Loot table | `kaverin` |
    | Conversation | `kaverin` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:100` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "kaverin",
     "name": "Kaverin",
     "iconID": "monsters_ld1:100",
     "maxHP": 320,
     "maxAP": 5,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "giant",
     "attackDamage": {
      "min": 1,
      "max": 20
     },
     "spawnGroup": "kaverin",
     "phraseID": "kaverin",
     "droplistID": "kaverin",
     "attackCost": 3,
     "attackChance": 65,
     "criticalSkill": 30,
     "criticalMultiplier": 3.0,
     "blockChance": 90,
     "damageResistance": 6
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kaverin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kaverin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kaverin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kaverin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
