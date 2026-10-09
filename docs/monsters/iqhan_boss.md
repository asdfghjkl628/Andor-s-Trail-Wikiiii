---
description: "Iqhan chaos enslaver is an NPC who can also be fought in Andor's Trail, found in Pwcave 4."
---

# ![](../assets/icons/monsters/monsters_rltiles1_5.png){ .sprite } Iqhan chaos enslaver

**Where to find Iqhan chaos enslaver:** [Pwcave 4](../maps/pwcave4.md#pin-npc-iqhan_boss)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_5.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Pwcave 4 |
| **Class** | Undead |
| **HP** | 120 |
| **XP when defeated** | 339 |
| **Entry ID** | `iqhan_boss` |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 120 |
| XP when defeated | 339 |
| Damage | 2 to 13 |
| Attack chance | 170 |
| Block chance | 75 |
| Damage resistance | 2 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 30 |
| Critical multiplier | 2.0 |
| Critical hit chance | 19% |

**On hit:** On target: [Chaotic grip](../conditions/chaotic_grip.md) (magnitude 7, 5 rounds, 50% chance); [Chaotic curse](../conditions/chaotic_curse.md) (magnitude 3, 5 rounds, 50% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 50 to 100 |
| [Iqhan pendant](../items/iqhan_pendant.md) | 100% | 1 |
| [Dagger of the Shadow priests](../items/dagger_shadow_priests.md) | 100% | 1 |
| [Regular potion of health](../items/health.md) | 100% | 5 to 7 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Pwcave 4](../maps/pwcave4.md) | – | 1 | – |

## Dialogue simulator

Set your quest stages and items, then talk to Iqhan chaos enslaver. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/iqhan_boss.json" data-npc="Iqhan chaos enslaver" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-iqhan_boss"></span>**`iqhan_boss`** Iqhan chaos enslaver: “*wheeze*”

    - Next → [iqhan_boss_1](#d-iqhan_boss_1)

    <span id="d-iqhan_boss_1"></span>**`iqhan_boss_1`** Iqhan chaos enslaver: “[The figure points its finger towards you, in what looks to be an order for the nearby thralls to attack you]”

    - “Fight!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Chaotic curse](../conditions/chaotic_curse.md) (magnitude 3, 5 rounds, 50% chance) → (magnitude 3, 5 rounds, 50% chance)<br>On hit, condition on target: [Chaotic grip](../conditions/chaotic_grip.md) (magnitude 7, 5 rounds, 50% chance) → (magnitude 7, 5 rounds, 50% chance)<br>Dialogue: 1 line changed<br>· text: “(The figure points its finger towards you, in what looks to be an ord…” → “[The figure points its finger towards you, in what looks to be an ord…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `iqhan_boss` |
    | Spawn group | `iqhan_boss` |
    | Loot table | `iqhan_boss` |
    | Conversation | `iqhan_boss` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:5` |
    | Defined in | `res/raw/monsterlist_v0610_monsters2.json` |

    Raw data:

    ```json
    {
     "id": "iqhan_boss",
     "name": "Iqhan chaos enslaver",
     "iconID": "monsters_rltiles1:5",
     "maxHP": 120,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 2,
      "max": 13
     },
     "spawnGroup": "iqhan_boss",
     "phraseID": "iqhan_boss",
     "droplistID": "iqhan_boss",
     "attackCost": 3,
     "attackChance": 170,
     "criticalSkill": 30,
     "criticalMultiplier": 2.0,
     "blockChance": 75,
     "damageResistance": 2,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "chaotic_grip",
        "magnitude": 7,
        "duration": 5,
        "chance": "50"
       },
       {
        "condition": "chaotic_curse",
        "magnitude": 3,
        "duration": 5,
        "chance": "50"
       }
      ]
     }
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_boss.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_boss.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_boss.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=iqhan_boss.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
