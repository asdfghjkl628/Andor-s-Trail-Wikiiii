---
description: "Dunla is a non-player character (NPC) in Andor's Trail, found in Vilegard. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_rogue1_0.png){ .sprite } Dunla

**Where to find Dunla:** Vilegard: [Vilegard tavern](../maps/vilegard_tavern.md#pin-npc-dunla)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rogue1_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Shopkeeper |
| **Found in** | Vilegard |
| **Entry ID** | `dunla` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Sharp iron dagger](../items/dagger1.md) | 100% | 1 |
| [Villain's blade](../items/sword_villains.md) | 100% | 1 |
| [Fine shirt](../items/shirt2.md) | 100% | 1 |
| [Firm leather armor](../items/armour_firm_leather.md) | 100% | 1 |
| [Superior leather armor](../items/armor2.md) | 100% | 1 |
| [Hardened leather shirt](../items/shirt_dmgresist.md) | 100% | 1 |
| [Snakeskin gloves](../items/gloves3.md) | 100% | 1 |
| [Fine snakeskin gloves](../items/gloves4.md) | 100% | 1 |
| [Polished combat ring](../items/ring_polished_combat.md) | 100% | 1 |
| [Ring of backstabbing](../items/ring_backstab.md) | 100% | 1 |
| [Curved dagger](../items/daggr_curv.md) | 100% | 1 |
| [Bloodletter](../items/daggr_bloodlet.md) | 100% | 1 |
| [Polished gem](../items/gem3.md) | 100% | 5 |

## Quests

- [Beer Bootlegging](../quests/beer_bootlegging.md): stage 40
- [Thief apprentice](../quests/Thieves01.md): stage 30

## Dialogue simulator

Set your quest stages and items, then talk to Dunla. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/dunla_default.json" data-npc="Dunla" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (9 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-dunla_default"></span>**`dunla_default`** [Dunla](../monsters/dunla.md): “You look like a smart fellow. Need any supplies?”

    - “Sure, let me see what you have available.” → *shop opens*
    - “What can you tell me about yourself?” → [dunla_1](#d-dunla_1)
    - “I spoke to Tharwyn about who her beer 'distributor' is and she sent me to you.” *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-30) is 30; NOT reached stage 50 of [The ruthless Crackshot](../quests/Thieves03.md#stage-50))* → [dunla_beer](#d-dunla_beer)
    - “I spoke to Tharwyn about who her beer 'distributor' is and she sent me to you.” *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-30) is 30; reached stage 50 of [The ruthless Crackshot](../quests/Thieves03.md#stage-50))* → [dunla_beer_10](#d-dunla_beer_10)

    <span id="d-dunla_1"></span>**`dunla_1`** Dunla: “Me? I am no one. You didn't even see me. You certainly did not talk to me.”

    - “Troublemaker sent me to get your report.” *(if reached stage 25 of [Thief apprentice](../quests/Thieves01.md#stage-25); NOT reached stage 30 of [Thief apprentice](../quests/Thieves01.md#stage-30))* → [dunla_guild_1](#d-dunla_guild_1)

    <span id="d-dunla_beer"></span>**`dunla_beer`** Dunla: “She did, did she? Well, that is an insider topic, and you are not an "insider". Come back when you are.”


    <span id="d-dunla_beer_10"></span>**`dunla_beer_10`** Dunla: “She did, did she? What do you want to know?”

    - “What is this 'business agreement' that the taven owners have?” → [dunla_beer_20](#d-dunla_beer_20)

    <span id="d-dunla_guild_1"></span>**`dunla_guild_1`** Dunla: “What? I don't know what you are talking about.”

    - “You are no one. No one knows you. No one has seen you.” *(if NOT reached stage 30 of [Thief apprentice](../quests/Thieves01.md#stage-30))* → [dunla_guild_2a](#d-dunla_guild_2a)
    - “You are no one. No one knows you. No one has seen you.” *(if reached stage 30 of [Thief apprentice](../quests/Thieves01.md#stage-30))* → [dunla_guild_2b](#d-dunla_guild_2b)

    <span id="d-dunla_beer_20"></span>**`dunla_beer_20`** Dunla: “That is not for me to say.”

    - “Is the Thieves guild the 'distributors'?” → [dunla_beer_30](#d-dunla_beer_30)

    <span id="d-dunla_guild_2a"></span>**`dunla_guild_2a`** Dunla: “So, you are one of us. Here, take my journal.” — **effects:** gives 1× [Dunla's Journal](../items/Dunla_journal.md), sets stage 30 of [Thief apprentice](../quests/Thieves01.md#stage-30)

    - “Thank you.” → *conversation ends*
    - “Do you have anything to trade?” → *shop opens*

    <span id="d-dunla_guild_2b"></span>**`dunla_guild_2b`** Dunla: “Sorry, I don't have any more information for you.”

    - “Do you have anything to trade?” → *shop opens*
    - “Ok, bye.” → *conversation ends*

    <span id="d-dunla_beer_30"></span>**`dunla_beer_30`** Dunla: “Yes, yes we are, but if you want to learn more, go talk to Farrik back at our guild house.” — **effects:** sets stage 40 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-40)




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 3 lines added, 2 lines changed |
| [v0.8.2](../versions/0.8.2.md) | Dialogue: 4 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `dunla` |
    | Spawn group | `dunla` |
    | Loot table | `shop_dunla` |
    | Conversation | `dunla_default` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rogue1:0` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "dunla",
     "name": "Dunla",
     "iconID": "monsters_rogue1:0",
     "monsterClass": "humanoid",
     "spawnGroup": "dunla",
     "phraseID": "dunla_default",
     "droplistID": "shop_dunla"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dunla.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dunla.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dunla.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dunla.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
