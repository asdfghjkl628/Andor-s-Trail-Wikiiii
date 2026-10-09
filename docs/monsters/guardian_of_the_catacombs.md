---
description: "Guardian of the catacombs is an NPC who can also be fought in Andor's Trail, found in Fallhaven."
---

# ![](../assets/icons/monsters/monsters_rltiles2_45.png){ .sprite } Guardian of the catacombs

**Where to find Guardian of the catacombs:** Fallhaven: [Catacombs 1](../maps/catacombs1.md#pin-npc-guardian_of_the_catacombs)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_45.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Fallhaven |
| **Class** | Ghost |
| **HP** | 6 |
| **XP when defeated** | 25 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `guardian_of_the_catacombs` |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Ghost |
| HP | 6 |
| XP when defeated | 25 |
| Damage | 1 to 6 |
| Attack chance | 10 |
| Block chance | 10 |
| Damage resistance | 3 |
| Max AP | 10 |
| Attack cost | 9 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 4 to 12 |
| [Ruby gem](../items/gem2.md) | 25% | 1 |
| [Regular potion of health](../items/health.md) | 25% | 1 |
| [Empty vial](../items/vial_empty2.md) | 25% | 1 |
| [Leather gloves](../items/gloves1.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Catacombs 1](../maps/catacombs1.md) | Fallhaven | 1 | – |

## Dialogue simulator

Set your quest stages and items, then talk to Guardian of the catacombs. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/catacombguard.json" data-npc="Guardian of the catacombs" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-catacombguard"></span>**`catacombguard`** Guardian of the catacombs: “Turn back while you still can, mortal. This is no place for you. Only death awaits you here.”

    - “Very well. I will turn back.” → *conversation ends*
    - “Move aside, I need to get deeper into the catacombs.” → [catacombguard1](#d-catacombguard1)
    - “By the Shadow, you will not stop me.” → [catacombguard1](#d-catacombguard1)

    <span id="d-catacombguard1"></span>**`catacombguard1`** Guardian of the catacombs: “Nooo, you shall not pass!”

    - “OK. Let's fight.” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |
| [v0.7.4](../versions/0.7.4.md) | Attack cost: 10 → 9 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `guardian_of_the_catacombs` |
    | Spawn group | `catacombguard1` |
    | Loot table | `catacombguard` |
    | Conversation | `catacombguard` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:45` |
    | Defined in | `res/raw/monsterlist_fallhaven_animals.json` |

    Raw data:

    ```json
    {
     "id": "guardian_of_the_catacombs",
     "name": "Guardian of the catacombs",
     "iconID": "monsters_rltiles2:45",
     "maxHP": 6,
     "maxAP": 10,
     "moveCost": 10,
     "unique": 1,
     "monsterClass": "ghost",
     "attackDamage": {
      "min": 1,
      "max": 6
     },
     "spawnGroup": "catacombguard1",
     "phraseID": "catacombguard",
     "droplistID": "catacombguard",
     "attackCost": 9,
     "attackChance": 10,
     "blockChance": 10,
     "damageResistance": 3
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guardian_of_the_catacombs.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guardian_of_the_catacombs.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guardian_of_the_catacombs.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guardian_of_the_catacombs.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
