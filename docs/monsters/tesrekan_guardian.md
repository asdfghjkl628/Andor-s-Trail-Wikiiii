---
description: "Dread guardian is an NPC you can also fight in Andor's Trail, found in Waterwayacave 1."
---

# ![](../assets/icons/monsters/monsters_redshrike1_3.png){ .sprite } Dread guardian

**Where to find Dread guardian:** [Waterwayacave 1](../maps/waterwayacave1.md#pin-npc-tesrekan_guardian)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_redshrike1_3.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Waterwayacave 1 |
| **Class** | Demon |
| **HP** | 200 |
| **XP when defeated** | 484 |
| **Immune to crits** | Yes |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

!!! warning "You can fight Dread guardian"
    Answering “I've killed worse than you!” starts a fight with Dread guardian.

## Combat

| | |
|---|---|
| Class | Demon |
| HP | 200 |
| XP when defeated | 484 |
| Damage | 6 to 11 |
| AC | 120 |
| BC | 150 |
| DR | 3 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**

**Its hits:** On target: [Fear](../conditions/fear.md) (magnitude 2, 3 rounds, 35% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Dialogue simulator

Set your quest stages and items, then talk to Dread guardian. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/tesrekan_guardian_0.json" data-npc="Dread guardian" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-tesrekan_guardian_0"></span>**`tesrekan_guardian_0`** Dread guardian: “You dare approach me? You will die!”

    - “I've killed worse than you!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

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
    | Entry ID | `tesrekan_guardian` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `tesrekan_guardian` |
    | Loot table | – |
    | Conversation | `tesrekan_guardian_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_redshrike1:3` |
    | Defined in | `res/raw/monsterlist_graveyard1.json` |

    Raw data:

    ```json
    {
     "id": "tesrekan_guardian",
     "name": "Dread guardian",
     "iconID": "monsters_redshrike1:3",
     "maxHP": 200,
     "unique": 1,
     "monsterClass": "demon",
     "attackDamage": {
      "min": 6,
      "max": 11
     },
     "spawnGroup": "tesrekan_guardian",
     "phraseID": "tesrekan_guardian_0",
     "attackCost": 3,
     "attackChance": 120,
     "blockChance": 150,
     "damageResistance": 3,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "fear",
        "magnitude": 2,
        "duration": 3,
        "chance": "35"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tesrekan_guardian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tesrekan_guardian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tesrekan_guardian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tesrekan_guardian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
