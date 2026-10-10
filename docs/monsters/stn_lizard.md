---
description: "Lizard is an enemy in Andor's Trail (reptile) with 50–100 HP, worth 118–190 XP, found in Flagstone Prison."
---

# ![](../assets/icons/monsters/monsters_tometik2_12.png){ .sprite } Lizard

**Where to find Lizard:** [Flagstone Prison, Flagstone 0 and 6 more](#v-stn_lizard), [Flagstone Prison, Waytogalmore 0](#v-stn_colonel_mons1)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik2_12.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Flagstone Prison |
| **Class** | Reptile, Humanoid |
| **HP** | 50–100 |
| **XP when defeated** | 118–190 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Flagstone Prison, Flagstone 0 and 6 more { #v-stn_lizard }

**Where:** Flagstone Prison: [Flagstone 0](../maps/flagstone0.md), Flagstone Prison: [Flagstone filler east 1](../maps/flagstone_filler_east_1.md), Flagstone Prison: [Flagstone filler east 2](../maps/flagstone_filler_east_2.md), Flagstone Prison: [Lake shore road 0](../maps/lake_shore_road_0.md), Flagstone Prison: [Lake shore road 2](../maps/lake_shore_road_2.md), Flagstone Prison: [Lake shore road 5](../maps/lake_shore_road_5.md) (+1 more)

### Combat

| | |
|---|---|
| Class | Reptile |
| HP | 50 |
| XP when defeated | 118 |
| Damage | 4 to 7 |
| AC | 40 |
| BC | 120 |
| DR | 5 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Flagstone 0](../maps/flagstone0.md) | Flagstone Prison | 5 | Appears later, during a quest |
| [Flagstone filler east 1](../maps/flagstone_filler_east_1.md) | Flagstone Prison | 3 | – |
| [Flagstone filler east 2](../maps/flagstone_filler_east_2.md) | Flagstone Prison | 4 | – |
| [Lake shore road 0](../maps/lake_shore_road_0.md) | Flagstone Prison | 2 | – |
| [Lake shore road 2](../maps/lake_shore_road_2.md) | Flagstone Prison | 5 | – |
| [Lake shore road 5](../maps/lake_shore_road_5.md) | Flagstone Prison | 1 | – |
| [Waytogalmore 0](../maps/waytogalmore0.md) | Flagstone Prison | 5 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Flagstone Prison, Waytogalmore 0 { #v-stn_colonel_mons1 }

**Where:** Flagstone Prison: [Waytogalmore 0](../maps/waytogalmore0.md)

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 100 |
| XP when defeated | 190 |
| Damage | 1 to 4 |
| AC | 40 |
| BC | 120 |
| DR | 5 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Waytogalmore 0](../maps/waytogalmore0.md) | Flagstone Prison | 1 | Appears later, during a quest |

### Quests that count defeats

- [Colonel Lutarc](../quests/stn_colonel.md#stage-112) with stepping on a trigger on [Waytogalmore 0](../maps/waytogalmore0.md) checks that this enemy has been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Lizard. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: location, combat statistics.

| Entry | Type | Section |
|---|---|---|
| `stn_lizard` | Enemy | [Flagstone Prison, Flagstone 0 and 6 more](#v-stn_lizard) |
| `stn_colonel_mons1` | Enemy | [Flagstone Prison, Waytogalmore 0](#v-stn_colonel_mons1) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: stn_lizard"

    | | |
    |---|---|
    | Entry ID | `stn_lizard` |
    | Type (wiki) | Enemy |
    | Spawn group | `stn_lizard` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_tometik2:12` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_lizard",
     "name": "Lizard",
     "iconID": "monsters_tometik2:12",
     "maxHP": 50,
     "maxAP": 10,
     "moveCost": 3,
     "unique": 1,
     "monsterClass": "reptile",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 4,
      "max": 7
     },
     "attackCost": 4,
     "attackChance": 40,
     "blockChance": 120,
     "damageResistance": 5
    }
    ```

??? info "Technical information: stn_colonel_mons1"

    | | |
    |---|---|
    | Entry ID | `stn_colonel_mons1` |
    | Type (wiki) | Enemy |
    | Spawn group | `stn_colonel_mons1` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_tometik2:12` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stn_colonel_mons1",
     "name": "Lizard",
     "iconID": "monsters_tometik2:12",
     "maxHP": 100,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 1,
      "max": 4
     },
     "attackCost": 4,
     "attackChance": 40,
     "blockChance": 120,
     "damageResistance": 5
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_lizard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_lizard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_lizard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_lizard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
