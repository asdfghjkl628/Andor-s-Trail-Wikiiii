---
description: "Captain Burry is an NPC who can also be fought in Andor's Trail, found in Remgard, Lake Laeroth, mountainlake_circe."
---

# ![](../assets/icons/monsters/monsters_karvis2_2.png){ .sprite } Captain Burry

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_karvis2_2.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Remgard, Lake Laeroth, mountainlake_circe |
| **Class** | Humanoid |
| **HP** | 1 |
| **XP when defeated** | 1 |
| **Entries in game data** | 2 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Captain Burry. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`ll2_captain`](#v-ll2_captain) | NPC | Lake Laeroth: [mountainlake21](../maps/mountainlake21.md#pin-npc-ll2_captain), Remgard: [mountainlake14](../maps/mountainlake14.md#pin-npc-ll2_captain) (+6 more) | – | – |
| [`ll2_captain_0`](#v-ll2_captain_0) | Enemy | [mountainlake_circe](../maps/mountainlake_circe.md) | – | 1 |

## Lake Laeroth, Mountainlake21 and 7 more (ll2_captain) { #v-ll2_captain }

**Entry ID:** `ll2_captain` · **Type:** NPC

**Location:** Lake Laeroth: [mountainlake21](../maps/mountainlake21.md#pin-npc-ll2_captain), Remgard: [mountainlake14](../maps/mountainlake14.md#pin-npc-ll2_captain), Remgard: [remgard2a](../maps/remgard2a.md#pin-npc-ll2_captain), [mountainlake22](../maps/mountainlake22.md#pin-npc-ll2_captain), [mountainlake27](../maps/mountainlake27.md#pin-npc-ll2_captain), [mountainlake29](../maps/mountainlake29.md#pin-npc-ll2_captain) (+2 more)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mountainlake14](../maps/mountainlake14.md) | Remgard | 1 | – |
| [mountainlake21](../maps/mountainlake21.md) | Lake Laeroth | 1 | – |
| [mountainlake22](../maps/mountainlake22.md) | – | 1 | – |
| [mountainlake27](../maps/mountainlake27.md) | – | 1 | – |
| [mountainlake29](../maps/mountainlake29.md) | – | 1 | – |
| [mountainlake_circe](../maps/mountainlake_circe.md) | – | 1 | Appears later, during a quest |
| [mountainlake_sub](../maps/mountainlake_sub.md) | – | 1 | – |
| [remgard2a](../maps/remgard2a.md) | Remgard | 1 | – |

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Captain Burry. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/ll2_captain.json" data-npc="Captain Burry" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ll2_captain-ll2_captain"></span>**`ll2_captain`** Captain Burry: “Hey, little landlubber - everything alright?”




### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ll2_captain)"

    | | |
    |---|---|
    | Entry ID | `ll2_captain` |
    | Spawn group | `ll2_captain` |
    | Loot table | – |
    | Conversation | `ll2_captain` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:2` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "ll2_captain",
     "name": "Captain Burry",
     "iconID": "monsters_karvis2:2",
     "monsterClass": "humanoid",
     "spawnGroup": "ll2_captain",
     "phraseID": "ll2_captain"
    }
    ```


## Mountainlake circe (ll2_captain_0) { #v-ll2_captain_0 }

**Entry ID:** `ll2_captain_0` · **Type:** Enemy

**Location:** [mountainlake_circe](../maps/mountainlake_circe.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mountainlake_circe](../maps/mountainlake_circe.md) | – | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ll2_captain_0)"

    | | |
    |---|---|
    | Entry ID | `ll2_captain_0` |
    | Spawn group | `ll2_captain_0` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:2` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "ll2_captain_0",
     "name": "Captain Burry",
     "iconID": "monsters_karvis2:2",
     "monsterClass": "humanoid",
     "spawnGroup": "ll2_captain_0"
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_captain.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_captain.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_captain.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_captain.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
