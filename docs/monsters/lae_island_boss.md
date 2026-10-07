---
description: "Dorhantarh is an NPC who can also be fought in Andor's Trail, found in final_cave2."
---

# ![](../assets/icons/monsters/monsters_newb_3_2.png){ .sprite } Dorhantarh

**Where to find Dorhantarh:** [final_cave2](../maps/final_cave2.md#pin-npc-lae_island_boss)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_3_2.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | final_cave2 |
| **Class** | Animal |
| **HP** | 297 |
| **XP when defeated** | 752 |
| **Entry ID** | `lae_island_boss` |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 297 |
| XP when defeated | 752 |
| Damage | 24 to 50 |
| Attack chance | 165 |
| Block chance | 127 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 6 AP |
| Critical skill | 3 |
| Critical multiplier | 3.0 |
| Critical hit chance | 2% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Dorhantarh's heart](../items/lae_island_boss_heart.md) | 100% | 1 |
| [Gold coins](../items/gold.md) | 100% | 100 to 1000 |
| [Raider's reach](../items/raiders_reach.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [final_cave2](../maps/final_cave2.md) | – | 1 | – |

## Quests that count defeats

- A conversation with walking into a blocked passage on [final_cave1](../maps/final_cave1.md), stepping on a trigger on [final_cave1](../maps/final_cave1.md) checks that this enemy has been defeated.
- [Not Pony Island](../quests/lae_centaurs.md#stage-160) with stepping on a trigger on [final_cave1](../maps/final_cave1.md) checks that this enemy has been defeated.
- A conversation with [Algangror](../monsters/algangror.md#v-lae_algangror3) ([final_cave2](../maps/final_cave2.md)), [Jhaeld](../monsters/jhaeld.md#v-lae_jhaeld3) ([final_cave2](../maps/final_cave2.md)) checks that this enemy has been defeated.
- [Not Pony Island](../quests/lae_centaurs.md#stage-210) with stepping on a trigger on [final_cave2](../maps/final_cave2.md) checks that at least 123 of these enemies have been defeated.
- A conversation with [Thalos, the centaur](../monsters/lae_centaur9.md) ([island2](../maps/island2.md)) checks that this enemy has been defeated.

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Dorhantarh. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/lae_island_boss.json" data-npc="Dorhantarh" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-lae_island_boss"></span>**`lae_island_boss`** Dorhantarh: “Ah, my dinner at last.”

    - Next → [lae_island_boss_10](#d-lae_island_boss_10)

    <span id="d-lae_island_boss_10"></span>**`lae_island_boss_10`** Dorhantarh: “And no horse meat this time. My servants promised me a delicious surprise tonight.”

    - “We'll see. Attack!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `lae_island_boss` |
    | Spawn group | `lae_island_boss` |
    | Loot table | `lae_island_boss` |
    | Conversation | `lae_island_boss` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_newb_3:2` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "lae_island_boss",
     "name": "Dorhantarh",
     "iconID": "monsters_newb_3:2",
     "maxHP": 297,
     "moveCost": 6,
     "unique": 1,
     "monsterClass": "animal",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 24,
      "max": 50
     },
     "spawnGroup": "lae_island_boss",
     "phraseID": "lae_island_boss",
     "droplistID": "lae_island_boss",
     "attackCost": 4,
     "attackChance": 165,
     "criticalSkill": 3,
     "criticalMultiplier": 3.0,
     "blockChance": 127
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_island_boss.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_island_boss.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_island_boss.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lae_island_boss.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
