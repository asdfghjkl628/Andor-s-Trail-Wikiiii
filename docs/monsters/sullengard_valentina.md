# ![](../assets/icons/monsters/monsters_ld1_167.png){ .sprite } Valentina

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_167.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `sullengard_valentina` |
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
| [sullengard1_aunts_house](../maps/sullengard1_aunts_house.md) | Sullengard | 1 | – |


## Quests

- [Search for Andor](../quests/andor.md): stages 100

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Valentina. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_valentina_0.json" data-npc="Valentina" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (13 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-sullengard_valentina_0"></span>**`sullengard_valentina_0`** [Valentina](../monsters/sullengard_valentina.md): “$playername, what are you doing here?!”

    - “Mom, I could ask you the same question.” → [sullengard_find_mother_10](#d-sullengard_find_mother_10)

    <span id="d-sullengard_find_mother_10"></span>**`sullengard_find_mother_10`** Valentina: “I'm your mother, answer my question.”

    - “Father sent me to look for Andor as he left shortly after you did and hasn't returned.” → [sullengard_find_mother_20](#d-sullengard_find_mother_20)

    <span id="d-sullengard_find_mother_20"></span>**`sullengard_find_mother_20`** Valentina: “What?! Where is he? Why is your father not with you?”

    - “I guess because he needed to stay home and watch over the house. Or maybe he thinks I'm ready for the challenge?” → [sullengard_find_mother_30](#d-sullengard_find_mother_30)

    <span id="d-sullengard_find_mother_30"></span>**`sullengard_find_mother_30`** Valentina: “Typical Mikhail! So lazy and irresponsible.”

    - “I guess, but I can handle myself and have learned a lot about Andor.” → [sullengard_find_mother_33](#d-sullengard_find_mother_33)
    - “I totally agree with you.” → [sullengard_find_mother_35](#d-sullengard_find_mother_35)

    <span id="d-sullengard_find_mother_33"></span>**`sullengard_find_mother_33`** Valentina: “You've grown up so fast. Stop doing that. You are making me feel old.”

    - “Sorry, mother. You have still not answered my question though. What are you doing here?” → [sullengard_find_mother_40](#d-sullengard_find_mother_40)

    <span id="d-sullengard_find_mother_35"></span>**`sullengard_find_mother_35`** Valentina: “Don't you dare talk ill of your father. He may be lazy, but he is still your father.”

    - “Sorry, mother. You are right, but you have still not answered my question. What are you doing here?” → [sullengard_find_mother_40](#d-sullengard_find_mother_40)

    <span id="d-sullengard_find_mother_40"></span>**`sullengard_find_mother_40`** Valentina: “I'm visiting my sister, your aunt Valeria.”

    - “Your sister? My aunt? What are you talking about?” → [sullengard_find_mother_50](#d-sullengard_find_mother_50)

    <span id="d-sullengard_find_mother_50"></span>**`sullengard_find_mother_50`** Valentina: “Yes, $playername. This is your aunt Valeria. Please say "hi".”

    - “Um...it's nice to meet you aunt Valeria.” → [sullengard_valeria_0](#d-sullengard_valeria_0)

    <span id="d-sullengard_valeria_0"></span>**`sullengard_valeria_0`** [Valeria](../monsters/sullengard_valeria.md): “Hello $playername, it's so wonderful to finally meet you after all of these years.”

    - “But, I don't have an aunt?” *(if NOT reached stage 100 of [Search for Andor](../quests/andor.md#stage-100))* → [sullengard_find_mother_60](#d-sullengard_find_mother_60)
    - “How come mother never spoke of you or told me that she had a sister?” → [sullengard_valeria_10](#d-sullengard_valeria_10)

    <span id="d-sullengard_find_mother_60"></span>**`sullengard_find_mother_60`** [Valentina](../monsters/sullengard_valentina.md): “$playername, I will explain this to you later.”

    - “OK, you promise?” → [sullengard_find_mother_70](#d-sullengard_find_mother_70)

    <span id="d-sullengard_valeria_10"></span>**`sullengard_valeria_10`** Valentina: “That is not for me to tell you. Maybe back at home, she will explain it to you.”

    - Next → [sullengard_find_mother_60](#d-sullengard_find_mother_60)

    <span id="d-sullengard_find_mother_70"></span>**`sullengard_find_mother_70`** Valentina: “Yes, but in the meantime, I'm going home and I expect you there shortly after me.”

    - “But what about my search for Andor? Father expects me to find him before I come home again.” → [sullengard_find_mother_80](#d-sullengard_find_mother_80)

    <span id="d-sullengard_find_mother_80"></span>**`sullengard_find_mother_80`** Valentina: “Just follow me home and we can talk there. I may have something to aid you in your search for Andor.” — **effects:** sets stage 100 of [Search for Andor](../quests/andor.md#stage-100), removes monsters from sullengard1_aunts_house, spawns monsters on home




## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 13 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_valentina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_valentina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_valentina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_valentina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `sullengard_valentina` |
    | Spawn group | `sullengard_valentina` |
    | Loot table | – |
    | Conversation | `sullengard_valentina_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:167` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_valentina",
     "name": "Valentina",
     "iconID": "monsters_ld1:167",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "sullengard_valentina",
     "phraseID": "sullengard_valentina_0"
    }
    ```


<small>Data from v0.8.18</small>
