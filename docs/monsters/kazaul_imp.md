---
description: "Kazaul imp is an enemy in Andor's Trail (demon) with 45 HP, worth 111 XP, found in Blackwater mountain 42. Drops: Gold coins, Polished sparkling gem, Regular potion of health, Small rock."
---

# ![](../assets/icons/monsters/monsters_rltiles1_45.png){ .sprite } Kazaul imp

**Found in:** [Blackwater mountain 42](../maps/blackwater_mountain42.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_45.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Blackwater mountain 42 |
| **Class** | Demon |
| **HP** | 45 |
| **XP when defeated** | 111 |
| **Immune to crits** | Yes |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Demon |
| HP | 45 |
| XP when defeated | 111 |
| Damage | 3 to 7 |
| AC | 70 |
| BC | 105 |
| DR | 1 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 23% (×2.0) |

**Immune to critical hits.**


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 6 to 25 |
| [Polished sparkling gem](../items/gem5.md) | 10% | 1 |
| [Regular potion of health](../items/health.md) | 10% | 1 |
| [Small rock](../items/rock.md) | 5% | 1 |
| [Rapier of lifesteal](../items/rapier_lifesteal.md) | 0.01% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Blackwater mountain 42](../maps/blackwater_mountain42.md) | – | 8 | – |


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
    | Entry ID | `kazaul_imp` |
    | Type (wiki) | Enemy |
    | Spawn group | `kazaul_2` |
    | Loot table | `kazaul_2` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:45` |
    | Defined in | `res/raw/monsterlist_v069_monsters.json` |

    Raw data:

    ```json
    {
     "id": "kazaul_imp",
     "name": "Kazaul imp",
     "iconID": "monsters_rltiles1:45",
     "maxHP": 45,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "demon",
     "attackDamage": {
      "min": 3,
      "max": 7
     },
     "spawnGroup": "kazaul_2",
     "droplistID": "kazaul_2",
     "attackCost": 3,
     "attackChance": 70,
     "criticalSkill": 40,
     "criticalMultiplier": 2.0,
     "blockChance": 105,
     "damageResistance": 1
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_imp.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_imp.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_imp.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_imp.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
