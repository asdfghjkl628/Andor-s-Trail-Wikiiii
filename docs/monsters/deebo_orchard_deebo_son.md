# ![](../assets/icons/monsters/monsters_tometik2_55.png){ .sprite } Howkin

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik2_55.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `deebo_orchard_deebo_son` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Deebo's Orchard |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

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
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [deebo_orchard_house](../maps/deebo_orchard_house.md) | Deebo's Orchard | 1 | – |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Howkin. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/deebo_orchard_howkin.json" data-npc="Howkin" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-deebo_orchard_howkin"></span>**`deebo_orchard_howkin`** Howkin: “Hey there. What are you here for? A job, maybe?”

    - Next → [deebo_orchard_howkin_10](#d-deebo_orchard_howkin_10)

    <span id="d-deebo_orchard_howkin_10"></span>**`deebo_orchard_howkin_10`** Howkin: “We could always use the help. Considering we have workers coming and going all the time.”

    - “That's nice. But I don't care. See you later.” → *conversation ends*
    - “Why is that?” → [deebo_orchard_howkin_20](#d-deebo_orchard_howkin_20)
    - “Who are you?” → [deebo_orchard_howkin_30](#d-deebo_orchard_howkin_30)

    <span id="d-deebo_orchard_howkin_20"></span>**`deebo_orchard_howkin_20`** Howkin: “Well, I guess it's because my father works the farmers too much and I don't pay them enough for their labor.”

    - “You guys need to treat your farmers with more respect.” → *conversation ends*

    <span id="d-deebo_orchard_howkin_30"></span>**`deebo_orchard_howkin_30`** Howkin: “My name is Howkin and I am Deebo's son. I run the business side of the orchard while father runs the farming aspects.”

    - “Oh, I understand.” → *conversation ends*
    - “Oh, I understand...that you don't like to get your hands dirty.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 4 lines added |
| [v0.8.4](../versions/0.8.4.md) | Dialogue: 1 line changed<br>· text: “Well, I guess it's because by father works the farmers too much and I…” → “Well, I guess it's because my father works the farmers too much and I…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=deebo_orchard_deebo_son.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=deebo_orchard_deebo_son.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=deebo_orchard_deebo_son.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=deebo_orchard_deebo_son.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `deebo_orchard_deebo_son` |
    | Spawn group | `deebo_orchard_deebo_son` |
    | Loot table | – |
    | Conversation | `deebo_orchard_howkin` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:55` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "deebo_orchard_deebo_son",
     "name": "Howkin",
     "iconID": "monsters_tometik2:55",
     "monsterClass": "humanoid",
     "spawnGroup": "deebo_orchard_deebo_son",
     "phraseID": "deebo_orchard_howkin"
    }
    ```


<small>Data from v0.8.18</small>
