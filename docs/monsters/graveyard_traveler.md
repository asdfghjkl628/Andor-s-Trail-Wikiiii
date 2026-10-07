# ![](../assets/icons/monsters/monsters_ld1_6.png){ .sprite } Waterway traveler

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_6.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `graveyard_traveler` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | graveyard0 |
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
| [graveyard0](../maps/graveyard0.md) | – | 1 | – |


## Quests

- [Mine for the taking](../quests/graveyard_quest.md): stages 20, 30

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Waterway traveler. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/graveyardtraveler_begin.json" data-npc="Waterway traveler" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (10 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-graveyardtraveler_begin"></span>**`graveyardtraveler_begin`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 10 of [Mine for the taking](../quests/graveyard_quest.md#stage-10); NOT reached stage 40 of [Mine for the taking](../quests/graveyard_quest.md#stage-40))* → [graveyardtraveler_10](#d-graveyardtraveler_10)
    - Next → [graveyardtraveler_00](#d-graveyardtraveler_00)

    <span id="d-graveyardtraveler_10"></span>**`graveyardtraveler_10`** Waterway traveler: “Hey, did you try to open that treasure chest?”

    - “Yes.” → [graveyardtraveler_20](#d-graveyardtraveler_20)
    - “No.” → *conversation ends*

    <span id="d-graveyardtraveler_00"></span>**`graveyardtraveler_00`** Waterway traveler: “Greetings, young traveler.”

    - “I opened that chest and got a powerful sword.” *(if reached stage 80 of [Mine for the taking](../quests/graveyard_quest.md#stage-80); NOT reached stage 90 of [Mine for the taking](../quests/graveyard_quest.md#stage-90); NOT reached stage 95 of [Mine for the taking](../quests/graveyard_quest.md#stage-95))* → [graveyardtraveler_99](#d-graveyardtraveler_99)

    <span id="d-graveyardtraveler_20"></span>**`graveyardtraveler_20`** Waterway traveler: “That chest is something of a local legend. Been there for generations. They say it is sealed with magic and can only be opened with a special key, which hangs on the neck of one of the undead that roam in a cemetery directly south of here.” — **effects:** sets stage 20 of [Mine for the taking](../quests/graveyard_quest.md#stage-20)

    - “Killing the undead is my specialty.” → [graveyardtraveler_30](#d-graveyardtraveler_30)
    - “Undead? I would love to hear the rest of your story but I am on a mission to find my brother.” → *conversation ends*

    <span id="d-graveyardtraveler_99"></span>**`graveyardtraveler_99`** Waterway traveler: “I should not have doubted you. Well done.”


    <span id="d-graveyardtraveler_30"></span>**`graveyardtraveler_30`** Waterway traveler: “You don't think someone has already tried? It's a treasure chest ... left outside ... in plain view ... unguarded.”

    - Next → [graveyardtraveler_40](#d-graveyardtraveler_40)

    <span id="d-graveyardtraveler_40"></span>**`graveyardtraveler_40`** Waterway traveler: “Listen kid. A hundred 'adventurers' before you have tried and failed to open that chest. The problem isn't killing some undead. It's getting into the cemetery, because it's protected by a magical barrier that prevents anyone from entering.”

    - “Interesting. Is there anything else you can tell me about the chest or cemetery?” → [graveyardtraveler_50](#d-graveyardtraveler_50)

    <span id="d-graveyardtraveler_50"></span>**`graveyardtraveler_50`** Waterway traveler: “That is all I know ... Come to think of it ... Hagale from the Wood Settlement was out here a few weeks ago asking about the chest. Something about him struck me as odd. It was as if he was in a trance.” — **effects:** sets stage 30 of [Mine for the taking](../quests/graveyard_quest.md#stage-30)

    - Next → [graveyardtraveler_60](#d-graveyardtraveler_60)

    <span id="d-graveyardtraveler_60"></span>**`graveyardtraveler_60`** Waterway traveler: “Maybe he knows more. You should give him a visit.”

    - “OK, I'll do that.” → *conversation ends*
    - “Where is the Wood settlement?” → [graveyardtraveler61](#d-graveyardtraveler61)

    <span id="d-graveyardtraveler61"></span>**`graveyardtraveler61`** Waterway traveler: “South of the Duleian road, close to Fallhaven.”

    - “OK. I'll go there now.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 10 lines added |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 1 line changed<br>· text: “Maybe he knows more. You should give him a visit.” → “Maybe he knows more. You should give him a visit.” |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=graveyard_traveler.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=graveyard_traveler.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=graveyard_traveler.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=graveyard_traveler.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `graveyard_traveler` |
    | Spawn group | `graveyard_traveler` |
    | Loot table | – |
    | Conversation | `graveyardtraveler_begin` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:6` |
    | Defined in | `res/raw/monsterlist_graveyard1.json` |

    Raw data:

    ```json
    {
     "id": "graveyard_traveler",
     "name": "Waterway traveler",
     "iconID": "monsters_ld1:6",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "graveyard_traveler",
     "phraseID": "graveyardtraveler_begin"
    }
    ```


<small>Data from v0.8.18</small>
