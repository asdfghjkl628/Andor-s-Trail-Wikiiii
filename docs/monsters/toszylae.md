---
description: "Toszylae is an NPC you can also fight in Andor's Trail, found in Waytobrimhavencave 3a. Starts I have it in me."
---

# ![](../assets/icons/monsters/monsters_liches_1.png){ .sprite } Toszylae

**Where to find Toszylae:** [Waytobrimhavencave 3a](../maps/waytobrimhavencave3a.md#pin-npc-toszylae)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_liches_1.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Role** | Starts [I have it in me](../quests/maggots.md) |
| **Found in** | Waytobrimhavencave 3a |
| **Class** | Undead |
| **HP** | 207 |
| **XP when defeated** | 449 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "You can fight Toszylae"
    Answering “You will pay for what you did to me!” starts a fight with Toszylae.

## Combat

| | |
|---|---|
| Class | Undead |
| HP | 207 |
| XP when defeated | 449 |
| Damage | 2 to 7 |
| AC | 80 |
| BC | 120 |
| DR | 4 |
| Attacks per turn | 4 (2 AP each, 8 AP) |
| Crit chance | 23% (×2.0) |

**Its hits:** Heal HP: 6; On target: [Minor weapon feebleness](../conditions/feebleness_minor.md) (magnitude 3, 3 rounds, 20% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 0 to 20 |
| [Demon heart](../items/toszylae_heart.md) | 100% | 1 |
| [Regular potion of health](../items/health.md) | 100% | 5 to 7 |
| [Polished sparkling gem](../items/gem5.md) | 100% | 2 |
| [Small rock](../items/rock.md) | 100% | 1 |

## Quests

- [An involuntary carrier](../quests/toszylae.md): stage 50
- [I have it in me](../quests/maggots.md): stage 10

## Dialogue simulator

Talk to Toszylae as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/toszylae.json" data-npc="Toszylae" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (11 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-toszylae"></span>**`toszylae`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 50 of [An involuntary carrier](../quests/toszylae.md#stage-50))* → [toszylae_10](#d-toszylae_10)
    - branch 2 → [toszylae_1](#d-toszylae_1)

    <span id="d-toszylae_10"></span>**`toszylae_10`** Toszylae: “[The lich seems to enjoy seeing you in pain]”

    - “You will pay for what you did to me!” → *fight starts*

    <span id="d-toszylae_1"></span>**`toszylae_1`** Toszylae: “[The lich looks at you with its burning eyes, and glances at the remains of the guardian you defeated]”

    - Next → [toszylae_2](#d-toszylae_2)

    <span id="d-toszylae_2"></span>**`toszylae_2`** Toszylae: “Kazaul'te vaarmun iktel urul. Klatam ku turum Kazaul'te?”

    - Next → [toszylae_3](#d-toszylae_3)

    <span id="d-toszylae_3"></span>**`toszylae_3`** Toszylae: “[The lich raises its hands towards the ceiling, chanting something you cannot understand]”

    - Next → [toszylae_4](#d-toszylae_4)

    <span id="d-toszylae_4"></span>**`toszylae_4`** Toszylae: “[While chanting, it slowly lowers its hands forward, until pointing directly at you]”

    - Next → [toszylae_5](#d-toszylae_5)

    <span id="d-toszylae_5"></span>**`toszylae_5`** Toszylae: “Klatam ku turum Kazaul'te.”

    - Next → [toszylae_6](#d-toszylae_6)

    <span id="d-toszylae_6"></span>**`toszylae_6`** Toszylae: “[As if having swallowed a thousand needles, you are suddenly stricken with a cascading series of spikes of pain throughout your stomach]” — **effects:** applies condition rotworm, sets stage 10 of [I have it in me](../quests/maggots.md#stage-10), sets stage 50 of [An involuntary carrier](../quests/toszylae.md#stage-50)

    - Next → [toszylae_7](#d-toszylae_7)

    <span id="d-toszylae_7"></span>**`toszylae_7`** Toszylae: “[You start to feel nauseous, and your stomach turns and twists - as if it has a life of its own]”

    - Next → [toszylae_8](#d-toszylae_8)

    <span id="d-toszylae_8"></span>**`toszylae_8`** Toszylae: “[The pain increases slightly, and you start to realize that something is moving inside of you]”

    - Next → [toszylae_9](#d-toszylae_9)

    <span id="d-toszylae_9"></span>**`toszylae_9`** Toszylae: “[The lich must have infected you with something]”

    - “What is happening to me!?” → [toszylae_10](#d-toszylae_10)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Minor weapon feebleness](../conditions/feebleness_minor.md) (magnitude 3, 3 rounds, 20% chance) → (magnitude 3, 3 rounds, 20% chance)<br>Dialogue: 9 lines changed<br>· text: “(The lich looks at you with its burning eyes, and glances at the rema…” → “[The lich looks at you with its burning eyes, and glances at the rema…”<br>· text: “(The lich raises its hands towards the ceiling, chanting something yo…” → “[The lich raises its hands towards the ceiling, chanting something yo…” |

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
    | Entry ID | `toszylae` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `toszylae` |
    | Loot table | `toszylae` |
    | Conversation | `toszylae` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_liches:1` |
    | Defined in | `res/raw/monsterlist_v0611_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "toszylae",
     "name": "Toszylae",
     "iconID": "monsters_liches:1",
     "maxHP": 207,
     "maxAP": 8,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 2,
      "max": 7
     },
     "spawnGroup": "toszylae",
     "phraseID": "toszylae",
     "droplistID": "toszylae",
     "attackCost": 2,
     "attackChance": 80,
     "criticalSkill": 40,
     "criticalMultiplier": 2.0,
     "blockChance": 120,
     "damageResistance": 4,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 6,
       "max": 6
      },
      "conditionsTarget": [
       {
        "condition": "feebleness_minor",
        "magnitude": 3,
        "duration": 3,
        "chance": "20"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=toszylae.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=toszylae.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=toszylae.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=toszylae.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
