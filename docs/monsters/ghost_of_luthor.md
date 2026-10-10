---
description: "Ghost of Luthor is an NPC you can also fight in Andor's Trail."
---

# ![](../assets/icons/monsters/monsters_liches_2.png){ .sprite } Ghost of Luthor

**Where to find Ghost of Luthor:** appears during a quest or scripted event.

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_liches_2.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Class** | Ghost |
| **HP** | 86 |
| **XP when defeated** | 133 |
| **Immune to crits** | Yes |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "You can fight Ghost of Luthor"
    Answering “By the Shadow, what are you?” starts a fight with Ghost of Luthor.

## Combat

| | |
|---|---|
| Class | Ghost |
| HP | 86 |
| XP when defeated | 133 |
| Damage | 2 to 5 |
| AC | 120 |
| BC | 50 |
| DR | 3 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 12% (×2.0) |

**Immune to critical hits.**


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 1 to 5 |
| [Glass gem](../items/gem1.md) | 100% | 1 |
| [Key of Luthor](../items/key_luthor.md) | 100% | 1 |
| [Major flask of health](../items/health_major.md) | 100% | 1 |

## Dialogue simulator

Set your quest stages and items, then talk to Ghost of Luthor. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/luthor.json" data-npc="Ghost of Luthor" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-luthor"></span>**`luthor`** Ghost of Luthor: “*hissss* What mortal disturbs my sleep?”

    - “By the Shadow, what are you?” → *fight starts*
    - “At last, a worthy fight! I have been waiting for this.” → *fight starts*
    - “Whatever, let's get this over with.” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect) |

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
    | Entry ID | `ghost_of_luthor` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `luthor` |
    | Loot table | `luthor` |
    | Conversation | `luthor` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_liches:2` |
    | Defined in | `res/raw/monsterlist_fallhaven_animals.json` |

    Raw data:

    ```json
    {
     "id": "ghost_of_luthor",
     "name": "Ghost of Luthor",
     "iconID": "monsters_liches:2",
     "maxHP": 86,
     "maxAP": 10,
     "moveCost": 10,
     "unique": 1,
     "monsterClass": "ghost",
     "attackDamage": {
      "min": 2,
      "max": 5
     },
     "spawnGroup": "luthor",
     "phraseID": "luthor",
     "droplistID": "luthor",
     "attackCost": 5,
     "attackChance": 120,
     "criticalSkill": 15,
     "criticalMultiplier": 2.0,
     "blockChance": 50,
     "damageResistance": 3
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ghost_of_luthor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ghost_of_luthor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ghost_of_luthor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ghost_of_luthor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
