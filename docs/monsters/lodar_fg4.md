---
description: "Insane Feygard guard is an NPC who can also be fought in Andor's Trail, found in lodar8."
---

# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Insane Feygard guard

**Where to find Insane Feygard guard:** [lodar8](../maps/lodar8.md#pin-npc-lodar_fg4)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | lodar8 |
| **Class** | Humanoid |
| **HP** | 212 |
| **XP when defeated** | 347 |
| **Entry ID** | `lodar_fg4` |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 212 |
| XP when defeated | 347 |
| Damage | 1 to 11 |
| Attack chance | 75 |
| Block chance | 90 |
| Damage resistance | 3 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 10 AP |
| Critical skill | 20 |
| Critical multiplier | 3.0 |
| Critical hit chance | 15% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 30% | 1 to 20 |
| [Iron mace](../items/mace_iron.md) | 5% | 1 |
| [Broken wooden buckler](../items/broken_buckler.md) | 5% | 1 |
| [Mead](../items/mead.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [lodar8](../maps/lodar8.md) | – | 1 | – |

## Quests

- [A lost potion](../quests/lodar.md): stage 73

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Insane Feygard guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/lodar_fg4.json" data-npc="Insane Feygard guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (11 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-lodar_fg4"></span>**`lodar_fg4`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 50 of [Searching for madness](../quests/lodar2.md#stage-50))* → [lodar_fg4_a](#d-lodar_fg4_a)
    - branch 2 → [lodar_fg4_0](#d-lodar_fg4_0)

    <span id="d-lodar_fg4_a"></span>**`lodar_fg4_a`** Insane Feygard guard: “I seem to have lost track of where I am. I was looking for something.”


    <span id="d-lodar_fg4_0"></span>**`lodar_fg4_0`** Insane Feygard guard: “I'll find it.”

    - Next → [lodar_fg4_1](#d-lodar_fg4_1)

    <span id="d-lodar_fg4_1"></span>**`lodar_fg4_1`** Insane Feygard guard: “Soon, it will all be mine.”

    - Next → [lodar_fg4_2](#d-lodar_fg4_2)

    <span id="d-lodar_fg4_2"></span>**`lodar_fg4_2`** Insane Feygard guard: “I'll find what lurks beneath.”

    - “Lurks beneath?” → [lodar_fg4_3](#d-lodar_fg4_3)

    <span id="d-lodar_fg4_3"></span>**`lodar_fg4_3`** Insane Feygard guard: “[The guard turns towards you, almost as if he didn't notice you before]”

    - Next → [lodar_fg4_4](#d-lodar_fg4_4)

    <span id="d-lodar_fg4_4"></span>**`lodar_fg4_4`** Insane Feygard guard: “What, who are you?”

    - Next → [lodar_fg4_5](#d-lodar_fg4_5)

    <span id="d-lodar_fg4_5"></span>**`lodar_fg4_5`** Insane Feygard guard: “Are you one of ... them?”

    - “One of who?” → [lodar_fg4_6](#d-lodar_fg4_6)
    - “[Lie] Yes, I an one of them. Bow down to me.” → [lodar_fg4_6](#d-lodar_fg4_6)
    - “What are you talking about?” → [lodar_fg4_6](#d-lodar_fg4_6)

    <span id="d-lodar_fg4_6"></span>**`lodar_fg4_6`** Insane Feygard guard: “Oh yes, you are one of them. What lurks beneath demands that I purge this land from all of you.”

    - Next → [lodar_fg4_7](#d-lodar_fg4_7)

    <span id="d-lodar_fg4_7"></span>**`lodar_fg4_7`** Insane Feygard guard: “You will be the first of my glorious victories.”

    - “Let's see who's victorious!” → [lodar_fg4_8](#d-lodar_fg4_8)
    - “Please don't hurt me!” → [lodar_fg4_8](#d-lodar_fg4_8)
    - “All right, a fight! I've been wanting to slay more of you Feygard scum.” → [lodar_fg4_8](#d-lodar_fg4_8)

    <span id="d-lodar_fg4_8"></span>**`lodar_fg4_8`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 73 of [A lost potion](../quests/lodar.md#stage-73)

    - branch 1 → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect)<br>Dialogue: 3 lines changed<br>· text: “(the guard turns towards you, almost as if he didn't notice you befor…” → “[The guard turns towards you, almost as if he didn't notice you befor…”<br>· text: “Are you one of .. them?” → “Are you one of ... them?” |
| [v0.8.7](../versions/0.8.7.md) | Class: added (humanoid) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `lodar_fg4` |
    | Spawn group | `lodar_fg4` |
    | Loot table | `lodar_fg` |
    | Conversation | `lodar_fg4` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles3:14` |
    | Defined in | `res/raw/monsterlist_v070_lodarnpcs.json` |

    Raw data:

    ```json
    {
     "id": "lodar_fg4",
     "name": "Insane Feygard guard",
     "iconID": "monsters_rltiles3:14",
     "maxHP": 212,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 1,
      "max": 11
     },
     "spawnGroup": "lodar_fg4",
     "phraseID": "lodar_fg4",
     "droplistID": "lodar_fg",
     "attackCost": 3,
     "attackChance": 75,
     "criticalSkill": 20,
     "criticalMultiplier": 3.0,
     "blockChance": 90,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lodar_fg4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lodar_fg4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lodar_fg4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lodar_fg4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
