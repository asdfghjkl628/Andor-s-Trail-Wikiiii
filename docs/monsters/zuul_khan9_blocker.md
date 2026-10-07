# ![](../assets/icons/monsters/monsters_tometik3_44.png){ .sprite } Black fog

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik3_44.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `zuul_khan9_blocker` |
| **Type** | NPC |
| **Class** | Animal |
| **HP** | 1 |
| **Found in** | mushroom_m3_1, mywildcave4 |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mushroom_m3_1](../maps/mushroom_m3_1.md) | – | 1 | – |
| [mywildcave4](../maps/mywildcave4.md) | – | 1 | – |


## Quests

- [Fungi panic](../quests/fungi_panic.md): stages 169, 170

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Black fog. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/zuul_khan9_blocker.json" data-npc="Black fog" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-zuul_khan9_blocker"></span>**`zuul_khan9_blocker`** Black fog: “You shall not pass.”

    - “Your master is dead. Begone!” *(if killed 1× [Zuul'khan](../monsters/zuul_khan9.md); NOT killed 1× [Zuul'khan](../monsters/gison_thiefboss.md))* → [zuul_khan9_blocker_20](#d-zuul_khan9_blocker_20)
    - “Your master is dead forever now. Begone!” *(if killed 1× [Zuul'khan](../monsters/gison_thiefboss.md))* → [zuul_khan9_blocker_10](#d-zuul_khan9_blocker_10)
    - “Why me? What have I done to deserve this?” → *conversation ends*

    <span id="d-zuul_khan9_blocker_20"></span>**`zuul_khan9_blocker_20`** Black fog: “No. We were expecting you to say so. We were told not to leave.” — **effects:** sets stage 169 of [Fungi panic](../quests/fungi_panic.md#stage-169)

    - “I need to know what's behind this, but obviously I can't get past that way. I had best try to find another way.” *(if NOT reached stage 40 of [A raid for a cookbook](../quests/gison_cookbook.md#stage-40))* → *conversation ends*
    - “Well, you are learning.” → *conversation ends*

    <span id="d-zuul_khan9_blocker_10"></span>**`zuul_khan9_blocker_10`** [Dummy NPC](../monsters/none.md): “The black fog hisses and instantly vanishes.” — **effects:** removes monsters from mywildcave4, removes monsters from mushroom_m3_1, sets stage 170 of [Fungi panic](../quests/fungi_panic.md#stage-170)

    - “At last.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zuul_khan9_blocker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zuul_khan9_blocker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zuul_khan9_blocker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zuul_khan9_blocker.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `zuul_khan9_blocker` |
    | Spawn group | `zuul_khan9_blocker` |
    | Loot table | – |
    | Conversation | `zuul_khan9_blocker` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik3:44` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "zuul_khan9_blocker",
     "name": "Black fog",
     "iconID": "monsters_tometik3:44",
     "moveCost": 5,
     "monsterClass": "animal",
     "spawnGroup": "zuul_khan9_blocker",
     "phraseID": "zuul_khan9_blocker"
    }
    ```


<small>Data from v0.8.18</small>
