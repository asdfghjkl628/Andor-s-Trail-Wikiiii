# ![](../assets/icons/monsters/monsters_ld2_47.png){ .sprite } Benzimos

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld2_47.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `haunted_benzimos` |
| **Type** | Enemy |
| **Class** | Demon |
| **HP** | 291 |
| **XP when killed** | 980 |
| **Found in** | haunted_house_basement |
| **Immune to crits** | Yes |
| **Introduced** | [v0.8.3](../versions/0.8.3.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 291 |
| Damage | 19 to 20 |
| Attack chance | 219 |
| Block chance | 198 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 10 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Crit chance | 9% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons can't be critically hit. Your crit build will have to sit this one out.

**On hit:** On target: Fear (magnitude 3, 3 rounds, 50% chance); Death Plague (magnitude 2, 3 rounds, 15% chance)

**When hit:** On self: Regeneration (magnitude 7, 1 rounds, 100% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 250 to 500 |
| [Shield of the undead](../items/shield_of_undead.md) | 100% | 1 |
| [Major flask of health](../items/health_major.md) | 100% | 2 to 4 |
| [Tonic of blood](../items/tonic_of_blood.md) | 100% | 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [haunted_house_basement](../maps/haunted_house_basement.md) | – | 1 | – |


## Quests that count kills

- [The Dead are Walking](../quests/dead_walking.md#stage-60) with stepping on a trigger on [haunted_house_basement](../maps/haunted_house_basement.md) checks that you've killed at least 1


## Version history

| Version | Change |
|---|---|
| [v0.8.3](../versions/0.8.3.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=haunted_benzimos.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=haunted_benzimos.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=haunted_benzimos.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=haunted_benzimos.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `haunted_benzimos` |
    | Spawn group | `haunted_benzimos` |
    | Loot table | `benzimos_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_ld2:47` |
    | Defined in | `res/raw/monsterlist_haunted_forest.json` |

    Raw data:

    ```json
    {
     "id": "haunted_benzimos",
     "name": "Benzimos",
     "iconID": "monsters_ld2:47",
     "maxHP": 291,
     "unique": 1,
     "monsterClass": "demon",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 19,
      "max": 20
     },
     "droplistID": "benzimos_dl",
     "attackCost": 3,
     "attackChance": 219,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 198,
     "damageResistance": 0,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "fear",
        "magnitude": 3,
        "duration": 3,
        "chance": "50"
       },
       {
        "condition": "death_plague",
        "magnitude": 2,
        "duration": 3,
        "chance": "15"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "regen2",
        "magnitude": 7,
        "duration": 1,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
