---
description: "Snake master is an NPC you can also fight in Andor's Trail, found in Snakecave 3."
---

# ![](../assets/icons/monsters/monsters_liches_1.png){ .sprite } Snake master

**Where to find Snake master:** [Snakecave 3](../maps/snakecave3.md#pin-npc-snake_master)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_liches_1.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Snakecave 3 |
| **Class** | Undead |
| **HP** | 55 |
| **XP when defeated** | 112 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "You can fight Snake master"
    Answering “Great, I have been waiting for a fight!” starts a fight with Snake master.

## Combat

| | |
|---|---|
| Class | Undead |
| HP | 55 |
| XP when defeated | 112 |
| Damage | 1 to 4 |
| AC | 60 |
| BC | 10 |
| DR | 4 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 58% (×3.0) |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 9 |
| [Venomous Dagger](../items/dagger_venom.md) | 100% | 1 |
| [Polished gem](../items/gem3.md) | 100% | 1 |
| [Regular potion of health](../items/health.md) | 100% | 1 |
| [Ewmondold's map](../items/inspiring_snake_master_map.md) | 100% | 1 |

## Quests that count defeats

- [Perception is not reality](../quests/new_snake_master.md#stage-10) with [Ewmondold](../monsters/ewmondold_snake_master.md#v-inspiring_snake_master) ([Wild 2](../maps/wild2.md)) checks that this enemy has been defeated.
- [Perception is not reality](../quests/new_snake_master.md#stage-20) with [Ewmondold](../monsters/ewmondold_snake_master.md#v-inspiring_snake_master) ([Wild 2](../maps/wild2.md)) checks that this enemy has been defeated.

## Dialogue simulator

Set your quest stages and items, then talk to Snake master. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/snakemaster.json" data-npc="Snake master" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-snakemaster"></span>**`snakemaster`** Snake master: “Well well, what have we here? A visitor, how nice. I'm impressed you got this far through all my minions. Now prepare to die, puny creature.”

    - “Great, I have been waiting for a fight!” → *fight starts*
    - “Let's see who dies here.” → *fight starts*
    - “Please don't hurt me!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect) |

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
    | Entry ID | `snake_master` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `cavesnake3_boss` |
    | Loot table | `snakemaster` |
    | Conversation | `snakemaster` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_liches:1` |
    | Defined in | `res/raw/monsterlist_crossglen_animals.json` |

    Raw data:

    ```json
    {
     "id": "snake_master",
     "name": "Snake master",
     "iconID": "monsters_liches:1",
     "maxHP": 55,
     "unique": 1,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 1,
      "max": 4
     },
     "spawnGroup": "cavesnake3_boss",
     "phraseID": "snakemaster",
     "droplistID": "snakemaster",
     "attackCost": 5,
     "attackChance": 60,
     "criticalSkill": 200,
     "criticalMultiplier": 3.0,
     "blockChance": 10,
     "damageResistance": 4
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=snake_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=snake_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=snake_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=snake_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
