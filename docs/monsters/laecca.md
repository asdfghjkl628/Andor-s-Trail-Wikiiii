# ![](../assets/icons/monsters/monsters_rltiles1_72.png){ .sprite } Laecca

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_72.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `laecca` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Prim |
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
| [blackwater_mountain21](../maps/blackwater_mountain21.md) | Prim | 1 | – |


## Quests

- [Clouded intent](../quests/prim_hunt.md): stages 11, 15

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Laecca. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/laecca_1.json" data-npc="Laecca" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (13 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-laecca_1"></span>**`laecca_1`** Laecca: “Hello. I am Laecca, mountain guide.”

    - “What do you do around here?” → [laecca_2](#d-laecca_2)
    - “'Mountain guide', what does that mean?” → [laecca_2](#d-laecca_2)

    <span id="d-laecca_2"></span>**`laecca_2`** Laecca: “I keep an eye on the mountain pass, to make sure no more of those beasts make their way down here.”

    - “Then what are you doing indoors here? Shouldn't you be outside guarding then?” → [laecca_4](#d-laecca_4)
    - “Sounds like a noble cause.” → [laecca_3](#d-laecca_3)
    - “What beasts are you talking about?” → [laecca_9](#d-laecca_9)

    <span id="d-laecca_4"></span>**`laecca_4`** Laecca: “Very funny. I have to rest too you know. Keeping the monsters away is hard work.”

    - Next → [laecca_5](#d-laecca_5)

    <span id="d-laecca_3"></span>**`laecca_3`** Laecca: “Yeah, sure. It may sound that way. In reality, it's a lot of hard work.”

    - Next → [laecca_5](#d-laecca_5)

    <span id="d-laecca_9"></span>**`laecca_9`** Laecca: “Pfft, 'What beasts?'. The gornaud beasts of course.”

    - Next → [laecca_10](#d-laecca_10)

    <span id="d-laecca_5"></span>**`laecca_5`** Laecca: “There used to be more of us mountain guides, but not many have survived the attack of the beasts.”

    - “Sounds like you aren't really cut out to do your job properly.” → [laecca_6](#d-laecca_6)
    - “I'm sorry to hear that.” → [laecca_8](#d-laecca_8)
    - “What beasts are you talking about?” → [laecca_9](#d-laecca_9)

    <span id="d-laecca_10"></span>**`laecca_10`** Laecca: “Scratching their claws against the bare rock at night. *shrug*”

    - Next → [laecca_11](#d-laecca_11)

    <span id="d-laecca_6"></span>**`laecca_6`** Laecca: “Perhaps.”

    - Next → [laecca_7](#d-laecca_7)

    <span id="d-laecca_8"></span>**`laecca_8`** Laecca: “Thank you for your concern.”

    - “Is there anything I can do to help?” → [laecca_13](#d-laecca_13)

    <span id="d-laecca_11"></span>**`laecca_11`** Laecca: “At first, I thought they were acting on pure instinct. But recently, I have started to believe they are smarter than regular beasts.”

    - Next → [laecca_12](#d-laecca_12)

    <span id="d-laecca_7"></span>**`laecca_7`** Laecca: “Anyway. I have some things to tend to. Nice talking to you.”

    - “Goodbye.” → *conversation ends*

    <span id="d-laecca_13"></span>**`laecca_13`** Laecca: “You should talk to Guthbered. He is usually in the main hall. Look for a stone house in the center of the village.” — **effects:** sets stage 15 of [Clouded intent](../quests/prim_hunt.md#stage-15)


    <span id="d-laecca_12"></span>**`laecca_12`** Laecca: “Their attacks are getting more and more clever.” — **effects:** sets stage 11 of [Clouded intent](../quests/prim_hunt.md#stage-11)

    - “Is there anything I can do to help?” → [laecca_13](#d-laecca_13)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed<br>· text: “Pfft, 'What beasts?'. The Gornaud beasts of course.” → “Pfft, 'What beasts?'. The gornaud beasts of course.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=laecca.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=laecca.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=laecca.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=laecca.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `laecca` |
    | Spawn group | `laecca` |
    | Loot table | – |
    | Conversation | `laecca_1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:72` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "laecca",
     "name": "Laecca",
     "iconID": "monsters_rltiles1:72",
     "monsterClass": "humanoid",
     "spawnGroup": "laecca",
     "phraseID": "laecca_1"
    }
    ```


<small>Data from v0.8.18</small>
