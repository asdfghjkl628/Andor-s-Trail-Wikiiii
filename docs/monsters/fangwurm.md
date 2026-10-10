---
description: "Fangwurm is a non-player character (NPC) in Andor's Trail, found in Brimhaven."
---

# ![](../assets/icons/monsters/monsters_ld1_2.png){ .sprite } Fangwurm

**Where to find Fangwurm:** Brimhaven: [Brimhaven church](../maps/brimhaven_church.md#pin-npc-fangwurm)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld1_2.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Brimhaven |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Quests

- [A quick glance](../quests/quick_glance.md): stages 77, 78
- [Quick glance: statue found (hidden flag)](../quests/quick_glance_hidden_found_statue.md): stages 50, 60

## Dialogue simulator

Talk to Fangwurm as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/fangwurm_start.json" data-npc="Fangwurm" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (11 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-fangwurm_start"></span>**`fangwurm_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 85 of [A quick glance](../quests/quick_glance.md#stage-85))* → [fangwurm_thank_rescuing_sister](#d-fangwurm_thank_rescuing_sister)
    - branch 2 *(if reached stage 30 of [Quick glance: statue found (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-30); reached stage 90 of [A quick glance](../quests/quick_glance.md#stage-90))* → [fangwurm_angry_2](#d-fangwurm_angry_2)
    - branch 3 *(if reached stage 50 of [Quick glance: statue found (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-50))* → [fangwurm_angry](#d-fangwurm_angry)
    - branch 4 *(if reached stage 60 of [Quick glance: statue found (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-60))* → [fangwurm_thank_killing_basilisk](#d-fangwurm_thank_killing_basilisk)
    - branch 5 *(if reached stage 90 of [A quick glance](../quests/quick_glance.md#stage-90))* → [fangwurm_thank_killing_basilisk_2](#d-fangwurm_thank_killing_basilisk_2)
    - branch 6 → [fangwurm_talking](#d-fangwurm_talking)

    <span id="d-fangwurm_thank_rescuing_sister"></span>**`fangwurm_thank_rescuing_sister`** Fangwurm: “Juttarka told me that you saved her life. Thank you. May the Shadow always be with you.”


    <span id="d-fangwurm_angry_2"></span>**`fangwurm_angry_2`** Fangwurm: “Anakis told me that you took the blood for yourself instead of trying to help his sister. Please leave now.”


    <span id="d-fangwurm_angry"></span>**`fangwurm_angry`** Fangwurm: “I am sad that you took the blood for yourself instead of trying to help Anakis' sister. Please leave now.” — **effects:** sets stage 50 of [Quick glance: statue found (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-50)


    <span id="d-fangwurm_thank_killing_basilisk"></span>**`fangwurm_thank_killing_basilisk`** Fangwurm: “Thank you for killing the Basilisk, but it would be better if you had talked to me before killing it, because its magical blood is now dried up and wasted. May the Shadow always be with you.” — **effects:** sets stage 60 of [Quick glance: statue found (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-60)


    <span id="d-fangwurm_thank_killing_basilisk_2"></span>**`fangwurm_thank_killing_basilisk_2`** Fangwurm: “Anakis told me that you killed the Basilisk. Thank you, but it would be better if you had talked to me before killing it, because its magical blood is now dried up and wasted. May the Shadow always be with you.”


    <span id="d-fangwurm_talking"></span>**`fangwurm_talking`** Fangwurm: “May the Shadow be with you.”

    - “I killed the Basilisk and took the blood for myself.” *(if reached stage 30 of [Quick glance: statue found (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-30); NOT reached stage 85 of [A quick glance](../quests/quick_glance.md#stage-85))* → [fangwurm_angry](#d-fangwurm_angry)
    - “I killed the Basilisk in the cave.” *(if NOT reached stage 30 of [Quick glance: statue found (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-30); killed 1× [Ancient basilisk](../monsters/old_basilisk.md); reached stage 20 of [A quick glance](../quests/quick_glance.md#stage-20))* → [fangwurm_thank_killing_basilisk](#d-fangwurm_thank_killing_basilisk)
    - “Can you please tell me again, what you know about the Basilisk's blood?” *(if reached stage 77 of [A quick glance](../quests/quick_glance.md#stage-77))* → [fangwurm_info_about_blood](#d-fangwurm_info_about_blood)
    - “I believe that Anakis' sister was turned to stone by the Basilisk in the cave. Do you have any idea if I could help her?” *(if NOT reached stage 77 of [A quick glance](../quests/quick_glance.md#stage-77); reached stage 50 of [A quick glance](../quests/quick_glance.md#stage-50))* → [fangwurm_info_about_blood](#d-fangwurm_info_about_blood)
    - “Anakis' sister is missing. Can you tell me more about the Basilisk in the cave?” *(if reached stage 20 of [A quick glance](../quests/quick_glance.md#stage-20); NOT reached stage 50 of [A quick glance](../quests/quick_glance.md#stage-50))* → [fangwurm_info_basilisk](#d-fangwurm_info_basilisk)
    - “I am looking for my brother, Andor. He looks a bit like me.” → [fangwurm_talking_1a](#d-fangwurm_talking_1a)

    <span id="d-fangwurm_info_about_blood"></span>**`fangwurm_info_about_blood`** Fangwurm: “The Basilisk's blood has special properties. It can protect against damage if applied to the skin. Fresh, warm, Basilisks blood might even heal a person that has been turned to stone. But how can you kill a Basilisk if you can't even look…” — **effects:** sets stage 77 of [A quick glance](../quests/quick_glance.md#stage-77)

    - “I already killed the Basilisk.” *(if killed 1× [Ancient basilisk](../monsters/old_basilisk.md))* → [fangwurm_thank_killing_basilisk](#d-fangwurm_thank_killing_basilisk)
    - “You are right, it will not be possible to kill the Basilisk.” → *conversation ends*
    - “I will find a way to kill the Basilisk.” → [fangwurm_info_vial](#d-fangwurm_info_vial)

    <span id="d-fangwurm_info_basilisk"></span>**`fangwurm_info_basilisk`** Fangwurm: “The Basilisk will turn you to stone when you go near him and your eyes meet its eyes. You should not look at it. Come back to me if you know what happened to Anakis' sister.”


    <span id="d-fangwurm_talking_1a"></span>**`fangwurm_talking_1a`** Fangwurm: “Yes, I know someone who looks almost like you, but he and his parents are from this town.”

    - Next → [fangwurm_talking](#d-fangwurm_talking)

    <span id="d-fangwurm_info_vial"></span>**`fangwurm_info_vial`** Fangwurm: “You would need a special crystal vial that is resistant to the Basilisk's blood to handle it. The potion maker in Fallhaven might sell them. May the Shadow be with you.” — **effects:** sets stage 78 of [A quick glance](../quests/quick_glance.md#stage-78)




## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 11 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `fangwurm` |
    | Type (wiki) | NPC |
    | Spawn group | `fangwurm` |
    | Loot table | – |
    | Conversation | `fangwurm_start` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:2` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "fangwurm",
     "name": "Fangwurm",
     "iconID": "monsters_ld1:2",
     "unique": 1,
     "phraseID": "fangwurm_start"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fangwurm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fangwurm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fangwurm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fangwurm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
