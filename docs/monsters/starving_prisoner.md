---
description: "Starving prisoner is an NPC you can also fight in Andor's Trail, found in Flagstone Prison."
---

# ![](../assets/icons/monsters/monsters_misc_11.png){ .sprite } Starving prisoner

**Where to find Starving prisoner:** Flagstone Prison: [Flagstone 1](../maps/flagstone1.md#pin-npc-starving_prisoner), Flagstone Prison: [Flagstone 2](../maps/flagstone2.md#pin-npc-starving_prisoner), Flagstone Prison: [Flagstone inner](../maps/flagstone_inner.md#pin-npc-starving_prisoner), Flagstone Prison: [Flagstone upper](../maps/flagstone_upper.md#pin-npc-starving_prisoner)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_misc_11.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Flagstone Prison |
| **Class** | Humanoid |
| **HP** | 10 |
| **XP when defeated** | 27 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "You can fight Starving prisoner"
    Answering “Calm down, I was just...” starts a fight with Starving prisoner.

## Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 10 |
| XP when defeated | 27 |
| Damage | 3 to 5 |
| AC | 60 |
| BC | 60 |
| DR | 0 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Small rock](../items/rock.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Flagstone 1](../maps/flagstone1.md) | Flagstone Prison | 2 | – |
| [Flagstone 2](../maps/flagstone2.md) | Flagstone Prison | 1 | – |
| [Flagstone inner](../maps/flagstone_inner.md) | Flagstone Prison | 1 | – |
| [Flagstone upper](../maps/flagstone_upper.md) | Flagstone Prison | 1 | – |

## Dialogue simulator

Talk to Starving prisoner as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/prisoner2.json" data-npc="Starving prisoner" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-prisoner2"></span>**`prisoner2`** Starving prisoner: “Aaaa! Who's there? I will not be enslaved again!”

    - “Calm down, I was just...” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

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
    | Entry ID | `starving_prisoner` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `prisoner2` |
    | Loot table | `prisoner` |
    | Conversation | `prisoner2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_misc:11` |
    | Defined in | `res/raw/monsterlist_wilderness.json` |

    Raw data:

    ```json
    {
     "id": "starving_prisoner",
     "name": "Starving prisoner",
     "iconID": "monsters_misc:11",
     "maxHP": 10,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 3,
      "max": 5
     },
     "spawnGroup": "prisoner2",
     "phraseID": "prisoner2",
     "droplistID": "prisoner",
     "attackCost": 3,
     "attackChance": 60,
     "blockChance": 60
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=starving_prisoner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=starving_prisoner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=starving_prisoner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=starving_prisoner.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
