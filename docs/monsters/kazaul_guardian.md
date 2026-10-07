---
description: "Kazaul guardian is an NPC who can also be fought in Andor's Trail, found in blackwater_mountain42."
---

# ![](../assets/icons/monsters/monsters_rltiles1_42.png){ .sprite } Kazaul guardian

**Where to find Kazaul guardian:** [blackwater_mountain42](../maps/blackwater_mountain42.md#pin-npc-kazaul_guardian)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_42.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | blackwater_mountain42 |
| **Class** | Demon |
| **HP** | 95 |
| **XP when defeated** | 175 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `kazaul_guardian` |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Demon |
| HP | 95 |
| XP when defeated | 175 |
| Damage | 3 to 8 |
| Attack chance | 70 |
| Block chance | 90 |
| Damage resistance | 3 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 40 |
| Critical multiplier | 2.0 |
| Critical hit chance | 23% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 52 |
| [Polished gem](../items/gem3.md) | 100% | 1 |
| [Regular potion of health](../items/health.md) | 100% | 2 |
| [Shadow of the slayer](../items/shadow_slayer.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [blackwater_mountain42](../maps/blackwater_mountain42.md) | – | 1 | – |

## Quests

- [Lights in the dark](../quests/kazaul.md): stage 50

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Kazaul guardian. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/kazaul_guardian.json" data-npc="Kazaul guardian" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-kazaul_guardian"></span>**`kazaul_guardian`** Kazaul guardian: “Kazaul...”

    - “What?” → [kazaul_guardian_1](#d-kazaul_guardian_1)
    - “Kazaul, destroyer of bright dreams.” *(if reached stage 40 of [Lights in the dark](../quests/kazaul.md#stage-40))* → [kazaul_guardian_2](#d-kazaul_guardian_2)

    <span id="d-kazaul_guardian_1"></span>**`kazaul_guardian_1`** Kazaul guardian: “[The guardian looks completely unaware of your presence]”


    <span id="d-kazaul_guardian_2"></span>**`kazaul_guardian_2`** Kazaul guardian: “[The guardian looks down upon you with its burning eyes]”

    - “Kazaul, defiler of the Elytharan Temple.” → [kazaul_guardian_3](#d-kazaul_guardian_3)

    <span id="d-kazaul_guardian_3"></span>**`kazaul_guardian_3`** Kazaul guardian: “[You see the burning eyes of the guardian instantly turn into a dark red haze]” — **effects:** sets stage 50 of [Lights in the dark](../quests/kazaul.md#stage-50)

    - “A fight, I have been waiting for this!” → *fight starts*
    - “Please don't kill me!” → *fight starts*
    - “For the Shadow!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | minor data change<br>Dialogue: 4 lines changed<br>· text: “(The guardian looks down upon you with its burning eyes)” → “[The guardian looks down upon you with its burning eyes]”<br>· text: “Kazaul..” → “Kazaul...” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `kazaul_guardian` |
    | Spawn group | `kazaul_guardian` |
    | Loot table | `kazaul_guardian` |
    | Conversation | `kazaul_guardian` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:42` |
    | Defined in | `res/raw/monsterlist_v069_monsters.json` |

    Raw data:

    ```json
    {
     "id": "kazaul_guardian",
     "name": "Kazaul guardian",
     "iconID": "monsters_rltiles1:42",
     "maxHP": 95,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "demon",
     "attackDamage": {
      "min": 3,
      "max": 8
     },
     "spawnGroup": "kazaul_guardian",
     "phraseID": "kazaul_guardian",
     "droplistID": "kazaul_guardian",
     "attackCost": 5,
     "attackChance": 70,
     "criticalSkill": 40,
     "criticalMultiplier": 2.0,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_guardian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_guardian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_guardian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_guardian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
