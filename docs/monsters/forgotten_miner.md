---
description: "Forgotten miner is an enemy in Andor's Trail (ghost) with 228 HP, worth 621 XP, found in Undertell 05, Undertell 13, Undertell 14. Drops: Gold coins, Undertell diamond, Raw sapphire, Vein ruby."
---

# ![](../assets/icons/monsters/monsters_misc_4.png){ .sprite } Forgotten miner

**Found in:** [Undertell 05](../maps/undertell_05.md), [Undertell 13](../maps/undertell_13.md), [Undertell 14](../maps/undertell_14.md), [Undertell 15](../maps/undertell_15.md) (+9 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_misc_4.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Undertell 05, Undertell 13, Undertell 14 |
| **Class** | Ghost |
| **HP** | 228 |
| **XP when defeated** | 621 |
| **Immune to crits** | Yes |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Combat

| | |
|---|---|
| Class | Ghost |
| HP | 228 |
| XP when defeated | 621 |
| Damage | 8 to 14 |
| AC | 170 |
| BC | 166 |
| DR | 5 |
| Attacks per turn | 3 (4 AP each, 12 AP) |
| Crit chance | 15% (×2.0) |

**Immune to critical hits.**


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 25% | 5 to 25 |
| [Undertell diamond](../items/undertell_diamond.md) | 1% | 1 |
| [Raw sapphire](../items/raw_sapphire.md) | 1% | 1 |
| [Vein ruby](../items/vein_ruby.md) | 1% | 1 |
| [Amethyst](../items/amethyst.md) | 1% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Undertell 05](../maps/undertell_05.md) | – | 2 | – |
| [Undertell 13](../maps/undertell_13.md) | – | 7 | – |
| [Undertell 14](../maps/undertell_14.md) | – | 4 | – |
| [Undertell 15](../maps/undertell_15.md) | – | 4 | – |
| [Undertell 23](../maps/undertell_23.md) | – | 3 | – |
| [Undertell 24](../maps/undertell_24.md) | – | 2 | – |
| [Undertell 3 00](../maps/undertell_3_00.md) | – | 3 | Appears later, during a quest |
| [Undertell 3 01](../maps/undertell_3_01.md) | – | 1 | Appears later, during a quest |
| [Undertell 3 02](../maps/undertell_3_02.md) | – | 7 | Appears later, during a quest |
| [Undertell 3 03](../maps/undertell_3_03.md) | – | 2 | Appears later, during a quest |
| [Undertell 3 11](../maps/undertell_3_11.md) | – | 4 | Appears later, during a quest |
| [Undertell 3 12](../maps/undertell_3_12.md) | – | 3 | Appears later, during a quest |
| [Undertell 3 13](../maps/undertell_3_13.md) | – | 4 | Appears later, during a quest |


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

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
    | Entry ID | `forgotten_miner` |
    | Type (wiki) | Enemy |
    | Spawn group | `forgotten_miner` |
    | Loot table | `forgotten_miner_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_misc:4` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "forgotten_miner",
     "name": "Forgotten miner",
     "iconID": "monsters_misc:4",
     "maxHP": 228,
     "maxAP": 12,
     "moveCost": 5,
     "monsterClass": "ghost",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 8,
      "max": 14
     },
     "droplistID": "forgotten_miner_dl",
     "attackCost": 4,
     "attackChance": 170,
     "criticalSkill": 20,
     "criticalMultiplier": 2.0,
     "blockChance": 166,
     "damageResistance": 5
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forgotten_miner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forgotten_miner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forgotten_miner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forgotten_miner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
