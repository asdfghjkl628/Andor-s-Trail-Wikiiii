---
description: "Karth the Unbowed is an NPC you can also fight in Andor's Trail, found in Stoutford."
---

# ![](../assets/icons/monsters/monsters_tometik8_45.png){ .sprite } Karth the Unbowed

**Where to find Karth the Unbowed:** Stoutford: [Stoutford castle barrack 1](../maps/stoutford_castle_barrack1.md#pin-npc-erwyn_commander)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik8_45.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Stoutford |
| **Class** | Undead |
| **HP** | 90 |
| **XP when defeated** | 196 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

!!! warning "You can fight Karth the Unbowed"
    Answering “For that you have to get me first, lazybones!” starts a fight with Karth the Unbowed.

## Combat

| | |
|---|---|
| Class | Undead |
| HP | 90 |
| XP when defeated | 196 |
| Damage | 15 to 23 |
| AC | 150 |
| BC | 75 |
| DR | 4 |
| Attacks per turn | 1 (10 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Quests that count defeats

- [Stoutford's old castle](../quests/stoutford_castle.md#stage-30) with [Yolgen](../monsters/yolgen.md) ([Stoutford church](../maps/stoutford_church.md)) checks that this enemy has been defeated.
- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-47) with stepping on a trigger on [Waytogalmore 0](../maps/waytogalmore0.md), stepping on a trigger on [Wild 18](../maps/wild18.md) checks that this enemy has been defeated.

## Dialogue simulator

Set your quest stages and items, then talk to Karth the Unbowed. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stoutford_castle_2.json" data-npc="Karth the Unbowed" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-stoutford_castle_2"></span>**`stoutford_castle_2`** Karth the Unbowed: “I shall crush you little mortal!”

    - “For that you have to get me first, lazybones!” → *fight starts*



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
    | Entry ID | `erwyn_commander` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `erwyn_commander` |
    | Loot table | – |
    | Conversation | `stoutford_castle_2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik8:45` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "erwyn_commander",
     "name": "Karth the Unbowed",
     "iconID": "monsters_tometik8:45",
     "maxHP": 90,
     "unique": 1,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 15,
      "max": 23
     },
     "spawnGroup": "erwyn_commander",
     "phraseID": "stoutford_castle_2",
     "attackChance": 150,
     "blockChance": 75,
     "damageResistance": 4
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_commander.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_commander.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_commander.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_commander.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
