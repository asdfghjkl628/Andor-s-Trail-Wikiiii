---
description: "Dark spirit is an NPC you can also fight in Andor's Trail, found in Crossglen, Galmore 32."
---

# ![](../assets/icons/monsters/monsters_newb_1_686.png){ .sprite } Dark spirit

**Where to find Dark spirit:** [Crossglen, Crossglen farmhouse](#v-crossglen_dark_spirit), [Galmore 32](#v-undertell_dark_spirit)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_newb_1_686.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Crossglen, Galmore 32 |
| **Class** | Demon |
| **HP** | 470–509 |
| **XP when defeated** | 851–999 |
| **Immune to crits** | Yes |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Crossglen, Crossglen farmhouse { #v-crossglen_dark_spirit }

**Where:** Crossglen: [Crossglen farmhouse](../maps/crossglen_farmhouse.md)

### Combat

| | |
|---|---|
| Class | Demon |
| HP | 470 |
| XP when defeated | 851 |
| Damage | 7 to 10 |
| AC | 135 |
| BC | 130 |
| DR | 3 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 1% (×2.0) |

**Immune to critical hits.**

**Its hits:** Heal HP: 1 to 3

**When you hit it:** Heal HP: 3 to 6


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Tonic of blood](../items/tonic_of_blood.md) | 100% | 3 to 4 |
| [Gold coins](../items/gold.md) | 100% | 65 to 100 |
| [Spiritbane potion](../items/spiritbane_potion.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Crossglen farmhouse](../maps/crossglen_farmhouse.md) | Crossglen | 1 | Appears later, during a quest |

### Quests that count defeats

- [A familiar shadow](../quests/familiar_shadow.md#stage-50) with stepping on a trigger on [Crossglen](../maps/crossglen.md) checks that this enemy has been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Galmore 32 { #v-undertell_dark_spirit }

**Where:** [Galmore 32](../maps/galmore_32.md#pin-npc-undertell_dark_spirit)

!!! warning "You can fight Dark spirit"
    The conversation can lead straight into a fight with Dark spirit.

    Answering “Let me show you the darkness of my power!” during [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-4) starts a fight with Dark spirit.

### Combat

| | |
|---|---|
| Class | Demon |
| HP | 509 |
| XP when defeated | 999 |
| Damage | 9 to 10 |
| AC | 155 |
| BC | 142 |
| DR | 6 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 2% (×2.0) |

**Immune to critical hits.**

**Its hits:** Heal HP: 2 to 4

**When you hit it:** Heal HP: 5 to 8


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 75 to 110 |
| [Tonic of blood](../items/tonic_of_blood.md) | 100% | 4 to 8 |
| [Elytharan gloves](../items/elytharan_gloves.md) | 100% | 1 |

### Quests that count defeats

- A conversation with stepping on a trigger on [Galmore 32](../maps/galmore_32.md) checks that this enemy has been defeated.

### Quests

- [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md): stage 4

### Dialogue simulator

Talk to Dark spirit as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/galmore_dark_spirit_selector.json" data-npc="Dark spirit" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-undertell_dark_spirit-galmore_dark_spirit_selector"></span>**`galmore_dark_spirit_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 4 of [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-4))* → *fight starts*
    - branch 2 → [galmore_dark_spirit_10](#d-undertell_dark_spirit-galmore_dark_spirit_10)

    <span id="d-undertell_dark_spirit-galmore_dark_spirit_10"></span>**`galmore_dark_spirit_10`** Dark spirit: “Destroy me? Foolish mortal! I am older than your bloodline, stronger than your resolve. You will break, just like the others. Their despair feeds me, and yours will be no different!”

    - Next → [galmore_dark_spirit_11](#d-undertell_dark_spirit-galmore_dark_spirit_11)

    <span id="d-undertell_dark_spirit-galmore_dark_spirit_11"></span>**`galmore_dark_spirit_11`** [Dummy NPC](../monsters/none.md): “The spirit swirls with dark energy, causing the ground to tremble as it prepares to attack.”

    - Next → [galmore_dark_spirit_20](#d-undertell_dark_spirit-galmore_dark_spirit_20)

    <span id="d-undertell_dark_spirit-galmore_dark_spirit_20"></span>**`galmore_dark_spirit_20`** [Dark spirit](../monsters/crossglen_dark_spirit.md#v-undertell_dark_spirit): “Let me show you what true suffering feels like. You will know despair, and your name will be forgotten in the darkness of my power!” — **effects:** spawns monsters on galmore_32, sets stage 4 of [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-4)

    - “Let me show you the darkness of my power!” → *fight starts*



### Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Dark spirit. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location, combat statistics, loot or shop stock, movement.

| Entry | Type | Section |
|---|---|---|
| `crossglen_dark_spirit` | Enemy | [Crossglen, Crossglen farmhouse](#v-crossglen_dark_spirit) |
| `undertell_dark_spirit` | NPC/Enemy | [Galmore 32](#v-undertell_dark_spirit) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: crossglen_dark_spirit"

    | | |
    |---|---|
    | Entry ID | `crossglen_dark_spirit` |
    | Type (wiki) | Enemy |
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

??? info "Technical information: undertell_dark_spirit"

    | | |
    |---|---|
    | Entry ID | `undertell_dark_spirit` |
    | Type (wiki) | NPC/Enemy |
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
