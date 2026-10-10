---
description: "Kazaul acolyte is a non-player character (NPC) in Andor's Trail, found in Undertell 5."
---

# ![](../assets/icons/monsters/monsters_ld2_96.png){ .sprite } Kazaul acolyte

**Where to find Kazaul acolyte:** [Undertell 5](../maps/undertell_5.md#pin-npc-kazaul_acolyte)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld2_96.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Undertell 5 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Quests

- [The fifth master](../quests/fifth_master.md): stage 85

## Dialogue simulator

Set your quest stages and items, then talk to Kazaul acolyte. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/anavrin_resurrection_narrator_10.json" data-npc="Kazaul acolyte" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-anavrin_resurrection_narrator_10"></span>**`anavrin_resurrection_narrator_10`** [Dummy NPC](../monsters/none.md): “The Kazaul acolyte stands before Anavrin's shrine, its hands trembling as it unrolls the aged parchment. The air grows colder, shadows stretching across the floor.”

    - “[Wait for the ritual to begin.]” → [anavrin_resurrection_narrator_15](#d-anavrin_resurrection_narrator_15)

    <span id="d-anavrin_resurrection_narrator_15"></span>**`anavrin_resurrection_narrator_15`** [Dummy NPC](../monsters/none.md): “The acolyte begins to read from the pages, the syllables harsh and alien.”

    - “[Wait for the ritual to begin.]” → [anavrin_resurrection_10](#d-anavrin_resurrection_10)

    <span id="d-anavrin_resurrection_10"></span>**`anavrin_resurrection_10`** [Kazaul acolyte](../monsters/kazaul_acolyte.md): “Kazaul'te varmun iktel urul. Klatam ur turum Anavrin. Kazaul'thra mor'gul ven'taar. Uruk tharum vel Kazaul'ten mor. Kazaul hamat urul. Kazaul'the vurmor Anavrin urthaal!”

    - “[Keep listening.]” → [anavrin_resurrection_narrator_20](#d-anavrin_resurrection_narrator_20)

    <span id="d-anavrin_resurrection_narrator_20"></span>**`anavrin_resurrection_narrator_20`** [Kazaul acolyte](../monsters/kazaul_acolyte.md): “Kulauil hamar urum Kazaul'te...Kazaul hamat urul...Klaatu ur turum Kazaul'te!”

    - Next → [anavrin_resurrection_narrator_30](#d-anavrin_resurrection_narrator_30)

    <span id="d-anavrin_resurrection_narrator_30"></span>**`anavrin_resurrection_narrator_30`** [Dummy NPC](../monsters/none.md): “The parchment disintegrates in its grasp. The acolyte trembles violently, energy surging around the shrine.”

    - “[Watch what happens.]” → [anavrin_resurrection_20](#d-anavrin_resurrection_20)

    <span id="d-anavrin_resurrection_20"></span>**`anavrin_resurrection_20`** [Dummy NPC](../monsters/none.md): “The acolyte exhales, its voice fading to a whisper. The silence...broken...Its body turns to dust, carried away by unseen breath as the air shudders with awakening power. So...the Fifth Master breathes once more.” — **effects:** spawns monsters on undertell_5, removes monsters from undertell_5

    - “What...what have I done?” → [anavrin_resurrection_30](#d-anavrin_resurrection_30)

    <span id="d-anavrin_resurrection_30"></span>**`anavrin_resurrection_30`** [Anavrin](../monsters/anavrin.md): “You have undone silence itself, mortal. The rift shall open again, and through it we will see our dominion restored.” — **effects:** sets stage 85 of [The fifth master](../quests/fifth_master.md#stage-85)

    - “[Try to comprehend the revelation.]” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `kazaul_acolyte` |
    | Type (wiki) | NPC |
    | Spawn group | `kazaul_acolyte` |
    | Loot table | – |
    | Conversation | `anavrin_resurrection_narrator_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:96` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "kazaul_acolyte",
     "name": "Kazaul acolyte",
     "iconID": "monsters_ld2:96",
     "phraseID": "anavrin_resurrection_narrator_10"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_acolyte.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_acolyte.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_acolyte.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_acolyte.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
