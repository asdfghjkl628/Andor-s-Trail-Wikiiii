---
description: "Nightmare is an enemy in Andor's Trail (humanoid) with 120 HP, worth 1827 XP, found in Guynmart Castle."
---

# ![](../assets/icons/monsters/monsters_tometik8_24.png){ .sprite } Nightmare

**Where to find Nightmare:** [Guynmart Castle, Guynmart tower 0](#v-guynmart_mare), [Guynmart Castle, Guynmart tower 0](#v-guynmart_mare0)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik8_24.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Guynmart Castle |
| **Class** | Humanoid |
| **HP** | 120 |
| **XP when defeated** | 1,827 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Guynmart Castle, Guynmart tower 0 { #v-guynmart_mare }

**Where:** Guynmart Castle: [Guynmart tower 0](../maps/guynmart_tower_0.md)

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 120 |
| XP when defeated | 1,827 |
| Damage | 8 to 25 |
| AC | 90 |
| BC | 500 |
| DR | 200 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Guynmart tower 0](../maps/guynmart_tower_0.md) | Guynmart Castle | 2 | Appears later, during a quest |

### Quests that count defeats

- [Unusual experiences and achievements](../quests/achievements.md#stage-130) with a scripted event checks that at least 2 of these enemies have been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Guynmart Castle, Guynmart tower 0 (2) { #v-guynmart_mare0 }

**Where:** Guynmart Castle: [Guynmart tower 0](../maps/guynmart_tower_0.md)


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Nightmare. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: combat statistics, movement.

| Entry | Type | Section |
|---|---|---|
| `guynmart_mare` | Enemy | [Guynmart Castle, Guynmart tower 0](#v-guynmart_mare) |
| `guynmart_mare0` | Scenery | [Guynmart Castle, Guynmart tower 0](#v-guynmart_mare0) |

- `guynmart_mare0` has no conversation and no combat statistics. Other conversations use it as their speaker (the `switchToNPC` field), which is how its name and picture appear in dialogue. The game data also places it on Guynmart Castle: [Guynmart tower 0](../maps/guynmart_tower_0.md).

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: guynmart_mare"

    | | |
    |---|---|
    | Entry ID | `guynmart_mare` |
    | Type (wiki) | Enemy |
    | Spawn group | `guynmart_mare` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_tometik8:24` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_mare",
     "name": "Nightmare",
     "iconID": "monsters_tometik8:24",
     "maxHP": 120,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 0,
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 8,
      "max": 25
     },
     "attackCost": 5,
     "attackChance": 90,
     "blockChance": 500,
     "damageResistance": 200
    }
    ```

??? info "Technical information: guynmart_mare0"

    | | |
    |---|---|
    | Entry ID | `guynmart_mare0` |
    | Type (wiki) | Scenery |
    | Spawn group | `guynmart_mare0` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik8:24` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_mare0",
     "name": "Nightmare",
     "iconID": "monsters_tometik8:24"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_mare.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_mare.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_mare.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_mare.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
