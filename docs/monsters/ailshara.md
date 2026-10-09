---
description: "Ailshara is a non-player character (NPC) in Andor's Trail, found in Crossroads Guardhouse. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_men_8.png){ .sprite } Ailshara

**Where to find Ailshara:** Crossroads Guardhouse: [Houseatcrossroads 0](../maps/houseatcrossroads0.md#pin-npc-ailshara)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_8.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Shopkeeper |
| **Found in** | Crossroads Guardhouse |
| **Entry ID** | `ailshara` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Sharp steel dagger](../items/dagger_sharp_steel.md) | 100% | 1 |
| [Superior iron dagger](../items/dagger2.md) | 100% | 1 |
| [Quickstrike dagger](../items/quickdagger1.md) | 100% | 1 |
| [Hard leather armor](../items/armor3.md) | 100% | 1 |
| [Leather shirt of misfortune](../items/armour_misfortune.md) | 100% | 1 |
| [Villain's leather armor](../items/armour_leather_villain.md) | 100% | 1 |
| [Fine leather gloves](../items/gloves2.md) | 100% | 1 |
| [Troublemaker's gloves](../items/gloves_troublemaker.md) | 100% | 1 |
| [Leather gloves of attack](../items/gloves_leather_attack.md) | 100% | 1 |
| [Polished ring of backstabbing](../items/ring_polished_backstab.md) | 100% | 1 |

## Quests

- [Feygard errands](../quests/feygard_shipment.md): stages 30, 35, 82

## Dialogue simulator

Set your quest stages and items, then talk to Ailshara. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/ailshara.json" data-npc="Ailshara" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (21 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-ailshara"></span>**`ailshara`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 82 of [Feygard errands](../quests/feygard_shipment.md#stage-82))* → [ailshara_completed_y_1](#d-ailshara_completed_y_1)
    - branch 2 *(if reached stage 80 of [Feygard errands](../quests/feygard_shipment.md#stage-80))* → [ailshara_completed_n_1](#d-ailshara_completed_n_1)
    - branch 3 *(if reached stage 35 of [Feygard errands](../quests/feygard_shipment.md#stage-35))* → [ailshara_deliver_1](#d-ailshara_deliver_1)
    - branch 4 *(if reached stage 25 of [Feygard errands](../quests/feygard_shipment.md#stage-25))* → [ailshara_interested_1](#d-ailshara_interested_1)
    - branch 5 → [ailshara_1](#d-ailshara_1)

    <span id="d-ailshara_completed_y_1"></span>**`ailshara_completed_y_1`** Ailshara: “Hello again my Shadow friend. How may I help you?”

    - “Let me see what you have to trade.” → *shop opens*

    <span id="d-ailshara_completed_n_1"></span>**`ailshara_completed_n_1`** Ailshara: “Sigh, it's you. What do you want?”

    - “Let me see what you have to trade.” → *shop opens*

    <span id="d-ailshara_deliver_1"></span>**`ailshara_deliver_1`** Ailshara: “Hello again. Did you deliver those items to the smith in Vilegard?”

    - “Yes, it is done.” *(if reached stage 55 of [Feygard errands](../quests/feygard_shipment.md#stage-55))* → [ailshara_deliver_2_s](#d-ailshara_deliver_2_s)
    - “Never mind that, let me see what you have to trade.” → *shop opens*
    - “No. I will help Feygard instead.” → [ailshara_fg_1](#d-ailshara_fg_1)
    - “Can you tell me again what I was supposed to do?” → [ailshara_interested_4](#d-ailshara_interested_4)
    - “Not yet.” → [ailshara_interested_9](#d-ailshara_interested_9)

    <span id="d-ailshara_interested_1"></span>**`ailshara_interested_1`** Ailshara: “Psst, hey you! I saw you talking to Gandoren over there, and I happened to notice that you exchanged some items. Anything interesting?”

    - “Never mind that, let me see what you have to trade.” → *shop opens*
    - “I better not talk about it.” → [ailshara_interested_2](#d-ailshara_interested_2)
    - “Gandoren specifically asked me not to talk to you about it.” → [ailshara_interested_2](#d-ailshara_interested_2)
    - “Yes, Gandoren wants me to deliver some equipment for Feygard. Do you want a part of the deal?” → [ailshara_interested_4](#d-ailshara_interested_4)

    <span id="d-ailshara_1"></span>**`ailshara_1`** Ailshara: “Psst, hey. Interested in doing some trading? I am always looking for acquiring ... well, items of others...”

    - “Sure, let me see what you have.” → *shop opens*
    - “Items of others?” → [ailshara_2](#d-ailshara_2)

    <span id="d-ailshara_deliver_2_s"></span>**`ailshara_deliver_2_s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 81 of [Feygard errands](../quests/feygard_shipment.md#stage-81))* → [ailshara_deliver_3](#d-ailshara_deliver_3)
    - branch 2 → [ailshara_deliver_2](#d-ailshara_deliver_2)

    <span id="d-ailshara_fg_1"></span>**`ailshara_fg_1`** Ailshara: “By the Shadow, you sound like one of those deceptive snobs from Feygard.”

    - Next → [ailshara_fg_2](#d-ailshara_fg_2)

    <span id="d-ailshara_interested_4"></span>**`ailshara_interested_4`** Ailshara: “Let me tell you my plan. As you might know, everyone believes there will be some coming conflict between the deceptive snobs of Feygard and the glorious people of Nor City.”

    - Next → [ailshara_interested_5](#d-ailshara_interested_5)

    <span id="d-ailshara_interested_9"></span>**`ailshara_interested_9`** Ailshara: “Shadow be with you. May the Shadow guide you on the clouded paths that you walk.”


    <span id="d-ailshara_interested_2"></span>**`ailshara_interested_2`** Ailshara: “Hah, of course. Gandoren would not like it if I were to get a glimpse into his business. I assume you are helping him deliver those items somewhere. Tell me this, what did he promise you in return? Gold? Honor? No?”

    - “Now that you mention it, he didn't actually say there would be a reward.” → [ailshara_interested_3](#d-ailshara_interested_3)
    - “I am doing this for the glory of Feygard.” → [ailshara_fg_1](#d-ailshara_fg_1)
    - “Helping Feygard seems like the right thing to do.” → [ailshara_fg_1](#d-ailshara_fg_1)
    - “What would you propose instead?” → [ailshara_interested_4](#d-ailshara_interested_4)

    <span id="d-ailshara_2"></span>**`ailshara_2`** Ailshara: “Oh yes. You see, these Feygard patrol guards carry some really interesting things. They don't seem to care much if some of their shipments ... well, disappear.”

    - “OK, let me see what you have.” → *shop opens*
    - “I should really not get involved in this. Goodbye.” → *conversation ends*

    <span id="d-ailshara_deliver_3"></span>**`ailshara_deliver_3`** Ailshara: “Excellent! You do indeed walk with the Shadow my friend. I am glad to hear that there are at least a few decent folk still around.” — **effects:** sets stage 82 of [Feygard errands](../quests/feygard_shipment.md#stage-82)

    - Next → [ailshara_delivered_1](#d-ailshara_delivered_1)

    <span id="d-ailshara_deliver_2"></span>**`ailshara_deliver_2`** Ailshara: “Good. You should also try to convince Gandoren into thinking that you helped him.”


    <span id="d-ailshara_fg_2"></span>**`ailshara_fg_2`** Ailshara: “Shadow help you, child. You should question yourself whether you really are making the right choice here.”


    <span id="d-ailshara_interested_5"></span>**`ailshara_interested_5`** Ailshara: “Any help we can bring to Nor City in this matter is welcome. These items that Gandoren gave you would be useful to our people in the southern lands.” — **effects:** sets stage 30 of [Feygard errands](../quests/feygard_shipment.md#stage-30)

    - Next → [ailshara_interested_6](#d-ailshara_interested_6)

    <span id="d-ailshara_interested_3"></span>**`ailshara_interested_3`** Ailshara: “As usual, Feygard keeps all its riches to itself. What if I were to tell you there was a way for you to gain from all this as well?”

    - “Sounds interesting, please go on.” → [ailshara_interested_4](#d-ailshara_interested_4)
    - “I have no problem helping Feygard without any personal gain.” → [ailshara_fg_1](#d-ailshara_fg_1)
    - “I better not get involved in this, goodbye.” → *conversation ends*

    <span id="d-ailshara_delivered_1"></span>**`ailshara_delivered_1`** Ailshara: “Your help will be most appreciated by the people of Nor City, and you will be welcome among us.”


    <span id="d-ailshara_interested_6"></span>**`ailshara_interested_6`** Ailshara: “These items, if you were to deliver them to our allies down in Vilegard, then the Shadow would look favorably upon you.”

    - Next → [ailshara_interested_7](#d-ailshara_interested_7)

    <span id="d-ailshara_interested_7"></span>**`ailshara_interested_7`** Ailshara: “This way, the people could get back some piece of the riches that Feygard has stolen from all of us.”

    - Next → [ailshara_interested_8](#d-ailshara_interested_8)

    <span id="d-ailshara_interested_8"></span>**`ailshara_interested_8`** Ailshara: “If you indeed are walking in the Shadow, then deliver these items to the smith in Vilegard. He will be able to make good use of them. He might also have some other task for you.” — **effects:** sets stage 35 of [Feygard errands](../quests/feygard_shipment.md#stage-35)

    - “I will see what I can do.” → [ailshara_interested_9](#d-ailshara_interested_9)
    - “No. I will help Feygard instead.” → [ailshara_fg_1](#d-ailshara_fg_1)
    - “Whatever, I choose my own path.” → [ailshara_interested_9](#d-ailshara_interested_9)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 5 lines changed<br>· text: “Psst, hey. Interested in doing some trading? I am always looking for …” → “Psst, hey. Interested in doing some trading? I am always looking for …”<br>· text: “Oh yes. You see, these Feygard patrol guards carry some really intere…” → “Oh yes. You see, these Feygard patrol guards carry some really intere…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `ailshara` |
    | Spawn group | `ailshara` |
    | Loot table | `shop_ailshara` |
    | Conversation | `ailshara` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:8` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "ailshara",
     "name": "Ailshara",
     "iconID": "monsters_men:8",
     "monsterClass": "humanoid",
     "spawnGroup": "ailshara",
     "phraseID": "ailshara",
     "droplistID": "shop_ailshara"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ailshara.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ailshara.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ailshara.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ailshara.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
