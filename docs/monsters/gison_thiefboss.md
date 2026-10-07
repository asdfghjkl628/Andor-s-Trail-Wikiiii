# ![](../assets/icons/monsters/monsters_rltiles2_88.png){ .sprite } Zuul'khan

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_88.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `gison_thiefboss` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 175 |
| **XP when killed** | 266 |
| **Found in** | mywildcave4 |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 175 |
| Damage | 3 to 6 |
| Attack chance | 120 |
| Block chance | 60 |
| Damage resistance | 1 |
| Max AP | 20 |
| Attack cost | 5 AP |
| Attacks per turn | 4 |
| Move cost | 6 AP |
| Critical skill | 20 |
| Critical multiplier | 2.0 |
| Crit chance | 15% |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mywildcave4](../maps/mywildcave4.md) | – | 1 | – |


## Quests that count kills

- [Fungi panic](../quests/fungi_panic.md#stage-170) with [Black fog](../monsters/zuul_khan9_blocker.md) ([mushroom_m3_1](../maps/mushroom_m3_1.md)) checks that you've killed at least 1


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Zuul'khan. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/gison_thiefboss.json" data-npc="Zuul&#x27;khan" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-gison_thiefboss"></span>**`gison_thiefboss`** Zuul'khan: “[muttering ominous words]”

    - “Hi!” → [gison_thiefboss_10](#d-gison_thiefboss_10)

    <span id="d-gison_thiefboss_10"></span>**`gison_thiefboss_10`** Zuul'khan: “What ...? You again? How did you get in here?”

    - “I have come to retrieve a book that does not belong to you.” → [gison_thiefboss_20](#d-gison_thiefboss_20)

    <span id="d-gison_thiefboss_20"></span>**`gison_thiefboss_20`** Zuul'khan: “Ha! You made a serious error coming here. I have a use for you though.”

    - “You want me to help you?” → [gison_thiefboss_30](#d-gison_thiefboss_30)

    <span id="d-gison_thiefboss_30"></span>**`gison_thiefboss_30`** Zuul'khan: “Not exactly. My fungi leader is almost ready. It just needs to be fed some more to grow in strength.”

    - “Fed? On what?” → [gison_thiefboss_40](#d-gison_thiefboss_40)

    <span id="d-gison_thiefboss_40"></span>**`gison_thiefboss_40`** Zuul'khan: “One thing it likes is annoying children, like you. Thank you for volunteering!”

    - “Sorry, I don't think so. I will destroy you and your fungi leader!” → *fight starts*
    - “Sorry for disturbing you. I will leave immediately.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gison_thiefboss.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gison_thiefboss.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gison_thiefboss.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gison_thiefboss.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `gison_thiefboss` |
    | Spawn group | `gison_thiefboss` |
    | Loot table | – |
    | Conversation | `gison_thiefboss` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:88` |
    | Defined in | `res/raw/monsterlist_gison.json` |

    Raw data:

    ```json
    {
     "id": "gison_thiefboss",
     "name": "Zuul'khan",
     "iconID": "monsters_rltiles2:88",
     "maxHP": 175,
     "maxAP": 20,
     "moveCost": 6,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 3,
      "max": 6
     },
     "spawnGroup": "gison_thiefboss",
     "phraseID": "gison_thiefboss",
     "attackCost": 5,
     "attackChance": 120,
     "criticalSkill": 20,
     "criticalMultiplier": 2.0,
     "blockChance": 60,
     "damageResistance": 1
    }
    ```


<small>Data from v0.8.18</small>
