---
description: "Forgotten miner is an enemy in Andor's Trail (ghost) with 228 HP, worth 621 XP, found in undertell_05, undertell_13, undertell_14. Drops: Gold coins, Undertell diamond, Raw sapphire, Vein ruby."
---

# ![](../assets/icons/monsters/monsters_misc_4.png){ .sprite } Forgotten miner

**Found in:** [undertell_05](../maps/undertell_05.md), [undertell_13](../maps/undertell_13.md), [undertell_14](../maps/undertell_14.md), [undertell_15](../maps/undertell_15.md) (+9 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_misc_4.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | undertell_05, undertell_13, undertell_14 |
| **Class** | Ghost |
| **HP** | 228 |
| **XP when defeated** | 621 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `forgotten_miner` |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Ghost |
| HP | 228 |
| XP when defeated | 621 |
| Damage | 8 to 14 |
| Attack chance | 170 |
| Block chance | 166 |
| Damage resistance | 5 |
| Max AP | 12 |
| Attack cost | 4 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 20 |
| Critical multiplier | 2.0 |
| Critical hit chance | 15% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

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
| [undertell_05](../maps/undertell_05.md) | – | 2 | – |
| [undertell_13](../maps/undertell_13.md) | – | 7 | – |
| [undertell_14](../maps/undertell_14.md) | – | 4 | – |
| [undertell_15](../maps/undertell_15.md) | – | 4 | – |
| [undertell_23](../maps/undertell_23.md) | – | 3 | – |
| [undertell_24](../maps/undertell_24.md) | – | 2 | – |
| [undertell_3_00](../maps/undertell_3_00.md) | – | 3 | Appears later, during a quest |
| [undertell_3_01](../maps/undertell_3_01.md) | – | 1 | Appears later, during a quest |
| [undertell_3_02](../maps/undertell_3_02.md) | – | 7 | Appears later, during a quest |
| [undertell_3_03](../maps/undertell_3_03.md) | – | 2 | Appears later, during a quest |
| [undertell_3_11](../maps/undertell_3_11.md) | – | 4 | Appears later, during a quest |
| [undertell_3_12](../maps/undertell_3_12.md) | – | 3 | Appears later, during a quest |
| [undertell_3_13](../maps/undertell_3_13.md) | – | 4 | Appears later, during a quest |


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `forgotten_miner` |
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


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


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
