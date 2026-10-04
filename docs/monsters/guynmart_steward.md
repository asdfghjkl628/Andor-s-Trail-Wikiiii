# ![](../assets/icons/monsters/monsters_ld1_11.png){ .sprite } Unkorh

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_11.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `guynmart_steward` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Guynmart Castle |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

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
| [guynmart_main_1](../maps/guynmart_main_1.md) | Guynmart Castle | 1 | – |


## Quests

- [Roses](../quests/guynmart.md): stages 40

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Unkorh. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_steward_10.json" data-npc="Unkorh" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (12 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_steward_10"></span>**`guynmart_steward_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 → [guynmart_steward_20](#d-guynmart_steward_20)

    <span id="d-guynmart_steward_20"></span>**`guynmart_steward_20`** Unkorh: “Hello - I am Unkorh, Steward of Guynmart Castle. I have never seen you here before. Are you looking for something?”

    - “I would like to buy something to eat.” → [guynmart_steward_30](#d-guynmart_steward_30)
    - “I have a message for Lord Guynmart.” → [guynmart_steward_40](#d-guynmart_steward_40)
    - “I would like to see Lady Hannah.” → [guynmart_steward_50](#d-guynmart_steward_50)
    - “Eh ... I...” → [guynmart_steward_22](#d-guynmart_steward_22)

    <span id="d-guynmart_steward_30"></span>**`guynmart_steward_30`** Unkorh: “The cook shall give you some bread. And he can provide you with further provisions, if you can pay for them.” — **effects:** sets stage 40 of [Roses](../quests/guynmart.md#stage-40)

    - Next → [guynmart_steward_32](#d-guynmart_steward_32)

    <span id="d-guynmart_steward_40"></span>**`guynmart_steward_40`** Unkorh: “You have a message for our Lord?”

    - “Yes.” → [guynmart_steward_42](#d-guynmart_steward_42)

    <span id="d-guynmart_steward_50"></span>**`guynmart_steward_50`** Unkorh: “Lady Hannah is not in the mood to receive people. Something else?”

    - “Eh ... I...” → [guynmart_steward_22](#d-guynmart_steward_22)
    - “I would like to buy something to eat.” → [guynmart_steward_30](#d-guynmart_steward_30)
    - “I have a message for Lord Guynmart.” → [guynmart_steward_40](#d-guynmart_steward_40)
    - “No, thank you, I will leave now.” → *conversation ends*

    <span id="d-guynmart_steward_22"></span>**`guynmart_steward_22`** Unkorh: “Stop stuttering, kid. What do you want?”

    - “I would like to buy something to eat.” → [guynmart_steward_30](#d-guynmart_steward_30)
    - “I have a message for Lord Guynmart.” → [guynmart_steward_40](#d-guynmart_steward_40)
    - “I would like to see Lady Hannah.” → [guynmart_steward_50](#d-guynmart_steward_50)

    <span id="d-guynmart_steward_32"></span>**`guynmart_steward_32`** Unkorh: “Take the left stairway and ask for Hofala, our cook.”

    - “Thank you. I will go upstairs.” → *conversation ends*

    <span id="d-guynmart_steward_42"></span>**`guynmart_steward_42`** Unkorh: “Lord Guynmart is uproad tending to urgent affairs. I expect him back tomorrow.”

    - Next → [guynmart_steward_44](#d-guynmart_steward_44)

    <span id="d-guynmart_steward_44"></span>**`guynmart_steward_44`** Unkorh: “Deliver your message to me. I will pass it to Lord Guynmart when he returns.”

    - “Eh, Guynmart shall ... he...” → [guynmart_steward_45](#d-guynmart_steward_45)
    - “I have orders to give it directly to Lord Guynmart.” → [guynmart_steward_46](#d-guynmart_steward_46)

    <span id="d-guynmart_steward_45"></span>**`guynmart_steward_45`** Unkorh: “I don't believe a single word you say. Don't waste my time. I have important things to do.”


    <span id="d-guynmart_steward_46"></span>**`guynmart_steward_46`** Unkorh: “You have? Then you must wait. Leave now and come back tomorrow.”

    - “Wait!” → [guynmart_steward_48](#d-guynmart_steward_48)

    <span id="d-guynmart_steward_48"></span>**`guynmart_steward_48`** Unkorh: “Yes?”

    - “I would like to buy something to eat.” → [guynmart_steward_30](#d-guynmart_steward_30)
    - “I would like to see Lady Hannah.” → [guynmart_steward_50](#d-guynmart_steward_50)



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 12 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_steward.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_steward.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_steward.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_steward.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `guynmart_steward` |
    | Spawn group | `guynmart_steward` |
    | Loot table | – |
    | Conversation | `guynmart_steward_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:11` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_steward",
     "name": "Unkorh",
     "iconID": "monsters_ld1:11",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_steward_10"
    }
    ```


<small>Data from v0.8.18</small>
