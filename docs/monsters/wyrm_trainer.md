# ![](../assets/icons/monsters/monsters_rltiles2_0.png){ .sprite } Wyrm trainer

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_0.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `wyrm_trainer` |
| **Type** | Enemy |
| **Class** | Undead |
| **HP** | 69 |
| **XP when killed** | 199 |
| **Found in** | Blackwater Mountain |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 69 |
| Damage | 2 to 9 |
| Attack chance | 90 |
| Block chance | 90 |
| Damage resistance | 4 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**On hit:** Heal HP: 1; On target: Minor fatigue (magnitude 1, 10 rounds, 70% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


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
| [blackwater_mountain36](../maps/blackwater_mountain36.md) | Blackwater Mountain | 4 | – |
| [blackwater_mountain37](../maps/blackwater_mountain37.md) | Blackwater Mountain | 3 | – |
| [blackwater_mountain38](../maps/blackwater_mountain38.md) | Blackwater Mountain | 4 | – |


## Quests that count kills

- A conversation with [General's henchman](../monsters/ortholion_guard1.md) ([blackwater_mountain11](../maps/blackwater_mountain11.md)), [Feygard scout](../monsters/ortholion_guard6.md) ([blackwater_mountain10](../maps/blackwater_mountain10.md)) checks that you've killed at least 1


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | hitEffect: {"conditionsTarget": [{"chance": 70, "c… → {"conditionsTarget": [{"chance": "70", … |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wyrm_trainer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wyrm_trainer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wyrm_trainer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wyrm_trainer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `wyrm_trainer` |
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


<small>Data from v0.8.18</small>
