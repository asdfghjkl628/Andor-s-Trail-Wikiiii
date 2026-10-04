# The agent and the beast

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `bwm_agent` |
| **In journal** | Yes |
| **Stages** | 25 (completes at 240, 250, 251) |
| **Started by** | [Agent](../monsters/agent1.md) ([blackwater_mountain5](../maps/blackwater_mountain5.md)) |
| **NPCs involved** | [Agent](../monsters/agent1.md), [Agent](../monsters/agent4.md), [Agent](../monsters/agent6.md), [Agent](../monsters/agent2.md), [Agent](../monsters/agent5.md), [Agent](../monsters/agent3.md) +2 |
| **Locations** | [blackwater_mountain14](../maps/blackwater_mountain14.md), [blackwater_mountain17](../maps/blackwater_mountain17.md), [blackwater_mountain29](../maps/blackwater_mountain29.md), [blackwater_mountain30](../maps/blackwater_mountain30.md) |
| **Total XP** | 8,250 |
| **Related quests** | 4 |

</div>

## Overview

> I met a man seeking help for his settlement, the 'Blackwater mountain'. Supposedly, his settlement is being attacked by monsters and bandits, and they need help from the outside.

## Prerequisites to start

None: talk to [Agent](../monsters/agent1.md) ([blackwater_mountain5](../maps/blackwater_mountain5.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Clouded intent](prim_hunt.md#stage-25) | stage 25 reached, for stage 25 here |
| Requires | [Clouded intent](prim_hunt.md#stage-50) | stage 50 reached, for stage 251 here |
| Requires | [Clouded intent](prim_hunt.md#stage-100) | stage 100 reached, for stage 250 here |
| Requires | [Clouded intent](prim_hunt.md#stage-251) | stage 251 reached, for stage 80 here |
| Unlocks | [Search for Andor](andor.md#stage-110) | stage 110 there needs stage 60 here |
| Unlocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-16) | stage 16 there needs stage 240 here |
| Unlocks | [Clouded intent](prim_hunt.md#stage-30) | stage 30 there needs stage 251 here |
| Unlocks | [Clouded intent](prim_hunt.md#stage-250) | stage 250 there needs stage 150 here |
| Unlocks | [Clouded intent](prim_hunt.md#stage-251) | stage 251 there needs stage 95 here |
| Unlocks | [A difference of opinion](sisterfight.md#stage-50) | stage 50 there needs stage 240 here |
| Unlocks | [A difference of opinion](sisterfight.md#stage-51) | stage 51 there needs stage 240 here |
| Unlocks | [A difference of opinion](sisterfight.md#stage-55) | stage 55 there needs stage 240 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | I met a man seeking help for his settlement, the 'Blackwater mountain'. Supposedly, his settlement is being attacked by monsters and bandits, and they need help from the outside. | [Agent](../monsters/agent1.md) ([blackwater_mountain5](../maps/blackwater_mountain5.md)) | – | – |
| <span id="stage-5"></span>5 | I have agreed to help the man and Blackwater mountain in dealing with the problem. | [Agent](../monsters/agent1.md) ([blackwater_mountain5](../maps/blackwater_mountain5.md)) | – | – |
| <span id="stage-10"></span>10 | The man told me to meet him on the other side of the collapsed mine. He will crawl through the mine shaft and I will descend into the pitch-black abandoned mine.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Blackwater mountain5](../maps/blackwater_mountain5.md).</span> | [Agent](../monsters/agent1.md) ([blackwater_mountain5](../maps/blackwater_mountain5.md)) | – | removes monsters from blackwater_mountain5 |
| <span id="stage-20"></span>20 | I have navigated through the pitch-black abandoned mine, and met the man on the other side. He seemed very anxious about telling me to head straight to the east once I exit the mine. I should meet the man at the bottom of the mountain to the east. | [Agent](../monsters/agent2.md) ([blackwater_mountain9](../maps/blackwater_mountain9.md)) | – | – |
| <span id="stage-25"></span>25 | I heard a story about Prim and the Blackwater mountain settlement fighting against each other. | [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) | – | – |
| <span id="stage-30"></span>30 | I should follow the mountain path up the mountain to the Blackwater mountain settlement. | [Agent](../monsters/agent3.md) ([blackwater_mountain14](../maps/blackwater_mountain14.md)) | – | – |
| <span id="stage-40"></span>40 | I met the man again on my way up to Blackwater mountain. I should proceed further up the mountain. | [Agent](../monsters/agent4.md) ([blackwater_mountain17](../maps/blackwater_mountain17.md)) | – | – |
| <span id="stage-50"></span>50 | I have made it up to the snow-filled parts of the Blackwater mountain. The man told me to proceed further up the mountain. Apparently, the Blackwater mountain settlement is close by. | [Agent](../monsters/agent5.md) ([blackwater_mountain30](../maps/blackwater_mountain30.md)) | – | – |
| <span id="stage-60"></span>60 | I have reached the Blackwater mountain settlement. I should find and talk to their battle master, Harlenn.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Blackwater mountain38](../maps/blackwater_mountain38.md).</span> | [Agent](../monsters/agent6.md) ([blackwater_mountain38](../maps/blackwater_mountain38.md)) | – | – |
| <span id="stage-65"></span>65 | I have spoken to Harlenn in the Blackwater mountain settlement. Apparently, the settlement is under attack by a number of monsters, the aulaeth and white wyrms. On top of that, they are being attacked by the people of Prim. | [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) | – | – |
| <span id="stage-66"></span>66 | Harlenn thinks the people of Prim are behind the monster attacks somehow. | [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) | stage 65 | – |
| <span id="stage-70"></span>70 | Harlenn wants me to give a message to Guthbered of Prim. Either the people of Prim stop their attacks on the Blackwater mountain settlement, or they will have to be dealt with themselves. I should go talk to Guthbered in Prim. | [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) | – | – |
| <span id="stage-80"></span>80 | Guthbered denies that the people of Prim have anything to do with the monster attacks on the Blackwater mountain settlement. I should go talk to Harlenn. | [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) | stage 70 | – |
| <span id="stage-90"></span>90 | Harlenn is sure that the people of Prim are behind the attacks somehow. | [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) | stage 70, stage 80 | – |
| <span id="stage-95"></span>95 | Harlenn wants me to go to Prim and look for signs that they are preparing for an attack on the settlement. I should go look for clues around where Guthbered stays. | [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) | – | – |
| <span id="stage-100"></span>100 | I have found some plans in Prim about recruiting mercenaries and attacking the Blackwater mountain settlement. I should go talk to Harlenn immediately. | reading a sign on [blackwater_mountain29](../maps/blackwater_mountain29.md) | stage 95 | – |
| <span id="stage-110"></span>110 | Harlenn thanked me for investigating the attack plans. | [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) | stage 100, stage 95 | 1,150 XP |
| <span id="stage-120"></span>120 | To make the attacks on the Blackwater mountain settlement stop, Harlenn wants me to assassinate Guthbered in Prim. | [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) | – | – |
| <span id="stage-130"></span>130 | I have started a fight with Guthbered. | [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) | – | faction “fct_prim” set to -10 |
| <span id="stage-131"></span>131 | I told Guthbered that I was sent to kill him, but I let him live. He thanked me deeply, and left Prim. | [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) | – | 2,100 XP |
| <span id="stage-149"></span>149 | I have told Harlenn that Guthbered is gone. | [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) | hand over 1× [Guthbered's ring](../items/guthbered_id.md), stage 120 | – |
| <span id="stage-150"></span>150 | Harlenn thanked me for the help I have provided. Hopefully, the attacks on the Blackwater mountain settlement should stop now. | [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) | stage 149 | 5,000 XP<br>gives [Sword of Shadow's rage](../items/clouded_rage.md), [Gold coins](../items/gold.md), [Regular potion of health](../items/health.md) |
| <span id="stage-240"></span>240 | I am now trusted in the Blackwater mountain settlement, and all services should be available for me to use. **(completes quest)** | [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) | stage 150 | – |
| <span id="stage-250"></span>250 | I have decided to not help the people of the Blackwater mountain settlement. **(completes quest)** | [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md))<br>[Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) | stage 70 | – |
| <span id="stage-251"></span>251 | Since I am helping Prim, Harlenn no longer wants to talk to me. **(completes quest)** | [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) | – | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 1: 1 route"

    1. Talk to [Agent](../monsters/agent1.md) ([blackwater_mountain5](../maps/blackwater_mountain5.md)) → choose “What is the matter?” → **stage 1**. NPC: “The people of my settlement, the Blackwater mountain, are slowly being reduced in numbers by the monsters and the…”

???+ note "Stage 5: 1 route"

    1. Talk to [Agent](../monsters/agent1.md) ([blackwater_mountain5](../maps/blackwater_mountain5.md)) → choose “I guess I could help, I have killed a few monsters here and there.” → **stage 5**. NPC: “Excellent. The Blackwater mountain settlement is some distance away. Frankly, I am amazed that I made it this far alive.”

???+ note "Stage 10: 1 route"

    1. Talk to [Agent](../monsters/agent1.md) ([blackwater_mountain5](../maps/blackwater_mountain5.md)) → choose “OK, I'll go through the pitch-black mine.” → **stage 10**; also removes monsters from blackwater_mountain5. NPC: “Let's meet at the other side of this mine shaft.”

???+ note "Stage 20: 1 route"

    1. Talk to [Agent](../monsters/agent2.md) ([blackwater_mountain9](../maps/blackwater_mountain9.md)) → the conversation leads here automatically — **conditions:** reached stage 20 of [The agent and the beast](../quests/bwm_agent.md#stage-20) → **stage 20**. NPC: “I'll wait for you by the steps up to the mountain pass. See you there! Remember, go east once you exit the mine.”

???+ note "Stage 25: 1 route"

    1. Talk to [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → choose “Any ideas where they might be coming from?” — **conditions:** reached stage 25 of [Clouded intent](../quests/prim_hunt.md#stage-25) → **stage 25**. NPC: “We used to trade with them up there, but that all changed once they got greedy.”

???+ note "Stage 30: 1 route"

    1. Talk to [Agent](../monsters/agent3.md) ([blackwater_mountain14](../maps/blackwater_mountain14.md)) → the conversation leads here automatically — **conditions:** reached stage 30 of [The agent and the beast](../quests/bwm_agent.md#stage-30) → **stage 30**. NPC: “Beware of the nasty monsters, they can really cause some harm!”

???+ note "Stage 40: 1 route"

    1. Talk to [Agent](../monsters/agent4.md) ([blackwater_mountain17](../maps/blackwater_mountain17.md)) → the conversation leads here automatically — **conditions:** reached stage 40 of [The agent and the beast](../quests/bwm_agent.md#stage-40) → **stage 40**. NPC: “Meet me further up the mountain, and we will talk more.”

???+ note "Stage 50: 1 route"

    1. Talk to [Agent](../monsters/agent5.md) ([blackwater_mountain30](../maps/blackwater_mountain30.md)) → the conversation leads here automatically — **conditions:** reached stage 50 of [The agent and the beast](../quests/bwm_agent.md#stage-50) → **stage 50**. NPC: “Now hurry. We are almost there. Follow the snowy path to the north, and you should reach the settlement in no time.”

???+ note "Stage 60: 1 route"

    1. Talk to [Agent](../monsters/agent6.md) ([blackwater_mountain38](../maps/blackwater_mountain38.md)) → choose “Are we there yet?” → **stage 60**. NPC: “You should go down these stairs and talk to our battle master, Harlenn. He can usually be found at the third level down.”

???+ note "Stage 65: 1 route"

    1. Talk to [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) → choose “Those? They were no match for me.” — **conditions:** reached stage 65 of [The agent and the beast](../quests/bwm_agent.md#stage-65) → **stage 65**. NPC: “On top of that, we are being attacked by raids from those bastards down in that low-life town of Prim at the base of…”

???+ note "Stage 66: 1 route"

    1. Talk to [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) → choose “What have they done?” — **conditions:** reached stage 65 of [The agent and the beast](../quests/bwm_agent.md#stage-65) → **stage 66**. NPC: “We are almost certain they are the ones behind these monsters also.”

???+ note "Stage 70: 1 route"

    1. Talk to [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) → choose “No, not yet.” — **conditions:** reached stage 70 of [The agent and the beast](../quests/bwm_agent.md#stage-70) → **stage 70**. NPC: “Good. Now hurry! We don't know how much time we have left before they attack again.”

???+ note "Stage 80: 1 route"

    1. Talk to [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → choose “Harlenn in the Blackwater mountain settlement wants you to stop your attacks on their settlement.” — **conditions:** reached stage 251 of [Clouded intent](../quests/prim_hunt.md#stage-251); reached stage 70 of [The agent and the beast](../quests/bwm_agent.md#stage-70) → **stage 80**. NPC: “That's completely insane. We!? Stop OUR attacks?! You tell him that we have nothing to do with what happens up there.…”

???+ note "Stage 90: 1 route"

    1. Talk to [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) → choose “Yes, I talked to him. He denies that they are behind any of the attacks.” — **conditions:** reached stage 70 of [The agent and the beast](../quests/bwm_agent.md#stage-70); reached stage 80 of [The agent and the beast](../quests/bwm_agent.md#stage-80) → **stage 90**. NPC: “Besides, they have always been treacherous. No, of course they are behind the attacks.”

???+ note "Stage 95: 1 route"

    1. Talk to [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) → choose “Sure, sounds easy.” — **conditions:** reached stage 95 of [The agent and the beast](../quests/bwm_agent.md#stage-95) → **stage 95**. NPC: “Good. Try not to be seen. You should go look for any clues around where that deceiving Guthbered stays.”

???+ note "Stage 100: 1 route"

    1. reading a sign on [blackwater_mountain29](../maps/blackwater_mountain29.md) → the conversation leads here automatically — **conditions:** reached stage 95 of [The agent and the beast](../quests/bwm_agent.md#stage-95) → **stage 100**. NPC: “Among the papers, you find plans for recruiting mercenaries for Prim and training fighters for a larger attack on the…”

???+ note "Stage 110: 1 route"

    1. Talk to [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) → choose “Yes. I found plans that they are recruiting mercenaries and will attack your settlement.” — **conditions:** reached stage 95 of [The agent and the beast](../quests/bwm_agent.md#stage-95); reached stage 100 of [The agent and the beast](../quests/bwm_agent.md#stage-100) → **stage 110**. NPC: “Anyway, thank you for your help in finding this evidence.”

???+ note "Stage 120: 2 routes"

    1. Talk to [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) → choose “Not yet, but I am working on it.” — **conditions:** reached stage 120 of [The agent and the beast](../quests/bwm_agent.md#stage-120) → **stage 120**. NPC: “Excellent. Return to me once the deed is done.”
    2. Talk to [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) → choose “I will remove him, but I will try to find a peaceful solution to this.” — **conditions:** reached stage 120 of [The agent and the beast](../quests/bwm_agent.md#stage-120) → **stage 120**. NPC: “Fine. Do whatever you need to remove him, but I don't want to deal with their attacks anymore.”

???+ note "Stage 130: 1 route"

    1. Talk to [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → the conversation leads here automatically — **conditions:** reached stage 130 of [The agent and the beast](../quests/bwm_agent.md#stage-130) → **stage 130**; also faction “fct_prim” set to -10. NPC: “I had hoped it would not come to this. I'm afraid that you will not survive this encounter. Yet another life on my…”

???+ note "Stage 131: 1 route"

    1. Talk to [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → the conversation leads here automatically — **conditions:** reached stage 131 of [The agent and the beast](../quests/bwm_agent.md#stage-131) → **stage 131**. NPC: “Thank you friend, for talking some sense into me.”

???+ note "Stage 149: 1 route"

    1. Talk to [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) → choose “Yes, he is dead.” — **conditions:** reached stage 120 of [The agent and the beast](../quests/bwm_agent.md#stage-120); hand over 1× [Guthbered's ring](../items/guthbered_id.md) → **stage 149**. NPC: “Ha ha! He is finally gone! Now we can rest comfortably in our settlement.”

???+ note "Stage 150: 1 route"

    1. Talk to [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) → the conversation leads here automatically — **conditions:** reached stage 149 of [The agent and the beast](../quests/bwm_agent.md#stage-149) → **stage 150**; also gives [Sword of Shadow's rage](../items/clouded_rage.md), [Gold coins](../items/gold.md), [Regular potion of health](../items/health.md). NPC: “Thank you friend. Here, have these items as a token of our appreciation for your help.”

???+ note "Stage 240: 1 route"

    1. Talk to [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) → the conversation leads here automatically — **conditions:** reached stage 150 of [The agent and the beast](../quests/bwm_agent.md#stage-150) → **stage 240**. NPC: “Thank you, friend. Your help is greatly appreciated. Everyone in the Blackwater mountain settlement will want to talk…”

???+ note "Stage 250: 2 routes"

    1. Talk to [Guthbered](../monsters/guthbered.md) ([blackwater_mountain29](../maps/blackwater_mountain29.md)) → the conversation leads here automatically — **conditions:** reached stage 100 of [Clouded intent](../quests/prim_hunt.md#stage-100) → **stage 250**. NPC: “Thank you again for your help.”
    2. Talk to [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) → choose “No. In fact, I think I should help the people of Prim instead.” — **conditions:** reached stage 70 of [The agent and the beast](../quests/bwm_agent.md#stage-70) → **stage 250**. NPC: “Bah. Then you are useless to me. Why did you even bother to come up here and waste my time? Begone.”

???+ note "Stage 251: 1 route"

    1. Talk to [Harlenn](../monsters/harlenn.md) ([blackwater_mountain45](../maps/blackwater_mountain45.md)) → the conversation leads here automatically — **conditions:** reached stage 50 of [Clouded intent](../quests/prim_hunt.md#stage-50) → **stage 251**. NPC: “Of course we can't have that here. We can't have a spy in our midst. You should leave our settlement while you still…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | stage 1 journal text changed; stage 5 journal text changed; stage 25 journal text changed; stage 30 journal text changed; stage 40 journal text changed; stage 50 journal text changed (+8 more)<br>Dialogue: 11 lines changed<br>· text: “Excellent. The Blackwater settlement is some distance away. Frankly, …” → “Excellent. The Blackwater mountain settlement is some distance away. …”<br>· text: “I had hoped it would not come to this. You will not survive this enco…” → “I had hoped it would not come to this. I'm afraid that you will not s…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bwm_agent.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bwm_agent.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bwm_agent.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bwm_agent.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=bwm_agent.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `bwm_agent` |
    | showInLog | 1 |
    | Stage IDs | 1, 5, 10, 20, 25, 30, 40, 50, 60, 65, 66, 70, 80, 90, 95, 100, 110, 120, 130, 131, 149, 150, 240, 250, 251 |
    | Dialogue nodes setting stages | 1: `bwm_agent_1_4`, 5: `bwm_agent_1_7`, 10: `bwm_agent_1_14`, 20: `bwm_agent_2_7`, 25: `guthbered_22`, 30: `bwm_agent_3_4`, 40: `bwm_agent_4_5`, 50: `bwm_agent_5_6`, 60: `bwm_agent_6_4`, 65: `harlenn_14`, 66: `harlenn_17`, 70: `harlenn_22`, 80: `guthbered_attacks_1`, 90: `harlenn_talkedto_guth_3`, 95: `harlenn_talkedto_guth_11`, 100: `sign_blackwater29_qstarted_1`, 110: `harlenn_lookforsigns_5`, 120: `harlenn_lookforsigns_11`, 120: `harlenn_lookforsigns_12`, 130: `guthbered_sentbybwm_fight`, 131: `guthbered_sentbybwm_leave`, 149: `harlenn_killguth_2`, 150: `harlenn_killguth_4`, 240: `harlenn_completed`, 250: `guthbered_completed_2`, 250: `harlenn_prim_7`, 251: `harlenn_workingforprim_2` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
