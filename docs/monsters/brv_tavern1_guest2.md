# ![](../assets/icons/monsters/monsters_ld1_64.png){ .sprite } Forlin

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_64.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `brv_tavern1_guest2` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Brimhaven |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

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
| [brimhaven_tavern1](../maps/brimhaven_tavern1.md) | Brimhaven | 1 | – |


## Quests

- [A strange looking dagger](../quests/brv_dagger.md): stages 140

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Forlin. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_tavern1_guest2.json" data-npc="Forlin" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brv_tavern1_guest2"></span>**`brv_tavern1_guest2`** Forlin: “I'm drinking because my wife left me and took my beagle with her. Now how am I supposed to hunt?”

    - “I'm so sorry to hear about your problems. I love dogs too.” → *conversation ends*
    - “Hey, speaking of killing, I'm wondering if you know anything about Lawellyn's death?” *(if reached stage 130 of [A strange looking dagger](../quests/brv_dagger.md#stage-130))* → [brv_tavern1_guest2_asd_10](#d-brv_tavern1_guest2_asd_10)

    <span id="d-brv_tavern1_guest2_asd_10"></span>**`brv_tavern1_guest2_asd_10`** Forlin: “I may. Who's asking?”

    - “Well, I've been asked by Lawellyn's daughter, Arlish, to investigate his death.” → [brv_tavern1_guest2_asd_20](#d-brv_tavern1_guest2_asd_20)

    <span id="d-brv_tavern1_guest2_asd_20"></span>**`brv_tavern1_guest2_asd_20`** Forlin: “Oh, OK. Arlish helped me a lot in school when we were kids, so I feel like I owe it to her to help you.”

    - Next → [brv_tavern1_guest2_asd_30](#d-brv_tavern1_guest2_asd_30)

    <span id="d-brv_tavern1_guest2_asd_30"></span>**`brv_tavern1_guest2_asd_30`** Forlin: “Don't tell the bartender, but I like to frequent the tavern in Loneford a lot, and as such, I've developed quite a friendship with the owner Kizzo. One day we were talking about how scary the woods between Loneford and Brimhaven can be at…”

    - Next → [brv_tavern1_guest2_asd_40](#d-brv_tavern1_guest2_asd_40)

    <span id="d-brv_tavern1_guest2_asd_40"></span>**`brv_tavern1_guest2_asd_40`** Forlin: “I suggest that you go talk to Kizzo.” — **effects:** sets stage 140 of [A strange looking dagger](../quests/brv_dagger.md#stage-140)




## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 1 line added |
| [v0.7.12](../versions/0.7.12.md) | name: Customer → Forlin<br>Dialogue: 4 lines added, 1 line changed<br>· text: “I hate myself, because I'm drinking...” → “I'm drinking because my wife left me and took my beagle with her. Now…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_tavern1_guest2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_tavern1_guest2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_tavern1_guest2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_tavern1_guest2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `brv_tavern1_guest2` |
    | Spawn group | `brv_tavern1_guest2` |
    | Loot table | – |
    | Conversation | `brv_tavern1_guest2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:64` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_tavern1_guest2",
     "name": "Forlin",
     "iconID": "monsters_ld1:64",
     "moveCost": 5,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_tavern1_guest2",
     "phraseID": "brv_tavern1_guest2"
    }
    ```


<small>Data from v0.8.18</small>
