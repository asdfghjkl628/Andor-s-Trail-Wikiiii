---
description: "Nuik is a non-player character (NPC) in Andor's Trail, found in Guynmart Castle."
---

# ![](../assets/icons/monsters/monsters_ld1_134.png){ .sprite } Nuik

**Where to find Nuik:** Guynmart Castle: [Guynmart](../maps/guynmart.md#pin-npc-guynmart_nuik)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_134.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Guynmart Castle |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Dialogue simulator

Set your quest stages and items, then talk to Nuik. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_nuik_10.json" data-npc="Nuik" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (10 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_nuik_10"></span>**`guynmart_nuik_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 200 of [Roses](../quests/guynmart.md#stage-200))* → [guynmart_nuik_20](#d-guynmart_nuik_20)
    - branch 2 *(if reached stage 64 of [Roses](../quests/guynmart.md#stage-64))* → [guynmart_nuik_80](#d-guynmart_nuik_80)
    - branch 3 *(if reached stage 62 of [Roses](../quests/guynmart.md#stage-62))* → [guynmart_nuik_100](#d-guynmart_nuik_100)
    - branch 4 → [guynmart_nuik_30](#d-guynmart_nuik_30)

    <span id="d-guynmart_nuik_20"></span>**`guynmart_nuik_20`** Nuik: “Hello $playername! It's a lovely day, isn't it?”


    <span id="d-guynmart_nuik_80"></span>**`guynmart_nuik_80`** Nuik: “Hi kid, where are you going in such a hurry?”

    - “Sorry, I have no time for small talk.” → *conversation ends*

    <span id="d-guynmart_nuik_100"></span>**`guynmart_nuik_100`** Nuik: “Hi kid, where are you going in such a hurry?”

    - “Hofala the cook sent me, I need some herbs for Lady Hannah's lunch.” → [guynmart_nuik_110](#d-guynmart_nuik_110)

    <span id="d-guynmart_nuik_30"></span>**`guynmart_nuik_30`** Nuik: “Hi Kid. Do you love flowers as much as I do?”

    - “Oh yes, I do! Maybe I will become a gardener myself.” → [guynmart_nuik_40](#d-guynmart_nuik_40)
    - “Lady Hannah asked me to bring her a rose. Please give me the most beautiful one you have.” *(if reached stage 70 of [Roses](../quests/guynmart.md#stage-70))* → [guynmart_nuik_50](#d-guynmart_nuik_50)

    <span id="d-guynmart_nuik_110"></span>**`guynmart_nuik_110`** Nuik: “You are lucky! I have just gathered some wonderful fresh herbs. Take these to Hofala.” — **effects:** gives [Hannah's special herbs](../items/guynmart_herbs.md)

    - “Thanks a lot!” → *conversation ends*

    <span id="d-guynmart_nuik_40"></span>**`guynmart_nuik_40`** Nuik: “That is nice.”

    - “May I pick some flowers?” → [guynmart_nuik_60](#d-guynmart_nuik_60)
    - “Could you sell me one rose?” → [guynmart_nuik_70](#d-guynmart_nuik_70)
    - “Bye.” → *conversation ends*

    <span id="d-guynmart_nuik_50"></span>**`guynmart_nuik_50`** Nuik: “No, sorry, anyone could come to me and ask this. I can not give you any flowers.”

    - “May I pick the rose myself?” → [guynmart_nuik_60](#d-guynmart_nuik_60)
    - “Bye.” → *conversation ends*

    <span id="d-guynmart_nuik_60"></span>**`guynmart_nuik_60`** Nuik: “No, this is strictly forbidden! The only person who is allowed to pick flowers is Lady Hannah herself.”

    - “Could you sell me one rose?” → [guynmart_nuik_70](#d-guynmart_nuik_70)
    - “Bye.” → *conversation ends*

    <span id="d-guynmart_nuik_70"></span>**`guynmart_nuik_70`** Nuik: “Are you kidding? These flowers are priceless! You can't pay for them!”

    - “May I pick the rose myself?” → [guynmart_nuik_60](#d-guynmart_nuik_60)
    - “Lady Hannah asked me to bring her a rose. Please give me the most beautiful one you have.” *(if reached stage 70 of [Roses](../quests/guynmart.md#stage-70))* → [guynmart_nuik_50](#d-guynmart_nuik_50)
    - “Bye.” → *conversation ends*



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
    | Entry ID | `guynmart_nuik` |
    | Type (wiki) | NPC |
    | Spawn group | `guynmart_nuik` |
    | Loot table | – |
    | Conversation | `guynmart_nuik_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:134` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_nuik",
     "name": "Nuik",
     "iconID": "monsters_ld1:134",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_nuik_10"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_nuik.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_nuik.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_nuik.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_nuik.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
