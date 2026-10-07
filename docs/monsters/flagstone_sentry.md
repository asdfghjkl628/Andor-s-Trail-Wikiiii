---
description: "Flagstone sentry is a non-player character (NPC) in Andor's Trail, found in Flagstone Prison."
---

# ![](../assets/icons/monsters/monsters_men_3.png){ .sprite } Flagstone sentry

**Where to find Flagstone sentry:** Flagstone Prison: [flagstone0](../maps/flagstone0.md#pin-npc-flagstone_sentry)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_3.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Flagstone Prison |
| **Entry ID** | `flagstone_sentry` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [Ancient secrets](../quests/flagstone.md): stages 10, 30, 40, 70

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Flagstone sentry. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/flagstone_sentry.json" data-npc="Flagstone sentry" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (23 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-flagstone_sentry"></span>**`flagstone_sentry`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 60 of [Ancient secrets](../quests/flagstone.md#stage-60))* → [flagstone_sentry_return4](#d-flagstone_sentry_return4)
    - branch 2 *(if reached stage 40 of [Ancient secrets](../quests/flagstone.md#stage-40))* → [flagstone_sentry_return3](#d-flagstone_sentry_return3)
    - branch 3 → [flagstone_sentry_select0](#d-flagstone_sentry_select0)

    <span id="d-flagstone_sentry_return4"></span>**`flagstone_sentry_return4`** Flagstone sentry: “Hello again. It seems something happened inside Flagstone that made the undead weaker. I'm sure we have you to thank for it.”

    - “In the depths of Flagstone, I had to fight a winged demon and found a prisoner called Narael. He told me that he has…” → [flagstone_sentry_45](#d-flagstone_sentry_45)

    <span id="d-flagstone_sentry_return3"></span>**`flagstone_sentry_return3`** Flagstone sentry: “Hello again. How is the investigation of the undead in Flagstone going?”

    - “No progress yet.” → [flagstone_sentry_43](#d-flagstone_sentry_43)

    <span id="d-flagstone_sentry_select0"></span>**`flagstone_sentry_select0`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [Ancient secrets](../quests/flagstone.md#stage-30))* → [flagstone_sentry_return2](#d-flagstone_sentry_return2)
    - branch 2 *(if reached stage 10 of [Ancient secrets](../quests/flagstone.md#stage-10))* → [flagstone_sentry_return1](#d-flagstone_sentry_return1)
    - branch 3 → [flagstone_sentry_1](#d-flagstone_sentry_1)

    <span id="d-flagstone_sentry_45"></span>**`flagstone_sentry_45`** Flagstone sentry: “This is both good and bad news. I am truly grateful that you rid us of the warden and his thralls. Talk to Yolgen for a reward. We will make sure that we recover this prisoner.” — **effects:** removes monsters from flagstone4, sets stage 70 of [Ancient secrets](../quests/flagstone.md#stage-70)

    - “Thank you.” → *conversation ends*
    - “Thank you. Shadow be with you.” → *conversation ends*

    <span id="d-flagstone_sentry_43"></span>**`flagstone_sentry_43`** Flagstone sentry: “Well, keep looking. Return to me if you need my advice.”


    <span id="d-flagstone_sentry_return2"></span>**`flagstone_sentry_return2`** Flagstone sentry: “Hello again. Have you found the former warden in Flagstone yet?”

    - “I slew the former warden and found a peculiar necklace among his remains.” *(if hand over 1× [Flagstone Warden's necklace](../items/necklace_flagstone.md))* → [flagstone_sentry_23](#d-flagstone_sentry_23)
    - “Can you tell me the story again?” → [flagstone_sentry_3](#d-flagstone_sentry_3)
    - “Not yet. I have to keep looking.” → *conversation ends*

    <span id="d-flagstone_sentry_return1"></span>**`flagstone_sentry_return1`** Flagstone sentry: “Hello again. Did you enter Flagstone? I am surprised you actually returned.”

    - “Can you tell me the story again?” → [flagstone_sentry_4](#d-flagstone_sentry_4)
    - “There is a guardian in the lower levels of Flagstone that cannot be approached and the former prisoners are undead now.” *(if reached stage 20 of [Ancient secrets](../quests/flagstone.md#stage-20))* → [flagstone_sentry_20](#d-flagstone_sentry_20)

    <span id="d-flagstone_sentry_1"></span>**`flagstone_sentry_1`** Flagstone sentry: “Halt! Who's there? No one is allowed to approach Flagstone.”

    - Next → [flagstone_sentry_2](#d-flagstone_sentry_2)

    <span id="d-flagstone_sentry_23"></span>**`flagstone_sentry_23`** Flagstone sentry: “Oh this looks most interesting. Let's take a look. Hmm. It has got some weird inscriptions on it that say 'Daylight Shadow'. Maybe you could try these words on the demon? So perhaps the warden did have something to do with the demon after…” — **effects:** sets stage 40 of [Ancient secrets](../quests/flagstone.md#stage-40)

    - “That might work. Thank you.” → *conversation ends*

    <span id="d-flagstone_sentry_3"></span>**`flagstone_sentry_3`** Flagstone sentry: “Flagstone has been overrun by undead, and we are standing guard here to make sure no undead escape.”

    - “Can you tell me the story about Flagstone?” → [flagstone_sentry_4](#d-flagstone_sentry_4)

    <span id="d-flagstone_sentry_4"></span>**`flagstone_sentry_4`** Flagstone sentry: “Flagstone Prison was built a few hundred years ago by house Gorland of Stoutford and used until the Noble Wars, when the house was vanquished. This dreadful place has been abandoned ever since.”

    - Next → [flagstone_sentry_8](#d-flagstone_sentry_8)

    <span id="d-flagstone_sentry_20"></span>**`flagstone_sentry_20`** Flagstone sentry: “A guardian and undead prisoners you say? This is troubling news, since it means there is some larger force behind all this.”

    - Next → [flagstone_sentry_21](#d-flagstone_sentry_21)

    <span id="d-flagstone_sentry_2"></span>**`flagstone_sentry_2`** Flagstone sentry: “You should turn back while you still can.”

    - Next → [flagstone_sentry_3](#d-flagstone_sentry_3)

    <span id="d-flagstone_sentry_8"></span>**`flagstone_sentry_8`** Flagstone sentry: “For years, no one took notice of Flagstone, although there were occasional reports from travelers of terrible screams coming from the camp.”

    - Next → [flagstone_sentry_9](#d-flagstone_sentry_9)

    <span id="d-flagstone_sentry_21"></span>**`flagstone_sentry_21`** Flagstone sentry: “You should look for the former warden. Maybe he has something to do with all of this. If you find him you should return here with any important news.” — **effects:** sets stage 30 of [Ancient secrets](../quests/flagstone.md#stage-30)

    - “OK, I will go and look for the former warden.” → *conversation ends*

    <span id="d-flagstone_sentry_9"></span>**`flagstone_sentry_9`** Flagstone sentry: “But recently, undead started pouring out of Flagstone and started to threaten Stoutford and the trade routes nearby.”

    - Next → [flagstone_sentry_10](#d-flagstone_sentry_10)

    <span id="d-flagstone_sentry_10"></span>**`flagstone_sentry_10`** Flagstone sentry: “So, here we are. I have to guard the road from undead, so that they do not spread farther than Flagstone.”

    - Next → [flagstone_sentry_11](#d-flagstone_sentry_11)

    <span id="d-flagstone_sentry_11"></span>**`flagstone_sentry_11`** Flagstone sentry: “So, I would advise you to leave unless you want to be overrun by undead.”

    - “Can I investigate the Flagstone ruins?” → [flagstone_sentry_12](#d-flagstone_sentry_12)
    - “Yes, I should leave.” → *conversation ends*

    <span id="d-flagstone_sentry_12"></span>**`flagstone_sentry_12`** Flagstone sentry: “Are you really sure you want to head in there? Well, OK, fine by me.”

    - Next → [flagstone_sentry_13](#d-flagstone_sentry_13)

    <span id="d-flagstone_sentry_13"></span>**`flagstone_sentry_13`** Flagstone sentry: “I won't stop you, and I won't mourn you if you never return.”

    - Next → [flagstone_sentry_14](#d-flagstone_sentry_14)

    <span id="d-flagstone_sentry_14"></span>**`flagstone_sentry_14`** Flagstone sentry: “Go ahead. Let me know if there's anything I can tell you that would help.”

    - Next → [flagstone_sentry_15](#d-flagstone_sentry_15)

    <span id="d-flagstone_sentry_15"></span>**`flagstone_sentry_15`** Flagstone sentry: “Return here if you need my advice.” — **effects:** sets stage 10 of [Ancient secrets](../quests/flagstone.md#stage-10)

    - “OK. I will return to you if there is anything I need help with.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Renamed “Flagstone Sentry” → “Flagstone sentry”<br>Dialogue: 1 line added, 14 lines changed<br>· text: “For years, no one took notice of Flagstone. Except for the occasional…” → “For years, no one took notice of Flagstone, although there were occas…”<br>· text: “A guardian you say? This is troubling news, since it means there is s…” → “A guardian and undead prisoners you say? This is troubling news, sinc…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `flagstone_sentry` |
    | Spawn group | `flagstone_sentry` |
    | Loot table | – |
    | Conversation | `flagstone_sentry` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:3` |
    | Defined in | `res/raw/monsterlist_wilderness.json` |

    Raw data:

    ```json
    {
     "id": "flagstone_sentry",
     "name": "Flagstone sentry",
     "iconID": "monsters_men:3",
     "monsterClass": "humanoid",
     "spawnGroup": "flagstone_sentry",
     "phraseID": "flagstone_sentry"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=flagstone_sentry.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=flagstone_sentry.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=flagstone_sentry.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=flagstone_sentry.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
