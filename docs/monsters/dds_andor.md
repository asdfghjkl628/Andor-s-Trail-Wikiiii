---
description: "Andor is an NPC who can also be fought in Andor's Trail, found in road5_house, wayto_feygard_duleian_2, final_cave1, final_cave2, Mt. Galmore."
---

# ![](../assets/icons/monsters/monsters_maksiu1_1.png){ .sprite } Andor

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_maksiu1_1.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | road5_house, wayto_feygard_duleian_2, final_cave1, final_cave2, Mt. Galmore |
| **Class** | Humanoid |
| **HP** | 200 |
| **XP when defeated** | 258 |
| **Entries in game data** | 4 |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

!!! info "4 entries in the game data"
    The game's data files define 4 separate characters named Andor. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location, combat statistics, loot or shop stock, faction, movement. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`dds_andor`](#v-dds_andor) | NPC | [road5_house](../maps/road5_house.md#pin-npc-dds_andor), [wayto_feygard_duleian_2](../maps/wayto_feygard_duleian_2.md#pin-npc-dds_andor) | – | – |
| [`lae_andor2`](#v-lae_andor2) | NPC | [final_cave1](../maps/final_cave1.md#pin-npc-lae_andor2) | – | – |
| [`lae_andor3`](#v-lae_andor3) | NPC/Enemy | [final_cave2](../maps/final_cave2.md#pin-npc-lae_andor3) | – | 200 |
| [`mg2_andor`](#v-mg2_andor) | Enemy | Mt. Galmore: [galmore_52](../maps/galmore_52.md), [galmore_72](../maps/galmore_72.md) | – | 1 |

## Road5 house and 1 more (dds_andor) { #v-dds_andor }

**Entry ID:** `dds_andor` · **Type:** NPC

**Location:** [road5_house](../maps/road5_house.md#pin-npc-dds_andor), [wayto_feygard_duleian_2](../maps/wayto_feygard_duleian_2.md#pin-npc-dds_andor)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [road5_house](../maps/road5_house.md) | – | 1 | Appears later, during a quest |
| [wayto_feygard_duleian_2](../maps/wayto_feygard_duleian_2.md) | – | 1 | Appears later, during a quest |

### Quests

- [Darkness in the Daylight](../quests/darkness_in_daylight.md): stages 300, 310
- [Search for Andor](../quests/andor.md): stages 145, 147, 999
- [Shadows](../quests/shadows.md): stages 280, 290

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Andor. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/dds_andor.json" data-npc="Andor" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (12 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

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


??? info "Technical information (dds_andor)"

    | | |
    |---|---|
    | Entry ID | `dds_andor` |
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


## Final cave1 (lae_andor2) { #v-lae_andor2 }

**Entry ID:** `lae_andor2` · **Type:** NPC

**Location:** [final_cave1](../maps/final_cave1.md#pin-npc-lae_andor2)

### Quests

- [Not Pony Island](../quests/lae_centaurs.md): stage 170

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Andor. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_algangror2.json" data-npc="Andor" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

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


??? info "Technical information (lae_andor2)"

    | | |
    |---|---|
    | Entry ID | `lae_andor2` |
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


## Final cave2 (lae_andor3) { #v-lae_andor3 }

**Entry ID:** `lae_andor3` · **Type:** NPC/Enemy

**Location:** [final_cave2](../maps/final_cave2.md#pin-npc-lae_andor3)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: this character belongs to the faction `lae_andor3`, and the game treats members of a faction as hostile once your standing with that faction drops below zero.

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 200 |
| XP when defeated | 258 |
| Damage | 10 to 22 |
| Attack chance | 70 |
| Block chance | 50 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 4 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 10 to 100 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [final_cave2](../maps/final_cave2.md) | – | 1 | – |

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Andor. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_andor3.json" data-npc="Andor" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-lae_andor3-lae_andor3"></span>**`lae_andor3`** Andor: “You really believed I was your brother? Hahaha!” — **effects:** faction “lae_andor3” set to -99




### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (lae_andor3)"

    | | |
    |---|---|
    | Entry ID | `lae_andor3` |
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


## Mt. Galmore, Galmore 52 and 1 more (mg2_andor) { #v-mg2_andor }

**Entry ID:** `mg2_andor` · **Type:** Enemy

**Location:** Mt. Galmore: [galmore_52](../maps/galmore_52.md), [galmore_72](../maps/galmore_72.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 1 |
| XP when defeated | 1 |
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
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [galmore_52](../maps/galmore_52.md) | Mt. Galmore | 1 | Appears later, during a quest |
| [galmore_72](../maps/galmore_72.md) | – | 1 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (mg2_andor)"

    | | |
    |---|---|
    | Entry ID | `mg2_andor` |
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



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


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
