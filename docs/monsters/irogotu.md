---
description: "Irogotu is an NPC you can also fight in Andor's Trail, found in Jan pitcave 3."
---

# ![](../assets/icons/monsters/monsters_liches_0.png){ .sprite } Irogotu

**Where to find Irogotu:** [Jan pitcave 3](../maps/jan_pitcave3.md#pin-npc-irogotu)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_liches_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Jan pitcave 3 |
| **Class** | Undead |
| **HP** | 61 |
| **XP when defeated** | 123 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "You can fight Irogotu"
    Answering “Very well, let's see who dies here.” starts a fight with Irogotu.

## Combat

| | |
|---|---|
| Class | Undead |
| HP | 61 |
| XP when defeated | 123 |
| Damage | 2 to 5 |
| AC | 50 |
| BC | 70 |
| DR | 4 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 23% (×3.0) |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Irogotu's necklace](../items/neck_irogotu.md) | 100% | 1 |
| [Gandir's ring](../items/ring_gandir.md) | 100% | 1 |
| [Regular potion of health](../items/health.md) | 100% | 1 |

## Dialogue simulator

Set your quest stages and items, then talk to Irogotu. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/irogotu.json" data-npc="Irogotu" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-irogotu"></span>**`irogotu`** Irogotu: “Well hello there. Another adventurer coming to steal my bounty. This is MY CAVE. The treasure will be MINE!”

    - “Did you kill Gandir?” *(if reached stage 10 of [Fallen friends](../quests/jan.md#stage-10))* → [irogotu1](#d-irogotu1)

    <span id="d-irogotu1"></span>**`irogotu1`** Irogotu: “That whelp Gandir? He was in my way. I merely used him as a tool to dig deeper into the cave.”

    - Next → [irogotu2](#d-irogotu2)

    <span id="d-irogotu2"></span>**`irogotu2`** Irogotu: “Besides, I never really liked him anyway.”

    - “I guess he deserved to die. Did he have a ring on him?” → [irogotu3](#d-irogotu3)
    - “Jan mentioned something about a ring?” → [irogotu3](#d-irogotu3)

    <span id="d-irogotu3"></span>**`irogotu3`** Irogotu: “NO! You cannot have it. It's mine! And who are you anyway kid, coming down here to disturb me?!”

    - “I'm not a kid anymore! Now give me that ring!” → [irogotu4](#d-irogotu4)
    - “Give me that ring and we might both come out of here alive.” → [irogotu4](#d-irogotu4)

    <span id="d-irogotu4"></span>**`irogotu4`** Irogotu: “No. If you want it you will have to take it from me by force, and I should tell you that my powers are great. Besides, you probably wouldn't dare fight me anyway.”

    - “Very well, let's see who dies here.” → *fight starts*
    - “By the Shadow, Gandir will be avenged.” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect)<br>Dialogue: 1 line changed |

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
    | Entry ID | `irogotu` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `pitcave_boss` |
    | Loot table | `irogotu` |
    | Conversation | `irogotu` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_liches:0` |
    | Defined in | `res/raw/monsterlist_crossglen_animals.json` |

    Raw data:

    ```json
    {
     "id": "irogotu",
     "name": "Irogotu",
     "iconID": "monsters_liches:0",
     "maxHP": 61,
     "unique": 1,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 2,
      "max": 5
     },
     "spawnGroup": "pitcave_boss",
     "phraseID": "irogotu",
     "droplistID": "irogotu",
     "attackCost": 3,
     "attackChance": 50,
     "criticalSkill": 40,
     "criticalMultiplier": 3.0,
     "blockChance": 70,
     "damageResistance": 4
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=irogotu.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=irogotu.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=irogotu.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=irogotu.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
