---
description: "Stuephant is a non-player character (NPC) in Andor's Trail, found in Guynmart Castle. Starts Marble hunting."
---

# ![](../assets/icons/monsters/monsters_maksiu1_0.png){ .sprite } Stuephant

**Where to find Stuephant:** Guynmart Castle: [Guynmart wood 10](../maps/guynmart_wood_10.md#pin-npc-guynmart_child)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_maksiu1_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Starts [Marble hunting](../quests/guynmart_marbles.md) |
| **Found in** | Guynmart Castle |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Quests

- [Marble hunting](../quests/guynmart_marbles.md): stages 10, 90

## Dialogue simulator

Set your quest stages and items, then talk to Stuephant. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_child_10.json" data-npc="Stuephant" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (10 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_child_10"></span>**`guynmart_child_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 21 of [Marble hunting](../quests/guynmart_marbles.md#stage-21); reached stage 22 of [Marble hunting](../quests/guynmart_marbles.md#stage-22); reached stage 23 of [Marble hunting](../quests/guynmart_marbles.md#stage-23); reached stage 24 of [Marble hunting](../quests/guynmart_marbles.md#stage-24); reached stage 25 of [Marble hunting](../quests/guynmart_marbles.md#stage-25); hand over 5× [Stuephant's marble](../items/guynmart_marble.md))* → [guynmart_child_90](#d-guynmart_child_90)
    - branch 2 *(if reached stage 90 of [Marble hunting](../quests/guynmart_marbles.md#stage-90))* → [guynmart_child_80](#d-guynmart_child_80)
    - branch 3 *(if reached stage 10 of [Marble hunting](../quests/guynmart_marbles.md#stage-10))* → [guynmart_child_50](#d-guynmart_child_50)
    - branch 4 → [guynmart_child_12](#d-guynmart_child_12)

    <span id="d-guynmart_child_90"></span>**`guynmart_child_90`** Stuephant: “My lost marbles! All five! Great, thank you! [Stuephant takes the marbles]” — **effects:** sets stage 90 of [Marble hunting](../quests/guynmart_marbles.md#stage-90)

    - “You're welcome.” → *conversation ends*

    <span id="d-guynmart_child_80"></span>**`guynmart_child_80`** Stuephant: “Thank you again for finding my marbles.”


    <span id="d-guynmart_child_50"></span>**`guynmart_child_50`** Stuephant: “*Sob* ... so you didn't find my marbles ... *sob*”

    - “I haven't given up yet. Please be patient.” → *conversation ends*

    <span id="d-guynmart_child_12"></span>**`guynmart_child_12`** Stuephant: “*Sob*”

    - “Don't cry, little one. What's your name?” → [guynmart_child_14](#d-guynmart_child_14)

    <span id="d-guynmart_child_14"></span>**`guynmart_child_14`** Stuephant: “*Sob* ... Stuephant ... *sob*”

    - “There there now. What's the matter?” → [guynmart_child_20](#d-guynmart_child_20)

    <span id="d-guynmart_child_20"></span>**`guynmart_child_20`** Stuephant: “I have lost my five best marbles!”

    - “Oh dear, That is all? I will find them for you.” → [guynmart_child_30](#d-guynmart_child_30)
    - “Look, here I have a nice teddy bear for you.” *(if hand over 1× [Old Teddy Bear](../items/guynmart_doll.md))* → [guynmart_child_22](#d-guynmart_child_22)
    - “The quicker I leave, the sooner I have silence and peace again.” → *conversation ends*

    <span id="d-guynmart_child_30"></span>**`guynmart_child_30`** Stuephant: “I have lost them here in the yard or in the field over there.” — **effects:** sets stage 10 of [Marble hunting](../quests/guynmart_marbles.md#stage-10), spawns monsters on guynmart_wood_10, spawns monsters on guynmart_wood_10, spawns monsters on guynmart_wood_10, spawns monsters on guynmart_wood_10, spawns monsters on guynmart_wood_10

    - Next → [guynmart_child_32](#d-guynmart_child_32)

    <span id="d-guynmart_child_22"></span>**`guynmart_child_22`** Stuephant: “Great - thank you!”

    - “Much better. Now tell me about your marbles.” → [guynmart_child_30](#d-guynmart_child_30)

    <span id="d-guynmart_child_32"></span>**`guynmart_child_32`** Stuephant: “Five beautiful marbles. Maybe you should look more than once in each place. They are so small you could easily miss them.”

    - “Don't be so sad, I will find them soon.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 10 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `guynmart_child` |
    | Type (wiki) | NPC |
    | Spawn group | `guynmart_child` |
    | Loot table | – |
    | Conversation | `guynmart_child_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_maksiu1:0` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_child",
     "name": "Stuephant",
     "iconID": "monsters_maksiu1:0",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_child_10"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_child.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_child.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_child.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_child.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
