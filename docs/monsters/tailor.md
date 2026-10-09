---
description: "Tailor is a non-player character (NPC) in Andor's Trail, found in Fallhaven. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_men2_0.png){ .sprite } Tailor

**Where to find Tailor:** Fallhaven: [Fallhaven clothes](../maps/fallhaven_clothes.md#pin-npc-tailor)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men2_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Shopkeeper |
| **Found in** | Fallhaven |
| **Entry ID** | `tailor` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Green hat](../items/hat1.md) | 100% | 1 |
| [Fine green hat](../items/hat2.md) | 100% | 1 |
| [Cloth shirt](../items/shirt1.md) | 100% | 1 |
| [Torn shirt](../items/shirt_torn.md) | 100% | 1 |
| [Weathered shirt](../items/shirt_weathered.md) | 100% | 1 |
| [Patched cloth shirt](../items/shirt_patched_cloth.md) | 100% | 1 |
| [Fine shirt](../items/shirt2.md) | 100% | 1 |
| [Hardened leather shirt](../items/shirt_dmgresist.md) | 100% | 1 |
| [Gloves of fumbling](../items/gloves_fumbling.md) | 100% | 1 |
| [Fancy gloves](../items/gloves_fancy.md) | 100% | 1 |
| [Crude cloth gloves](../items/gloves_crude_cloth.md) | 100% | 1 |
| [Blood-stained gloves](../items/used_gloves.md) | 100% | 1 |
| [Bar brawler's gloves](../items/gloves_barbrawler.md) | 100% | 1 |
| [Gloves of swift attack](../items/gloves_attack1.md) | 100% | 1 |
| [Crude leather boots](../items/boots_crude_leather.md) | 100% | 1 |
| [Sewn footwear](../items/boots_sewn.md) | 100% | 1 |
| [Leather boots](../items/boots1.md) | 100% | 1 |
| [Snakeskin boots](../items/boots3.md) | 100% | 1 |
| [Jewel of Fallhaven](../items/jewel_fallhaven.md) | 100% | 1 |
| [Ring of fumbling](../items/ring_fumbling.md) | 100% | 1 |
| [Mundane ring](../items/ring1.md) | 100% | 1 |
| [Polished ring](../items/ring2.md) | 100% | 1 |

## Quests

- [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md): stage 68

## Dialogue simulator

Set your quest stages and items, then talk to Tailor. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/fallhaven_clothes_0.json" data-npc="Tailor" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (9 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-fallhaven_clothes_0"></span>**`fallhaven_clothes_0`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 69 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-69))* → [fallhaven_clothes](#d-fallhaven_clothes)
    - Next *(if reached stage 66 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-66))* → [fallhaven_clothes_10](#d-fallhaven_clothes_10)
    - Next *(if reached stage 68 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-68))* → [fallhaven_clothes_40](#d-fallhaven_clothes_40)
    - Next → [fallhaven_clothes](#d-fallhaven_clothes)

    <span id="d-fallhaven_clothes"></span>**`fallhaven_clothes`** Tailor: “Welcome to my shop. Please browse my selection of fine clothing and jewelry.”

    - “Let me see your wares.” → *shop opens*

    <span id="d-fallhaven_clothes_10"></span>**`fallhaven_clothes_10`** [Tailor](../monsters/tailor.md): “Hey! What are you doing here? How did you get in?” — **effects:** sets stage 68 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-68)

    - “By the door. Why?” → [fallhaven_clothes_20](#d-fallhaven_clothes_20)

    <span id="d-fallhaven_clothes_40"></span>**`fallhaven_clothes_40`** Tailor: “I know your face. How dare you to come back?”

    - “Are you sure you don't mix me with my brother?” → [fallhaven_clothes_42](#d-fallhaven_clothes_42)

    <span id="d-fallhaven_clothes_20"></span>**`fallhaven_clothes_20`** Tailor: “Nonsense. I would have noticed.”

    - Next → [fallhaven_clothes_30](#d-fallhaven_clothes_30)

    <span id="d-fallhaven_clothes_42"></span>**`fallhaven_clothes_42`** Tailor: “Andor? I know that boy all too well.”

    - “Let me see your wares.” *(if wearing [Jewel of Fallhaven](../items/jewel_fallhaven.md))* → [fallhaven_clothes_44](#d-fallhaven_clothes_44)
    - “Let me see your wares.” *(if NOT wearing [Jewel of Fallhaven](../items/jewel_fallhaven.md))* → *shop opens*

    <span id="d-fallhaven_clothes_30"></span>**`fallhaven_clothes_30`** [Tailor](../monsters/tailor.md): “Leave immediatly, or I'll call the guards!”

    - Next → [fallhaven_clothes_32](#d-fallhaven_clothes_32)

    <span id="d-fallhaven_clothes_44"></span>**`fallhaven_clothes_44`** Tailor: “You wear the stolen valuable necklace and dare lie to my face?”

    - Next → [fallhaven_clothes_30](#d-fallhaven_clothes_30)

    <span id="d-fallhaven_clothes_32"></span>**`fallhaven_clothes_32`** Tailor: “And don't dare to enter my house again!”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.8.12.1](../versions/0.8.12.1.md) | Conversation changed<br>Dialogue: 8 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `tailor` |
    | Spawn group | `fallhaven_clothes` |
    | Loot table | `shop_fallhaven_clothes` |
    | Conversation | `fallhaven_clothes_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men2:0` |
    | Defined in | `res/raw/monsterlist_fallhaven_npcs.json` |

    Raw data:

    ```json
    {
     "id": "tailor",
     "name": "Tailor",
     "iconID": "monsters_men2:0",
     "monsterClass": "humanoid",
     "spawnGroup": "fallhaven_clothes",
     "phraseID": "fallhaven_clothes_0",
     "droplistID": "shop_fallhaven_clothes"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tailor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tailor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tailor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tailor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
