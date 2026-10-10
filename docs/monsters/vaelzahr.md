---
description: "Vaelzahr is a non-player character (NPC) in Andor's Trail, found in Undertell 7 00. Starts The fifth master."
---

# ![](../assets/icons/monsters/monsters_liches_2.png){ .sprite } Vaelzahr

**Where to find Vaelzahr:** [Undertell 7 00](../maps/undertell_7_00.md#pin-npc-vaelzahr)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_liches_2.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Starts [The fifth master](../quests/fifth_master.md) |
| **Found in** | Undertell 7 00 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Quests

- [The fifth master](../quests/fifth_master.md): stages 10, 20, 78
- [Undertell story flags (hidden flag)](../quests/undertell_hidden.md): stages 5, 7, 89

## Dialogue simulator

Talk to Vaelzahr as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/vaelzahr_initial_selector.json" data-npc="Vaelzahr" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (23 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-vaelzahr_initial_selector"></span>**`vaelzahr_initial_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 5 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-5))* → [kazaul_masters_not_met_10](#d-kazaul_masters_not_met_10)
    - branch 2 *(if reached stage 5 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-5); NOT reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10))* → [kazaul_masters_met_but_no_quest_started_10](#d-kazaul_masters_met_but_no_quest_started_10)
    - branch 3 *(if reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10); NOT reached stage 20 of [The fifth master](../quests/fifth_master.md#stage-20))* → [the_fifth_master_10](#d-the_fifth_master_10)
    - branch 4 *(if carry 1× [The Ritual of Five Aspects](../items/ancient_kazaul_ritual.md))* → [masters_send_to_thalen_10](#d-masters_send_to_thalen_10)
    - branch 5 *(if reached stage 90 of [The fifth master](../quests/fifth_master.md#stage-90))* → [vaelzahr_after_fifth_master_narrator](#d-vaelzahr_after_fifth_master_narrator)
    - branch 6 → [vaelzahr_intro_10_narrator](#d-vaelzahr_intro_10_narrator)

    <span id="d-kazaul_masters_not_met_10"></span>**`kazaul_masters_not_met_10`** Vaelzahr: “[While pointing its finger in your direction.] You! How did you get past our army?”

    - “"Our"? There's more of you bosses?” → [kazaul_masters_not_met_20](#d-kazaul_masters_not_met_20)

    <span id="d-kazaul_masters_met_but_no_quest_started_10"></span>**`kazaul_masters_met_but_no_quest_started_10`** Vaelzahr: “If you ever leave while I am talking to you again, I will end your life. Understood?”

    - “[Terrified] Yes.” → [kazaul_masters_not_met_30](#d-kazaul_masters_not_met_30)

    <span id="d-the_fifth_master_10"></span>**`the_fifth_master_10`** Vaelzahr: “[The air grows heavy as the master studies you.] You are bold to walk here. Perhaps bold enough to be of use. One of our own is missing. The fifth master, Anavrin, lies silent. The Ritual of Five Aspects was taken from us long ago.…” — **effects:** sets stage 10 of [The fifth master](../quests/fifth_master.md#stage-10)

    - “You want me to find this ritual?” → [the_fifth_master_20](#d-the_fifth_master_20)

    <span id="d-masters_send_to_thalen_10"></span>**`masters_send_to_thalen_10`** Vaelzahr: “[The Master's hollow eyes flare briefly with dim blue fire.] You hold the Ritual of Five Aspects, mortal. But its meaning lies beyond your grasp. Only Thalen, our brother of Knowledge, can speak the words. Seek him where the thoughts of…”

    - “Thalen? What will he do with it?” → [masters_send_to_thalen_20](#d-masters_send_to_thalen_20)

    <span id="d-vaelzahr_after_fifth_master_narrator"></span>**`vaelzahr_after_fifth_master_narrator`** [Dummy NPC](../monsters/none.md): “Vaelzahr's voice is a rasping whisper.”

    - Next → [vaelzahr_after_fifth_master](#d-vaelzahr_after_fifth_master)

    <span id="d-vaelzahr_intro_10_narrator"></span>**`vaelzahr_intro_10_narrator`** [Dummy NPC](../monsters/none.md): “The walls pulse faintly, as if the stone itself had veins. A deep, rasping voice speaks within your chest.”

    - Next → [vaelzahr_oegyth_selector](#d-vaelzahr_oegyth_selector)

    <span id="d-kazaul_masters_not_met_20"></span>**`kazaul_masters_not_met_20`** Vaelzahr: “We are "masters", not "bosses". And yes, there are five of us.” — **effects:** sets stage 5 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-5)

    - Next → [kazaul_masters_not_met_30](#d-kazaul_masters_not_met_30)

    <span id="d-kazaul_masters_not_met_30"></span>**`kazaul_masters_not_met_30`** Vaelzahr: “Well, currently there are only four of us masters. We are not complete.”

    - “"Complete"? What is that supposed to mean?” → [the_fifth_master_10](#d-the_fifth_master_10)

    <span id="d-the_fifth_master_20"></span>**`the_fifth_master_20`** Vaelzahr: “Yes. The Ritual of Five Aspects lies lost among your kind. Long ago, a mortal scribe named Varnel served the Kazaul, writing our words into form. But when fear took him, he fled with the ritual and hid among your people. Bring it back to…” — **effects:** sets stage 20 of [The fifth master](../quests/fifth_master.md#stage-20)

    - “Then I will find it.” → [the_fifth_master_accept](#d-the_fifth_master_accept)
    - “I do not trust you, but I will look.” → [the_fifth_master_accept](#d-the_fifth_master_accept)

    <span id="d-masters_send_to_thalen_20"></span>**`masters_send_to_thalen_20`** Vaelzahr: “He will guide your unlearned hands. He alone can draw the pattern that binds the Five. Without him, the ritual is only ink on lost parchment.” — **effects:** sets stage 78 of [The fifth master](../quests/fifth_master.md#stage-78), sets stage 7 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-7)

    - “I will find him.” → *conversation ends*

    <span id="d-vaelzahr_after_fifth_master"></span>**`vaelzahr_after_fifth_master`** [Vaelzahr](../monsters/vaelzahr.md): “I felt the pulse the moment it stirred. Death is restless again. I welcome the silence no more.”

    - “[Leave.]” → *conversation ends*

    <span id="d-vaelzahr_oegyth_selector"></span>**`vaelzahr_oegyth_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if carry 1× [oegyth_crystal](../items/oegyth_crystal.md))* → [vaelzahr_oegyth_10](#d-vaelzahr_oegyth_10)
    - branch 2 → [vaelzahr_intro_10](#d-vaelzahr_intro_10)

    <span id="d-the_fifth_master_accept"></span>**`the_fifth_master_accept`** Vaelzahr: “[The master's eyes flare with dim light.] Then go, mortal. Seek the lost ritual. In the ruins of your kind lies our key to completion. Return only when it is found.”

    - “I understand.” → *conversation ends*

    <span id="d-vaelzahr_oegyth_10"></span>**`vaelzahr_oegyth_10`** [Vaelzahr](../monsters/vaelzahr.md): “You arrive carrying an echo that is not yours.”

    - “What are you talking about” → [vaelzahr_oegyth_20](#d-vaelzahr_oegyth_20)

    <span id="d-vaelzahr_intro_10"></span>**`vaelzahr_intro_10`** [Vaelzahr](../monsters/vaelzahr.md): “Mortality remembers pain. Even now, your blood knows me.”

    - “You sound crazy.” → *conversation ends*

    <span id="d-vaelzahr_oegyth_20"></span>**`vaelzahr_oegyth_20`** Vaelzahr: “Your kind drags history behind it, even when it thinks it walks alone.”

    - “You are being vague on purpose” → [vaelzahr_oegyth_30](#d-vaelzahr_oegyth_30)

    <span id="d-vaelzahr_oegyth_30"></span>**`vaelzahr_oegyth_30`** Vaelzahr: “You carry what your kind calls an Oegyth crystal.”

    - “So you know what it is?” → [master_oegyth_20](#d-master_oegyth_20)

    <span id="d-master_oegyth_20"></span>**`master_oegyth_20`** Vaelzahr: “Names are comforts. They make old things feel small.”

    - “Where did it come from?” → [master_oegyth_30](#d-master_oegyth_30)

    <span id="d-master_oegyth_30"></span>**`master_oegyth_30`** Vaelzahr: “It was placed where power would grow teeth and learn to walk.”

    - “Placed by who?” → [master_oegyth_40](#d-master_oegyth_40)

    <span id="d-master_oegyth_40"></span>**`master_oegyth_40`** Vaelzahr: “Some tools were made for rule. Others were made to be watched.”

    - “So this crystal is a tool?” → [master_oegyth_50](#d-master_oegyth_50)

    <span id="d-master_oegyth_50"></span>**`master_oegyth_50`** Vaelzahr: “We no longer shape the world so openly. But what was shaped does not forget the hand that shaped it.” — **effects:** sets stage 89 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-89)

    - “Then what should I do with it?” → [master_oegyth_60](#d-master_oegyth_60)

    <span id="d-master_oegyth_60"></span>**`master_oegyth_60`** Vaelzahr: “Keep it close. Power that is not understood still teaches obedience.”




## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 23 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `vaelzahr` |
    | Type (wiki) | NPC |
    | Spawn group | `vaelzahr` |
    | Loot table | – |
    | Conversation | `vaelzahr_initial_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_liches:2` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "vaelzahr",
     "name": "Vaelzahr",
     "iconID": "monsters_liches:2",
     "unique": 1,
     "monsterClass": "undead",
     "phraseID": "vaelzahr_initial_selector"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vaelzahr.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vaelzahr.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vaelzahr.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vaelzahr.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
