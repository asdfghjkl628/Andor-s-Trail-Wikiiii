# Mine for the taking

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `graveyard_quest` |
| **In journal** | Yes |
| **Stages** | 13 (completes at 90, 95, 100, 105) |
| **Started by** | stepping on a trigger on [graveyard0](../maps/graveyard0.md) |
| **NPCs involved** | [Graveyard king](../monsters/graveyardking.md), [Hagale](../monsters/algore.md), [Waterway traveler](../monsters/graveyard_traveler.md) |
| **Locations** | [graveyard0](../maps/graveyard0.md), [graveyard1](../maps/graveyard1.md), [woodsettlement0](../maps/woodsettlement0.md) |
| **Total XP** | 5,500 |

</div>

## Overview

> I stumbled across a treasure chest in a clearing south of the Waterway house but the chest is protected by some form of magic and cannot be opened.

## Prerequisites to start

Start with stepping on a trigger on [graveyard0](../maps/graveyard0.md). Required:

- NOT reached stage 80 of [Mine for the taking](../quests/graveyard_quest.md#stage-80)
- NOT reached stage 70 of [Mine for the taking](../quests/graveyard_quest.md#stage-70)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

No links to other quests were found in the dialogue conditions.

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I stumbled across a treasure chest in a clearing south of the Waterway house but the chest is protected by some form of magic and cannot be opened.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Graveyard0](../maps/graveyard0.md).</span> | stepping on a trigger on [graveyard0](../maps/graveyard0.md) | – | – |
| <span id="stage-20"></span>20 | I encountered a traveler a short distance from the treasure chest. He told me there is a legend that the key to the chest is held by one of the undead that roam the cemetery to the south of the chest. However, the entrance to the cemetery is sealed by a magical force. | [Waterway traveler](../monsters/graveyard_traveler.md) ([graveyard0](../maps/graveyard0.md)) | stage 10 | – |
| <span id="stage-30"></span>30 | The traveler told me that Hagale in the Wood settlement might know how to enter the cemetery. | [Waterway traveler](../monsters/graveyard_traveler.md) ([graveyard0](../maps/graveyard0.md)) | stage 10 | – |
| <span id="stage-35"></span>35 | I went to the Wood settlement and found Hagale. He was a drunk mess and would not speak to me unless I brought him two Lowyna's special brew. | [Hagale](../monsters/algore.md) ([woodsettlement0](../maps/woodsettlement0.md)) | stage 30 | – |
| <span id="stage-40"></span>40 | Hagale said that the entrance to the cemetery was also sealed with magic to safeguard the key to the chest. The seal can only be broken by defeating the undead monster. However, Hagale found an ancient text that allows the holder to temporarily enter the cemetery. Hagale gave me the text. | [Hagale](../monsters/algore.md) ([woodsettlement0](../maps/woodsettlement0.md)) | hand over 2× [Lowyna's special brew](../items/drink_lowyn2.md), stage 35 | gives 1× [Ancient text](../items/graveyardtext.md) |
| <span id="stage-50"></span>50 | I returned to the cemetery and was able to enter it using the ancient text just as Hagale had claimed.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Graveyard1](../maps/graveyard1.md).</span> | walking into a blocked passage on [graveyard1](../maps/graveyard1.md) | carry 1× [Ancient text](../items/graveyardtext.md), stage 40 | 500 XP<br>spawns monsters on graveyard1 |
| <span id="stage-60"></span>60 | I hacked through a horde of undead until I encountered one wearing a key. | [Graveyard king](../monsters/graveyardking.md) ([graveyard1](../maps/graveyard1.md)) | – | – |
| <span id="stage-70"></span>70 | I killed the undead and took the key.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Graveyard1](../maps/graveyard1.md).</span> | stepping on a trigger on [graveyard1](../maps/graveyard1.md) | – | – |
| <span id="stage-80"></span>80 | I opened the chest, which contained a powerful sword. Next time I'm in the Wood settlement I should see if Hagale is still around.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Graveyard0](../maps/graveyard0.md).</span> | stepping on a trigger on [graveyard0](../maps/graveyard0.md) | hand over 1× [Graveyard key](../items/graveyardkey.md), stage 70 | 2,500 XP<br>gives 1× [LifeTaker](../items/lifetaker.md) |
| <span id="stage-90"></span>90 | Hagale tried to rob me and take the sword, but I killed him and took it back. **(completes quest)** | [Hagale](../monsters/algore.md) ([woodsettlement0](../maps/woodsettlement0.md)) | carry 1× [LifeTaker](../items/lifetaker.md), stage 80 | – |
| <span id="stage-95"></span>95 | Hagale tried to rob me and take the sword. He lost his wife and daughter and wasn't thinking straight. I gave him the sword without a fight. **(completes quest)** | [Hagale](../monsters/algore.md) ([woodsettlement0](../maps/woodsettlement0.md)) | hand over 1× [LifeTaker](../items/lifetaker.md), stage 80 | 1,500 XP |
| <span id="stage-100"></span>100 | Hagale wanted some of the gold I got from selling the sword. It seemed fair to give him a share. **(completes quest)** | [Hagale](../monsters/algore.md) ([woodsettlement0](../maps/woodsettlement0.md)) | pay 1,000 gold, stage 80 | 1,000 XP |
| <span id="stage-105"></span>105 | Hagale tried to rob me of the gold I got from selling the sword. I had no choice but to kill him. **(completes quest)** | [Hagale](../monsters/algore.md) ([woodsettlement0](../maps/woodsettlement0.md)) | stage 80 | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. stepping on a trigger on [graveyard0](../maps/graveyard0.md) → choose “Nothing my weapon couldn't handle.” — **conditions:** NOT reached stage 80 of [Mine for the taking](../quests/graveyard_quest.md#stage-80); NOT reached stage 70 of [Mine for the taking](../quests/graveyard_quest.md#stage-70) → **stage 10**. NPC: “Multiple strikes from your weapon do not damage the chest. The chest is protected by some form of magic.”

???+ note "Stage 20: 1 route"

    1. Talk to [Waterway traveler](../monsters/graveyard_traveler.md) ([graveyard0](../maps/graveyard0.md)) → choose “Yes.” — **conditions:** reached stage 10 of [Mine for the taking](../quests/graveyard_quest.md#stage-10); NOT reached stage 40 of [Mine for the taking](../quests/graveyard_quest.md#stage-40) → **stage 20**. NPC: “That chest is something of a local legend. Been there for generations. They say it is sealed with magic and can only…”

???+ note "Stage 30: 1 route"

    1. Talk to [Waterway traveler](../monsters/graveyard_traveler.md) ([graveyard0](../maps/graveyard0.md)) → choose “Interesting. Is there anything else you can tell me about the chest or cemetery?” — **conditions:** reached stage 10 of [Mine for the taking](../quests/graveyard_quest.md#stage-10); NOT reached stage 40 of [Mine for the taking](../quests/graveyard_quest.md#stage-40) → **stage 30**. NPC: “That is all I know ... Come to think of it ... Hagale from the Wood Settlement was out here a few weeks ago asking…”

???+ note "Stage 35: 1 route"

    1. Talk to [Hagale](../monsters/algore.md) ([woodsettlement0](../maps/woodsettlement0.md)) → choose “I heard you were interested in that unattended treasure chest by the Waterway house.” — **conditions:** reached stage 30 of [Mine for the taking](../quests/graveyard_quest.md#stage-30); NOT reached stage 40 of [Mine for the taking](../quests/graveyard_quest.md#stage-40) → **stage 35**. NPC: “Oh yeah? What's it to you kid? ... BURP ... If you want to know, it will cost you two bottles of Lowyna's special brew.”

???+ note "Stage 40: 1 route"

    1. Talk to [Hagale](../monsters/algore.md) ([woodsettlement0](../maps/woodsettlement0.md)) → choose “I'm sorry for your losses. You have suffered a lot. I want to finish what you started. Do you still have…” — **conditions:** reached stage 35 of [Mine for the taking](../quests/graveyard_quest.md#stage-35); NOT reached stage 40 of [Mine for the taking](../quests/graveyard_quest.md#stage-40); hand over 2× [Lowyna's special brew](../items/drink_lowyn2.md) → **stage 40**; also gives 1× [Ancient text](../items/graveyardtext.md). NPC: “[Hagale finishes the second bottle of Lowyna's special brew] Sure do. I hope you know what you're doing kid.”

???+ note "Stage 50: 1 route"

    1. walking into a blocked passage on [graveyard1](../maps/graveyard1.md) → the conversation leads here automatically — **conditions:** reached stage 40 of [Mine for the taking](../quests/graveyard_quest.md#stage-40); carry 1× [Ancient text](../items/graveyardtext.md); NOT reached stage 70 of [Mine for the taking](../quests/graveyard_quest.md#stage-70) → **stage 50**; also spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1, spawns monsters on graveyard1. NPC: “The text begins to radiate light. The ground begins to shake as darkness fills the sky. A loud cracking sound is…”

???+ note "Stage 60: 1 route"

    1. Talk to [Graveyard king](../monsters/graveyardking.md) ([graveyard1](../maps/graveyard1.md)) → the conversation leads here automatically → **stage 60**. NPC: “[You notice this undead is wearing a key around its neck]”

???+ note "Stage 70: 1 route"

    1. stepping on a trigger on [graveyard1](../maps/graveyard1.md) → the conversation leads here automatically — **conditions:** killed 1× [Graveyard king](../monsters/graveyardking.md) → **stage 70**

???+ note "Stage 80: 1 route"

    1. stepping on a trigger on [graveyard0](../maps/graveyard0.md) → choose “I have the key right here.” — **conditions:** NOT reached stage 80 of [Mine for the taking](../quests/graveyard_quest.md#stage-80); hand over 1× [Graveyard key](../items/graveyardkey.md); reached stage 70 of [Mine for the taking](../quests/graveyard_quest.md#stage-70) → **stage 80**; also gives 1× [LifeTaker](../items/lifetaker.md). NPC: “You open the chest and discover a powerful sword infused with unholy magic.”

???+ note "Stage 90: 1 route"

    1. Talk to [Hagale](../monsters/algore.md) ([woodsettlement0](../maps/woodsettlement0.md)) → choose “I went through hell to get this sword. I won't give it to you without a fight.” — **conditions:** reached stage 80 of [Mine for the taking](../quests/graveyard_quest.md#stage-80); NOT reached stage 90 of [Mine for the taking](../quests/graveyard_quest.md#stage-90); NOT reached stage 95 of [Mine for the taking](../quests/graveyard_quest.md#stage-95); NOT reached stage 100 of [Mine for the taking](../quests/graveyard_quest.md#stage-100); NOT reached stage 105 of [Mine for the taking](../quests/graveyard_quest.md#stage-105); carry 1× [LifeTaker](../items/lifetaker.md) → **stage 90**. NPC: “Let's go.”

???+ note "Stage 95: 1 route"

    1. Talk to [Hagale](../monsters/algore.md) ([woodsettlement0](../maps/woodsettlement0.md)) → choose “I went through a lot to get this sword ... but you suffered more than me. I won't fight you. If you want it…” — **conditions:** reached stage 80 of [Mine for the taking](../quests/graveyard_quest.md#stage-80); NOT reached stage 90 of [Mine for the taking](../quests/graveyard_quest.md#stage-90); NOT reached stage 95 of [Mine for the taking](../quests/graveyard_quest.md#stage-95); NOT reached stage 100 of [Mine for the taking](../quests/graveyard_quest.md#stage-100); NOT reached stage 105 of [Mine for the taking](../quests/graveyard_quest.md#stage-105); hand over 1× [LifeTaker](../items/lifetaker.md) → **stage 95**. NPC: “Alright hand it over. Be quick about it.”

???+ note "Stage 100: 1 route"

    1. Talk to [Hagale](../monsters/algore.md) ([woodsettlement0](../maps/woodsettlement0.md)) → choose “OK, OK. I guess it's fair that you should get a share. Here's 1,000 gold.” — **conditions:** reached stage 80 of [Mine for the taking](../quests/graveyard_quest.md#stage-80); NOT reached stage 90 of [Mine for the taking](../quests/graveyard_quest.md#stage-90); NOT reached stage 95 of [Mine for the taking](../quests/graveyard_quest.md#stage-95); NOT reached stage 100 of [Mine for the taking](../quests/graveyard_quest.md#stage-100); NOT reached stage 105 of [Mine for the taking](../quests/graveyard_quest.md#stage-105); NOT carry 1× [LifeTaker](../items/lifetaker.md); NOT wearing [LifeTaker](../items/lifetaker.md); pay 1,000 gold → **stage 100**. NPC: “Thanks kid. It's good to see you have some honor.”

???+ note "Stage 105: 1 route"

    1. Talk to [Hagale](../monsters/algore.md) ([woodsettlement0](../maps/woodsettlement0.md)) → choose “No way! I fought to get the sword, and the profit is mine!” — **conditions:** reached stage 80 of [Mine for the taking](../quests/graveyard_quest.md#stage-80); NOT reached stage 90 of [Mine for the taking](../quests/graveyard_quest.md#stage-90); NOT reached stage 95 of [Mine for the taking](../quests/graveyard_quest.md#stage-95); NOT reached stage 100 of [Mine for the taking](../quests/graveyard_quest.md#stage-100); NOT reached stage 105 of [Mine for the taking](../quests/graveyard_quest.md#stage-105); NOT carry 1× [LifeTaker](../items/lifetaker.md); NOT wearing [LifeTaker](../items/lifetaker.md) → **stage 105**. NPC: “We'll see about that.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 14 lines added |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 2 lines changed<br>· text: “Lets go.” → “Let's go.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=graveyard_quest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=graveyard_quest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=graveyard_quest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=graveyard_quest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=graveyard_quest.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `graveyard_quest` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 35, 40, 50, 60, 70, 80, 90, 95, 100, 105 |
    | Dialogue nodes setting stages | 10: `graveyard_quest4`, 20: `graveyardtraveler_20`, 30: `graveyardtraveler_50`, 35: `algore_10`, 40: `algore_87`, 50: `graveyardwall_2`, 60: `graveyardking_1`, 70: `graveyardbosskill_20`, 80: `graveyard_quest_end`, 90: `algore_99a`, 95: `algore_99b`, 100: `algore_99g`, 100: `algore_99h`, 105: `algore_99i` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
