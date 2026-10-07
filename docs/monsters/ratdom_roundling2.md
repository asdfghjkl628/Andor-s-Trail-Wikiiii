# ![](../assets/icons/monsters/monsters_rltiles1_134.png){ .sprite } Roundling

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_134.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `ratdom_roundling2` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 200 |
| **XP when killed** | 241 |
| **Found in** | Entry |
| **Introduced** | [v0.8.5](../versions/0.8.5.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 200 |
| Damage | 10 to 30 |
| Attack chance | 120 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_448](../maps/ratdom_maze_448.md) | Entry | 5 | appears later in a quest |


## Quests

- [Yellow is it](../quests/ratdom_quest.md): stages 960
- [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md): stages 13

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Roundling. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/ratdom_roundling2.json" data-npc="Roundling" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ratdom_roundling2"></span>**`ratdom_roundling2`** Roundling: “A thief who thinks to get through with our treasure, is due to give his life upon a strife, and all his stolen goods too.”

    - “Eh, let us think a minute.” → *conversation ends*
    - “Well, OK. We have no chance against so many roundlings.” → [ratdom_roundling2_10](#d-ratdom_roundling2_10)
    - “Never - attack!” → [ratdom_roundling2_90](#d-ratdom_roundling2_90)

    <span id="d-ratdom_roundling2_10"></span>**`ratdom_roundling2_10`** [Clevred](../monsters/ratdom_rat.md): “Coward! You didn't even try.”

    - “Never call me coward! Attack!” → [ratdom_roundling2_90](#d-ratdom_roundling2_90)
    - “They are too many for us, we would be killed. Let's give up the artifact.” → [ratdom_roundling2_12](#d-ratdom_roundling2_12)

    <span id="d-ratdom_roundling2_90"></span>**`ratdom_roundling2_90`** *(silent check: the first matching branch below is taken)* — **effects:** faction “fct_ratdom_roundling2” set to -10

    - branch 1 → *fight starts*

    <span id="d-ratdom_roundling2_12"></span>**`ratdom_roundling2_12`** Roundling: “Never! I'd rather die!”

    - “If you think so, then let's attack!” → [ratdom_roundling2_90](#d-ratdom_roundling2_90)
    - “Die you will, if you can't let go of it. I will leave it behind.” → [ratdom_roundling2_20](#d-ratdom_roundling2_20)

    <span id="d-ratdom_roundling2_20"></span>**`ratdom_roundling2_20`** Roundling: “I see. I thought you were braver. Go then, I don't want to see you again!” — **effects:** sets stage 960 of [Yellow is it](../quests/ratdom_quest.md#stage-960), clears stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10), clears stage 11 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-11), sets stage 13 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-13), removes monsters from ratdom_maze_627, removes monsters from ratdom_maze_627, removes monsters from ratdom_maze_448, removes monsters from home, removes monsters from ratdom_bwm1




## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_roundling2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_roundling2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_roundling2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_roundling2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `ratdom_roundling2` |
    | Spawn group | `ratdom_roundling2` |
    | Loot table | – |
    | Conversation | `ratdom_roundling2` |
    | Faction | `fct_ratdom_roundling2` |
    | Movement | helpOthers |
    | Icon | `monsters_rltiles1:134` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_roundling2",
     "name": "Roundling",
     "iconID": "monsters_rltiles1:134",
     "maxHP": 200,
     "monsterClass": "humanoid",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 10,
      "max": 30
     },
     "spawnGroup": "ratdom_roundling2",
     "faction": "fct_ratdom_roundling2",
     "phraseID": "ratdom_roundling2",
     "attackCost": 5,
     "attackChance": 120
    }
    ```


<small>Data from v0.8.18</small>
