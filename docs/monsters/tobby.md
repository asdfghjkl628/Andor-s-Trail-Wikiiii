# ![](../assets/icons/monsters/monsters_ld1_65.png){ .sprite } Tobby

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_65.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `tobby` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | guynmart_wood_19 |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

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
| [guynmart_wood_19](../maps/guynmart_wood_19.md) | – | 1 | – |


## Quests

- [Sobby's Trail](../quests/tobby.md): stages 10, 20, 21, 22

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Tobby. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/tobby.json" data-npc="Tobby" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (14 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-tobby"></span>**`tobby`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 20 of [Sobby's Trail](../quests/tobby.md#stage-20))* → [tobby_20](#d-tobby_20)
    - branch 2 *(if reached stage 10 of [Sobby's Trail](../quests/tobby.md#stage-10))* → [tobby_10](#d-tobby_10)
    - branch 3 → [tobby_1](#d-tobby_1)

    <span id="d-tobby_20"></span>**`tobby_20`** Tobby: “I am glad you want to help me.” — **effects:** sets stage 20 of [Sobby's Trail](../quests/tobby.md#stage-20)

    - “Sure thing. We brother-seekers must stand together.” → [tobby_22](#d-tobby_22)

    <span id="d-tobby_10"></span>**`tobby_10`** Tobby: “My father had sent me to look for him. But I dare not pass the kobolds in the ravine.”

    - “You are sure your brother went that way?” → [tobby_12](#d-tobby_12)

    <span id="d-tobby_1"></span>**`tobby_1`** Tobby: “Oh good, somebody comes to help me. Hey kid!”

    - “What?” → [tobby_2](#d-tobby_2)

    <span id="d-tobby_22"></span>**`tobby_22`** Tobby: “I want to get some provisions from the house, just a second ...” — **effects:** removes monsters from guynmart_wood_19, spawns monsters on guynmart_wood_19

    - “Go ahead, I'll wait and when you are ready, you can follow me. We will head south.” → *conversation ends*
    - “OK. And tell your father that his rat problem is solved.” *(if killed 1× [Tiny rat](../monsters/tobby_trainingrat.md))* → [tobby_30](#d-tobby_30)
    - “OK. And bring your father this loaf of bread.” *(if NOT killed 1× [Tiny rat](../monsters/tobby_trainingrat.md); hand over 1× [Bread](../items/bread.md))* → [tobby_32](#d-tobby_32)

    <span id="d-tobby_12"></span>**`tobby_12`** Tobby: “Absolutely. Once he was told of a lovely village hidden in the forest to the southeast.”

    - Next → [tobby_14](#d-tobby_14)

    <span id="d-tobby_2"></span>**`tobby_2`** Tobby: “I am Tobby. Please, you must help me.”

    - “I am $playername. What can I do for you?” → [tobby_3](#d-tobby_3)

    <span id="d-tobby_30"></span>**`tobby_30`** Tobby: “Oh, how did you know?” — **effects:** sets stage 21 of [Sobby's Trail](../quests/tobby.md#stage-21)

    - “I just had an inspiration.” → *conversation ends*
    - “Also here, bring him a loaf of bread.” *(if hand over 1× [Bread](../items/bread.md))* → [tobby_32](#d-tobby_32)

    <span id="d-tobby_32"></span>**`tobby_32`** Tobby: “Now I'm speechless - thank you!” — **effects:** sets stage 22 of [Sobby's Trail](../quests/tobby.md#stage-22)

    - “Hurry now.” → *conversation ends*

    <span id="d-tobby_14"></span>**`tobby_14`** Tobby: “Since then not a single day passed when he didn't talk about it.”

    - Next → [tobby_16](#d-tobby_16)

    <span id="d-tobby_3"></span>**`tobby_3`** Tobby: “I can't seem to find my brother, Sobby. He hasn't been back since he left last year.” — **effects:** sets stage 10 of [Sobby's Trail](../quests/tobby.md#stage-10)

    - “Never mind, he will probably not be back too soon.” → [tobby_10](#d-tobby_10)

    <span id="d-tobby_16"></span>**`tobby_16`** Tobby: “And now he is gone.”

    - “And you neither dare pass the kobolds, nor tell your father that you give up.” → [tobby_18](#d-tobby_18)

    <span id="d-tobby_18"></span>**`tobby_18`** Tobby: “Well, yes.”

    - Next → [tobby_19](#d-tobby_19)

    <span id="d-tobby_19"></span>**`tobby_19`** Tobby: “You have come from the south, so you know how to pass these nasty kobolds, right?”

    - “Well, OK. I'll help you.” → [tobby_20](#d-tobby_20)



## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 14 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tobby.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tobby.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tobby.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tobby.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `tobby` |
    | Spawn group | `tobby` |
    | Loot table | – |
    | Conversation | `tobby` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:65` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "tobby",
     "name": "Tobby",
     "iconID": "monsters_ld1:65",
     "moveCost": 5,
     "monsterClass": "humanoid",
     "phraseID": "tobby"
    }
    ```


<small>Data from v0.8.18</small>
