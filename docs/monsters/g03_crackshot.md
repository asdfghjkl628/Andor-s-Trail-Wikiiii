---
description: "Crackshot is an NPC you can also fight in Andor's Trail, found in Crackshot hideout 3."
---

# ![](../assets/icons/monsters/monsters_ld1_80.png){ .sprite } Crackshot

**Where to find Crackshot:** [Crackshot hideout 3](../maps/crackshot_hideout3.md#pin-npc-g03_crackshot)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_80.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Crackshot hideout 3 |
| **Class** | Humanoid |
| **HP** | 133 |
| **XP when defeated** | 271 |
| **Introduced** | [v0.7.8](../versions/0.7.8.md) |

</div>

!!! warning "You can fight Crackshot"
    Answering “The Feygard soldiers will be avenged!” starts a fight with Crackshot.

    Answering “Hah! Let's see if you're as strong as Umar has said.” starts a fight with Crackshot.

    Crackshot turns hostile if you fall out with their faction.

## Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 133 |
| XP when defeated | 271 |
| Damage | 5 to 11 |
| AC | 110 |
| BC | 100 |
| DR | 4 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 15% (×3.0) |

**Its hits:** On self: [Combo](../conditions/g03_combo.md) (magnitude 1, 1 round, 25% chance)

**When you hit it:** On self: [Concentration](../conditions/g03_concentration.md) (magnitude 1, 2 rounds, 33% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 10 to 125 |
| [Villain's leather armor](../items/armour_leather_villain.md) | 20% | 1 |
| [Yatagan](../items/sword_g03_crackshot.md) | 100% | 1 |
| [Key of Luthor](../items/g03_luthor.md) | 100% | 1 |

## Quests that count defeats

- [Thieves story flags (hidden flag)](../quests/thieves_hidden.md#stage-90) with [Feygard patrol sergeant](../monsters/g03_sergeant.md) ([Crackshot hideout 3](../maps/crackshot_hideout3.md)) checks that this enemy has been defeated.
- [The ruthless Crackshot](../quests/Thieves03.md#stage-35) with stepping on a trigger on [Crackshot hideout 3](../maps/crackshot_hideout3.md) checks that this enemy has been defeated.
- A conversation with stepping on a trigger on [Crackshot hideout 3](../maps/crackshot_hideout3.md) checks that this enemy has been defeated.

## Dialogue simulator

Set your quest stages and items, then talk to Crackshot. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guild03_crackshot_1.json" data-npc="Crackshot" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guild03_crackshot_1"></span>**`guild03_crackshot_1`** [Crackshot](../monsters/g03_crackshot.md): “Oh ho! Welcome to my base, kid.”

    - “Hmm .... This is not the place where I would choose to live.” → [guild03_crackshot_2a](#d-guild03_crackshot_2a)
    - “You are under arrest for the crimes you've committed against Feygard!” → [guild03_crackshot_2b](#d-guild03_crackshot_2b)

    <span id="d-guild03_crackshot_2a"></span>**`guild03_crackshot_2a`** Crackshot: “Haven't you realized yet? Your life is not going to be much longer.” — **effects:** faction “crackshot” set to -10

    - “Hah! Let's see if you're as strong as Umar has said.” → *fight starts*
    - “Prepare to die!” → *fight starts*

    <span id="d-guild03_crackshot_2b"></span>**`guild03_crackshot_2b`** Crackshot: “*laugh* Are you serious?”

    - Next → [guild03_crackshot_3](#d-guild03_crackshot_3)

    <span id="d-guild03_crackshot_3"></span>**`guild03_crackshot_3`** Crackshot: “Do you really believe such words are worth anything here?”

    - Next → [guild03_crackshot_4](#d-guild03_crackshot_4)

    <span id="d-guild03_crackshot_4"></span>**`guild03_crackshot_4`** Crackshot: “Let's see if you can arrest me after I have finished with you!” — **effects:** faction “crackshot” set to -10

    - “The Feygard soldiers will be avenged!” → *fight starts*
    - “Your head will serve as proof!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 5 lines added |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

- `g03_crackshot` belongs to the faction `crackshot`. The game treats any character as hostile once your standing with its faction is below zero.

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `g03_crackshot` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `g03_crackshot` |
    | Loot table | `drop_g03_crackshot` |
    | Conversation | `guild03_crackshot_1` |
    | Faction | `crackshot` |
    | Movement | protectSpawn |
    | Icon | `monsters_ld1:80` |
    | Defined in | `res/raw/monsterlist_omicronrg9.json` |

    Raw data:

    ```json
    {
     "id": "g03_crackshot",
     "name": "Crackshot",
     "iconID": "monsters_ld1:80",
     "maxHP": 133,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 5,
      "max": 11
     },
     "spawnGroup": "g03_crackshot",
     "faction": "crackshot",
     "phraseID": "guild03_crackshot_1",
     "droplistID": "drop_g03_crackshot",
     "attackCost": 5,
     "attackChance": 110,
     "criticalSkill": 20,
     "criticalMultiplier": 3.0,
     "blockChance": 100,
     "damageResistance": 4,
     "hitEffect": {
      "conditionsSource": [
       {
        "condition": "g03_combo",
        "magnitude": 1,
        "duration": 1,
        "chance": "25"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "g03_concentration",
        "magnitude": 1,
        "duration": 2,
        "chance": "33"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_crackshot.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_crackshot.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_crackshot.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_crackshot.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
