# ![](../assets/icons/monsters/monsters_gisons_3.png){ .sprite } Weak fungi

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_gisons_3.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `weak_fungi` |
| **Type** | Enemy |
| **Class** | Animal |
| **HP** | 20 |
| **XP when killed** | 23 |
| **Found in** | bogsten2, bogsten3, mushroom_m2_2 |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 20 |
| Damage | 1 to 2 |
| Attack chance | 110 |
| Block chance | 10 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Spores of the giant mushroom](../items/fungi_panic_spores.md) | 1% | 1 |
| [Bogsten's mushroom](../items/mushroom_bogsten.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [bogsten2](../maps/bogsten2.md) | – | 4 | – |
| [bogsten3](../maps/bogsten3.md) | – | 8 | – |
| [mushroom_m2_2](../maps/mushroom_m2_2.md) | – | 4 | – |
| [mushroom_m2_4](../maps/mushroom_m2_4.md) | – | 5 | – |
| [mushroom_m2_5](../maps/mushroom_m2_5.md) | – | 3 | – |
| [mushroom_m3_1](../maps/mushroom_m3_1.md) | – | 1 | – |
| [mushroom_m3_2](../maps/mushroom_m3_2.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=weak_fungi.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=weak_fungi.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=weak_fungi.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=weak_fungi.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `weak_fungi` |
    | Spawn group | `weak_fungi` |
    | Loot table | `weak_fungi` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_gisons:3` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "weak_fungi",
     "name": "Weak fungi",
     "iconID": "monsters_gisons:3",
     "maxHP": 20,
     "maxAP": 10,
     "moveCost": 10,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 1,
      "max": 2
     },
     "spawnGroup": "weak_fungi",
     "droplistID": "weak_fungi",
     "attackCost": 5,
     "attackChance": 110,
     "blockChance": 10
    }
    ```


<small>Data from v0.8.18</small>
