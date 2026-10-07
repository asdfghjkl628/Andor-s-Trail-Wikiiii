---
description: "Andor's statue is an NPC who can also be fought in Andor's Trail, found in Crossglen."
---

# ![](../assets/icons/monsters/monsters_maksiu1_1.png){ .sprite } Andor's statue

**Where to find Andor's statue:** Crossglen: [crossglen_cave](../maps/crossglen_cave.md#pin-npc-ratdom_rat_statue)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_maksiu1_1.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Crossglen |
| **Class** | Humanoid |
| **HP** | 90 |
| **XP when defeated** | 89 |
| **Entry ID** | `ratdom_rat_statue` |
| **Introduced** | [v0.8.5](../versions/0.8.5.md) |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 90 |
| XP when defeated | 89 |
| Damage | 1 to 4 |
| Attack chance | 60 |
| Block chance | 40 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 99 AP |
| Attacks per turn | 0 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Bread](../items/bread.md) | 100% | 1 to 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [crossglen_cave](../maps/crossglen_cave.md) | Crossglen | 1 | Appears later, during a quest |

## Quests

- [Yellow is it](../quests/ratdom_quest.md): stages 60, 80

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Andor's statue. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/ratdom_rat_statue.json" data-npc="Andor&#x27;s statue" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ratdom_rat_statue"></span>**`ratdom_rat_statue`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if wearing [Pickhatchet](../items/ratdom_pickaxe.md))* → *fight starts*
    - branch 2 *(if reached stage 82 of [Yellow is it](../quests/ratdom_quest.md#stage-82))* → [ratdom_rat_statue_40](#d-ratdom_rat_statue_40)
    - branch 3 *(if reached stage 70 of [Yellow is it](../quests/ratdom_quest.md#stage-70))* → [ratdom_rat_statue_30](#d-ratdom_rat_statue_30)
    - branch 4 → [ratdom_rat_statue_20](#d-ratdom_rat_statue_20)

    <span id="d-ratdom_rat_statue_40"></span>**`ratdom_rat_statue_40`** [Clevred](../monsters/ratdom_rat.md): “When will you finally try to use the pickaxe?”


    <span id="d-ratdom_rat_statue_30"></span>**`ratdom_rat_statue_30`** [Clevred](../monsters/ratdom_rat.md): “Andor's statue may be cleared away with a pickaxe. Hadn't I mentioned it?” — **effects:** sets stage 80 of [Yellow is it](../quests/ratdom_quest.md#stage-80)


    <span id="d-ratdom_rat_statue_20"></span>**`ratdom_rat_statue_20`** [Dummy NPC](../monsters/none.md): “You see a beautifully crafted statue of your brother Andor.” — **effects:** sets stage 60 of [Yellow is it](../quests/ratdom_quest.md#stage-60)




## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `ratdom_rat_statue` |
    | Spawn group | `ratdom_rat_statue` |
    | Loot table | `drop_ratdom_mara` |
    | Conversation | `ratdom_rat_statue` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_maksiu1:1` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_rat_statue",
     "name": "Andor's statue",
     "iconID": "monsters_maksiu1:1",
     "maxHP": 90,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 1,
      "max": 4
     },
     "spawnGroup": "ratdom_rat_statue",
     "phraseID": "ratdom_rat_statue",
     "droplistID": "drop_ratdom_mara",
     "attackCost": 99,
     "attackChance": 60,
     "blockChance": 40
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_rat_statue.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_rat_statue.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_rat_statue.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_rat_statue.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
