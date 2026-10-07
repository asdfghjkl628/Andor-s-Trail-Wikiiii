# ![](../assets/icons/monsters/monsters_dogs_4.png){ .sprite } Galmore wolf

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_dogs_4.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `mg2_wolves` |
| **Type** | NPC |
| **Class** | Animal |
| **HP** | 251 |
| **XP when killed** | 679 |
| **Found in** | Mt. Galmore |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 251 |
| Damage | 15 to 20 |
| Attack chance | 177 |
| Block chance | 153 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 3 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Crit chance | 9% |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Meat](../items/meat.md) | 20% | 1 to 3 |
| [Gold coins](../items/gold.md) | 10% | 1 to 21 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [galmore_54](../maps/galmore_54.md) | Mt. Galmore | 12 | – |
| [galmore_55](../maps/galmore_55.md) | Mt. Galmore | 1 | – |
| [galmore_64](../maps/galmore_64.md) | Mt. Galmore | 1 | – |


## Quests

- [Unusual experiences and achievements](../quests/achievements.md): stages 200
- [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md): stages 70

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Galmore wolf. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/mg2_wolves.json" data-npc="Galmore wolf" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (9 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-mg2_wolves"></span>**`mg2_wolves`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if wearing [Wolfpack's animal hide](../items/packhide.md))* → [mg2_wolves_1](#d-mg2_wolves_1)
    - branch 2 → [mg2_wolves_2](#d-mg2_wolves_2)

    <span id="d-mg2_wolves_1"></span>**`mg2_wolves_1`** Galmore wolf: “Grrr. You look like a grrreat wolf, but smell two-leggish.”

    - “Grrr, grrr” → [mg2_wolves_10](#d-mg2_wolves_10)
    - “I am the big bad wolf from the stories. Fear me!” → [mg2_wolves_10](#d-mg2_wolves_10)
    - “Move out of my way!” → *NPC leaves*

    <span id="d-mg2_wolves_2"></span>**`mg2_wolves_2`** Galmore wolf: “Grrroarrrr! It's a two-leg!” — **effects:** faction “mg2_wolves_faction” set to -666

    - “Attack!” → *fight starts*

    <span id="d-mg2_wolves_10"></span>**`mg2_wolves_10`** Galmore wolf: “You may go thrrrough herrre. No tarrrrying.” — **effects:** sets stage 200 of [Unusual experiences and achievements](../quests/achievements.md#stage-200)

    - “Agrrreed.” → *conversation ends*
    - “I am hungrrry.” *(if NOT reached stage 70 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-70))* → [mg2_wolves_20](#d-mg2_wolves_20)
    - “I am hungrrry.” *(if reached stage 70 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-70))* → [mg2_wolves_30](#d-mg2_wolves_30)

    <span id="d-mg2_wolves_20"></span>**`mg2_wolves_20`** Galmore wolf: “We can prrrovide you with good rrraw meat.”

    - “Do.” → [mg2_wolves_22](#d-mg2_wolves_22)
    - “No, thank you.” → *conversation ends*

    <span id="d-mg2_wolves_30"></span>**`mg2_wolves_30`** Galmore wolf: “We've alrrready given you. Now go.”

    - “Grrr.” → *conversation ends*
    - “That was looong ago. Long forrrgotten.” *(if 100 rounds passed since timer “mg2_wolves”)* → [mg2_wolves_40](#d-mg2_wolves_40)

    <span id="d-mg2_wolves_22"></span>**`mg2_wolves_22`** Galmore wolf: “Much grrreat meat. Twenty fourrr bites.” — **effects:** sets stage 70 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-70), gives 24× [Meat](../items/meat.md), starts timer “mg2_wolves”

    - “Tha... I mean grrr.” → *conversation ends*

    <span id="d-mg2_wolves_40"></span>**`mg2_wolves_40`** Galmore wolf: “Parrrasite.”

    - “What?” → [mg2_wolves_42](#d-mg2_wolves_42)

    <span id="d-mg2_wolves_42"></span>**`mg2_wolves_42`** Galmore wolf: “Nothing. OK, look herrre.”

    - Next → [mg2_wolves_22](#d-mg2_wolves_22)



## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 9 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_wolves.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_wolves.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_wolves.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_wolves.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `mg2_wolves` |
    | Spawn group | `mg2_wolves` |
    | Loot table | `canine_dl` |
    | Conversation | `mg2_wolves` |
    | Faction | `mg2_wolves_faction` |
    | Movement | – |
    | Icon | `monsters_dogs:4` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "mg2_wolves",
     "name": "Galmore wolf",
     "iconID": "monsters_dogs:4",
     "maxHP": 251,
     "moveCost": 3,
     "unique": 1,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 15,
      "max": 20
     },
     "faction": "mg2_wolves_faction",
     "phraseID": "mg2_wolves",
     "droplistID": "canine_dl",
     "attackCost": 3,
     "attackChance": 177,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 153
    }
    ```


<small>Data from v0.8.18</small>
