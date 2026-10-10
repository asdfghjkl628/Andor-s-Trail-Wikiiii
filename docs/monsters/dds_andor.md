---
description: "Andor is an NPC you can also fight in Andor's Trail, found in Road 5 house, Wayto feygard duleian 2, Final cave 1, Final cave 2, Mt. Galmore."
---

# ![](../assets/icons/monsters/monsters_maksiu1_1.png){ .sprite } Andor

**Where to find Andor:** [Road 5 house and 1 more](#v-dds_andor), [Final cave 1](#v-lae_andor2), [Final cave 2](#v-lae_andor3), [Mt. Galmore, Galmore 52 and 1 more](#v-mg2_andor)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_maksiu1_1.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Road 5 house, Wayto feygard duleian 2, Final cave 1, Final cave 2, Mt. Galmore |
| **Class** | Humanoid |
| **HP** | 200 |
| **XP when defeated** | 258 |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Road 5 house and 1 more { #v-dds_andor }

**Where:** [Road 5 house](../maps/road5_house.md#pin-npc-dds_andor), [Wayto feygard duleian 2](../maps/wayto_feygard_duleian_2.md#pin-npc-dds_andor)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Road 5 house](../maps/road5_house.md) | – | 1 | Appears later, during a quest |
| [Wayto feygard duleian 2](../maps/wayto_feygard_duleian_2.md) | – | 1 | Appears later, during a quest |

### Quests

- [Darkness in the Daylight](../quests/darkness_in_daylight.md): stages 300, 310
- [Search for Andor](../quests/andor.md): stages 145, 147, 999
- [Shadows](../quests/shadows.md): stages 280, 290

### Dialogue simulator

Talk to Andor as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/dds_andor.json" data-npc="Andor" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (12 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-dds_andor-dds_andor"></span>**`dds_andor`** Andor: “Hey, who's that running over?”

    - “Hey, Andor!” *(if reached stage 280 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-280))* → [dds_andor_2](#d-dds_andor-dds_andor_2)
    - “Hey, Andor!” *(if reached stage 260 of [Shadows](../quests/shadows.md#stage-260))* → [dds_andor_4](#d-dds_andor-dds_andor_4)

    <span id="d-dds_andor-dds_andor_2"></span>**`dds_andor_2`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 300 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-300)

    - branch 1 → [dds_andor_10](#d-dds_andor-dds_andor_10)

    <span id="d-dds_andor-dds_andor_4"></span>**`dds_andor_4`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 280 of [Shadows](../quests/shadows.md#stage-280)

    - branch 1 → [dds_andor_10](#d-dds_andor-dds_andor_10)

    <span id="d-dds_andor-dds_andor_10"></span>**`dds_andor_10`** Andor: “Hello, $playername, is it really you? You have grown.”

    - “I've finally found you!” → [dds_andor_20](#d-dds_andor-dds_andor_20)

    <span id="d-dds_andor-dds_andor_20"></span>**`dds_andor_20`** Andor: “Why? Did you miss me so much? Or do you not want to have to do Mikhail's work all by yourself?”

    - “Don't talk nonsense. I'm glad to see you. Come home with me.” → [dds_andor_30](#d-dds_andor-dds_andor_30)

    <span id="d-dds_andor-dds_andor_30"></span>**`dds_andor_30`** Andor: “I can't. At least not yet.”

    - “But why? Does someone want to do something bad to you? I won't allow that.” → [dds_andor_40](#d-dds_andor-dds_andor_40)

    <span id="d-dds_andor-dds_andor_40"></span>**`dds_andor_40`** Andor: “[Andor laughs dryly] Let it go, it's the big brother's job to keep an eye on things.”

    - “But ...” → [dds_andor_50](#d-dds_andor-dds_andor_50)

    <span id="d-dds_andor-dds_andor_50"></span>**`dds_andor_50`** Andor: “No. It's not possible. You'll understand that one day.”

    - “Are you just going to disappear again? Please don't!” *(if reached stage 280 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-280))* → [dds_andor_52](#d-dds_andor-dds_andor_52)
    - “Are you just going to disappear again? Please don't!” *(if reached stage 260 of [Shadows](../quests/shadows.md#stage-260))* → [dds_andor_54](#d-dds_andor-dds_andor_54)

    <span id="d-dds_andor-dds_andor_52"></span>**`dds_andor_52`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 310 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-310), sets stage 145 of [Search for Andor](../quests/andor.md#stage-145)

    - branch 1 → [dds_andor_60](#d-dds_andor-dds_andor_60)

    <span id="d-dds_andor-dds_andor_54"></span>**`dds_andor_54`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 290 of [Shadows](../quests/shadows.md#stage-290), sets stage 147 of [Search for Andor](../quests/andor.md#stage-147)

    - branch 1 → [dds_andor_60](#d-dds_andor-dds_andor_60)

    <span id="d-dds_andor-dds_andor_60"></span>**`dds_andor_60`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 999 of [Search for Andor](../quests/andor.md#stage-999)

    - branch 1 → [dds_andor_62](#d-dds_andor-dds_andor_62)

    <span id="d-dds_andor-dds_andor_62"></span>**`dds_andor_62`** Andor: “Don't worry - we'll see each other again, in happier days.” — **effects:** removes monsters from wayto_feygard_duleian_2, removes monsters from road5_house, sets stage 999 of [Search for Andor](../quests/andor.md#stage-999)

    - “Wait!” → *NPC leaves*



### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 12 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Final cave 1 { #v-lae_andor2 }

**Where:** [Final cave 1](../maps/final_cave1.md#pin-npc-lae_andor2)

### Quests

- [Not Pony Island](../quests/lae_centaurs.md): stage 170

### Dialogue simulator

Talk to Andor as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_algangror2.json" data-npc="Andor" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (6 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-lae_andor2-lae_algangror2"></span>**`lae_algangror2`** Andor: “$playername, what have you done?”

    - Next → [lae_algangror2_10](#d-lae_andor2-lae_algangror2_10)

    <span id="d-lae_andor2-lae_algangror2_10"></span>**`lae_algangror2_10`** Andor: “Now we are all locked in here! We will all starve to death!”

    - Next → [lae_algangror2_20](#d-lae_andor2-lae_algangror2_20)

    <span id="d-lae_andor2-lae_algangror2_20"></span>**`lae_algangror2_20`** Andor: “It is all your fault!”

    - “Hey - I did nothing!” → [lae_algangror2_30](#d-lae_andor2-lae_algangror2_30)

    <span id="d-lae_andor2-lae_algangror2_30"></span>**`lae_algangror2_30`** Andor: “Our only chance of survival lies in that stairway over there.”

    - “What is down there?” → [lae_algangror2_50](#d-lae_andor2-lae_algangror2_50)
    - “You didn't try it yourself yet?” → [lae_algangror2_50](#d-lae_andor2-lae_algangror2_50)
    - “Why did all that gold disappear for a few moments?” → [lae_algangror2_32](#d-lae_andor2-lae_algangror2_32)

    <span id="d-lae_andor2-lae_algangror2_50"></span>**`lae_algangror2_50`** Andor: “We can't use those stairs. Some invisible force holds us back. But maybe you can do it?” — **effects:** sets stage 170 of [Not Pony Island](../quests/lae_centaurs.md#stage-170)

    - “OK you weaklings - I'll show you.” → *conversation ends*
    - “Well, I could at least try.” → *conversation ends*

    <span id="d-lae_andor2-lae_algangror2_32"></span>**`lae_algangror2_32`** Andor: “Did it? You must have dreamed that.”

    - “If you say so.” → [lae_algangror2_30](#d-lae_andor2-lae_algangror2_30)
    - “Hmm ...” → [lae_algangror2_30](#d-lae_andor2-lae_algangror2_30)



### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Final cave 2 { #v-lae_andor3 }

**Where:** [Final cave 2](../maps/final_cave2.md#pin-npc-lae_andor3)

!!! warning "You can fight Andor"
    Andor turns hostile if you fall out with their faction.

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 200 |
| XP when defeated | 258 |
| Damage | 10 to 22 |
| AC | 70 |
| BC | 50 |
| DR | 0 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 10 to 100 |

### Dialogue simulator

Talk to Andor as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_andor3.json" data-npc="Andor" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-lae_andor3-lae_andor3"></span>**`lae_andor3`** Andor: “You really believed I was your brother? Hahaha!” — **effects:** faction “lae_andor3” set to -99




### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Mt. Galmore, Galmore 52 and 1 more { #v-mg2_andor }

**Where:** Mt. Galmore: [Galmore 52](../maps/galmore_52.md), [Galmore 72](../maps/galmore_72.md)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 52](../maps/galmore_52.md) | Mt. Galmore | 1 | Appears later, during a quest |
| [Galmore 72](../maps/galmore_72.md) | – | 1 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**4 entries.** The game data defines 4 separate characters named Andor. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location, combat statistics, loot or shop stock, faction, movement.

| Entry | Type | Section |
|---|---|---|
| `dds_andor` | NPC | [Road 5 house and 1 more](#v-dds_andor) |
| `lae_andor2` | NPC | [Final cave 1](#v-lae_andor2) |
| `lae_andor3` | NPC/Enemy | [Final cave 2](#v-lae_andor3) |
| `mg2_andor` | Scenery | [Mt. Galmore, Galmore 52 and 1 more](#v-mg2_andor) |

- `lae_andor3` belongs to the faction `lae_andor3`. The game treats any character as hostile once your standing with its faction is below zero.
- `mg2_andor` has no conversation and no combat statistics. Other conversations use it as their speaker (the `switchToNPC` field), which is how its name and picture appear in dialogue. The game data also places it on Mt. Galmore: [Galmore 52](../maps/galmore_52.md), [Galmore 72](../maps/galmore_72.md).

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: dds_andor"

    | | |
    |---|---|
    | Entry ID | `dds_andor` |
    | Type (wiki) | NPC |
    | Spawn group | `dds_andor` |
    | Loot table | – |
    | Conversation | `dds_andor` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_maksiu1:1` |
    | Defined in | `res/raw/monsterlist_darknessanddaylight.json` |

    Raw data:

    ```json
    {
     "id": "dds_andor",
     "name": "Andor",
     "iconID": "monsters_maksiu1:1",
     "monsterClass": "humanoid",
     "spawnGroup": "dds_andor",
     "phraseID": "dds_andor"
    }
    ```

??? info "Technical information: lae_andor2"

    | | |
    |---|---|
    | Entry ID | `lae_andor2` |
    | Type (wiki) | NPC |
    | Spawn group | `lae_andor2` |
    | Loot table | – |
    | Conversation | `lae_algangror2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_maksiu1:1` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_andor2",
     "name": "Andor",
     "iconID": "monsters_maksiu1:1",
     "monsterClass": "humanoid",
     "spawnGroup": "lae_andor2",
     "phraseID": "lae_algangror2"
    }
    ```

??? info "Technical information: lae_andor3"

    | | |
    |---|---|
    | Entry ID | `lae_andor3` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `lae_andor3` |
    | Loot table | `lae_andor3` |
    | Conversation | `lae_andor3` |
    | Faction | `lae_andor3` |
    | Movement | wholeMap |
    | Icon | `monsters_maksiu1:1` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_andor3",
     "name": "Andor",
     "iconID": "monsters_maksiu1:1",
     "maxHP": 200,
     "moveCost": 4,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 10,
      "max": 22
     },
     "spawnGroup": "lae_andor3",
     "faction": "lae_andor3",
     "phraseID": "lae_andor3",
     "droplistID": "lae_andor3",
     "attackCost": 4,
     "attackChance": 70,
     "blockChance": 50
    }
    ```

??? info "Technical information: mg2_andor"

    | | |
    |---|---|
    | Entry ID | `mg2_andor` |
    | Type (wiki) | Scenery |
    | Spawn group | `mg2_andor` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_maksiu1:1` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "mg2_andor",
     "name": "Andor",
     "iconID": "monsters_maksiu1:1",
     "monsterClass": "humanoid",
     "spawnGroup": "mg2_andor"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_andor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_andor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_andor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_andor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
