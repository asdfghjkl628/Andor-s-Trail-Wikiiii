# ![](../assets/icons/monsters/monsters_rltiles1_74.png){ .sprite } Eraepsekahs

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_74.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `eraepsekahs` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Remgard |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

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
| [remgard_tavern0](../maps/remgard_tavern0.md) | Remgard | 1 | – |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Eraepsekahs. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/eraep_0.json" data-npc="Eraepsekahs" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-eraep_0"></span>**`eraep_0`** Eraepsekahs: “Hello. Can I help you?”

    - “I am looking for my brother, Andor. He looks a bit like me. Have you seen him?” → [eraep_1](#d-eraep_1)

    <span id="d-eraep_1"></span>**`eraep_1`** Eraepsekahs: “There was someone that came here recently that looked somewhat like you, but I didn't speak to him. Sorry, that's all the information I can give you.”

    - “OK. Thanks. Bye.” → *conversation ends*
    - “Thanks. What do you do around here?” → [eraep_2](#d-eraep_2)

    <span id="d-eraep_2"></span>**`eraep_2`** Eraepsekahs: “I came here for the solitude. I wish to be a playwright. So I am writing my first play. I hope that someday I will be famous.”

    - “Best of luck. Sounds like a boring thing to do to me.” → *conversation ends*
    - “What is the play about?” → [eraep_3](#d-eraep_3)

    <span id="d-eraep_3"></span>**`eraep_3`** Eraepsekahs: “It is set in a very small village. So I called it "Hamlet". An old Dhayavarian word for a very small village.”

    - “Life in a small village? I come from one. It must be a very boring play.” → [eraep_4](#d-eraep_4)

    <span id="d-eraep_4"></span>**`eraep_4`** Eraepsekahs: “Not at all. It involves murder, revenge for the murder, but the murderer knows the avenger is coming, so plots to kill him. There's ghosts too.”

    - “OK. Sounds more exciting than I thought. If you finish it and I happen to be close to a showing, perhaps I will watch.” → *conversation ends*
    - “Sounds exciting! But if you really want to get the audience's attention you need to add some s...” → [eraep_5](#d-eraep_5)

    <span id="d-eraep_5"></span>**`eraep_5`** Eraepsekahs: “Enough! It is my play. I do not need your advice!”

    - “OK. I was only going to make a suggestion. Bye.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=eraepsekahs.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=eraepsekahs.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=eraepsekahs.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=eraepsekahs.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `eraepsekahs` |
    | Spawn group | `eraepsekahs` |
    | Loot table | – |
    | Conversation | `eraep_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:74` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "eraepsekahs",
     "name": "Eraepsekahs",
     "iconID": "monsters_rltiles1:74",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "eraep_0"
    }
    ```


<small>Data from v0.8.18</small>
