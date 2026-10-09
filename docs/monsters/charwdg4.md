---
description: "Charwood goblin is an NPC who can also be fought in Andor's Trail, found in Charwood."
---

# ![](../assets/icons/monsters/monsters_rltiles4_18.png){ .sprite } Charwood goblin

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles4_18.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Charwood |
| **Class** | Humanoid |
| **HP** | 73–81 |
| **XP when defeated** | 151–162 |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game data defines 2 separate characters named Charwood goblin. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, location, combat statistics, appearance. Each entry has its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`charwdg4`](#v-charwdg4) | Enemy | Charwood: [Lostmine 0](../maps/lostmine0.md), Charwood: [Lostmine 1](../maps/lostmine1.md) (+13 more) | – | 73 |
| [`charwdgg`](#v-charwdgg) | NPC/Enemy | Charwood: [Waytolostmine 0](../maps/waytolostmine0.md#pin-npc-charwdgg) | – | 81 |

## Charwood, Lostmine 0 and 14 more (charwdg4) { #v-charwdg4 }

**Entry ID:** `charwdg4` · **Type:** Enemy

**Location:** Charwood: [Lostmine 0](../maps/lostmine0.md), Charwood: [Lostmine 1](../maps/lostmine1.md), Charwood: [Lostmine 1a](../maps/lostmine1a.md), Charwood: [Lostmine 2](../maps/lostmine2.md), Charwood: [Minerhouse 0](../maps/minerhouse0.md), Charwood: [Minerhouse 1](../maps/minerhouse1.md) (+9 more)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 73 |
| XP when defeated | 151 |
| Damage | 7 to 9 |
| Attack chance | 144 |
| Block chance | 63 |
| Damage resistance | 4 |
| Max AP | 10 |
| Attack cost | 6 AP |
| Attacks per turn | 1 |
| Move cost | 5 AP |
| Critical skill | 25 |
| Critical multiplier | 3.0 |
| Critical hit chance | 17% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 30% | 1 to 20 |
| [Iron mace](../items/mace_iron.md) | 1% | 1 |
| [Broken wooden buckler](../items/broken_buckler.md) | 1% | 1 |
| [Ointment of bleeding wounds](../items/pot_bleeding_ointment.md) | 5% | 1 |
| [Raw perch](../items/rawperch.md) | 10% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Lostmine 0](../maps/lostmine0.md) | Charwood | 8 | – |
| [Lostmine 1](../maps/lostmine1.md) | Charwood | 4 | – |
| [Lostmine 1a](../maps/lostmine1a.md) | Charwood | 2 | – |
| [Lostmine 2](../maps/lostmine2.md) | Charwood | 3 | – |
| [Lostmine 2a](../maps/lostmine2a.md) | – | 1 | – |
| [Minerhouse 0](../maps/minerhouse0.md) | Charwood | 3 | – |
| [Minerhouse 1](../maps/minerhouse1.md) | Charwood | 2 | – |
| [Minerhouse 2](../maps/minerhouse2.md) | Charwood | 4 | – |
| [Minerhouse 3](../maps/minerhouse3.md) | Charwood | 6 | – |
| [Minerhouse 7](../maps/minerhouse7.md) | Charwood | 5 | – |
| [Minerhouse 8](../maps/minerhouse8.md) | Charwood | 1 | – |
| [Minerhouse 9](../maps/minerhouse9.md) | Charwood | 2 | – |
| [Waytolostmine 1](../maps/waytolostmine1.md) | Charwood | 8 | – |
| [Waytolostmine 2](../maps/waytolostmine2.md) | Charwood | 12 | – |
| [Waytolostmine 3](../maps/waytolostmine3.md) | Charwood | 19 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (charwdg4)"

    | | |
    |---|---|
    | Entry ID | `charwdg4` |
    | Spawn group | `charwdg2` |
    | Loot table | `charwdg` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles4:18` |
    | Defined in | `res/raw/monsterlist_v070_charwood.json` |

    Raw data:

    ```json
    {
     "id": "charwdg4",
     "name": "Charwood goblin",
     "iconID": "monsters_rltiles4:18",
     "maxHP": 73,
     "moveCost": 5,
     "attackDamage": {
      "min": 7,
      "max": 9
     },
     "spawnGroup": "charwdg2",
     "droplistID": "charwdg",
     "attackCost": 6,
     "attackChance": 144,
     "criticalSkill": 25,
     "criticalMultiplier": 3.0,
     "blockChance": 63,
     "damageResistance": 4
    }
    ```


## Charwood, Waytolostmine 0 (charwdgg) { #v-charwdgg }

**Entry ID:** `charwdgg` · **Type:** NPC/Enemy

**Location:** Charwood: [Waytolostmine 0](../maps/waytolostmine0.md#pin-npc-charwdgg)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 81 |
| XP when defeated | 162 |
| Damage | 7 to 9 |
| Attack chance | 147 |
| Block chance | 65 |
| Damage resistance | 4 |
| Max AP | 10 |
| Attack cost | 6 AP |
| Attacks per turn | 1 |
| Move cost | 5 AP |
| Critical skill | 25 |
| Critical multiplier | 3.0 |
| Critical hit chance | 17% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 30% | 1 to 20 |
| [Iron mace](../items/mace_iron.md) | 1% | 1 |
| [Broken wooden buckler](../items/broken_buckler.md) | 1% | 1 |
| [Ointment of bleeding wounds](../items/pot_bleeding_ointment.md) | 5% | 1 |
| [Raw perch](../items/rawperch.md) | 10% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Waytolostmine 0](../maps/waytolostmine0.md) | Charwood | 1 | – |

### Quests

- [Destined for great things](../quests/charwood1.md): stage 40

### Dialogue simulator

Set your quest stages and items, then talk to Charwood goblin. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/charwoodm.json" data-npc="Charwood goblin" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-charwdgg-charwoodm"></span>**`charwoodm`** Charwood goblin: “Bow before the might of the Thukuzun!” — **effects:** sets stage 40 of [Destined for great things](../quests/charwood1.md#stage-40)

    - “I bow to no one.” → *fight starts*
    - “Bow down to your own death!” → *fight starts*
    - “Fight!” → *fight starts*



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (charwdgg)"

    | | |
    |---|---|
    | Entry ID | `charwdgg` |
    | Spawn group | `charwdgg` |
    | Loot table | `charwdg` |
    | Conversation | `charwoodm` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles4:22` |
    | Defined in | `res/raw/monsterlist_v070_charwood.json` |

    Raw data:

    ```json
    {
     "id": "charwdgg",
     "name": "Charwood goblin",
     "iconID": "monsters_rltiles4:22",
     "maxHP": 81,
     "moveCost": 5,
     "unique": 1,
     "attackDamage": {
      "min": 7,
      "max": 9
     },
     "phraseID": "charwoodm",
     "droplistID": "charwdg",
     "attackCost": 6,
     "attackChance": 147,
     "criticalSkill": 25,
     "criticalMultiplier": 3.0,
     "blockChance": 65,
     "damageResistance": 4
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=charwdg4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=charwdg4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=charwdg4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=charwdg4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
