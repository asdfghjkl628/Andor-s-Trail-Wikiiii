# ![](../assets/icons/monsters/monsters_rltiles1_85.png){ .sprite } Kuldan

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_85.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `kuldan` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Loneford |
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
| [loneford3](../maps/loneford3.md) | Loneford | 1 | – |


## Quests

- [Flows through the veins](../quests/loneford.md): stages 54, 55

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Kuldan. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/kuldan.json" data-npc="Kuldan" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (15 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-kuldan"></span>**`kuldan`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 55 of [Flows through the veins](../quests/loneford.md#stage-55))* → [kuldan_c_1](#d-kuldan_c_1)
    - branch 2 *(if reached stage 54 of [Flows through the veins](../quests/loneford.md#stage-54))* → [kuldan_bc_1](#d-kuldan_bc_1)
    - branch 3 → [kuldan_1](#d-kuldan_1)

    <span id="d-kuldan_c_1"></span>**`kuldan_c_1`** Kuldan: “Feygard is grateful for your assistance in solving the mystery of the illness here in Loneford.”

    - Next → [kuldan_c_2](#d-kuldan_c_2)

    <span id="d-kuldan_bc_1"></span>**`kuldan_bc_1`** Kuldan: “What is this? This smells like Narwood poison. You say you retrieved this from Buceth?” — **effects:** sets stage 54 of [Flows through the veins](../quests/loneford.md#stage-54)

    - “Buceth was part of a mission by the Nor City priests to poison the water well here in Loneford.” → [kuldan_bc_2](#d-kuldan_bc_2)

    <span id="d-kuldan_1"></span>**`kuldan_1`** Kuldan: “Please report any suspicious behavior you might see.”

    - “I know what the cause of the illness is. Have a look at this vial that Buceth had on him.” *(if reached stage 50 of [Flows through the veins](../quests/loneford.md#stage-50); hand over 1× [Buceth's vial of green liquid](../items/buceth_vial.md))* → [kuldan_bc_1](#d-kuldan_bc_1)
    - “Who are you?” → [kuldan_2](#d-kuldan_2)

    <span id="d-kuldan_c_2"></span>**`kuldan_c_2`** Kuldan: “We are trying to help the last few people that are still ill here now. Loneford might require our assistance from Feygard for quite some time.”


    <span id="d-kuldan_bc_2"></span>**`kuldan_bc_2`** Kuldan: “But this means ... it is the water that the people are getting ill from? This explains a lot of things.”

    - Next → [kuldan_bc_3](#d-kuldan_bc_3)

    <span id="d-kuldan_2"></span>**`kuldan_2`** Kuldan: “I am Kuldan, captain of this here detachment of guards in Loneford. Now, if you will excuse me, I have work to do.”


    <span id="d-kuldan_bc_3"></span>**`kuldan_bc_3`** Kuldan: “You my friend have done Loneford a great service by finding this, and by extension, Feygard as well. We should go catch Buceth for what he has done.”

    - “He is already dead.” → [kuldan_bc_4](#d-kuldan_bc_4)

    <span id="d-kuldan_bc_4"></span>**`kuldan_bc_4`** Kuldan: “Dead you say? Hmm, not quite the way we do things in Feygard, but I guess this is an exceptional case.”

    - Next → [kuldan_bc_5](#d-kuldan_bc_5)

    <span id="d-kuldan_bc_5"></span>**`kuldan_bc_5`** Kuldan: “I always suspected that those savages from Nor City were behind this all along.”

    - Next → [kuldan_bc_6](#d-kuldan_bc_6)

    <span id="d-kuldan_bc_6"></span>**`kuldan_bc_6`** Kuldan: “It's good to know that we now at least have some evidence to back up our claims.”

    - Next → [kuldan_bc_7](#d-kuldan_bc_7)

    <span id="d-kuldan_bc_7"></span>**`kuldan_bc_7`** Kuldan: “As for Loneford, I guess we will have to start bringing in water from Feygard to help the people here. Good thing they have us around, what would they do otherwise?”

    - Next → [kuldan_bc_8](#d-kuldan_bc_8)

    <span id="d-kuldan_bc_8"></span>**`kuldan_bc_8`** Kuldan: “And you, my friend - you should of course be sufficiently rewarded for your assistance in this matter. You should travel to the glorious city of Feygard to the northwest and report to the castle steward there for further instructions.”

    - Next → [kuldan_bc_9](#d-kuldan_bc_9)

    <span id="d-kuldan_bc_9"></span>**`kuldan_bc_9`** Kuldan: “I happen to know the castle steward personally, and I will send word to him about your help here.”

    - Next → [kuldan_bc_10](#d-kuldan_bc_10)

    <span id="d-kuldan_bc_10"></span>**`kuldan_bc_10`** Kuldan: “For the glory of Feygard, the people of Loneford may live on thanks to your help.” — **effects:** sets stage 55 of [Flows through the veins](../quests/loneford.md#stage-55)




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 5 lines changed<br>· text: “Dead you say? Hm, not quite the way we do things in Feygard, but I gu…” → “Dead you say? Hmm, not quite the way we do things in Feygard, but I g…”<br>· text: “But this means.. It is the water that the people are getting ill from…” → “But this means ... it is the water that the people are getting ill fr…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kuldan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kuldan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kuldan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kuldan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `kuldan` |
    | Spawn group | `kuldan` |
    | Loot table | – |
    | Conversation | `kuldan` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:85` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "kuldan",
     "name": "Kuldan",
     "iconID": "monsters_rltiles1:85",
     "monsterClass": "humanoid",
     "spawnGroup": "kuldan",
     "phraseID": "kuldan"
    }
    ```


<small>Data from v0.8.18</small>
