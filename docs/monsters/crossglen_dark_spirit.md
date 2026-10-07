---
description: "Dark spirit is an NPC who can also be fought in Andor's Trail, found in Crossglen, galmore_32."
---

# ![](../assets/icons/monsters/monsters_newb_1_686.png){ .sprite } Dark spirit

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_686.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Crossglen, galmore_32 |
| **Class** | Demon |
| **HP** | 470–509 |
| **XP when defeated** | 851–999 |
| **Immune to critical hits** | Yes |
| **Entries in game data** | 2 |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Dark spirit. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location, combat statistics, loot or shop stock, movement. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`crossglen_dark_spirit`](#v-crossglen_dark_spirit) | Enemy | Crossglen: [crossglen_farmhouse](../maps/crossglen_farmhouse.md) | – | 470 |
| [`undertell_dark_spirit`](#v-undertell_dark_spirit) | NPC/Enemy | [galmore_32](../maps/galmore_32.md#pin-npc-undertell_dark_spirit) | – | 509 |

## Crossglen, Crossglen farmhouse (crossglen_dark_spirit) { #v-crossglen_dark_spirit }

**Entry ID:** `crossglen_dark_spirit` · **Type:** Enemy

**Location:** Crossglen: [crossglen_farmhouse](../maps/crossglen_farmhouse.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Demon |
| HP | 470 |
| XP when defeated | 851 |
| Damage | 7 to 10 |
| Attack chance | 135 |
| Block chance | 130 |
| Damage resistance | 3 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 2 AP |
| Critical skill | 2 |
| Critical multiplier | 2.0 |
| Critical hit chance | 1% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**On hit:** Heal HP: 1 to 3

**When hit:** Heal HP: 3 to 6


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Tonic of blood](../items/tonic_of_blood.md) | 100% | 3 to 4 |
| [Gold coins](../items/gold.md) | 100% | 65 to 100 |
| [Spiritbane potion](../items/spiritbane_potion.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [crossglen_farmhouse](../maps/crossglen_farmhouse.md) | Crossglen | 1 | Appears later, during a quest |

### Quests that count defeats

- [A familiar shadow](../quests/familiar_shadow.md#stage-50) with stepping on a trigger on [crossglen](../maps/crossglen.md) checks that this enemy has been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (crossglen_dark_spirit)"

    | | |
    |---|---|
    | Entry ID | `crossglen_dark_spirit` |
    | Spawn group | `crossglen_dark_spirit` |
    | Loot table | `crossglen_dark_spirit_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_newb_1:686` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "crossglen_dark_spirit",
     "name": "Dark spirit",
     "iconID": "monsters_newb_1:686",
     "maxHP": 470,
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "demon",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 7,
      "max": 10
     },
     "droplistID": "crossglen_dark_spirit_dl",
     "attackCost": 3,
     "attackChance": 135,
     "criticalSkill": 2,
     "criticalMultiplier": 2.0,
     "blockChance": 130,
     "damageResistance": 3,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 3
      }
     },
     "hitReceivedEffect": {
      "increaseCurrentHP": {
       "min": 3,
       "max": 6
      }
     }
    }
    ```


## Galmore 32 (undertell_dark_spirit) { #v-undertell_dark_spirit }

**Entry ID:** `undertell_dark_spirit` · **Type:** NPC/Enemy

**Location:** [galmore_32](../maps/galmore_32.md#pin-npc-undertell_dark_spirit)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Demon |
| HP | 509 |
| XP when defeated | 999 |
| Damage | 9 to 10 |
| Attack chance | 155 |
| Block chance | 142 |
| Damage resistance | 6 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 3 AP |
| Critical skill | 3 |
| Critical multiplier | 2.0 |
| Critical hit chance | 2% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**On hit:** Heal HP: 2 to 4

**When hit:** Heal HP: 5 to 8


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 75 to 110 |
| [Tonic of blood](../items/tonic_of_blood.md) | 100% | 4 to 8 |
| [Elytharan gloves](../items/elytharan_gloves.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [galmore_32](../maps/galmore_32.md) | – | 1 | Appears later, during a quest |

### Quests that count defeats

- A conversation with stepping on a trigger on [galmore_32](../maps/galmore_32.md) checks that this enemy has been defeated.

### Quests

- [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md): stage 4

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Dark spirit. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/galmore_dark_spirit_selector.json" data-npc="Dark spirit" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-undertell_dark_spirit-galmore_dark_spirit_selector"></span>**`galmore_dark_spirit_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 4 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-4))* → *fight starts*
    - branch 2 → [galmore_dark_spirit_10](#d-undertell_dark_spirit-galmore_dark_spirit_10)

    <span id="d-undertell_dark_spirit-galmore_dark_spirit_10"></span>**`galmore_dark_spirit_10`** Dark spirit: “Destroy me? Foolish mortal! I am older than your bloodline, stronger than your resolve. You will break, just like the others. Their despair feeds me, and yours will be no different!”

    - Next → [galmore_dark_spirit_11](#d-undertell_dark_spirit-galmore_dark_spirit_11)

    <span id="d-undertell_dark_spirit-galmore_dark_spirit_11"></span>**`galmore_dark_spirit_11`** [Dummy NPC](../monsters/none.md): “The spirit swirls with dark energy, causing the ground to tremble as it prepares to attack.”

    - Next → [galmore_dark_spirit_20](#d-undertell_dark_spirit-galmore_dark_spirit_20)

    <span id="d-undertell_dark_spirit-galmore_dark_spirit_20"></span>**`galmore_dark_spirit_20`** [Dark spirit](../monsters/crossglen_dark_spirit.md#v-undertell_dark_spirit): “Let me show you what true suffering feels like. You will know despair, and your name will be forgotten in the darkness of my power!” — **effects:** spawns monsters on galmore_32, sets stage 4 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-4)

    - “Let me show you the darkness of my power!” → *fight starts*



### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (undertell_dark_spirit)"

    | | |
    |---|---|
    | Entry ID | `undertell_dark_spirit` |
    | Spawn group | `undertell_dark_spirit` |
    | Loot table | `undertell_dark_spirit_dl` |
    | Conversation | `galmore_dark_spirit_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_1:686` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "undertell_dark_spirit",
     "name": "Dark spirit",
     "iconID": "monsters_newb_1:686",
     "maxHP": 509,
     "moveCost": 3,
     "unique": 1,
     "monsterClass": "demon",
     "attackDamage": {
      "min": 9,
      "max": 10
     },
     "phraseID": "galmore_dark_spirit_selector",
     "droplistID": "undertell_dark_spirit_dl",
     "attackCost": 3,
     "attackChance": 155,
     "criticalSkill": 3,
     "criticalMultiplier": 2.0,
     "blockChance": 142,
     "damageResistance": 6,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 2,
       "max": 4
      }
     },
     "hitReceivedEffect": {
      "increaseCurrentHP": {
       "min": 5,
       "max": 8
      }
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossglen_dark_spirit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossglen_dark_spirit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossglen_dark_spirit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossglen_dark_spirit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
