# ![](../assets/icons/monsters/monsters_rltiles1_122.png){ .sprite } Tesrekan

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_122.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `tesrekan` |
| **Type** | NPC |
| **Class** | Undead |
| **HP** | 350 |
| **XP when killed** | 852 |
| **Found in** | waterwayacave4 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 350 |
| Damage | 8 to 16 |
| Attack chance | 180 |
| Block chance | 140 |
| Damage resistance | 8 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Crit chance | 9% |

**On hit:** On target: Fear (magnitude 3, 5 rounds, 50% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Tesrekan's bone](../items/tesrekanbone.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [waterwayacave4](../maps/waterwayacave4.md) | – | 1 | – |


## Quests

- [Just the beginning](../quests/waterwayacave.md): stages 50

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Tesrekan. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/tesrekan.json" data-npc="Tesrekan" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-tesrekan"></span>**`tesrekan`** Tesrekan: “Ah, another puny mortal that has come to die and serve Tesrekan.” — **effects:** sets stage 50 of [Just the beginning](../quests/waterwayacave.md#stage-50)

    - Next → [tesrekan_1](#d-tesrekan_1)

    <span id="d-tesrekan_1"></span>**`tesrekan_1`** Tesrekan: “I will kill you, and then you will join my army of undead servants and soldiers.”

    - “I just destroyed a lot of your army.” → [tesrekan_2](#d-tesrekan_2)
    - “If you are so powerful why do you need an army?” → [tesrekan_3](#d-tesrekan_3)
    - “I have destroyed others like you, and I will destroy you!” → *fight starts*

    <span id="d-tesrekan_2"></span>**`tesrekan_2`** Tesrekan: “All the more reason for me to kill you and replenish what you have destroyed!”

    - “An army with no leader is not an army, so I will destroy you!” → *fight starts*

    <span id="d-tesrekan_3"></span>**`tesrekan_3`** Tesrekan: “Insolent human! I will make you my undead slave!”

    - “You don't have what it takes!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tesrekan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tesrekan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tesrekan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tesrekan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `tesrekan` |
    | Spawn group | `tesrekan` |
    | Loot table | `tesrekandrop` |
    | Conversation | `tesrekan` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:122` |
    | Defined in | `res/raw/monsterlist_graveyard1.json` |

    Raw data:

    ```json
    {
     "id": "tesrekan",
     "name": "Tesrekan",
     "iconID": "monsters_rltiles1:122",
     "maxHP": 350,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 8,
      "max": 16
     },
     "spawnGroup": "tesrekan",
     "phraseID": "tesrekan",
     "droplistID": "tesrekandrop",
     "attackCost": 3,
     "attackChance": 180,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 140,
     "damageResistance": 8,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "fear",
        "magnitude": 3,
        "duration": 5,
        "chance": "50"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
