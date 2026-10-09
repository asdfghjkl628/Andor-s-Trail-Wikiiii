---
description: "Venanra is a non-player character (NPC) in Andor's Trail, found in Brimhaven. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_ld1_187.png){ .sprite } Venanra

**Where to find Venanra:** Brimhaven: [Brimhaven 2 laundry](../maps/brimhaven2_laundry.md#pin-npc-brv_laundry_boss)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_187.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Shopkeeper |
| **Found in** | Brimhaven |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Green dress](../items/green_dress.md) | 100% | 10 |

## Quests

- [A strange looking dagger](../quests/brv_dagger.md): stage 180
- [Brimhaven multipurpose story flags (hidden flag)](../quests/brv_nondisplay_multipurpose.md): stages 10, 15
- [Brimhaven warehouse delivery (hidden flag)](../quests/brv_wh_delivery_nondisplay.md): stage 40

## Dialogue simulator

Set your quest stages and items, then talk to Venanra. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_laundry_boss_0.json" data-npc="Venanra" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (16 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_laundry_boss_0"></span>**`brv_laundry_boss_0`** Venanra: “Hello, what can I do for you?”

    - “Can you sell me something?” *(if NOT reached stage 10 of [Brimhaven multipurpose story flags (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-10))* → [brv_laundry_boss_1](#d-brv_laundry_boss_1)
    - “I want to buy the dresses.” *(if reached stage 15 of [Brimhaven multipurpose story flags (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-15))* → *shop opens*
    - “I want you to improve some of my clothes.” *(if reached stage 10 of [Brimhaven multipurpose story flags (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-10))* → [brv_laundry_boss_4](#d-brv_laundry_boss_4)
    - “I am looking for my brother, Andor. He looks a bit like me.” → [brv_laundry_boss_0b](#d-brv_laundry_boss_0b)
    - “Have you ever seen a glove like this? [Shows Venanra the glove.]” *(if reached stage 170 of [A strange looking dagger](../quests/brv_dagger.md#stage-170); carry 1× [Suspect's glove](../items/ogea_glove.md))* → [brv_laundry_boss_10](#d-brv_laundry_boss_10)
    - “Did you order an 'Old, worn cape'?” *(if hand over 1× [Old, worn cape](../items/brv_wh_item_06.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 50 of [Delivery](../quests/brv_wh_delivery.md#stage-50))* → [brv_wh_delivery_venanra](#d-brv_wh_delivery_venanra)

    <span id="d-brv_laundry_boss_1"></span>**`brv_laundry_boss_1`** Venanra: “We are working on some nice green dresses. We can also repair and improve your clothes.” — **effects:** sets stage 10 of [Brimhaven multipurpose story flags (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-10), sets stage 15 of [Brimhaven multipurpose story flags (hidden flag)](../quests/brv_nondisplay_multipurpose.md#stage-15)

    - “I want to buy the dresses.” → *shop opens*
    - “What clothes can be improved and how much does it cost?” → [brv_laundry_boss_4](#d-brv_laundry_boss_4)

    <span id="d-brv_laundry_boss_4"></span>**`brv_laundry_boss_4`** Venanra: “Improving a fine green hat costs 1,397 gold, fine snakeskin gloves costs 640 gold, and improving superior leather boots costs 432 gold.”

    - “I don't have any of this equipment. Can you sell me something else?” *(if NOT carry 1× [Fine green hat](../items/hat2.md); NOT carry 1× [Fine snakeskin gloves](../items/gloves4.md); NOT carry 1× [Superior leather boots](../items/boots2.md))* → [brv_laundry_boss_1](#d-brv_laundry_boss_1)
    - “Please improve my fine green hat.” *(if carry 1× [Fine green hat](../items/hat2.md); NOT have 1,397 gold)* → [brv_laundry_boss_5b](#d-brv_laundry_boss_5b)
    - “Please improve my fine green hat.” *(if hand over 1× [Fine green hat](../items/hat2.md); pay 1,397 gold)* → [brv_laundry_boss_5](#d-brv_laundry_boss_5)
    - “Please improve my fine snakeskin gloves.” *(if carry 1× [Fine snakeskin gloves](../items/gloves4.md); NOT have 640 gold)* → [brv_laundry_boss_6b](#d-brv_laundry_boss_6b)
    - “Please improve my fine snakeskin gloves.” *(if hand over 1× [Fine snakeskin gloves](../items/gloves4.md); pay 640 gold)* → [brv_laundry_boss_6](#d-brv_laundry_boss_6)
    - “Please improve my superior leather boots.” *(if carry 1× [Superior leather boots](../items/boots2.md); NOT have 432 gold)* → [brv_laundry_boss_7b](#d-brv_laundry_boss_7b)
    - “Please improve my superior leather boots.” *(if hand over 1× [Superior leather boots](../items/boots2.md); pay 432 gold)* → [brv_laundry_boss_7](#d-brv_laundry_boss_7)
    - “Can you sell me something else?” → [brv_laundry_boss_1](#d-brv_laundry_boss_1)

    <span id="d-brv_laundry_boss_0b"></span>**`brv_laundry_boss_0b`** Venanra: “Sorry. I haven't seen anyone that looks like you.”

    - Next → [brv_laundry_boss_0](#d-brv_laundry_boss_0)

    <span id="d-brv_laundry_boss_10"></span>**`brv_laundry_boss_10`** Venanra: “Well, yes, I have. In fact, I made one exactly like it a couple of years ago for a customer. I remember because it is a very unique looking glove.”

    - “Can you remember who the customer was?” → [brv_laundry_boss_20](#d-brv_laundry_boss_20)

    <span id="d-brv_wh_delivery_venanra"></span>**`brv_wh_delivery_venanra`** Venanra: “Yes I did, kid. Incredibly, it has become the latest fashion to buy new capes with holes. Here's my delivery fee.” — **effects:** clears stage 50 of [Delivery](../quests/brv_wh_delivery.md#stage-50), sets stage 40 of [Brimhaven warehouse delivery (hidden flag)](../quests/brv_wh_delivery_nondisplay.md#stage-40), gives 10× [Gold coins](../items/gold.md)

    - “Thank you.” → *conversation ends*

    <span id="d-brv_laundry_boss_5b"></span>**`brv_laundry_boss_5b`** Venanra: “You don't have the required 1,397 gold to improve your fine green hat.”

    - Next → [brv_laundry_boss_2](#d-brv_laundry_boss_2)

    <span id="d-brv_laundry_boss_5"></span>**`brv_laundry_boss_5`** Venanra: “I will immediatelly give it to my worker. Please wait until he is finished. [You wait some time.] Here is your enhanced hat.” — **effects:** gives 1× [Enhanced green hat](../items/hat2enhanced.md)

    - Next → [brv_laundry_boss_2](#d-brv_laundry_boss_2)

    <span id="d-brv_laundry_boss_6b"></span>**`brv_laundry_boss_6b`** Venanra: “You don't have the required 640 gold to improve your fine snakeskin gloves.”

    - Next → [brv_laundry_boss_2](#d-brv_laundry_boss_2)

    <span id="d-brv_laundry_boss_6"></span>**`brv_laundry_boss_6`** Venanra: “I will immediatelly give it to my worker. Please wait until he is finished. [You wait some time.] Here are your enhanced gloves.” — **effects:** gives 1× [Enhanced snakeskin gloves](../items/gloves4enhanced.md)

    - Next → [brv_laundry_boss_2](#d-brv_laundry_boss_2)

    <span id="d-brv_laundry_boss_7b"></span>**`brv_laundry_boss_7b`** Venanra: “You don't have the required 432 gold to improve your superior leather boots.”

    - Next → [brv_laundry_boss_2](#d-brv_laundry_boss_2)

    <span id="d-brv_laundry_boss_7"></span>**`brv_laundry_boss_7`** Venanra: “I will immediatelly give it to my worker. Please wait until he is finished. [You wait some time.] Here are your enhanced boots.” — **effects:** gives 1× [Enhanced leather boots](../items/boots2enhanced.md)

    - Next → [brv_laundry_boss_2](#d-brv_laundry_boss_2)

    <span id="d-brv_laundry_boss_20"></span>**`brv_laundry_boss_20`** Venanra: “Um, let me think for a second...ah, yes, it was for Ogea.”

    - Next → [brv_laundry_boss_30](#d-brv_laundry_boss_30)

    <span id="d-brv_laundry_boss_2"></span>**`brv_laundry_boss_2`** Venanra: “What else can I do for you?”

    - “I want you to improve some of my clothes.” → [brv_laundry_boss_4](#d-brv_laundry_boss_4)
    - “Can you sell something to me?” → [brv_laundry_boss_1](#d-brv_laundry_boss_1)

    <span id="d-brv_laundry_boss_30"></span>**`brv_laundry_boss_30`** Venanra: “He came to me with a story that he lost his glove while hunting one night and how he wanted me to make him a replacement as he could not afford to purchase a new pair.”

    - “Are you sure?” → [brv_laundry_boss_40](#d-brv_laundry_boss_40)

    <span id="d-brv_laundry_boss_40"></span>**`brv_laundry_boss_40`** Venanra: “Oh, absolutely. I'm sure.” — **effects:** sets stage 180 of [A strange looking dagger](../quests/brv_dagger.md#stage-180)




## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 11 lines added |
| [v0.7.12](../versions/0.7.12.md) | Renamed “Laundry owner” → “Venanra”<br>Dialogue: 4 lines added, 2 lines changed |
| [v0.7.17](../versions/0.7.17.md) | Dialogue: 1 line added, 1 line changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 2 lines changed<br>· text: “You don't have the required 1,397 gold to improve your fine green hat.” → “You don't have the required {1397} gold to improve your fine green ha…”<br>· text: “Improving a fine green hat costs 1,397 gold, fine snakeskin gloves co…” → “Improving a fine green hat costs {1397} gold, fine snakeskin gloves c…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brv_laundry_boss` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_laundry_boss` |
    | Loot table | `brv_laundry` |
    | Conversation | `brv_laundry_boss_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:187` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_laundry_boss",
     "name": "Venanra",
     "iconID": "monsters_ld1:187",
     "phraseID": "brv_laundry_boss_0",
     "droplistID": "brv_laundry"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_laundry_boss.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_laundry_boss.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_laundry_boss.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_laundry_boss.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
