---
description: "Preabola fly is an enemy in Andor's Trail (insect) with 109 HP, worth 405 XP, found in Sullengard. Drops: Insect wing, Insect stinger."
---

# ![](../assets/icons/monsters/monsters_rltiles2_170.png){ .sprite } Preabola fly

**Found in:** Sullengard: [sullengard_pond](../maps/sullengard_pond.md), [aidem_camp](../maps/aidem_camp.md), [sullengard10](../maps/sullengard10.md), [sullengard_pond_east](../maps/sullengard_pond_east.md) (+11 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_170.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Sullengard |
| **Class** | Insect |
| **HP** | 109 |
| **XP when defeated** | 405 |
| **Entry ID** | `preabola_fly` |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Insect |
| HP | 109 |
| XP when defeated | 405 |
| Damage | 9 to 11 |
| Attack chance | 170 |
| Block chance | 205 |
| Damage resistance | 8 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 3 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**On hit:** On target: Minor sting (magnitude 5, 5 rounds, 25% chance); Vulnerability (magnitude 5, 3 rounds, 10% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Insect wing](../items/insectwing.md) | 10% | 1 |
| [Insect stinger](../items/insect_stinger.md) | 10% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [aidem_camp](../maps/aidem_camp.md) | – | 2 | – |
| [sullengard10](../maps/sullengard10.md) | – | 2 | – |
| [sullengard_pond](../maps/sullengard_pond.md) | Sullengard | 7 | – |
| [sullengard_pond_east](../maps/sullengard_pond_east.md) | – | 4 | – |
| [sullengard_woods5](../maps/sullengard_woods5.md) | – | 4 | – |
| [sullengard_woods6](../maps/sullengard_woods6.md) | – | 15 | – |
| [sullengard_woods7](../maps/sullengard_woods7.md) | – | 6 | – |
| [sullengard_woods8](../maps/sullengard_woods8.md) | – | 7 | – |
| [sullengard_woods9](../maps/sullengard_woods9.md) | – | 4 | – |
| [way_to_aidem_camp_1](../maps/way_to_aidem_camp_1.md) | – | 7 | – |
| [way_to_sullengard_east10](../maps/way_to_sullengard_east10.md) | – | 3 | – |
| [way_to_sullengard_east11](../maps/way_to_sullengard_east11.md) | – | 7 | – |
| [way_to_sullengard_east8](../maps/way_to_sullengard_east8.md) | – | 6 | – |
| [way_to_sullengard_east9](../maps/way_to_sullengard_east9.md) | – | 5 | – |
| [way_to_sullengard_east9a](../maps/way_to_sullengard_east9a.md) | – | 5 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `preabola_fly` |
    | Spawn group | `preabola_fly` |
    | Loot table | `flying_insect_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_rltiles2:170` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "preabola_fly",
     "name": "Preabola fly",
     "iconID": "monsters_rltiles2:170",
     "maxHP": 109,
     "moveCost": 3,
     "monsterClass": "insect",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 9,
      "max": 11
     },
     "spawnGroup": "preabola_fly",
     "droplistID": "flying_insect_dl",
     "attackCost": 4,
     "attackChance": 170,
     "blockChance": 205,
     "damageResistance": 8,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "sting_minor",
        "magnitude": 5,
        "duration": 5,
        "chance": "25"
       },
       {
        "condition": "vulnerability",
        "magnitude": 5,
        "duration": 3,
        "chance": "10"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=preabola_fly.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=preabola_fly.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=preabola_fly.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=preabola_fly.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
