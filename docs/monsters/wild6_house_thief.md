---
description: "Rennik is a non-player character (NPC) in Andor's Trail, found in Blackwater Mountain."
---

# ![](../assets/icons/monsters/monsters_tometik6_36.png){ .sprite } Rennik

**Where to find Rennik:** Blackwater Mountain: [wild6_house](../maps/wild6_house.md#pin-npc-wild6_house_thief)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik6_36.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Blackwater Mountain |
| **Entry ID** | `wild6_house_thief` |
| **Introduced** | [v0.8.8](../versions/0.8.8.md) |

</div>

## Quests

- [Wanted men](../quests/wanted_men.md): stage 57
- [Sutdove_nondisplay (hidden flag)](../quests/sutdover_hidden.md): stage 2

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Rennik. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/thief_rennik_selector.json" data-npc="Rennik" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-thief_rennik_selector"></span>**`thief_rennik_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 57 of [Wanted men](../quests/wanted_men.md#stage-57); NOT reached stage 2 of [Sutdove_nondisplay (hidden flag)](../quests/sutdover_hidden.md#stage-2))* → [thief_rennik_10](#d-thief_rennik_10)
    - Next *(if NOT reached stage 57 of [Wanted men](../quests/wanted_men.md#stage-57); reached stage 2 of [Sutdove_nondisplay (hidden flag)](../quests/sutdover_hidden.md#stage-2))* → [thief_rennik_20](#d-thief_rennik_20)
    - Next → [thief_rennik_generic_10](#d-thief_rennik_generic_10)

    <span id="d-thief_rennik_10"></span>**`thief_rennik_10`** Rennik: “Ah, $playername has finally returned. Please, take this crystal and some gold as our thanks to you.” — **effects:** gives [Gold coins](../items/gold.md), [Nixite crystal](../items/nixite_crystal.md), sets stage 2 of [Sutdove_nondisplay (hidden flag)](../quests/sutdover_hidden.md#stage-2)

    - “Thank you.” → [thief_rennik_20](#d-thief_rennik_20)

    <span id="d-thief_rennik_20"></span>**`thief_rennik_20`** Rennik: “You will be happy to hear that we have captured Defy and his four accomplices before they could steal from us.”

    - “That's great news indeed. Where are they now?” → [thief_rennik_30](#d-thief_rennik_30)

    <span id="d-thief_rennik_generic_10"></span>**`thief_rennik_generic_10`** Rennik: “I am here now to watch out for suspicious activity and people.”


    <span id="d-thief_rennik_30"></span>**`thief_rennik_30`** Rennik: “We are keeping them in our holding cage in Fallhaven.” — **effects:** sets stage 57 of [Wanted men](../quests/wanted_men.md#stage-57), spawns monsters on guildbrig2

    - “Is there anything else that I should know about?” → [thief_rennik_40](#d-thief_rennik_40)

    <span id="d-thief_rennik_40"></span>**`thief_rennik_40`** Rennik: “Yes. That fifth man, the one that was not one of us...”

    - “You mean Alaric?” → [thief_rennik_50](#d-thief_rennik_50)

    <span id="d-thief_rennik_50"></span>**`thief_rennik_50`** Rennik: “His name is not important to me...”

    - Next → [thief_rennik_55](#d-thief_rennik_55)

    <span id="d-thief_rennik_55"></span>**`thief_rennik_55`** Rennik: “We've learned that he was part of a crime in Sullengard. You may want to visit Sullengard and inform them that we have their guy.”

    - “I will. Thank you again.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added<br>Dialogue: 8 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `wild6_house_thief` |
    | Spawn group | `wild6_house_thief_spawn` |
    | Loot table | – |
    | Conversation | `thief_rennik_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik6:36` |
    | Defined in | `res/raw/monsterlist_mt_galmore.json` |

    Raw data:

    ```json
    {
     "id": "wild6_house_thief",
     "name": "Rennik",
     "iconID": "monsters_tometik6:36",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "wild6_house_thief_spawn",
     "phraseID": "thief_rennik_selector"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild6_house_thief.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild6_house_thief.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild6_house_thief.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wild6_house_thief.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
