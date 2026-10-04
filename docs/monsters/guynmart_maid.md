# ![](../assets/icons/monsters/monsters_ld1_221.png){ .sprite } Maid

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_221.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `guynmart_maid` |
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
| [guynmart_main_3](../maps/guynmart_main_3.md) | Guynmart Castle | 1 | – |


## Quests

- [Roses](../quests/guynmart.md): stages 50

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Maid. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_maid_10.json" data-npc="Maid" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (10 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_maid_10"></span>**`guynmart_maid_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 181 of [Roses](../quests/guynmart.md#stage-181))* → [guynmart_maid_11](#d-guynmart_maid_11)
    - branch 2 *(if reached stage 180 of [Roses](../quests/guynmart.md#stage-180))* → [guynmart_maid_12](#d-guynmart_maid_12)
    - branch 3 *(if reached stage 50 of [Roses](../quests/guynmart.md#stage-50))* → [guynmart_maid_14](#d-guynmart_maid_14)
    - branch 4 → [guynmart_maid_20](#d-guynmart_maid_20)

    <span id="d-guynmart_maid_11"></span>**`guynmart_maid_11`** Maid: “Since Lady Hannah was married, she never sings anymore.”

    - “So she's finally grown up.” → *conversation ends*
    - “Oh.” → *conversation ends*

    <span id="d-guynmart_maid_12"></span>**`guynmart_maid_12`** Maid: “Since Lady Hannah was married, she is singing all day long. Thank you for your help.”

    - “It is nice that she is happy again.” → *conversation ends*
    - “I do such things all the time.” → *conversation ends*

    <span id="d-guynmart_maid_14"></span>**`guynmart_maid_14`** Maid: “Could you already help Lady Hannah?”

    - “I haven't finished yet.” → *conversation ends*
    - “Please tell me again what I should do for Hannah and Lovis.” → [guynmart_maid_50](#d-guynmart_maid_50)

    <span id="d-guynmart_maid_20"></span>**`guynmart_maid_20`** Maid: “Hello. What are you doing in Lady Hannah's room?”

    - “Oh, sorry, I had better leave.” → *conversation ends*
    - “I would like to see Lady Hannah. I heard she has some problems. Maybe I could help her.” → [guynmart_maid_50](#d-guynmart_maid_50)

    <span id="d-guynmart_maid_50"></span>**`guynmart_maid_50`** Maid: “You have heard something of Lovis? Where is he? He has been missing for almost a week.”

    - “Perhaps I could go and find Lovis for her.” → [guynmart_maid_60](#d-guynmart_maid_60)

    <span id="d-guynmart_maid_60"></span>**`guynmart_maid_60`** Maid: “You would do this? That is very kind of you.”

    - Next → [guynmart_maid_62](#d-guynmart_maid_62)

    <span id="d-guynmart_maid_62"></span>**`guynmart_maid_62`** Maid: “Please go directly to Hannah. She will be on top of the tower again, looking for Lovis.”

    - Next → [guynmart_maid_64](#d-guynmart_maid_64)

    <span id="d-guynmart_maid_64"></span>**`guynmart_maid_64`** Maid: “Hmm, probably the guard will stop you. Let me think...”

    - Next → [guynmart_maid_66](#d-guynmart_maid_66)

    <span id="d-guynmart_maid_66"></span>**`guynmart_maid_66`** Maid: “Ah yes - tell the cook that I asked you to take lunch to Lady Hannah. He hates climbing stairs, so he will gladly agree.” — **effects:** sets stage 50 of [Roses](../quests/guynmart.md#stage-50)

    - “Good idea! I will try this immediately.” → *conversation ends*
    - “No way - I am not your servant.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 10 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_maid.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_maid.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_maid.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_maid.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `guynmart_maid` |
    | Spawn group | `guynmart_maid` |
    | Loot table | – |
    | Conversation | `guynmart_maid_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:221` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_maid",
     "name": "Maid",
     "iconID": "monsters_ld1:221",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_maid_10"
    }
    ```


<small>Data from v0.8.18</small>
