# Thief apprentice

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `Thieves01` |
| **In journal** | Yes |
| **Stages** | 13 (completes at 60) |
| **Started by** | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) |
| **NPCs involved** | [Dunla](../monsters/dunla.md), [Fanamor](../monsters/fanamor.md), [Feygard scout](../monsters/feygard_scout.md), [Leta](../monsters/leta.md), [Thoronir](../monsters/thoronir.md), [Troublemaker](../monsters/troublemaker.md) +1 |
| **Locations** | [crossroads](../maps/crossroads.md), [fallhaven_church](../maps/fallhaven_church.md), [fallhaven_derelict2](../maps/fallhaven_derelict2.md), [fallhaven_derelict2_t](../maps/fallhaven_derelict2_t.md) |
| **Total XP** | 4,550 |
| **Related quests** | 9 |

</div>

## Overview

> After giving him the key of Luthor and talking with Umar about Andor, I needed to ask him about Thieves' Guild itself. I want to join them to see what kind of jobs they do.

## Prerequisites to start

Start with [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)). Required:

- reached stage 51 of [Search for Andor](../quests/andor.md#stage-51)
- reached stage 100 of [Key of Luthor](../quests/bucus.md#stage-100)
- NOT reached stage 5 of [Thief apprentice](../quests/Thieves01.md#stage-5)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Search for Andor](andor.md#stage-51) | stage 51 reached, for stages 5, 10 here |
| Requires | [Disallowed substance](bonemeal.md#stage-100) | stage 100 reached, for stage 50 here |
| Requires | [Key of Luthor](bucus.md#stage-100) | stage 100 reached, for stage 5 here |
| Requires | [scores (hidden flag)](scores.md#stage-18) | stage 18 reached, for stage 50 here |
| Requires | [Thieves Hidden (hidden flag)](thieves_hidden.md#stage-100) | stage 100 reached, for stage 60 here |
| Mutually exclusive | [Thieves Hidden (hidden flag)](thieves_hidden.md#stage-110) | stage 110 must NOT be reached, for stage 60 here |
| Unlocks | [Immaculate kidnapping](Thieves02.md#stage-45) | stage 45 there needs stage 60 here |
| Unlocks | [Immaculate kidnapping](Thieves02.md#stage-60) | stage 60 there needs stage 60 here |
| Unlocks | [Immaculate kidnapping](Thieves02.md#stage-70) | stage 70 there needs stage 60 here |
| Unlocks | [A familiar shadow](familiar_shadow.md#stage-10) | stage 10 there needs stage 60 here |
| Unlocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-60) | stage 60 there needs stage 60 here |
| Unlocks | [Thieves Hidden (hidden flag)](thieves_hidden.md#stage-80) | stage 80 there needs stage 45 here |
| Unlocks | [Thieves Hidden (hidden flag)](thieves_hidden.md#stage-100) | stage 100 there needs stages 20, 51, 55 here |
| Unlocks | [Thieves Hidden (hidden flag)](thieves_hidden.md#stage-110) | stage 110 there needs stage 20 here |
| Unlocks | [Wanted men](wanted_men.md#stage-45) | stage 45 there needs stage 60 here |
| Unlocks | [Wanted men](wanted_men.md#stage-50) | stage 50 there needs stage 60 here |
| Unlocks | [Wanted men](wanted_men.md#stage-55) | stage 55 there needs stage 60 here |
| Unlocks | [Wanted men](wanted_men.md#stage-65) | stage 65 there needs stage 60 here |
| Unlocks | [Wanted men](wanted_men.md#stage-80) | stage 80 there needs stage 60 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-5"></span>5 | After giving him the key of Luthor and talking with Umar about Andor, I needed to ask him about Thieves' Guild itself. I want to join them to see what kind of jobs they do. | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | – | – |
| <span id="stage-10"></span>10 | Umar told me to talk with Troublemaker regarding my first task for the Guild. | [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 5 | – |
| <span id="stage-15"></span>15 | Troublemaker told me to bring him three journals from spies of the guild. First I have to talk with Leta in my village, then with Dunla in Vilegard's tavern, and finally with Fanamor somewhere around Crossroads guardhouse. | [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 10 | – |
| <span id="stage-20"></span>20 | I have to remember to tell them the password "You are no one. No one knows you. No one has seen you." | [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 10 | – |
| <span id="stage-25"></span>25 | Leta gave me her journal and advised me to not raise suspicion. | [Leta](../monsters/leta.md) | stage 20 | 250 XP<br>gives 1× [Leta's Journal](../items/Leta_journal.md) |
| <span id="stage-30"></span>30 | I got Dunla's journal without any problem. I have set out to get the last journal. | [Dunla](../monsters/dunla.md) ([vilegard_tavern](../maps/vilegard_tavern.md)) | stage 25 | 650 XP<br>gives 1× [Dunla's Journal](../items/Dunla_journal.md) |
| <span id="stage-35"></span>35 | Fanamor gave me her journal. | [Fanamor](../monsters/fanamor.md) ([crossroads](../maps/crossroads.md)) | stage 30 | spawns monsters on crossroads |
| <span id="stage-40"></span>40 | Fanamor has been gravely wounded, and the Feygard Scout grabbed the journal. | [Fanamor](../monsters/fanamor.md) ([crossroads](../maps/crossroads.md))<br>[Feygard scout](../monsters/feygard_scout.md) ([crossroads](../maps/crossroads.md)) | stage 35 | 150 XP |
| <span id="stage-45"></span>45 | After I had killed the Feygard scout I talked again with Fanamor. She's losing blood quickly, so I have to bring her a bandage. I need to find a trustworthy priest. | [Fanamor](../monsters/fanamor.md) ([crossroads](../maps/crossroads.md)) | stage 40 | 750 XP<br>starts timer “Fanamorbleeding” |
| <span id="stage-50"></span>50 | Thoronir gave me a bandage. I have to return to Fanamor as soon as possible. | [Thoronir](../monsters/thoronir.md) ([fallhaven_church](../maps/fallhaven_church.md)) | stage 45 | gives 1× [Bandage](../items/bandage.md) |
| <span id="stage-51"></span>51 | Unfortunately, I was not able to save Fanamor's life. However, I did get her journal. | [Fanamor](../monsters/fanamor.md) ([crossroads](../maps/crossroads.md)) | stage 45 | – |
| <span id="stage-55"></span>55 | Fanamor is alive and will find her own way to return. | [Fanamor](../monsters/fanamor.md) ([crossroads](../maps/crossroads.md)) | hand over 1× [Bandage](../items/bandage.md), stage 45, stage 50 | 1,000 XP<br>removes monsters from crossroads<br>spawns monsters on fallhaven_derelict2 |
| <span id="stage-60"></span>60 | I returned to Troublemaker and gave him the journals. He told me to talk with Umar, maybe he has another task for me. **(completes quest)** | [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 20 | 1,750 XP<br>gives 900× [Gold coins](../items/gold.md)<br>sets stage 110 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-110) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 5: 1 route"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “But I really want to join your guild!” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); reached stage 100 of [Key of Luthor](../quests/bucus.md#stage-100); NOT reached stage 5 of [Thief apprentice](../quests/Thieves01.md#stage-5) → **stage 5**. NPC: “OK, OK. You will get a chance. But I warn you that from now on, you cannot go back on your choice.”

???+ note "Stage 10: 2 routes"

    1. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “I will take your opportunity!” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); reached stage 5 of [Thief apprentice](../quests/Thieves01.md#stage-5); NOT reached stage 10 of [Thief apprentice](../quests/Thieves01.md#stage-10); NOT latest stage of [Thief apprentice](../quests/Thieves01.md#stage-60) is 60 → **stage 10**. NPC: “Very well. Let's see if you're good enough to join our guild. Talk with Troublemaker. He will tell you what you have…”
    2. Talk to [Umar](../monsters/umar.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Anything else?” — **conditions:** reached stage 51 of [Search for Andor](../quests/andor.md#stage-51); reached stage 5 of [Thief apprentice](../quests/Thieves01.md#stage-5); NOT reached stage 10 of [Thief apprentice](../quests/Thieves01.md#stage-10); NOT latest stage of [Thief apprentice](../quests/Thieves01.md#stage-60) is 60 → **stage 10**. NPC: “Not for now. Make sure nobody sees you doing suspicious things. Good luck.”

???+ note "Stage 15: 1 route"

    1. Talk to [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Sounds easy, I'll do it.” — **conditions:** reached stage 10 of [Thief apprentice](../quests/Thieves01.md#stage-10) → **stage 15**. NPC: “Good. We have three people on the job. The first one is a spy in Crossglen, Leta. I believe you know her. One of our…”

???+ note "Stage 20: 1 route"

    1. Talk to [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Anything else?” — **conditions:** reached stage 10 of [Thief apprentice](../quests/Thieves01.md#stage-10) → **stage 20**. NPC: “Ah! I almost forgot. You have to say the password if you want them to give you the journal. The password is "You are…”

???+ note "Stage 25: 1 route"

    1. Talk to [Leta](../monsters/leta.md) → choose “Umar sent me to get your journal.” — **conditions:** reached stage 20 of [Thief apprentice](../quests/Thieves01.md#stage-20); NOT reached stage 25 of [Thief apprentice](../quests/Thieves01.md#stage-25) → **stage 25**; also gives 1× [Leta's Journal](../items/Leta_journal.md). NPC: “Here. Make sure you don't raise any suspicion on your future jobs. Bye kid.”

???+ note "Stage 30: 1 route"

    1. Talk to [Dunla](../monsters/dunla.md) ([vilegard_tavern](../maps/vilegard_tavern.md)) → choose “You are no one. No one knows you. No one has seen you.” — **conditions:** reached stage 25 of [Thief apprentice](../quests/Thieves01.md#stage-25); NOT reached stage 30 of [Thief apprentice](../quests/Thieves01.md#stage-30) → **stage 30**; also gives 1× [Dunla's Journal](../items/Dunla_journal.md). NPC: “So, you are one of us. Here, take my journal.”

???+ note "Stage 35: 1 route"

    1. Talk to [Fanamor](../monsters/fanamor.md) ([crossroads](../maps/crossroads.md)) → choose “Umar sent me with the words "You are no one.No one knows you.No one has seen you." Now give me the journal…” — **conditions:** reached stage 30 of [Thief apprentice](../quests/Thieves01.md#stage-30) → **stage 35**; also spawns monsters on crossroads. NPC: “Take this. All I've seen is written here ...”

???+ note "Stage 40: 2 routes"

    1. Talk to [Fanamor](../monsters/fanamor.md) ([crossroads](../maps/crossroads.md)) → the conversation leads here automatically — **conditions:** reached stage 35 of [Thief apprentice](../quests/Thieves01.md#stage-35); NOT reached stage 40 of [Thief apprentice](../quests/Thieves01.md#stage-40) → **stage 40**. NPC: “(Grabs the book) What have we here? A lost kid trying to do business with this scum, hah? You are under arrest!”
    2. Talk to [Feygard scout](../monsters/feygard_scout.md) ([crossroads](../maps/crossroads.md)) → the conversation leads here automatically → **stage 40**. NPC: “(Grabs the book) What have we here? A lost kid trying to do business with this scum, hah? You are under arrest!”

???+ note "Stage 45: 1 route"

    1. Talk to [Fanamor](../monsters/fanamor.md) ([crossroads](../maps/crossroads.md)) → choose “Can I help?” — **conditions:** killed 1× [Feygard scout](../monsters/feygard_scout.md); reached stage 40 of [Thief apprentice](../quests/Thieves01.md#stage-40) → **stage 45**; also starts timer “Fanamorbleeding”. NPC: “I need a bandage quickly, or I will never return to the guild house. A priest might help ...”

???+ note "Stage 50: 1 route"

    1. Talk to [Thoronir](../monsters/thoronir.md) ([fallhaven_church](../maps/fallhaven_church.md)) → choose “Ehm ... My father has cut himself with an axe, and we don't have any bandages!” — **conditions:** reached stage 18 of [scores (hidden flag)](../quests/scores.md#stage-18); reached stage 45 of [Thief apprentice](../quests/Thieves01.md#stage-45); reached stage 100 of [Disallowed substance](../quests/bonemeal.md#stage-100); NOT reached stage 50 of [Thief apprentice](../quests/Thieves01.md#stage-50) → **stage 50**; also gives 1× [Bandage](../items/bandage.md). NPC: “This is what I have, take it. I expect this will be useful.”

???+ note "Stage 51: 1 route"

    1. Talk to [Fanamor](../monsters/fanamor.md) ([crossroads](../maps/crossroads.md)) → the conversation leads here automatically — **conditions:** 120 rounds passed since timer “Fanamorbleeding”; reached stage 45 of [Thief apprentice](../quests/Thieves01.md#stage-45) → **stage 51**. NPC: “(You look away when you see the corpse of Fanamor. Anklebiters probably had something to do with this horrible event.)”

???+ note "Stage 55: 1 route"

    1. Talk to [Fanamor](../monsters/fanamor.md) ([crossroads](../maps/crossroads.md)) → choose “Yes, I have it!” — **conditions:** reached stage 45 of [Thief apprentice](../quests/Thieves01.md#stage-45); hand over 1× [Bandage](../items/bandage.md); reached stage 50 of [Thief apprentice](../quests/Thieves01.md#stage-50) → **stage 55**; also removes monsters from crossroads, spawns monsters on fallhaven_derelict2. NPC: “(You help Fanamor put the bandage on the wound) ... I think I will be able ... to move in a few minutes. See you at…”

???+ note "Stage 60: 1 route"

    1. Talk to [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “I gave you the journals, so where's my reward?” — **conditions:** reached stage 20 of [Thief apprentice](../quests/Thieves01.md#stage-20); NOT reached stage 60 of [Thief apprentice](../quests/Thieves01.md#stage-60); reached stage 100 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-100); NOT reached stage 110 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-110) → **stage 60**; also gives 900× [Gold coins](../items/gold.md), sets stage 110 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-110). NPC: “You should talk with Umar. Maybe he has another task ... one that's more in your line of work, you know.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 14 lines added |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 1 line changed<br>· text: “I need a bandage quickly, or I will never return to the guild house.” → “I need a bandage quickly, or I will never return to the guild house. …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves01.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves01.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves01.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves01.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=Thieves01.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `Thieves01` |
    | showInLog | 1 |
    | Stage IDs | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 51, 55, 60 |
    | Dialogue nodes setting stages | 5: `umar_guild_3`, 10: `umar_guild_5a`, 10: `umar_guild_6b`, 15: `troublemaker_guild_8a`, 20: `troublemaker_guild_9`, 25: `leta_guild_3`, 30: `dunla_guild_2a`, 35: `fanamor_guild_2`, 40: `feygard_scout_3`, 45: `fanamor_guild_7b`, 50: `thoronir_guild_3`, 51: `fanamor_guild_0`, 55: `fanamor_guild_9a`, 60: `troublemaker_guild_12a` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
