---
description: "Erwyn's knight is an NPC you can also fight in Andor's Trail, found in Flagstone Prison."
---

# ![](../assets/icons/monsters/monsters_tometik8_41.png){ .sprite } Erwyn's knight

**Where to find Erwyn's knight:** Flagstone Prison: [Stoutford castle 0](../maps/stoutford_castle0.md#pin-npc-erwyn_knight), Flagstone Prison: [Waytogalmore 0](../maps/waytogalmore0.md#pin-npc-erwyn_knight), Flagstone Prison: [Waytogalmore 1](../maps/waytogalmore1.md#pin-npc-erwyn_knight), [Stoutford castle 1](../maps/stoutford_castle1.md#pin-npc-erwyn_knight)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_tometik8_41.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Flagstone Prison |
| **Class** | Undead |
| **HP** | 75 |
| **XP when defeated** | 121 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

!!! warning "You can fight Erwyn's knight"
    Answering “No thank you. Maybe another time.” starts a fight with Erwyn's knight.

## Combat

| | |
|---|---|
| Class | Undead |
| HP | 75 |
| XP when defeated | 121 |
| Damage | 4 to 6 |
| AC | 100 |
| BC | 70 |
| DR | 0 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Stoutford castle 0](../maps/stoutford_castle0.md) | Flagstone Prison | 3 | – |
| [Stoutford castle 1](../maps/stoutford_castle1.md) | – | 1 | – |
| [Waytogalmore 0](../maps/waytogalmore0.md) | Flagstone Prison | 1 | – |
| [Waytogalmore 1](../maps/waytogalmore1.md) | Flagstone Prison | 2 | – |

## Quests that count defeats

- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-46) with stepping on a trigger on [Waytogalmore 0](../maps/waytogalmore0.md), stepping on a trigger on [Wild 18](../maps/wild18.md) checks that at least 7 of these enemies have been defeated.
- A conversation with [Colonel Lutarc](../monsters/stn_colonel.md) ([Waytogalmore 0](../maps/waytogalmore0.md)), stepping on a trigger on [Waytogalmore 0](../maps/waytogalmore0.md) checks that this enemy has been defeated.

## Dialogue simulator

Talk to Erwyn's knight as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/stoutford_castle_0.json" data-npc="Erwyn&#x27;s knight" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-stoutford_castle_0"></span>**`stoutford_castle_0`** Erwyn's knight: “Ah another mortal! You shall be another servant in Lord Erwyn's army! Ha Ha!”

    - “No thank you. Maybe another time.” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `erwyn_knight` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `erwyn_knight` |
    | Loot table | – |
    | Conversation | `stoutford_castle_0` |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_tometik8:41` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "erwyn_knight",
     "name": "Erwyn's knight",
     "iconID": "monsters_tometik8:41",
     "maxHP": 75,
     "unique": 1,
     "monsterClass": "undead",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 4,
      "max": 6
     },
     "spawnGroup": "erwyn_knight",
     "phraseID": "stoutford_castle_0",
     "attackCost": 3,
     "attackChance": 100,
     "blockChance": 70
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_knight.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_knight.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_knight.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_knight.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
