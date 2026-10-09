---
description: "Wyrm trainer is an enemy in Andor's Trail (undead) with 69 HP, worth 199 XP, found in Blackwater Mountain. Drops: Gold coins, Bone, Small empty vial, Weak poison."
---

# ![](../assets/icons/monsters/monsters_rltiles2_0.png){ .sprite } Wyrm trainer

**Found in:** Blackwater Mountain: [Blackwater mountain 36](../maps/blackwater_mountain36.md), Blackwater Mountain: [Blackwater mountain 37](../maps/blackwater_mountain37.md), Blackwater Mountain: [Blackwater mountain 38](../maps/blackwater_mountain38.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Blackwater Mountain |
| **Class** | Undead |
| **HP** | 69 |
| **XP when defeated** | 199 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Undead |
| HP | 69 |
| XP when defeated | 199 |
| Damage | 2 to 9 |
| AC | 90 |
| BC | 90 |
| DR | 4 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** Heal HP: 1; On target: [Minor fatigue](../conditions/fatigue_minor.md) (magnitude 1, 10 rounds, 70% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 1 to 60 |
| [Bone](../items/bone.md) | 10% | 1 to 2 |
| [Small empty vial](../items/vial_empty1.md) | 25% | 1 |
| [Weak poison](../items/pot_poison_weak.md) | 5% | 1 to 3 |
| [Minor vial of health](../items/health_minor.md) | 10% | 1 to 2 |
| [Elytharan redeemer](../items/elytharan_redeemer.md) | 0.01% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Blackwater mountain 36](../maps/blackwater_mountain36.md) | Blackwater Mountain | 4 | – |
| [Blackwater mountain 37](../maps/blackwater_mountain37.md) | Blackwater Mountain | 3 | – |
| [Blackwater mountain 38](../maps/blackwater_mountain38.md) | Blackwater Mountain | 4 | – |

## Quests that count defeats

- A conversation with [General's henchman](../monsters/ortholion_guard1.md) ([Blackwater mountain 11](../maps/blackwater_mountain11.md)), [Feygard scout](../monsters/feygard_scout.md#v-ortholion_guard6) ([Blackwater mountain 10](../maps/blackwater_mountain10.md)) checks that this enemy has been defeated.


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Minor fatigue](../conditions/fatigue_minor.md) (magnitude 1, 10 rounds, 70% chance) → (magnitude 1, 10 rounds, 70% chance) |

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
    | Entry ID | `wyrm_trainer` |
    | Type (wiki) | Enemy |
    | Spawn group | `wyrm_4` |
    | Loot table | `wyrm_4` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:0` |
    | Defined in | `res/raw/monsterlist_v069_monsters.json` |

    Raw data:

    ```json
    {
     "id": "wyrm_trainer",
     "name": "Wyrm trainer",
     "iconID": "monsters_rltiles2:0",
     "maxHP": 69,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 2,
      "max": 9
     },
     "spawnGroup": "wyrm_4",
     "droplistID": "wyrm_4",
     "attackCost": 3,
     "attackChance": 90,
     "blockChance": 90,
     "damageResistance": 4,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 1
      },
      "conditionsTarget": [
       {
        "condition": "fatigue_minor",
        "magnitude": 1,
        "duration": 10,
        "chance": "70"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wyrm_trainer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wyrm_trainer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wyrm_trainer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wyrm_trainer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
