# ![](../assets/icons/monsters/monsters_ld1_225.png){ .sprite } Hannah

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_225.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `guynmart_hannah` |
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
| [guynmart](../maps/guynmart.md) | Guynmart Castle | 1 | – |


## Quests

- [Roses](../quests/guynmart.md): stages 70, 90, 100
- [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md): stages 7
- [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md): stages 34
- [shutters open (hidden flag)](../quests/guynmart_qRpl_shutters.md): stages 1

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Hannah. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_hannah_10.json" data-npc="Hannah" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (11 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_hannah_10"></span>**`guynmart_hannah_10`** *(silent check: the first matching branch below is taken)* — **effects:** removes monsters from guynmart_main_1, removes monsters from guynmart_main_2, sets stage 34 of [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-34)

    - branch 1 *(if carry 1× [Rose](../items/guynmart_rose.md))* → [guynmart_hannah_110](#d-guynmart_hannah_110)
    - branch 2 *(if reached stage 70 of [Roses](../quests/guynmart.md#stage-70))* → [guynmart_hannah_12](#d-guynmart_hannah_12)
    - branch 3 → [guynmart_hannah_20](#d-guynmart_hannah_20)

    <span id="d-guynmart_hannah_110"></span>**`guynmart_hannah_110`** Hannah: “Oh, what a lovely rose you found for me!”

    - Next → [guynmart_hannah_112](#d-guynmart_hannah_112)

    <span id="d-guynmart_hannah_12"></span>**`guynmart_hannah_12`** Hannah: “Go away, kid. I want to be alone. I cannot think clearly without the smell of another fresh, fragrant rose.”

    - “I will bring your rose now.” → *conversation ends*
    - “You and your stupid rose.” *(if reached stage 70 of [Roses](../quests/guynmart.md#stage-70))* → *conversation ends*

    <span id="d-guynmart_hannah_20"></span>**`guynmart_hannah_20`** Hannah: “I cannot think clearly ... I need a rose! A fresh, fragrant rose! Please bring me a rose from my garden...” — **effects:** sets stage 70 of [Roses](../quests/guynmart.md#stage-70), spawns monsters on guynmart, clears stage 1 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-1), sets stage 7 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-7)

    - “I have some delicious lunch for you.” *(if carry 1× [Hannah's lunch](../items/guynmart_lunch.md))* → [guynmart_hannah_30](#d-guynmart_hannah_30)
    - “I will go and ask Nuik.” → *conversation ends*

    <span id="d-guynmart_hannah_112"></span>**`guynmart_hannah_112`** Hannah: “Ah - beautiful. Just look!”

    - Next *(if hand over 1× [Rose](../items/guynmart_rose.md))* → [guynmart_hannah_114](#d-guynmart_hannah_114)

    <span id="d-guynmart_hannah_30"></span>**`guynmart_hannah_30`** Hannah: “How can you think of eating and drinking! My love has gone - I will never eat again! Take it for yourself or throw it away. And leave me alone now. A rose ... I need my rose...”

    - “I will bring your rose now.” → *conversation ends*

    <span id="d-guynmart_hannah_114"></span>**`guynmart_hannah_114`** Hannah: “[Hannah takes the rose] Now. I feel better again. Thank you.” — **effects:** sets stage 90 of [Roses](../quests/guynmart.md#stage-90)

    - Next → [guynmart_hannah_120](#d-guynmart_hannah_120)

    <span id="d-guynmart_hannah_120"></span>**`guynmart_hannah_120`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 100 of [Roses](../quests/guynmart.md#stage-100))* → [guynmart_hannah_122](#d-guynmart_hannah_122)
    - branch 2 → [guynmart_hannah_140](#d-guynmart_hannah_140)

    <span id="d-guynmart_hannah_122"></span>**`guynmart_hannah_122`** Hannah: “Have you found Lovis yet?”

    - “No, sorry. Not yet.” → *conversation ends*

    <span id="d-guynmart_hannah_140"></span>**`guynmart_hannah_140`** Hannah: “I would like to give you Lovis' flute. He used to play on it every day for me. When you find Lovis, show the flute as a token that I sent you.”

    - “I will not disappoint you.” → [guynmart_hannah_150](#d-guynmart_hannah_150)
    - “No, I do not feel like running back and forth.” → *conversation ends*

    <span id="d-guynmart_hannah_150"></span>**`guynmart_hannah_150`** Hannah: “So take this flute and take good care of it.” — **effects:** sets stage 100 of [Roses](../quests/guynmart.md#stage-100), gives 1× [Lovis' Flute](../items/guynmart_flute.md), sets stage 1 of [shutters open (hidden flag)](../quests/guynmart_qRpl_shutters.md#stage-1), removes monsters from guynmart_main_3, spawns monsters on guynmart_tower_3

    - “I will.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 11 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_hannah.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_hannah.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_hannah.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_hannah.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `guynmart_hannah` |
    | Spawn group | `guynmart_hannah` |
    | Loot table | – |
    | Conversation | `guynmart_hannah_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:225` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_hannah",
     "name": "Hannah",
     "iconID": "monsters_ld1:225",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_hannah_10"
    }
    ```


<small>Data from v0.8.18</small>
