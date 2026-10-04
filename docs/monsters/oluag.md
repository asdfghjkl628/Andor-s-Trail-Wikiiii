# ![](../assets/icons/monsters/monsters_men_8.png){ .sprite } Oluag

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_8.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `oluag` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | wild14_clearing |
| **Introduced** | v0.7.0 or earlier |

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
| [wild14_clearing](../maps/wild14_clearing.md) | – | 1 | – |


## Quests

- [Uncertain cause](../quests/wrye.md): stages 80

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Oluag. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/oluag_1.json" data-npc="Oluag" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (23 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-oluag_1"></span>**`oluag_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 80 of [Uncertain cause](../quests/wrye.md#stage-80))* → [oluag_grave_16](#d-oluag_grave_16)
    - branch 2 → [oluag_1_1](#d-oluag_1_1)

    <span id="d-oluag_grave_16"></span>**`oluag_grave_16`** Oluag: “Lousy kid. He could at least have had a few coins on him.”

    - “Thank you for the story. Goodbye.” → [oluag_goodbye](#d-oluag_goodbye)
    - “Thank you for the story. Shadow be with you.” → [oluag_goodbye](#d-oluag_goodbye)

    <span id="d-oluag_1_1"></span>**`oluag_1_1`** Oluag: “Hello. I am Oluag.”

    - “What are you doing here around these crates?” → [oluag_2](#d-oluag_2)

    <span id="d-oluag_goodbye"></span>**`oluag_goodbye`** Oluag: “Right. Goodbye.”


    <span id="d-oluag_2"></span>**`oluag_2`** Oluag: “Oh these. They are nothing. Never mind them. That grave over there is nothing to worry about either.”

    - “What grave?” → [oluag_grave_select](#d-oluag_grave_select)
    - “Nothing, really? This sounds suspicious.” → [oluag_boxes_1](#d-oluag_boxes_1)

    <span id="d-oluag_grave_select"></span>**`oluag_grave_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 80 of [Uncertain cause](../quests/wrye.md#stage-80))* → [oluag_grave_return](#d-oluag_grave_return)
    - branch 2 → [oluag_grave_1](#d-oluag_grave_1)

    <span id="d-oluag_boxes_1"></span>**`oluag_boxes_1`** Oluag: “No no, nothing suspicious at all. It's not like they contain any contraband or anything like that, hah!”

    - “What was that about a grave?” → [oluag_grave_select](#d-oluag_grave_select)
    - “OK then. I guess I didn't see anything.” → [oluag_goodbye](#d-oluag_goodbye)

    <span id="d-oluag_grave_return"></span>**`oluag_grave_return`** Oluag: “Look, I already told you the story.”

    - Next → [oluag_grave_5](#d-oluag_grave_5)

    <span id="d-oluag_grave_1"></span>**`oluag_grave_1`** Oluag: “Yeah, OK. So there is a grave right over there. I promise I had nothing to do with it.”

    - “Nothing? Really?” → [oluag_grave_2](#d-oluag_grave_2)
    - “OK then. I guess you didn't have anything to do with it.” → [oluag_goodbye](#d-oluag_goodbye)

    <span id="d-oluag_grave_5"></span>**`oluag_grave_5`** Oluag: “There was this kid I found. He had almost bled to death.”

    - Next → [oluag_grave_6](#d-oluag_grave_6)

    <span id="d-oluag_grave_2"></span>**`oluag_grave_2`** Oluag: “Well, when I say 'nothing', I really mean nothing. Or maybe just a little bit.”

    - “A little bit?” → [oluag_grave_3](#d-oluag_grave_3)

    <span id="d-oluag_grave_6"></span>**`oluag_grave_6`** Oluag: “I managed to get a few sentences out of him before he died.”

    - Next → [oluag_grave_7](#d-oluag_grave_7)

    <span id="d-oluag_grave_3"></span>**`oluag_grave_3`** Oluag: “OK, so maybe I just had a little bit to do with it.”

    - “You better start talking.” → [oluag_grave_5](#d-oluag_grave_5)
    - “What did you do?” → [oluag_grave_5](#d-oluag_grave_5)
    - “Do I have to beat it out of you?” → [oluag_grave_4](#d-oluag_grave_4)

    <span id="d-oluag_grave_7"></span>**`oluag_grave_7`** Oluag: “So I buried him over there by that grave.”

    - “What were the last sentences you heard him say?” → [oluag_grave_8](#d-oluag_grave_8)

    <span id="d-oluag_grave_4"></span>**`oluag_grave_4`** Oluag: “Relax, relax. I don't want any more fights.”

    - Next → [oluag_grave_5](#d-oluag_grave_5)

    <span id="d-oluag_grave_8"></span>**`oluag_grave_8`** Oluag: “Something about Vilegard and Ryndel maybe? I didn't really pay attention, I was more interested in what loot he had on him.”

    - “I should go check that grave. Goodbye.” → *conversation ends*
    - “Rincel, was that it? From Vilegard? Wrye's missing son.” *(if reached stage 40 of [Uncertain cause](../quests/wrye.md#stage-40))* → [oluag_grave_9](#d-oluag_grave_9)

    <span id="d-oluag_grave_9"></span>**`oluag_grave_9`** Oluag: “Yeah, that might be it. Anyway, so he said something about fulfilling a dream to see the great city of Feygard.”

    - Next → [oluag_grave_10](#d-oluag_grave_10)

    <span id="d-oluag_grave_10"></span>**`oluag_grave_10`** Oluag: “And he told me something about that he didn't dare tell anyone.”

    - “Maybe he didn't dare tell Wrye?” → [oluag_grave_11](#d-oluag_grave_11)

    <span id="d-oluag_grave_11"></span>**`oluag_grave_11`** Oluag: “Yeah sure, probably. He had set down here to camp, but got attacked by some monsters.”

    - Next → [oluag_grave_12](#d-oluag_grave_12)

    <span id="d-oluag_grave_12"></span>**`oluag_grave_12`** Oluag: “Apparently he was not as strong a fighter as, for example, someone like me. So the monsters wounded him too much for him to last the night.”

    - Next → [oluag_grave_13](#d-oluag_grave_13)

    <span id="d-oluag_grave_13"></span>**`oluag_grave_13`** Oluag: “Sadly, they also must have taken any loot with them, since I could not find any on him.”

    - Next → [oluag_grave_14](#d-oluag_grave_14)

    <span id="d-oluag_grave_14"></span>**`oluag_grave_14`** Oluag: “I heard the fighting and only managed to get to him after the monsters had fled.”

    - Next → [oluag_grave_15](#d-oluag_grave_15)

    <span id="d-oluag_grave_15"></span>**`oluag_grave_15`** Oluag: “So, anyway. Now he is buried over there. Rest in peace.” — **effects:** sets stage 80 of [Uncertain cause](../quests/wrye.md#stage-80)

    - Next → [oluag_grave_16](#d-oluag_grave_16)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 6 lines changed<br>· text: “Ok, so maybe I just had a little bit to do with it.” → “OK, so maybe I just had a little bit to do with it.”<br>· text: “Yeah, ok. So there is a grave right over there. I promise I had nothi…” → “Yeah, OK. So there is a grave right over there. I promise I had nothi…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=oluag.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=oluag.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=oluag.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=oluag.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `oluag` |
    | Spawn group | `oluag` |
    | Loot table | – |
    | Conversation | `oluag_1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:8` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "oluag",
     "name": "Oluag",
     "iconID": "monsters_men:8",
     "monsterClass": "humanoid",
     "spawnGroup": "oluag",
     "phraseID": "oluag_1"
    }
    ```


<small>Data from v0.8.18</small>
