# ![](../assets/icons/monsters/monsters_tometik6_1.png){ .sprite } Road rondel

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik6_1.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `road_rondel_blocker` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 120 |
| **XP when killed** | 310 |
| **Found in** | Wexlow Village |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 120 |
| Damage | 2 to 4 |
| Attack chance | 60 |
| Block chance | 200 |
| Damage resistance | 8 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 7 to 77 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [wayto_feygard_duleian_1](../maps/wayto_feygard_duleian_1.md) | Wexlow Village | 1 | – |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Road rondel. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/road_rondel_blocker_ip.json" data-npc="Road rondel" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-road_rondel_blocker_ip"></span>**`road_rondel_blocker_ip`** Road rondel: “Halt!”

    - “Wait a minute. Don't I know you from somewhere?” → [road_rondel_blocker_halt](#d-road_rondel_blocker_halt)

    <span id="d-road_rondel_blocker_halt"></span>**`road_rondel_blocker_halt`** Road rondel: “I said "halt"!”

    - “Yes! I know you. But I am pretty damn sure that I killed you back there [pointing southeast] on the bridge.” → [road_rondel_blocker_brother_1](#d-road_rondel_blocker_brother_1)

    <span id="d-road_rondel_blocker_brother_1"></span>**`road_rondel_blocker_brother_1`** Road rondel: “You killed my brother?!”

    - “Yes, it appears so, but I had no choice. You see, he wouldn't get out of my way. Kind of like you.” → [road_rondel_blocker_brother_2](#d-road_rondel_blocker_brother_2)

    <span id="d-road_rondel_blocker_brother_2"></span>**`road_rondel_blocker_brother_2`** Road rondel: “I am disheartened and full of rage hearing of this.”

    - “Well, if it's any consolation, you are about to join him.” *(if NOT carry 1× [Gem of warmth](../items/gem_fire.md))* → *fight starts*
    - “Step aside before I am forced to reunite you two.” *(if carry 1× [Gem of warmth](../items/gem_fire.md))* → [road_rondel_blocker_brother_3](#d-road_rondel_blocker_brother_3)

    <span id="d-road_rondel_blocker_brother_3"></span>**`road_rondel_blocker_brother_3`** Road rondel: “Of course.” — **effects:** removes monsters from wayto_feygard_duleian_1, spawns monsters on wayto_feygard_duleian_1




## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=road_rondel_blocker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=road_rondel_blocker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=road_rondel_blocker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=road_rondel_blocker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `road_rondel_blocker` |
    | Spawn group | `road_rondel_blocker` |
    | Loot table | `guynmart_drp_robber` |
    | Conversation | `road_rondel_blocker_ip` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik6:1` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "road_rondel_blocker",
     "name": "Road rondel",
     "iconID": "monsters_tometik6:1",
     "maxHP": 120,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 2,
      "max": 4
     },
     "phraseID": "road_rondel_blocker_ip",
     "droplistID": "guynmart_drp_robber",
     "attackCost": 4,
     "attackChance": 60,
     "blockChance": 200,
     "damageResistance": 8
    }
    ```


<small>Data from v0.8.18</small>
