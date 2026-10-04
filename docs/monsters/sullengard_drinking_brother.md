# ![](../assets/icons/monsters/monsters_ld1_130.png){ .sprite } Drinking brother

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_130.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `sullengard_drinking_brother` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Sullengard |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

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
| [sullengard_tavern](../maps/sullengard_tavern.md) | Sullengard | 1 | – |


## Quests

- [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md): stages 23

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Drinking brother. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_drinking_brother_0.json" data-npc="Drinking brother" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-sullengard_drinking_brother_0"></span>**`sullengard_drinking_brother_0`** Drinking brother: “Hey there kid. Us three here are brothers from Stoutford, but we travel all the way here for the vast greatness of brews! [burp]”

    - “Stoutford? Where's that?” *(if NOT reached stage 4 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-4))* → [sullengard_drinking_brother_10](#d-sullengard_drinking_brother_10)
    - “I'm looking for my my brother Andor. He looks a lot like me, but he is older. Have you seen him?” → [sullengard_drinking_brother_20](#d-sullengard_drinking_brother_20)
    - “I'm looking into the armory break-in and robbery and I am wondering if you saw or know anything about it?” *(if NOT reached stage 23 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-23); latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-30) is 30)* → [sullengard_drinking_brother_30](#d-sullengard_drinking_brother_30)

    <span id="d-sullengard_drinking_brother_10"></span>**`sullengard_drinking_brother_10`** Drinking brother: “Oh, you know nothing. I feel sorry for you.”


    <span id="d-sullengard_drinking_brother_20"></span>**`sullengard_drinking_brother_20`** Drinking brother: “Nope. Sorry kid.”


    <span id="d-sullengard_drinking_brother_30"></span>**`sullengard_drinking_brother_30`** Drinking brother: “Are you kidding? We are always in here enjoying ourselves. So unless the crime happened in here, I've not seen it.” — **effects:** sets stage 23 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-23)

    - “Thanks.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_drinking_brother.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_drinking_brother.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_drinking_brother.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_drinking_brother.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `sullengard_drinking_brother` |
    | Spawn group | `sullengard_drinking_brother` |
    | Loot table | – |
    | Conversation | `sullengard_drinking_brother_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:130` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_drinking_brother",
     "name": "Drinking brother",
     "iconID": "monsters_ld1:130",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "sullengard_drinking_brother",
     "phraseID": "sullengard_drinking_brother_0"
    }
    ```


<small>Data from v0.8.18</small>
