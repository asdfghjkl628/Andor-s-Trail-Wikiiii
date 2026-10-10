---
description: "Maonit troll is an enemy in Andor's Trail (giant) with 255 HP, worth 259 XP, found in Lake Laeroth. Drops: Gold coins, Meat, Animal hair, Crude ring of block."
---

# ![](../assets/icons/monsters/monsters_rltiles1_104.png){ .sprite } Maonit troll

**Found in:** Lake Laeroth: [Mountainlake 1](../maps/mountainlake1.md), Lake Laeroth: [Mountainlake 2](../maps/mountainlake2.md), [Mountainlake 0](../maps/mountainlake0.md), [Mountainlake 4](../maps/mountainlake4.md) (+3 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_104.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Lake Laeroth |
| **Class** | Giant |
| **HP** | 255 |
| **XP when defeated** | 259 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Giant |
| HP | 255 |
| XP when defeated | 259 |
| Damage | 1 to 20 |
| AC | 65 |
| BC | 20 |
| DR | 4 |
| Attacks per turn | 1 (4 AP each, 5 AP) |
| Crit chance | 9% (×3.0) |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 1 to 7 |
| [Meat](../items/meat.md) | 5% | 1 |
| [Animal hair](../items/hair.md) | 10% | 1 |
| [Crude ring of block](../items/ring_crude_block.md) | 1% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Mountainlake 0](../maps/mountainlake0.md) | – | 2 | – |
| [Mountainlake 1](../maps/mountainlake1.md) | Lake Laeroth | 8 | – |
| [Mountainlake 2](../maps/mountainlake2.md) | Lake Laeroth | 5 | – |
| [Mountainlake 4](../maps/mountainlake4.md) | – | 2 | – |
| [Waytolake 10](../maps/waytolake10.md) | – | 9 | – |
| [Waytolake 11](../maps/waytolake11.md) | – | 5 | – |
| [Waytolake 9](../maps/waytolake9.md) | – | 6 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect) |
| [v0.7.4](../versions/0.7.4.md) | Attack cost: 5 → 4 |

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
    | Entry ID | `maonit_1` |
    | Type (wiki) | Enemy |
    | Spawn group | `maonit_1` |
    | Loot table | `maonit` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:104` |
    | Defined in | `res/raw/monsterlist_v0611_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "maonit_1",
     "name": "Maonit troll",
     "iconID": "monsters_rltiles1:104",
     "maxHP": 255,
     "maxAP": 5,
     "moveCost": 5,
     "monsterClass": "giant",
     "attackDamage": {
      "min": 1,
      "max": 20
     },
     "spawnGroup": "maonit_1",
     "droplistID": "maonit",
     "attackCost": 4,
     "attackChance": 65,
     "criticalSkill": 10,
     "criticalMultiplier": 3.0,
     "blockChance": 20,
     "damageResistance": 4
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=maonit_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=maonit_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=maonit_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=maonit_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
