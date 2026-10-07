---
description: "Dark priest is an NPC who can also be fought in Andor's Trail, found in galmore_41."
---

# ![](../assets/icons/monsters/monsters_liches_3.png){ .sprite } Dark priest

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_liches_3.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | galmore_41 |
| **Class** | Demon |
| **HP** | 330 |
| **XP when defeated** | 1,128 |
| **Immune to critical hits** | Yes |
| **Entries in game data** | 3 |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

!!! info "3 entries in the game data"
    The game's data files define 3 separate characters named Dark priest. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, combat statistics, loot or shop stock, appearance. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`dds_dark_priest`](#v-dds_dark_priest) | NPC | [galmore_41](../maps/galmore_41.md#pin-npc-dds_dark_priest) | – | – |
| [`dds_dark_priest2`](#v-dds_dark_priest2) | NPC | [galmore_41](../maps/galmore_41.md#pin-npc-dds_dark_priest2) | – | – |
| [`dds_dark_priest_monster`](#v-dds_dark_priest_monster) | Enemy | [galmore_41](../maps/galmore_41.md) | – | 330 |

## Galmore 41 (dds_dark_priest) { #v-dds_dark_priest }

**Entry ID:** `dds_dark_priest` · **Type:** NPC

**Location:** [galmore_41](../maps/galmore_41.md#pin-npc-dds_dark_priest)

### Quests

- [Darkness in the Daylight](../quests/darkness_in_daylight.md): stage 250
- [Shadows](../quests/shadows.md): stage 230

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Dark priest. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/dds_dark_priest.json" data-npc="Dark priest" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-dds_dark_priest-dds_dark_priest"></span>**`dds_dark_priest`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 190 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-190))* → [dds_dark_priest_2](#d-dds_dark_priest-dds_dark_priest_2)
    - branch 2 *(if reached stage 165 of [Shadows](../quests/shadows.md#stage-165))* → [dds_dark_priest_4](#d-dds_dark_priest-dds_dark_priest_4)

    <span id="d-dds_dark_priest-dds_dark_priest_2"></span>**`dds_dark_priest_2`** Dark priest: “How dare you stop my spell?” — **effects:** sets stage 250 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-250)

    - “It is best for Dhayavar.” → [dds_dark_priest_10](#d-dds_dark_priest-dds_dark_priest_10)

    <span id="d-dds_dark_priest-dds_dark_priest_4"></span>**`dds_dark_priest_4`** Dark priest: “How dare you stop my spell?” — **effects:** sets stage 230 of [Shadows](../quests/shadows.md#stage-230)

    - “It is best for Dhayavar.” → [dds_dark_priest_10](#d-dds_dark_priest-dds_dark_priest_10)

    <span id="d-dds_dark_priest-dds_dark_priest_10"></span>**`dds_dark_priest_10`** Dark priest: “I have no time for this.” — **effects:** removes monsters from galmore_41, spawns monsters on galmore_41

    - “Oh, you are running away?” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (dds_dark_priest)"

    | | |
    |---|---|
    | Entry ID | `dds_dark_priest` |
    | Spawn group | `dds_dark_priest` |
    | Loot table | – |
    | Conversation | `dds_dark_priest` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_liches:3` |
    | Defined in | `res/raw/monsterlist_darknessanddaylight.json` |

    Raw data:

    ```json
    {
     "id": "dds_dark_priest",
     "name": "Dark priest",
     "iconID": "monsters_liches:3",
     "moveCost": 5,
     "monsterClass": "humanoid",
     "spawnGroup": "dds_dark_priest",
     "phraseID": "dds_dark_priest"
    }
    ```


## Galmore 41 (dds_dark_priest2) { #v-dds_dark_priest2 }

**Entry ID:** `dds_dark_priest2` · **Type:** NPC

**Location:** [galmore_41](../maps/galmore_41.md#pin-npc-dds_dark_priest2)

### Quests

- [Darkness in the Daylight](../quests/darkness_in_daylight.md): stage 260
- [Shadows](../quests/shadows.md): stage 240

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Dark priest. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/dds_dark_priest2.json" data-npc="Dark priest" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (13 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-dds_dark_priest2-dds_dark_priest2"></span>**`dds_dark_priest2`** [Dark priest](../monsters/dds_dark_priest.md#v-dds_dark_priest2): “You again? This must end now.”

    - “I completely agree.” *(if reached stage 190 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-190))* → [dds_dark_priest2_2](#d-dds_dark_priest2-dds_dark_priest2_2)
    - “I completely agree.” *(if reached stage 165 of [Shadows](../quests/shadows.md#stage-165))* → [dds_dark_priest2_102](#d-dds_dark_priest2-dds_dark_priest2_102)

    <span id="d-dds_dark_priest2-dds_dark_priest2_2"></span>**`dds_dark_priest2_2`** *(silent check: the first matching branch below is taken)* — **effects:** spawns monsters on galmore_41

    - branch 1 → [dds_dark_priest2_10](#d-dds_dark_priest2-dds_dark_priest2_10)

    <span id="d-dds_dark_priest2-dds_dark_priest2_102"></span>**`dds_dark_priest2_102`** *(silent check: the first matching branch below is taken)* — **effects:** spawns monsters on galmore_41

    - branch 1 → [dds_dark_priest2_110](#d-dds_dark_priest2-dds_dark_priest2_110)

    <span id="d-dds_dark_priest2-dds_dark_priest2_10"></span>**`dds_dark_priest2_10`** [Miri](../monsters/dds_miri.md): “You're no priest!”

    - “Miri! How did you get here?” → [dds_dark_priest2_20](#d-dds_dark_priest2-dds_dark_priest2_20)

    <span id="d-dds_dark_priest2-dds_dark_priest2_110"></span>**`dds_dark_priest2_110`** [Borvis](../monsters/dds_borvis.md): “You're no priest!”

    - “Borvis! At last!” → [dds_dark_priest2_120](#d-dds_dark_priest2-dds_dark_priest2_120)

    <span id="d-dds_dark_priest2-dds_dark_priest2_20"></span>**`dds_dark_priest2_20`** Dark priest: “I could not let you go alone.”

    - “You made me fight alone all the way here.” → [dds_dark_priest2_30](#d-dds_dark_priest2-dds_dark_priest2_30)

    <span id="d-dds_dark_priest2-dds_dark_priest2_120"></span>**`dds_dark_priest2_120`** Dark priest: “My legs are not as young as yours anymore.”

    - “You made me fight alone all way here.” → [dds_dark_priest2_130](#d-dds_dark_priest2-dds_dark_priest2_130)

    <span id="d-dds_dark_priest2-dds_dark_priest2_30"></span>**`dds_dark_priest2_30`** Dark priest: “Don't worry - it's worth it.”

    - “But it's unfair to ...” → [dds_dark_priest2_40](#d-dds_dark_priest2-dds_dark_priest2_40)

    <span id="d-dds_dark_priest2-dds_dark_priest2_130"></span>**`dds_dark_priest2_130`** Dark priest: “Don't worry - it's worth it.”

    - “But it's unfair to ...” → [dds_dark_priest2_140](#d-dds_dark_priest2-dds_dark_priest2_140)

    <span id="d-dds_dark_priest2-dds_dark_priest2_40"></span>**`dds_dark_priest2_40`** [Dark priest](../monsters/dds_dark_priest.md#v-dds_dark_priest2): “Are we going to do this now, or are you two going to talk all day?” — **effects:** removes monsters from galmore_41, spawns monsters on galmore_41, sets stage 260 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-260)

    - “Ah, sorry: KAZAUL EST!” → [dds_dark_priest2_50](#d-dds_dark_priest2-dds_dark_priest2_50)

    <span id="d-dds_dark_priest2-dds_dark_priest2_140"></span>**`dds_dark_priest2_140`** [Dark priest](../monsters/dds_dark_priest.md#v-dds_dark_priest2): “Are we going to do this now, or are you two going to talk all day?” — **effects:** removes monsters from galmore_41, spawns monsters on galmore_41, sets stage 240 of [Shadows](../quests/shadows.md#stage-240)

    - “Ah, sorry: KAZAUL EST!” → [dds_dark_priest2_150](#d-dds_dark_priest2-dds_dark_priest2_150)

    <span id="d-dds_dark_priest2-dds_dark_priest2_50"></span>**`dds_dark_priest2_50`** [Miri](../monsters/dds_miri.md): “That's its true form! A monster masquerading as a priest! Attack!”


    <span id="d-dds_dark_priest2-dds_dark_priest2_150"></span>**`dds_dark_priest2_150`** [Borvis](../monsters/dds_borvis.md): “That's its true form! A monster masquerading as a priest! Attack!”




### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 13 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (dds_dark_priest2)"

    | | |
    |---|---|
    | Entry ID | `dds_dark_priest2` |
    | Spawn group | `dds_dark_priest2` |
    | Loot table | – |
    | Conversation | `dds_dark_priest2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_liches:3` |
    | Defined in | `res/raw/monsterlist_darknessanddaylight.json` |

    Raw data:

    ```json
    {
     "id": "dds_dark_priest2",
     "name": "Dark priest",
     "iconID": "monsters_liches:3",
     "moveCost": 5,
     "monsterClass": "humanoid",
     "spawnGroup": "dds_dark_priest2",
     "phraseID": "dds_dark_priest2"
    }
    ```


## Galmore 41 (dds_dark_priest_monster) { #v-dds_dark_priest_monster }

**Entry ID:** `dds_dark_priest_monster` · **Type:** Enemy

**Location:** [galmore_41](../maps/galmore_41.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Demon |
| HP | 330 |
| XP when defeated | 1,128 |
| Damage | 18 to 30 |
| Attack chance | 301 |
| Block chance | 138 |
| Damage resistance | 5 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 40 |
| Critical multiplier | 2.0 |
| Critical hit chance | 23% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**When hit:** On target: Cinder rage (magnitude 2, 2 rounds, 100% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Judicar](../items/judicar.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [galmore_41](../maps/galmore_41.md) | – | 1 | Appears later, during a quest |

### Quests that count defeats

- [Shadows](../quests/shadows.md#stage-250) with [Borvis](../monsters/dds_borvis.md) ([galmore_41](../maps/galmore_41.md)) checks that this enemy has been defeated.
- [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-270) with [Miri](../monsters/dds_miri.md) ([galmore_41](../maps/galmore_41.md)) checks that this enemy has been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (dds_dark_priest_monster)"

    | | |
    |---|---|
    | Entry ID | `dds_dark_priest_monster` |
    | Spawn group | `dds_dark_priest_monster` |
    | Loot table | `dds_dark_priest_monster_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_3:4` |
    | Defined in | `res/raw/monsterlist_darknessanddaylight.json` |

    Raw data:

    ```json
    {
     "id": "dds_dark_priest_monster",
     "name": "Dark priest",
     "iconID": "monsters_newb_3:4",
     "maxHP": 330,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "demon",
     "attackDamage": {
      "min": 18,
      "max": 30
     },
     "spawnGroup": "dds_dark_priest_monster",
     "droplistID": "dds_dark_priest_monster_dl",
     "attackCost": 5,
     "attackChance": 301,
     "criticalSkill": 40,
     "criticalMultiplier": 2.0,
     "blockChance": 138,
     "damageResistance": 5,
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "cinder_rage",
        "magnitude": 2,
        "duration": 2,
        "chance": "100"
       }
      ]
     }
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_dark_priest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_dark_priest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_dark_priest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_dark_priest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
