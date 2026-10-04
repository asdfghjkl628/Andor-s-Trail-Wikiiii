# Flows through the veins

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `loneford` |
| **In journal** | Yes |
| **Stages** | 17 (completes at 55, 60) |
| **Started by** | [Gandoren](../monsters/gandoren.md), [Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md)) |
| **NPCs involved** | [Buceth](../monsters/buceth.md), [Farmer](../monsters/loneford_farmer0.md), [Gandoren](../monsters/gandoren.md), [Kuldan](../monsters/kuldan.md), [Landa](../monsters/landa.md), [Minarra](../monsters/minarra.md) +6 |
| **Locations** | [fields0](../maps/fields0.md), [houseatcrossroads4](../maps/houseatcrossroads4.md), [loneford1](../maps/loneford1.md), [loneford2](../maps/loneford2.md) |
| **Total XP** | 30,000 |
| **Related quests** | 5 |

</div>

## Overview

> I heard a story about Loneford. Apparently, a lot of people have become ill there recently, and some have even died. The cause is still unknown.

## Prerequisites to start

**Route 1** ([Gandoren](../monsters/gandoren.md)):

- reached stage 25 of [Feygard errands](../quests/feygard_shipment.md#stage-25)
- NOT reached stage 21 of [Flows through the veins](../quests/loneford.md#stage-21)

**Route 2** ([Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md))):

- reached stage 20 of [The path is clear to me](../quests/rogorn.md#stage-20)
- NOT reached stage 21 of [Flows through the veins](../quests/loneford.md#stage-21)

**Route 3** ([Farmer](../monsters/loneford_farmer0.md) ([loneford1](../maps/loneford1.md))):

- nothing

**Route 4** ([Villager](../monsters/loneford_villager0.md) ([loneford2](../maps/loneford2.md))):

- nothing

**Route 5** ([Villager](../monsters/loneford_villager1.md) ([loneford2](../maps/loneford2.md))):

- nothing

**Route 6** ([Villager](../monsters/loneford_villager3.md) ([loneford2](../maps/loneford2.md))):

- nothing


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Feygard errands](feygard_shipment.md#stage-25) | stage 25 reached, for stages 10, 11, 21 here |
| Requires | [I have it in me](maggots.md#stage-51) | stage 51 reached, for stages 23, 25 here |
| Requires | [The path is clear to me](rogorn.md#stage-20) | stage 20 reached, for stages 10, 11, 21 here |
| Unlocks | [Search for Andor](andor.md#stage-61) | stage 61 there needs stage 45 here |
| Unlocks | [Search for Andor](andor.md#stage-62) | stage 62 there needs stage 45 here |
| Unlocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-19) | stage 19 there needs stage 55 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I heard a story about Loneford. Apparently, a lot of people have become ill there recently, and some have even died. The cause is still unknown. | [Gandoren](../monsters/gandoren.md)<br>[Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md))<br>[Farmer](../monsters/loneford_farmer0.md) ([loneford1](../maps/loneford1.md))<br>+5 more | – | – |
| <span id="stage-11"></span>11 | I should investigate what could have caused the people of Loneford to become ill. To gather clues, I should ask the citizens of Loneford and the surrounding areas about what they think is the cause. | [Gandoren](../monsters/gandoren.md)<br>[Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md))<br>[Farmer](../monsters/loneford_farmer0.md) ([loneford1](../maps/loneford1.md))<br>+5 more | – | – |
| <span id="stage-21"></span>21 | The guards in the Crossroads guardhouse are certain that the illness in Loneford is caused by some sabotage done by the priests or people from Nor City. | [Gandoren](../monsters/gandoren.md)<br>[Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md)) | – | – |
| <span id="stage-22"></span>22 | Some villagers in Loneford believe that the illness is caused by the guards from Feygard, in some scheme to make the people suffer even more than they already have. | [Rolwynn](../monsters/rolwynn.md) ([fields0](../maps/fields0.md)) | stage 11 | – |
| <span id="stage-23"></span>23 | Talion, the chapel priest in Loneford, thinks that the illness is the work of the Shadow, as punishment for Loneford's lack of devotion to the Shadow. | [Talion](../monsters/talion.md) | stage 11 | – |
| <span id="stage-24"></span>24 | Taevinn in Loneford is certain that Sienn in the southeast barn has something to do with the illness. Apparently, Sienn keeps a pet around that has approached Taevinn in a threatening manner several times. | [Taevinn](../monsters/taevinn.md) ([loneford7](../maps/loneford7.md)) | stage 11 | – |
| <span id="stage-25"></span>25 | I should go see Landa in the Loneford tavern. Rumor has it that he saw something that he doesn't dare tell anyone. | [Rolwynn](../monsters/rolwynn.md) ([fields0](../maps/fields0.md))<br>[Taevinn](../monsters/taevinn.md) ([loneford7](../maps/loneford7.md))<br>[Talion](../monsters/talion.md) | stage 11, stage 21, stage 22, stage 23, stage 24 | – |
| <span id="stage-30"></span>30 | Landa confused me with someone else at first. He apparently saw a boy doing something around the town well during the night before the illness started. He was scared to talk to me at first since he thought I looked like the boy he had seen. Could it have been Andor that he saw? | [Landa](../monsters/landa.md) ([loneford6](../maps/loneford6.md)) | stage 25 | – |
| <span id="stage-31"></span>31 | Also, the night after he saw the boy at the well, he saw Buceth taking samples of the water in the well. Strangely enough, Buceth has not gotten ill like the others in the village. | [Landa](../monsters/landa.md) ([loneford6](../maps/loneford6.md)) | stage 25 | – |
| <span id="stage-35"></span>35 | I should go question Buceth at the Loneford chapel about what he was doing at the well, and about whether he knows anything about Andor. | [Landa](../monsters/landa.md) ([loneford6](../maps/loneford6.md)) | stage 25 | – |
| <span id="stage-41"></span>41 | I have bribed Buceth into talking to me. | [Buceth](../monsters/buceth.md) | pay 1,000 gold, stage 35 | – |
| <span id="stage-42"></span>42 | I have told Buceth that I am ready to follow the Shadow. | [Buceth](../monsters/buceth.md) | stage 35 | – |
| <span id="stage-45"></span>45 | Buceth tells me that he is assigned by the priests in Nor City to make sure the Shadow casts its glow over Loneford. Apparently, the priests had sent a boy to do some business in Loneford, and Buceth was tasked with gathering some samples from the water well. | [Buceth](../monsters/buceth.md) | – | – |
| <span id="stage-50"></span>50 | I have attacked Buceth. I should bring any evidence that Buceth has on him to Kuldan, the guard captain in the longhouse in Loneford. | [Buceth](../monsters/buceth.md) | – | – |
| <span id="stage-54"></span>54 | I have given the vial that Buceth had on him to Kuldan, the guard captain in Loneford. | [Kuldan](../monsters/kuldan.md) ([loneford3](../maps/loneford3.md)) | – | – |
| <span id="stage-55"></span>55 | Kuldan thanked me for solving the mystery of the illness in Loneford. They will start bringing in water with help from Feygard instead of drinking from the well from now on. Kuldan also told me to visit the castle steward in Feygard if I want to help further. **(completes quest)** | [Kuldan](../monsters/kuldan.md) ([loneford3](../maps/loneford3.md)) | stage 54 | 15,000 XP |
| <span id="stage-60"></span>60 | I have promised to keep Buceth's story a secret. If Andor was indeed here, he must have had a good reason for doing what he did. Buceth also told me to visit the chapel custodian in Nor City if I want to learn more about the Shadow. **(completes quest)** | [Buceth](../monsters/buceth.md) | stage 45 | 15,000 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 8 routes"

    1. Talk to [Gandoren](../monsters/gandoren.md) → choose “I'd rather talk about the troubles in Loneford that you had mentioned.” — **conditions:** reached stage 25 of [Feygard errands](../quests/feygard_shipment.md#stage-25); NOT reached stage 21 of [Flows through the veins](../quests/loneford.md#stage-21) → **stage 10**. NPC: “Everyone started investigating what could be the cause. Currently, the cause is still unknown.”
    2. Talk to [Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md)) → choose “I'd rather talk about the troubles in Loneford that you had mentioned.” — **conditions:** reached stage 20 of [The path is clear to me](../quests/rogorn.md#stage-20); NOT reached stage 21 of [Flows through the veins](../quests/loneford.md#stage-21) → **stage 10**. NPC: “Everyone started investigating what could be the cause. Currently, the cause is still unknown.”
    3. Talk to [Farmer](../monsters/loneford_farmer0.md) ([loneford1](../maps/loneford1.md)) → choose “What illness?” → **stage 10**. NPC: “We all started to investigate what could be the cause. We still aren't certain what the cause is, but we have our…”
    4. Talk to [Villager](../monsters/loneford_villager0.md) ([loneford2](../maps/loneford2.md)) → choose “What illness?” → **stage 10**. NPC: “We all started to investigate what could be the cause. We still aren't certain what the cause is, but we have our…”
    5. Talk to [Villager](../monsters/loneford_villager1.md) ([loneford2](../maps/loneford2.md)) → choose “What illness?” → **stage 10**. NPC: “We all started to investigate what could be the cause. We still aren't certain what the cause is, but we have our…”
    6. Talk to [Villager](../monsters/loneford_villager3.md) ([loneford2](../maps/loneford2.md)) → choose “What illness?” → **stage 10**. NPC: “We all started to investigate what could be the cause. We still aren't certain what the cause is, but we have our…”
    7. Talk to [Rolwynn](../monsters/rolwynn.md) ([fields0](../maps/fields0.md)) → choose “What illness?” → **stage 10**. NPC: “We all started to investigate what could be the cause. We still aren't certain what the cause is, but we have our…”
    8. Talk to [Taevinn](../monsters/taevinn.md) ([loneford7](../maps/loneford7.md)) → choose “What illness?” → **stage 10**. NPC: “We all started to investigate what could be the cause. We still aren't certain what the cause is, but we have our…”

???+ note "Stage 11: 8 routes"

    1. Talk to [Gandoren](../monsters/gandoren.md) → choose “I'd rather talk about the troubles in Loneford that you had mentioned.” — **conditions:** reached stage 25 of [Feygard errands](../quests/feygard_shipment.md#stage-25); NOT reached stage 21 of [Flows through the veins](../quests/loneford.md#stage-21) → **stage 11**. NPC: “Luckily, now Feygard has sent patrols up there to help guard the village at least. The people are still suffering…”
    2. Talk to [Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md)) → choose “I'd rather talk about the troubles in Loneford that you had mentioned.” — **conditions:** reached stage 20 of [The path is clear to me](../quests/rogorn.md#stage-20); NOT reached stage 21 of [Flows through the veins](../quests/loneford.md#stage-21) → **stage 11**. NPC: “Luckily, now Feygard has sent patrols up there to help guard the village at least. The people are still suffering…”
    3. Talk to [Farmer](../monsters/loneford_farmer0.md) ([loneford1](../maps/loneford1.md)) → choose “What illness?” → **stage 11**. NPC: “Luckily, now Feygard has sent patrols up here to help guard the village at least. We are still suffering though, and…”
    4. Talk to [Villager](../monsters/loneford_villager0.md) ([loneford2](../maps/loneford2.md)) → choose “What illness?” → **stage 11**. NPC: “Luckily, now Feygard has sent patrols up here to help guard the village at least. We are still suffering though, and…”
    5. Talk to [Villager](../monsters/loneford_villager1.md) ([loneford2](../maps/loneford2.md)) → choose “What illness?” → **stage 11**. NPC: “Luckily, now Feygard has sent patrols up here to help guard the village at least. We are still suffering though, and…”
    6. Talk to [Villager](../monsters/loneford_villager3.md) ([loneford2](../maps/loneford2.md)) → choose “What illness?” → **stage 11**. NPC: “Luckily, now Feygard has sent patrols up here to help guard the village at least. We are still suffering though, and…”
    7. Talk to [Rolwynn](../monsters/rolwynn.md) ([fields0](../maps/fields0.md)) → choose “What illness?” → **stage 11**. NPC: “Luckily, now Feygard has sent patrols up here to help guard the village at least. We are still suffering though, and…”
    8. Talk to [Taevinn](../monsters/taevinn.md) ([loneford7](../maps/loneford7.md)) → choose “What illness?” → **stage 11**. NPC: “Luckily, now Feygard has sent patrols up here to help guard the village at least. We are still suffering though, and…”

???+ note "Stage 21: 2 routes"

    1. Talk to [Gandoren](../monsters/gandoren.md) → choose “I'd rather talk about the troubles in Loneford that you had mentioned.” — **conditions:** reached stage 25 of [Feygard errands](../quests/feygard_shipment.md#stage-25); NOT reached stage 21 of [Flows through the veins](../quests/loneford.md#stage-21) → **stage 21**. NPC: “I tell you. Savages - that's what they are. No respect for the laws or authority.”
    2. Talk to [Minarra](../monsters/minarra.md) ([houseatcrossroads4](../maps/houseatcrossroads4.md)) → choose “I'd rather talk about the troubles in Loneford that you had mentioned.” — **conditions:** reached stage 20 of [The path is clear to me](../quests/rogorn.md#stage-20); NOT reached stage 21 of [Flows through the veins](../quests/loneford.md#stage-21) → **stage 21**. NPC: “I tell you. Savages - that's what they are. No respect for the laws or authority.”

???+ note "Stage 22: 1 route"

    1. Talk to [Rolwynn](../monsters/rolwynn.md) ([fields0](../maps/fields0.md)) → choose “What do you think is the cause of the illness?” — **conditions:** reached stage 11 of [Flows through the veins](../quests/loneford.md#stage-11) → **stage 22**. NPC: “I am sure that they did something to us as punishment for not following their *rules*. They are always talking about…”

???+ note "Stage 23: 1 route"

    1. Talk to [Talion](../monsters/talion.md) → choose “Do you know anything about the illness here in Loneford?” — **conditions:** reached stage 51 of [I have it in me](../quests/maggots.md#stage-51); reached stage 11 of [Flows through the veins](../quests/loneford.md#stage-11) → **stage 23**. NPC: “My feeling is that this illness is caused by the Shadow, as punishment to all of us here in Loneford.”

???+ note "Stage 24: 1 route"

    1. Talk to [Taevinn](../monsters/taevinn.md) ([loneford7](../maps/loneford7.md)) → choose “Do you know anything about the illness?” — **conditions:** reached stage 11 of [Flows through the veins](../quests/loneford.md#stage-11) → **stage 24**. NPC: “I tell you, there's mischief all around him and that thing he keeps around. I am sure they are up to something. They…”

???+ note "Stage 25: 3 routes"

    1. Talk to [Rolwynn](../monsters/rolwynn.md) ([fields0](../maps/fields0.md)) → choose “What do you think is the cause of the illness?” — **conditions:** reached stage 11 of [Flows through the veins](../quests/loneford.md#stage-11); reached stage 21 of [Flows through the veins](../quests/loneford.md#stage-21); reached stage 22 of [Flows through the veins](../quests/loneford.md#stage-22); reached stage 23 of [Flows through the veins](../quests/loneford.md#stage-23); reached stage 24 of [Flows through the veins](../quests/loneford.md#stage-24) → **stage 25**. NPC: “There's something else also. I talked to that drunk, Landa, in the tavern earlier today. He said he saw something but…”
    2. Talk to [Taevinn](../monsters/taevinn.md) ([loneford7](../maps/loneford7.md)) → choose “Do you know anything about the illness?” — **conditions:** reached stage 11 of [Flows through the veins](../quests/loneford.md#stage-11); reached stage 21 of [Flows through the veins](../quests/loneford.md#stage-21); reached stage 22 of [Flows through the veins](../quests/loneford.md#stage-22); reached stage 23 of [Flows through the veins](../quests/loneford.md#stage-23); reached stage 24 of [Flows through the veins](../quests/loneford.md#stage-24) → **stage 25**. NPC: “There's something else also. I talked to that drunk, Landa, in the tavern earlier today. He said he saw something but…”
    3. Talk to [Talion](../monsters/talion.md) → choose “Do you know anything about the illness here in Loneford?” — **conditions:** reached stage 51 of [I have it in me](../quests/maggots.md#stage-51); reached stage 11 of [Flows through the veins](../quests/loneford.md#stage-11); reached stage 21 of [Flows through the veins](../quests/loneford.md#stage-21); reached stage 22 of [Flows through the veins](../quests/loneford.md#stage-22); reached stage 23 of [Flows through the veins](../quests/loneford.md#stage-23); reached stage 24 of [Flows through the veins](../quests/loneford.md#stage-24) → **stage 25**. NPC: “There's something else also. I talked to that drunk, Landa, in the tavern earlier today. He said he saw something but…”

???+ note "Stage 30: 1 route"

    1. Talk to [Landa](../monsters/landa.md) ([loneford6](../maps/loneford6.md)) → choose “When was this?” — **conditions:** reached stage 25 of [Flows through the veins](../quests/loneford.md#stage-25) → **stage 30**. NPC: “Almost the whole village wanted to see what had happened to Hesor. I kept to myself and didn't dare talk to anyone.”

???+ note "Stage 31: 1 route"

    1. Talk to [Landa](../monsters/landa.md) ([loneford6](../maps/loneford6.md)) → choose “When was this?” — **conditions:** reached stage 25 of [Flows through the veins](../quests/loneford.md#stage-25) → **stage 31**. NPC: “Also, isn't it strange how Buceth has not gotten ill, while all the others in the village have gotten ill?”

???+ note "Stage 35: 1 route"

    1. Talk to [Landa](../monsters/landa.md) ([loneford6](../maps/loneford6.md)) → choose “When was this?” — **conditions:** reached stage 25 of [Flows through the veins](../quests/loneford.md#stage-25) → **stage 35**. NPC: “He must be up to something. He and that boy that looked like you. Are you sure it wasn't you?”

???+ note "Stage 41: 1 route"

    1. Talk to [Buceth](../monsters/buceth.md) → choose “Here's 1,000 gold, take it.” — **conditions:** reached stage 35 of [Flows through the veins](../quests/loneford.md#stage-35); pay 1,000 gold → **stage 41**. NPC: “You seem to realize the true value of the Shadow. Yes, this will do fine, thank you.”

???+ note "Stage 42: 1 route"

    1. Talk to [Buceth](../monsters/buceth.md) → choose “I am ready to follow the Shadow.” — **conditions:** reached stage 35 of [Flows through the veins](../quests/loneford.md#stage-35) → **stage 42**. NPC: “I am glad to hear that, but then again, I had a feeling all along that you would say that.”

???+ note "Stage 45: 1 route"

    1. Talk to [Buceth](../monsters/buceth.md) → choose “Do you know where he went after he left Loneford?” — **conditions:** reached stage 45 of [Flows through the veins](../quests/loneford.md#stage-45) → **stage 45**. NPC: “Apparently, the boy they sent was successful in his mission. The task that I did was also successful, if I may say so…”

???+ note "Stage 50: 1 route"

    1. Talk to [Buceth](../monsters/buceth.md) → the conversation leads here automatically — **conditions:** reached stage 50 of [Flows through the veins](../quests/loneford.md#stage-50) → **stage 50**. NPC: “Infidel, you will not defeat me! For the Shadow!”

???+ note "Stage 54: 1 route"

    1. Talk to [Kuldan](../monsters/kuldan.md) ([loneford3](../maps/loneford3.md)) → the conversation leads here automatically — **conditions:** reached stage 54 of [Flows through the veins](../quests/loneford.md#stage-54) → **stage 54**. NPC: “What is this? This smells like Narwood poison. You say you retrieved this from Buceth?”

???+ note "Stage 55: 1 route"

    1. Talk to [Kuldan](../monsters/kuldan.md) ([loneford3](../maps/loneford3.md)) → choose “He is already dead.” — **conditions:** reached stage 54 of [Flows through the veins](../quests/loneford.md#stage-54) → **stage 55**. NPC: “For the glory of Feygard, the people of Loneford may live on thanks to your help.”

???+ note "Stage 60: 2 routes"

    1. Talk to [Buceth](../monsters/buceth.md) → choose “Absolutely. Walk with the Shadow.” — **conditions:** reached stage 45 of [Flows through the veins](../quests/loneford.md#stage-45) → **stage 60**. NPC: “Thank you, my friend.”
    2. Talk to [Buceth](../monsters/buceth.md) → the conversation leads here automatically — **conditions:** reached stage 60 of [Flows through the veins](../quests/loneford.md#stage-60) → **stage 60**. NPC: “If you want to learn more about the Shadow, please visit the chapel custodian in Nor City. Tell them I sent you, and…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line changed<br>· text: “Also, isn't it strange how Buceth has not gotten ill, while all the o…” → “Also, isn't it strange how Buceth has not gotten ill, while all the o…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=loneford.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=loneford.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=loneford.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=loneford.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=loneford.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `loneford` |
    | showInLog | 1 |
    | Stage IDs | 10, 11, 21, 22, 23, 24, 25, 30, 31, 35, 41, 42, 45, 50, 54, 55, 60 |
    | Dialogue nodes setting stages | 10: `cr_loneford_st_6`, 10: `loneford_farmer_il_6`, 11: `cr_loneford_st_7`, 11: `loneford_farmer_il_7`, 21: `cr_loneford_st_10`, 22: `rolwynn_5`, 23: `talion_5`, 24: `taevinn_5`, 25: `loneford_ill_c_5`, 30: `landa_11`, 31: `landa_16`, 35: `landa_17`, 41: `buceth_gold_yes`, 42: `buceth_27`, 45: `buceth_story_9`, 50: `buceth_fight_1`, 54: `kuldan_bc_1`, 55: `kuldan_bc_10`, 60: `buceth_story_14`, 60: `buceth_story_15` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
