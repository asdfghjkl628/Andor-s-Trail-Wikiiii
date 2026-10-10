---
description: "Alaric is an NPC you can also fight in Andor's Trail, found in Aidem base 2, Fallhaven, Blackwater Mountain."
---

# ![](../assets/icons/monsters/monsters_tometik2_55.png){ .sprite } Alaric

**Where to find Alaric:** [Aidem base 2](#v-aidem_base_alaric), [Aidem base 2](#v-aidem_base_alaric_aggressive), [Fallhaven, Guildbrig 2](#v-aidem_jail_alaric), [Blackwater Mountain, Wild 6 house](#v-alaric_wild6house)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik2_55.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Aidem base 2, Fallhaven, Blackwater Mountain |
| **Class** | Humanoid |
| **HP** | 329 |
| **XP when defeated** | 707 |
| **Introduced** | [v0.8.8](../versions/0.8.8.md) |

</div>

## Aidem base 2 { #v-aidem_base_alaric }

**Where:** [Aidem base 2](../maps/aidem_base_2.md#pin-npc-aidem_base_alaric)

### Dialogue simulator

Set your quest stages and items, then talk to Alaric. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/aidem_base_alaric_10.json" data-npc="Alaric" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-aidem_base_alaric-aidem_base_alaric_10"></span>**`aidem_base_alaric_10`** Alaric: “It's so weird working with you after all that we've gone through.”

    - “We are not friends.” → *conversation ends*
    - “I would love nothing more than to see you punished for your crimes.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Aidem base 2 (2) { #v-aidem_base_alaric_aggressive }

**Where:** [Aidem base 2](../maps/aidem_base_2.md)

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 329 |
| XP when defeated | 707 |
| Damage | 7 to 9 |
| AC | 158 |
| BC | 170 |
| DR | 0 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 2% (×2.0) |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Aidem base 2](../maps/aidem_base_2.md) | – | 1 | Appears later, during a quest |

### Quests that count defeats

- [Wanted men](../quests/wanted_men.md#stage-76) with stepping on a trigger on [Aidem base 2](../maps/aidem_base_2.md) checks that this enemy has been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Fallhaven, Guildbrig 2 { #v-aidem_jail_alaric }

**Where:** Fallhaven: [Guildbrig 2](../maps/guildbrig2.md)


### Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Blackwater Mountain, Wild 6 house { #v-alaric_wild6house }

**Where:** Blackwater Mountain: [Wild 6 house](../maps/wild6_house.md#pin-npc-alaric_wild6house)

### Dialogue simulator

Set your quest stages and items, then talk to Alaric. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/alaric_wild6house.json" data-npc="Alaric" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-alaric_wild6house-alaric_wild6house"></span>**`alaric_wild6house`** Alaric: “I'm rich. I'm finally rich!”

    - “Only in gold. You have no friends.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**4 entries.** The game data defines 4 separate characters named Alaric. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location, combat statistics, movement.

| Entry | Type | Section |
|---|---|---|
| `aidem_base_alaric` | NPC | [Aidem base 2](#v-aidem_base_alaric) |
| `aidem_base_alaric_aggressive` | Enemy | [Aidem base 2](#v-aidem_base_alaric_aggressive) |
| `aidem_jail_alaric` | Scenery | [Fallhaven, Guildbrig 2](#v-aidem_jail_alaric) |
| `alaric_wild6house` | NPC | [Blackwater Mountain, Wild 6 house](#v-alaric_wild6house) |

- `aidem_jail_alaric` has no conversation and no combat statistics. It is a decoration, an animal or a figure in a scripted scene.

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: aidem_base_alaric"

    | | |
    |---|---|
    | Entry ID | `aidem_base_alaric` |
    | Type (wiki) | NPC |
    | Spawn group | `aidem_base_alaric` |
    | Loot table | – |
    | Conversation | `aidem_base_alaric_10` |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik2:55` |
    | Defined in | `res/raw/monsterlist_mt_galmore.json` |

    Raw data:

    ```json
    {
     "id": "aidem_base_alaric",
     "name": "Alaric",
     "iconID": "monsters_tometik2:55",
     "maxHP": 1,
     "moveCost": 10,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "helpOthers",
     "phraseID": "aidem_base_alaric_10"
    }
    ```

??? info "Technical information: aidem_base_alaric_aggressive"

    | | |
    |---|---|
    | Entry ID | `aidem_base_alaric_aggressive` |
    | Type (wiki) | Enemy |
    | Spawn group | `help_defy` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_tometik2:55` |
    | Defined in | `res/raw/monsterlist_mt_galmore.json` |

    Raw data:

    ```json
    {
     "id": "aidem_base_alaric_aggressive",
     "name": "Alaric",
     "iconID": "monsters_tometik2:55",
     "maxHP": 329,
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 7,
      "max": 9
     },
     "spawnGroup": "help_defy",
     "attackCost": 3,
     "attackChance": 158,
     "criticalSkill": 3,
     "criticalMultiplier": 2.0,
     "blockChance": 170
    }
    ```

??? info "Technical information: aidem_jail_alaric"

    | | |
    |---|---|
    | Entry ID | `aidem_jail_alaric` |
    | Type (wiki) | Scenery |
    | Spawn group | `aidem_jail_alaric` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:55` |
    | Defined in | `res/raw/monsterlist_mt_galmore.json` |

    Raw data:

    ```json
    {
     "id": "aidem_jail_alaric",
     "name": "Alaric",
     "iconID": "monsters_tometik2:55",
     "monsterClass": "humanoid"
    }
    ```

??? info "Technical information: alaric_wild6house"

    | | |
    |---|---|
    | Entry ID | `alaric_wild6house` |
    | Type (wiki) | NPC |
    | Spawn group | `alaric_wild6house` |
    | Loot table | – |
    | Conversation | `alaric_wild6house` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:55` |
    | Defined in | `res/raw/monsterlist_mt_galmore.json` |

    Raw data:

    ```json
    {
     "id": "alaric_wild6house",
     "name": "Alaric",
     "iconID": "monsters_tometik2:55",
     "phraseID": "alaric_wild6house"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aidem_base_alaric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aidem_base_alaric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aidem_base_alaric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aidem_base_alaric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
