# ![](../assets/icons/monsters/monsters_ld1_221.png){ .sprite } Kalypso

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_221.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `kalypso` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Remgard |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

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
| [mountainlake14](../maps/mountainlake14.md) | Remgard | 1 | – |
| [mountainlake19](../maps/mountainlake19.md) | – | 1 | – |


## Quests

- [A map of the Great Lake Laeroth](../quests/lake_map.md): stages 20, 22, 24

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Kalypso. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/kalypso.json" data-npc="Kalypso" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (22 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-kalypso"></span>**`kalypso`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 22 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-22))* → [kalypso_1](#d-kalypso_1)
    - branch 2 → [kalypso_10](#d-kalypso_10)

    <span id="d-kalypso_1"></span>**`kalypso_1`** Kalypso: “Take as much as you need.”

    - Next → [kalypso_2](#d-kalypso_2)

    <span id="d-kalypso_10"></span>**`kalypso_10`** Kalypso: “Oh. A traveler.”

    - “Hello.” → [kalypso_11](#d-kalypso_11)

    <span id="d-kalypso_2"></span>**`kalypso_2`** Kalypso: “You may leave whenever you wish.”

    - Next → [kalypso_3](#d-kalypso_3)

    <span id="d-kalypso_11"></span>**`kalypso_11`** Kalypso: “[examines you carefully] You look capable. But tired.”

    - “I rarely get time to rest.” → [kalypso_12](#d-kalypso_12)

    <span id="d-kalypso_3"></span>**`kalypso_3`** Kalypso: “But if you face storms or monsters tomorrow, you might prefer to do so at your strongest.”

    - “True.” → [kalypso_4](#d-kalypso_4)

    <span id="d-kalypso_12"></span>**`kalypso_12`** Kalypso: “I host those who pass through. You are free to come and go as you please.”

    - Next → [kalypso_13](#d-kalypso_13)

    <span id="d-kalypso_4"></span>**`kalypso_4`** Kalypso: “[points to the table] One grape is a courtesy. A meal is preparation.”


    <span id="d-kalypso_13"></span>**`kalypso_13`** [Dummy NPC](../monsters/none.md): “Kalypso picks a single grape from the plate.”

    - Next → [kalypso_14](#d-kalypso_14)

    <span id="d-kalypso_14"></span>**`kalypso_14`** [Kalypso](../monsters/kalypso.md): “These grow only here. The soil is... unusual.”

    - Next → [kalypso_15](#d-kalypso_15)

    <span id="d-kalypso_15"></span>**`kalypso_15`** Kalypso: “Try one. If you dislike it, I shall be offended for exactly three seconds.”

    - “Three seconds?” → [kalypso_16](#d-kalypso_16)
    - “That's funny.” → [kalypso_16](#d-kalypso_16)

    <span id="d-kalypso_16"></span>**`kalypso_16`** Kalypso: “It is not enchanted wine. Not a vow. Not chain that binds you.” — **effects:** sets stage 20 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-20)

    - Next → [kalypso_17](#d-kalypso_17)

    <span id="d-kalypso_17"></span>**`kalypso_17`** Kalypso: “It's just fruit.”

    - “Let me try your grape.” → [kalypso_19](#d-kalypso_19)
    - “I might have a closer look at it.” → [kalypso_18](#d-kalypso_18)

    <span id="d-kalypso_19"></span>**`kalypso_19`** Kalypso: “[watches intensely] Ah. You feel it, don't you?” — **effects:** applies condition heros_body, sets stage 22 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-22)

    - “Wow - I am the greatest!” → [kalypso_19a](#d-kalypso_19a)

    <span id="d-kalypso_18"></span>**`kalypso_18`** Kalypso: “[slightly amused] You may inspect it if that makes you feel heroic.”

    - “Looks OK. Let's eat it.” → [kalypso_19](#d-kalypso_19)

    <span id="d-kalypso_19a"></span>**`kalypso_19a`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 24 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-24))* → [kalypso_20](#d-kalypso_20)
    - branch 2 → [kalypso_19b](#d-kalypso_19b)

    <span id="d-kalypso_20"></span>**`kalypso_20`** Kalypso: “The island rewards those who survive long enough to reach it.”

    - Next → [kalypso_21](#d-kalypso_21)

    <span id="d-kalypso_19b"></span>**`kalypso_19b`** Kalypso: “As a token of my friendship, I give you this tiny green key.” — **effects:** gives 1× [Wooden green key from Kalypso](../items/ll2_key_kalypso.md), sets stage 24 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-24)

    - “Thank you.” → [kalypso_19c](#d-kalypso_19c)
    - “Where do I use it?” → [kalypso_19c](#d-kalypso_19c)

    <span id="d-kalypso_21"></span>**`kalypso_21`** Kalypso: “[Her eyes flashing] Muscles awakened. Breath deepens. Old fatigue loosens its grip.”

    - Next → [kalypso_22](#d-kalypso_22)

    <span id="d-kalypso_19c"></span>**`kalypso_19c`** Kalypso: “Keep it safe. You'll know when you can use it.”

    - “OK.” → [kalypso_20](#d-kalypso_20)

    <span id="d-kalypso_22"></span>**`kalypso_22`** Kalypso: “[Honest admiration] It suits you.”

    - “I feel strong!” → [kalypso_23](#d-kalypso_23)

    <span id="d-kalypso_23"></span>**`kalypso_23`** Kalypso: “Now have a look at yourself how you have evolved!”




## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 22 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kalypso.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kalypso.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kalypso.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kalypso.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `kalypso` |
    | Spawn group | `kalypso` |
    | Loot table | – |
    | Conversation | `kalypso` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:221` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "kalypso",
     "name": "Kalypso",
     "iconID": "monsters_ld1:221",
     "monsterClass": "humanoid",
     "spawnGroup": "kalypso",
     "phraseID": "kalypso"
    }
    ```


<small>Data from v0.8.18</small>
