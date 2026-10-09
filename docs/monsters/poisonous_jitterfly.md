---
description: "Poisonous jitterfly is an enemy in Andor's Trail (insect) with 97 HP, worth 316 XP, found in Deebo's Orchard. Drops: Insect wing, Insect stinger."
---

# ![](../assets/icons/monsters/monsters_rltiles2_65.png){ .sprite } Poisonous jitterfly

**Found in:** Deebo's Orchard: [Way to sullengard east 6](../maps/way_to_sullengard_east6.md), Deebo's Orchard: [Way to sullengard east 7](../maps/way_to_sullengard_east7.md), Deebo's Orchard: [Way to sullengard east 7a](../maps/way_to_sullengard_east7a.md), [Way to sullengard east 1](../maps/way_to_sullengard_east1.md) (+11 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_65.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Deebo's Orchard |
| **Class** | Insect |
| **HP** | 97 |
| **XP when defeated** | 316 |
| **Entry ID** | `poisonous_jitterfly` |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Insect |
| HP | 97 |
| XP when defeated | 316 |
| Damage | 6 to 8 |
| Attack chance | 118 |
| Block chance | 215 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 4 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**On hit:** On target: [Weak Poison](../conditions/poison_weak.md) (magnitude 5, 5 rounds, 70% chance); [Minor sting](../conditions/sting_minor.md) (magnitude 3, 3 rounds, 35% chance); [Insect contagion](../conditions/contagion.md) (magnitude 2, 3 rounds, 25% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Insect wing](../items/insectwing.md) | 10% | 1 |
| [Insect stinger](../items/insect_stinger.md) | 10% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Way to sullengard east 1](../maps/way_to_sullengard_east1.md) | – | 2 | – |
| [Way to sullengard east 10](../maps/way_to_sullengard_east10.md) | – | 6 | – |
| [Way to sullengard east 11](../maps/way_to_sullengard_east11.md) | – | 4 | – |
| [Way to sullengard east 2](../maps/way_to_sullengard_east2.md) | – | 2 | – |
| [Way to sullengard east 2a](../maps/way_to_sullengard_east2a.md) | – | 1 | – |
| [Way to sullengard east 4](../maps/way_to_sullengard_east4.md) | – | 3 | – |
| [Way to sullengard east 5](../maps/way_to_sullengard_east5.md) | – | 6 | – |
| [Way to sullengard east 6](../maps/way_to_sullengard_east6.md) | Deebo's Orchard | 11 | – |
| [Way to sullengard east 7](../maps/way_to_sullengard_east7.md) | Deebo's Orchard | 6 | – |
| [Way to sullengard east 7a](../maps/way_to_sullengard_east7a.md) | Deebo's Orchard | 6 | – |
| [Way to sullengard east 9](../maps/way_to_sullengard_east9.md) | – | 4 | – |
| [Way to sullengard east 9a](../maps/way_to_sullengard_east9a.md) | – | 5 | – |
| [Way to sullengard east ravine cabin](../maps/way_to_sullengard_east_ravine_cabin.md) | – | 10 | – |
| [Way to sullengard pond road](../maps/way_to_sullengard_pond_road.md) | – | 6 | – |
| [Way to sullengard west 6](../maps/way_to_sullengard_west_6.md) | – | 3 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `poisonous_jitterfly` |
    | Spawn group | `poisonous_jitterfly` |
    | Loot table | `flying_insect_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_rltiles2:65` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "poisonous_jitterfly",
     "name": "Poisonous jitterfly",
     "iconID": "monsters_rltiles2:65",
     "maxHP": 97,
     "moveCost": 4,
     "monsterClass": "insect",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 6,
      "max": 8
     },
     "spawnGroup": "poisonous_jitterfly",
     "droplistID": "flying_insect_dl",
     "attackCost": 3,
     "attackChance": 118,
     "blockChance": 215,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "poison_weak",
        "magnitude": 5,
        "duration": 5,
        "chance": "70"
       },
       {
        "condition": "sting_minor",
        "magnitude": 3,
        "duration": 3,
        "chance": "35"
       },
       {
        "condition": "contagion",
        "magnitude": 2,
        "duration": 3,
        "chance": "25"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=poisonous_jitterfly.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=poisonous_jitterfly.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=poisonous_jitterfly.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=poisonous_jitterfly.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
