# ![](../assets/icons/monsters/monsters_rltiles2_55.png){ .sprite } Mountain Sheep

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_55.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `bwm_sheep1` |
| **Type** | NPC |
| **Class** | Animal |
| **HP** | 30 |
| **XP when killed** | 33 |
| **Found in** | Blackwater Mountain |
| **Introduced** | [v0.8.10](../versions/0.8.10.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 30 |
| Damage | 1 to 5 |
| Attack chance | 60 |
| Block chance | 20 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 3 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Raw lamb meat](../items/lamb_meat_raw.md) | 20% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [bwmfill3](../maps/bwmfill3.md) | Blackwater Mountain | 10 | – |
| [bwmfill_tunlon](../maps/bwmfill_tunlon.md) | Blackwater Mountain | 2 | – |


## Quests that count kills

- A conversation with [Mountain Sheep](../monsters/bwm_sheep1.md) ([bwmfill3](../maps/bwmfill3.md)) checks that you've killed at least 1
- A conversation with stepping on a trigger on [bwmfill3](../maps/bwmfill3.md), [Tunlon](../monsters/tunlon.md) ([bwmfill3](../maps/bwmfill3.md)) checks that you've killed at least 1
- A conversation with [Tunlon](../monsters/tunlon.md) ([bwmfill3](../maps/bwmfill3.md)) checks that you've killed at least 1


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Mountain Sheep. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/bwm_sheep_dialogue.json" data-npc="Mountain Sheep" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-bwm_sheep_dialogue"></span>**`bwm_sheep_dialogue`** Mountain Sheep: “Baa!”

    - “[Pet]” *(if NOT killed 1× [Mountain Sheep](../monsters/bwm_sheep1.md))* → *conversation ends*
    - “You look tasty - attack!” *(if NOT killed 1× [Mountain Sheep](../monsters/bwm_sheep1.md); random chance (20%))* → *fight starts*
    - “Attack!” *(if killed 1× [Mountain Sheep](../monsters/bwm_sheep1.md))* → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.8.10](../versions/0.8.10.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_sheep1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_sheep1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_sheep1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_sheep1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `bwm_sheep1` |
    | Spawn group | `bwm_sheep` |
    | Loot table | `bwm_sheep` |
    | Conversation | `bwm_sheep_dialogue` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_rltiles2:55` |
    | Defined in | `res/raw/monsterlist_bwmfill.json` |

    Raw data:

    ```json
    {
     "id": "bwm_sheep1",
     "name": "Mountain Sheep",
     "iconID": "monsters_rltiles2:55",
     "maxHP": 30,
     "maxAP": 10,
     "moveCost": 3,
     "monsterClass": "animal",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 1,
      "max": 5
     },
     "spawnGroup": "bwm_sheep",
     "phraseID": "bwm_sheep_dialogue",
     "droplistID": "bwm_sheep",
     "attackCost": 5,
     "attackChance": 60,
     "blockChance": 20,
     "damageResistance": 0
    }
    ```


<small>Data from v0.8.18</small>
