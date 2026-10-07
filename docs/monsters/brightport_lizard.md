# ![](../assets/icons/monsters/monsters_johny_1.png){ .sprite } Green-claw-emyro

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_johny_1.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `brightport_lizard` |
| **Type** | NPC |
| **Class** | Reptile |
| **HP** | 160 |
| **XP when killed** | 600 |
| **Found in** | Burial cave, Greenscale tribe |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 160 |
| Damage | 14 to 36 |
| Attack chance | 180 |
| Block chance | 160 |
| Damage resistance | 4 |
| Max AP | 12 |
| Attack cost | 4 AP |
| Attacks per turn | 3 |
| Move cost | 4 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Lizardman bone](../items/brightport_bone.md) | 35% | 1 to 2 |
| [Gold coins](../items/gold.md) | 100% | 30 to 45 |
| [Lizard skin](../items/lizard_skin.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [brightport_cave10](../maps/brightport_cave10.md) | Burial cave | 1 | – |
| [brightport_lizard2](../maps/brightport_lizard2.md) | Greenscale tribe | 1 | – |


## Quests that count kills

- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-120) with stepping on a trigger on [brightport_cave17](../maps/brightport_cave17.md) checks that you've killed at least 1


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Green-claw-emyro. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_emyro_selector.json" data-npc="Green-claw-emyro" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_emyro_selector"></span>**`brightport_emyro_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 95 of [The balance of scales](../quests/brightport_lizard.md#stage-95))* → [brightport_emyro0](#d-brightport_emyro0)
    - Next *(if reached stage 95 of [The balance of scales](../quests/brightport_lizard.md#stage-95))* → [brightport_emyro1](#d-brightport_emyro1)

    <span id="d-brightport_emyro0"></span>**`brightport_emyro0`** Green-claw-emyro: “Hss, speak to the leader.”


    <span id="d-brightport_emyro1"></span>**`brightport_emyro1`** Green-claw-emyro: “You are friend of us now.”




## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_lizard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_lizard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_lizard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_lizard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `brightport_lizard` |
    | Spawn group | `lizard2` |
    | Loot table | `brightport_greenlizard` |
    | Conversation | `brightport_emyro_selector` |
    | Faction | `lizardfight` |
    | Movement | helpOthers |
    | Icon | `monsters_johny:1` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_lizard",
     "name": "Green-claw-emyro",
     "iconID": "monsters_johny:1",
     "maxHP": 160,
     "maxAP": 12,
     "moveCost": 4,
     "unique": 1,
     "monsterClass": "reptile",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 14,
      "max": 36
     },
     "spawnGroup": "lizard2",
     "faction": "lizardfight",
     "phraseID": "brightport_emyro_selector",
     "droplistID": "brightport_greenlizard",
     "attackCost": 4,
     "attackChance": 180,
     "blockChance": 160,
     "damageResistance": 4
    }
    ```


<small>Data from v0.8.18</small>
