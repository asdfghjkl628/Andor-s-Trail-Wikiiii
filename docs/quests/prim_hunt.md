# Clouded intent

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `prim_hunt` |
| **In journal** | Yes |
| **Stages** | 19 (completes at 240, 250, 251) |
| **Started by** | [Tonis](../monsters/tonis.md) ([blackwater_mountain10](../maps/blackwater_mountain10.md)) |
| **NPCs involved** | [Blackwater chamber guard](../monsters/blackwater_chamber_guard.md), [Guthbered](../monsters/guthbered.md), [Harlenn](../monsters/harlenn.md), [Laecca](../monsters/laecca.md), [Prim citizen](../monsters/prim_citizen.md), [Tonis](../monsters/tonis.md) |
| **Locations** | [blackwater_mountain10](../maps/blackwater_mountain10.md), [blackwater_mountain11](../maps/blackwater_mountain11.md), [blackwater_mountain21](../maps/blackwater_mountain21.md), [blackwater_mountain29](../maps/blackwater_mountain29.md) |
| **Total XP** | 8,250 |
| **Related quests** | 1 |

</div>

## Overview

> Just outside the collapsed mine on the way to Blackwater mountain, I met a man from the village of Prim. He begged me to help them.

## Prerequisites to start

None: talk to [Tonis](../monsters/tonis.md) ([blackwater_mountain10](../maps/blackwater_mountain10.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [The agent and the beast](bwm_agent.md#stage-95) | stage 95 reached, for stage 251 here |
| Requires | [The agent and the beast](bwm_agent.md#stage-150) | stage 150 reached, for stage 250 here |
| Requires | [The agent and the beast](bwm_agent.md#stage-251) | stage 251 reached, for stage 30 here |
| Unlocks | [The agent and the beast](bwm_agent.md#stage-25) | stage 25 there needs stage 25 here |
| Unlocks | [The agent and the beast](bwm_agent.md#stage-80) | stage 80 there needs stage 251 here |
| Unlocks | [The agent and the beast](bwm_agent.md#stage-250) | stage 250 there needs stage 100 here |
| Unlocks | [The agent and the beast](bwm_agent.md#stage-251) | stage 251 there needs stage 50 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Just outside the collapsed mine on the way to Blackwater mountain, I met a man from the village of Prim. He begged me to help them. | [Tonis](../monsters/tonis.md) ([blackwater_mountain10](../maps/blackwater_mountain10.md)) | – | – |
| <span id="stage-11"></span>11 | The village of Prim needs help from someone from the outside to deal with attacks from some monsters. I should speak to Guthbered in Prim if I want to help them. | [Tonis](../monsters/tonis.md) ([blackwater_mountain10](../maps/blackwater_mountain10.md))<br>[Prim citizen](../monsters/prim_citizen.md) ([blackwater_mountain11](../maps/blackwater_mountain11.md))<br>[Laecca](../monsters/laecca.md) ([blackwater_mountain21](../maps/blackwater_mountain21.md))<br>+1 more | stage 10, stage 20, stage 25 | – |
| <span id="stage-15"></span>15 | Guthbered can be found in the main hall of Prim. I should look for a stone house in the center of town. | [Prim citizen](../monsters/prim_citizen.md) ([blackwater_mountain11](../maps/blackwater_mountain11.md))<br>[Laecca](../monsters/laecca.md) ([blackwater_mountain21](../maps/blackwater_mountain21.md)) | – | – |
| <span id="stage-20"></span>20 | I talked to Guthbered about the story about Prim. Prim has recently been under constant attack from the Blackwater mountain settlement. | [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) | stage 25 | – |
| <span id="stage-25"></span>25 | Guthbered wants me to go up to the settlement atop the Blackwater mountain and ask their battle master Harlenn why (or if) they have summoned the gornaud monsters against Prim. | [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) | – | – |
| <span id="stage-30"></span>30 | I have talked to Harlenn about the attacks on Prim. He denies that the people of the Blackwater mountain settlement have anything to do with them. I should go talk to Guthbered in Prim again. | [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) | stage 25 | – |
| <span id="stage-40"></span>40 | Guthbered still believes that the people in the Blackwater mountain settlement have something to do with the attacks. | [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) | stage 25, stage 30 | – |
| <span id="stage-50"></span>50 | Guthbered wants me to go look for any clues that the people of the Blackwater mountain settlement is preparing for a larger attack on Prim. I should go look for hints near Harlenn's private quarters, but make sure not to be seen. | [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) | – | – |
| <span id="stage-60"></span>60 | I have found some papers around Harlenn's private quarters outlining a plan to attack Prim. I should go talk to Guthbered immediately. | reading a sign on [blackwater_mountain45](../maps/blackwater_mountain45.md) | stage 50 | – |
| <span id="stage-70"></span>70 | Guthbered thanked me for helping him find evidence of the plans for an attack. | [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) | stage 50, stage 60 | 1,150 XP |
| <span id="stage-80"></span>80 | In order to make the attacks on Prim stop, Guthbered wants me to kill Harlenn up in the Blackwater mountain settlement. | [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) | – | – |
| <span id="stage-90"></span>90 | I have started a fight with Harlenn. | [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) | – | faction “fct_bwm” set to -10 |
| <span id="stage-91"></span>91 | I told Harlenn that I was sent to kill him, but I let him live. He thanked me deeply, and left the settlement. | [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) | – | 2,100 XP |
| <span id="stage-99"></span>99 | I have told Guthbered that Harlenn is gone. | [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) | – | – |
| <span id="stage-100"></span>100 | Guthbered thanked me for the help I have provided to Prim. Hopefully, the attacks on Prim should stop now. As thanks, Guthbered gave me some items and a forged permit so that I can enter the inner chamber up in the Blackwater mountain settlement. | [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) | stage 99 | 5,000 XP<br>gives [Blackwater dagger](../items/bwm_dagger.md), [Gold coins](../items/gold.md), [Regular potion of health](../items/health.md), [Forged papers for Blackwater](../items/bwm_permit.md) |
| <span id="stage-140"></span>140 | I have shown the forged permit to the guard and was let through to the inner chamber. | [Blackwater chamber guard](../monsters/blackwater_chamber_guard.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) | hand over 1× [Forged papers for Blackwater](../items/bwm_permit.md) | – |
| <span id="stage-240"></span>240 | I am now trusted in Prim, and all services should be available for me to use. **(completes quest)** | [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) | stage 100 | – |
| <span id="stage-250"></span>250 | I have decided to not help the people of Prim. **(completes quest)** | [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md))<br>[Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) | stage 25, stage 30 | – |
| <span id="stage-251"></span>251 | Since I am helping the Blackwater mountain settlement, Guthbered no longer wants to talk to me. **(completes quest)** | [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) | – | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Tonis](../monsters/tonis.md) ([blackwater_mountain10](../maps/blackwater_mountain10.md)) → choose “What is the matter?” → **stage 10**. NPC: “We desperately need help from someone from the outside in our village of Prim.”

???+ note "Stage 11: 4 routes"

    1. Talk to [Tonis](../monsters/tonis.md) ([blackwater_mountain10](../maps/blackwater_mountain10.md)) → choose “Yes, he told me the story about Prim.” — **conditions:** reached stage 10 of [Clouded intent](../quests/prim_hunt.md#stage-10); reached stage 20 of [Clouded intent](../quests/prim_hunt.md#stage-20) → **stage 11**. NPC: “Good, thanks. We really need your help!”
    2. Talk to [Prim citizen](../monsters/prim_citizen.md) ([blackwater_mountain11](../maps/blackwater_mountain11.md)) → choose “Yes, I am here to help your village.” → **stage 11**. NPC: “Thank you. We really need your help.”
    3. Talk to [Laecca](../monsters/laecca.md) ([blackwater_mountain21](../maps/blackwater_mountain21.md)) → choose “What beasts are you talking about?” → **stage 11**. NPC: “Their attacks are getting more and more clever.”
    4. Talk to [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → choose “Tough luck.” — **conditions:** reached stage 25 of [Clouded intent](../quests/prim_hunt.md#stage-25) → **stage 11**. NPC: “On top of that, there are the attacks from the monsters that we have to deal with.”

???+ note "Stage 15: 2 routes"

    1. Talk to [Prim citizen](../monsters/prim_citizen.md) ([blackwater_mountain11](../maps/blackwater_mountain11.md)) → choose “Where can I find him?” → **stage 15**. NPC: “He is in the main hall right over there. The large stone house.”
    2. Talk to [Laecca](../monsters/laecca.md) ([blackwater_mountain21](../maps/blackwater_mountain21.md)) → choose “Is there anything I can do to help?” → **stage 15**. NPC: “You should talk to Guthbered. He is usually in the main hall. Look for a stone house in the center of the village.”

???+ note "Stage 20: 1 route"

    1. Talk to [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → choose “Any ideas where they might be coming from?” — **conditions:** reached stage 25 of [Clouded intent](../quests/prim_hunt.md#stage-25) → **stage 20**. NPC: “Those evil bastards up in the Blackwater mountain settlement probably summoned them to attack us. They would rather…”

???+ note "Stage 25: 2 routes"

    1. Talk to [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → choose “What was I supposed to do again?” — **conditions:** reached stage 25 of [Clouded intent](../quests/prim_hunt.md#stage-25) → **stage 25**. NPC: “I want you to go up there to their settlement and ask their battle master, Harlenn, why they are doing this to us.”
    2. Talk to [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → choose “OK, I will go ask Harlenn in the Blackwater mountain settlement why they are attacking your village.” — **conditions:** reached stage 25 of [Clouded intent](../quests/prim_hunt.md#stage-25) → **stage 25**. NPC: “Thank you friend.”

???+ note "Stage 30: 1 route"

    1. Talk to [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) → choose “Why are you people attacking the village of Prim?” — **conditions:** reached stage 251 of [The agent and the beast](../quests/bwm_agent.md#stage-251); reached stage 25 of [Clouded intent](../quests/prim_hunt.md#stage-25) → **stage 30**. NPC: “It is, of course, *they* who are the ones causing all the trouble.”

???+ note "Stage 40: 1 route"

    1. Talk to [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → choose “Yes, but Harlenn denies that they have anything to do with the attacks.” — **conditions:** reached stage 25 of [Clouded intent](../quests/prim_hunt.md#stage-25); reached stage 30 of [Clouded intent](../quests/prim_hunt.md#stage-30) → **stage 40**. NPC: “But I am sure they are! As false as they are, they must be. Always lying and deceiving. Causing destruction and turmoil.”

???+ note "Stage 50: 1 route"

    1. Talk to [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → choose “No, I am still looking.” — **conditions:** reached stage 50 of [Clouded intent](../quests/prim_hunt.md#stage-50) → **stage 50**. NPC: “Thank you, friend. Report back to me with your findings.”

???+ note "Stage 60: 1 route"

    1. reading a sign on [blackwater_mountain45](../maps/blackwater_mountain45.md) → the conversation leads here automatically — **conditions:** reached stage 50 of [Clouded intent](../quests/prim_hunt.md#stage-50) → **stage 60**. NPC: “Among the papers, you find what seems to be plans for training fighters, and plans for an attack on what looks like…”

???+ note "Stage 70: 1 route"

    1. Talk to [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → choose “Yes, I found some papers with a plan to attack Prim.” — **conditions:** reached stage 50 of [Clouded intent](../quests/prim_hunt.md#stage-50); reached stage 60 of [Clouded intent](../quests/prim_hunt.md#stage-60) → **stage 70**. NPC: “Thank you for finding this information for us.”

???+ note "Stage 80: 1 route"

    1. Talk to [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → choose “Not yet. I am still working on it.” — **conditions:** reached stage 80 of [Clouded intent](../quests/prim_hunt.md#stage-80) → **stage 80**. NPC: “Excellent. Return to me once you are done.”

???+ note "Stage 90: 1 route"

    1. Talk to [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) → the conversation leads here automatically — **conditions:** reached stage 90 of [Clouded intent](../quests/prim_hunt.md#stage-90) → **stage 90**; also faction “fct_bwm” set to -10. NPC: “Stop me?! Ha ha. Very well, let's see who is the one being stopped here.”

???+ note "Stage 91: 1 route"

    1. Talk to [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) → the conversation leads here automatically — **conditions:** reached stage 91 of [Clouded intent](../quests/prim_hunt.md#stage-91) → **stage 91**. NPC: “Thank you friend, for talking some sense into me.”

???+ note "Stage 99: 1 route"

    1. Talk to [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → the conversation leads here automatically — **conditions:** reached stage 99 of [Clouded intent](../quests/prim_hunt.md#stage-99) → **stage 99**. NPC: “While I am grateful for this news in knowing that he is dead, I am also saddened that it had to come to this.”

???+ note "Stage 100: 1 route"

    1. Talk to [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → the conversation leads here automatically — **conditions:** reached stage 99 of [Clouded intent](../quests/prim_hunt.md#stage-99) → **stage 100**; also gives [Blackwater dagger](../items/bwm_dagger.md), [Gold coins](../items/gold.md), [Regular potion of health](../items/health.md), [Forged papers for Blackwater](../items/bwm_permit.md). NPC: “Here, please accept these few items as some form of compensation for your help. Also, take this piece of paper that we…”

???+ note "Stage 140: 1 route"

    1. Talk to [Blackwater chamber guard](../monsters/blackwater_chamber_guard.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) → choose “Here, I have a written permit to enter.” — **conditions:** hand over 1× [Forged papers for Blackwater](../items/bwm_permit.md) → **stage 140**. NPC: “A permit you say? Let me see that.”

???+ note "Stage 240: 1 route"

    1. Talk to [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → the conversation leads here automatically — **conditions:** reached stage 100 of [Clouded intent](../quests/prim_hunt.md#stage-100) → **stage 240**. NPC: “I am sure everyone here in Prim will want to talk to you now.”

???+ note "Stage 250: 2 routes"

    1. Talk to [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → choose “Hmm, maybe I should help the people up in Blackwater mountain instead.” — **conditions:** reached stage 25 of [Clouded intent](../quests/prim_hunt.md#stage-25); reached stage 30 of [Clouded intent](../quests/prim_hunt.md#stage-30) → **stage 250**. NPC: “Fine. You should leave now while you still can, traitor.”
    2. Talk to [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) → the conversation leads here automatically — **conditions:** reached stage 150 of [The agent and the beast](../quests/bwm_agent.md#stage-150) → **stage 250**. NPC: “I'm sure the monster attacks will stop now when we kill the last few monsters that are outside the settlement.”

???+ note "Stage 251: 1 route"

    1. Talk to [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → the conversation leads here automatically — **conditions:** reached stage 95 of [The agent and the beast](../quests/bwm_agent.md#stage-95) → **stage 251**. NPC: “It is, of course, your choice. But if you are working for them, you are not welcome here in Prim. You should leave…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | stage 10 journal text changed; stage 20 journal text changed; stage 25 journal text changed; stage 30 journal text changed; stage 40 journal text changed; stage 50 journal text changed (+3 more)<br>Dialogue: 3 lines changed<br>· text: “Those evil bastards up in the Blackwater Mountain settlement probably…” → “Those evil bastards up in the Blackwater mountain settlement probably…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=prim_hunt.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=prim_hunt.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=prim_hunt.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=prim_hunt.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=prim_hunt.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `prim_hunt` |
    | showInLog | 1 |
    | Stage IDs | 10, 11, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 91, 99, 100, 140, 240, 250, 251 |
    | Dialogue nodes setting stages | 10: `tonis_6`, 11: `tonis_8`, 11: `prim_commoner1_2`, 11: `laecca_12`, 15: `prim_commoner1_4`, 15: `laecca_13`, 20: `guthbered_19`, 25: `guthbered_30`, 25: `guthbered_31`, 30: `harlenn_prim_2`, 40: `guthbered_talkedto_harl_3`, 50: `guthbered_talkedto_harl_13`, 60: `sign_blackwater45_qstarted_1`, 70: `guthbered_lookforsigns_4`, 80: `guthbered_lookforsigns_9`, 90: `harlenn_sentbyprim_2`, 91: `harlenn_sentbyprim_8`, 99: `guthbered_killharl_2`, 100: `guthbered_killharl_6`, 140: `blackwater_throneguard_3`, 240: `guthbered_completed_1`, 250: `guthbered_workingforbwm_1`, 250: `harlenn_completed_1`, 251: `guthbered_workingforbwm_3` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
