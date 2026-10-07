# ![](../assets/icons/monsters/monsters_ld1_3.png){ .sprite } Tahalendor

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_3.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `tahalendor2` |
| **Type** | NPC |
| **Class** | ? |
| **HP** | 1 |
| **Found in** | Stoutford |
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
| [stoutford_potion](../maps/stoutford_potion.md) | Stoutford | 1 | appears later in a quest |


## Quests

- [The thorns of vengeance](../quests/thorns_vengeance.md): stages 75, 80

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Tahalendor. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/tahalendor2_0.json" data-npc="Tahalendor" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (13 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-tahalendor2_0"></span>**`tahalendor2_0`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 75 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-75))* → [blornvale_thorns72_92](#d-blornvale_thorns72_92)
    - branch 2 *(if reached stage 72 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-72))* → [tahalendor2_20](#d-tahalendor2_20)
    - branch 3 *(if reached stage 71 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-71))* → [blornvale_thorns70_22](#d-blornvale_thorns70_22)
    - branch 4 → [tahalendor2_10](#d-tahalendor2_10)

    <span id="d-blornvale_thorns72_92"></span>**`blornvale_thorns72_92`** Tahalendor: “No more talk. Go now!”


    <span id="d-tahalendor2_20"></span>**`tahalendor2_20`** Tahalendor: “Well, I don't really believe it, but we could try. Blornvale, how did you kill Aryfora's father, your own brother?”

    - Next → [blornvale_thorns72_60](#d-blornvale_thorns72_60)

    <span id="d-blornvale_thorns70_22"></span>**`blornvale_thorns70_22`** [Tahalendor](../monsters/tahalendor2.md): “Well, it looks like the potion is already working. Blornvale, how did you kill Aryfora's father, your own brother?”

    - Next → [blornvale_thorns70_24](#d-blornvale_thorns70_24)

    <span id="d-tahalendor2_10"></span>**`tahalendor2_10`** Tahalendor: “What now?”


    <span id="d-blornvale_thorns72_60"></span>**`blornvale_thorns72_60`** [Blornvale](../monsters/stoutford_alchemist.md): “Of course not. Nobody is sadder about the loss than me.”

    - “He lies. Can't you see?” → [blornvale_thorns72_70](#d-blornvale_thorns72_70)

    <span id="d-blornvale_thorns70_24"></span>**`blornvale_thorns70_24`** [Blornvale](../monsters/stoutford_alchemist.md): “He was naive enough to take a potion from me. I poisoned him with the potion of Quick Death.”

    - Next → [blornvale_thorns70_26](#d-blornvale_thorns70_26)

    <span id="d-blornvale_thorns72_70"></span>**`blornvale_thorns72_70`** Tahalendor: “Here, Tahalendor, I'll give you a bottle of your favorite potion. And please take this child with you when you go.”

    - Next → [blornvale_thorns72_80](#d-blornvale_thorns72_80)

    <span id="d-blornvale_thorns70_26"></span>**`blornvale_thorns70_26`** [Tahalendor](../monsters/tahalendor2.md): “I thought so. Didn't you worry that someone would suspect you?”

    - Next → [blornvale_thorns70_28](#d-blornvale_thorns70_28)

    <span id="d-blornvale_thorns72_80"></span>**`blornvale_thorns72_80`** [Tahalendor](../monsters/tahalendor2.md): “I will, sorry for disturbing you.”

    - Next → [blornvale_thorns72_90](#d-blornvale_thorns72_90)

    <span id="d-blornvale_thorns70_28"></span>**`blornvale_thorns70_28`** [Blornvale](../monsters/stoutford_alchemist.md): “Only an alchemist could have found out, so I had only Aryfora herself to fear. But no one believed her accusations, not even you, Tahalendor.”

    - Next → [blornvale_thorns70_30](#d-blornvale_thorns70_30)

    <span id="d-blornvale_thorns72_90"></span>**`blornvale_thorns72_90`** Tahalendor: “And you child, go away now and tell no more fairy tales.” — **effects:** sets stage 75 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-75)

    - “But...” → [blornvale_thorns72_92](#d-blornvale_thorns72_92)

    <span id="d-blornvale_thorns70_30"></span>**`blornvale_thorns70_30`** [Tahalendor](../monsters/tahalendor2.md): “I have heard enough. Thank you, kid. I will ensure that Blornvale never makes trouble again.” — **effects:** sets stage 80 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-80), removes monsters from stoutford_potion, removes monsters from stoutford_potion

    - Next → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 13 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tahalendor2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tahalendor2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tahalendor2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tahalendor2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `tahalendor2` |
    | Spawn group | `tahalendor2` |
    | Loot table | – |
    | Conversation | `tahalendor2_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:3` |
    | Defined in | `res/raw/monsterlist_stoutford.json` |

    Raw data:

    ```json
    {
     "id": "tahalendor2",
     "name": "Tahalendor",
     "iconID": "monsters_ld1:3",
     "phraseID": "tahalendor2_0"
    }
    ```


<small>Data from v0.8.18</small>
