# Old friends?

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `kaverin` |
| **In journal** | Yes |
| **Stages** | 13 (completes at 21, 100) |
| **Started by** | [Kaverin](../monsters/kaverin.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) |
| **NPCs involved** | [Kaverin](../monsters/kaverin.md), [Unzel](../monsters/unzel.md), [Vacor](../monsters/vacor.md) |
| **Locations** | [fallhaven_sw](../maps/fallhaven_sw.md), [remgard_tavern1](../maps/remgard_tavern1.md), [wild6](../maps/wild6.md) |
| **Total XP** | 20,000 |
| **Related quests** | 1 |

</div>

## Overview

> I met Kaverin in Remgard, that apparently is an old acquaintance of Unzel, who lives outside of Fallhaven.

## Prerequisites to start

None: talk to [Kaverin](../monsters/kaverin.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Missing pieces](vacor.md#stage-60) | stage 60 reached, for stages 70, 75, 90 here |
| Requires | [Missing pieces](vacor.md#stage-61) | stage 61 reached, for stage 30 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I met Kaverin in Remgard, that apparently is an old acquaintance of Unzel, who lives outside of Fallhaven. | [Kaverin](../monsters/kaverin.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) | – | – |
| <span id="stage-20"></span>20 | Kaverin wants me to deliver a message to Unzel. | [Kaverin](../monsters/kaverin.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) | – | – |
| <span id="stage-21"></span>21 | I have declined to help Kaverin. **(completes quest)** | [Kaverin](../monsters/kaverin.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) | stage 20 | – |
| <span id="stage-22"></span>22 | I have agreed to deliver the message. | [Kaverin](../monsters/kaverin.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) | stage 20 | – |
| <span id="stage-25"></span>25 | Kaverin has given me the message that he wants me to deliver to Unzel. | [Kaverin](../monsters/kaverin.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) | stage 22 | gives [Kaverin's sealed message](../items/kaverin_message.md) |
| <span id="stage-30"></span>30 | I have delivered the message to Unzel. I should return to Kaverin in Remgard. | [Unzel](../monsters/unzel.md) ([wild6](../maps/wild6.md)) | carry 1× [Kaverin's sealed message](../items/kaverin_message.md), hand over 1× [Kaverin's sealed message](../items/kaverin_message.md), stage 25 | – |
| <span id="stage-40"></span>40 | Kaverin thanked me for delivering the message to Unzel. | [Kaverin](../monsters/kaverin.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) | – | 10,000 XP |
| <span id="stage-45"></span>45 | In return, Kaverin gave me an old map that he had acquired. Apparently, it leads to Vacor's old hideout. | [Kaverin](../monsters/kaverin.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) | stage 40 | gives [Map to Vacor's old hideout](../items/vacor_map.md) |
| <span id="stage-60"></span>60 | Kaverin was furious over the fact that I killed Unzel, and that I helped Vacor. He started attacking me. I should return to Vacor once Kaverin is dead. | [Kaverin](../monsters/kaverin.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) | – | – |
| <span id="stage-70"></span>70 | Kaverin was carrying a sealed message. Vacor immediately recognized the seal, and seemed very interested in it. | [Vacor](../monsters/vacor.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) | carry 1× [Kaverin's sealed message](../items/kaverin_message.md), stage 60 | – |
| <span id="stage-75"></span>75 | I have given Vacor the message that Kaverin was carrying. In return, Vacor gave me an old map, leading to his old hideout. | [Vacor](../monsters/vacor.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) | carry 1× [Kaverin's sealed message](../items/kaverin_message.md), hand over 1× [Kaverin's sealed message](../items/kaverin_message.md), stage 60 | 10,000 XP<br>gives [Map to Vacor's old hideout](../items/vacor_map.md) |
| <span id="stage-90"></span>90 | I should try to find Vacor's old hideout, on the road to the west of the former prison of Flagstone, southwest of Fallhaven.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Wild16](../maps/wild16.md).</span> | [Kaverin](../monsters/kaverin.md) ([remgard_tavern1](../maps/remgard_tavern1.md))<br>[Vacor](../monsters/vacor.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) | stage 45, stage 75 | – |
| <span id="stage-100"></span>100 | I have found Vacor's old hideout. **(completes quest)** | reading a sign on [wild16_cave](../maps/wild16_cave.md) | – | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path.*

???+ note "Stage 10: 1 route"

    1. Talk to [Kaverin](../monsters/kaverin.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) → choose “I'm from the village of Crossglen, far to the west of here.” → **stage 10**. NPC: “You wouldn't by any chance have met him, would you?”

???+ note "Stage 20: 1 route"

    1. Talk to [Kaverin](../monsters/kaverin.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) → the conversation leads here automatically — **conditions:** reached stage 20 of [Old friends?](../quests/kaverin.md#stage-20) → **stage 20**. NPC: “Would you be willing to deliver a message to him?”

???+ note "Stage 21: 1 route"

    1. Talk to [Kaverin](../monsters/kaverin.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) → choose “No, I am done helping you people.” — **conditions:** reached stage 20 of [Old friends?](../quests/kaverin.md#stage-20) → **stage 21**. NPC: “That is unfortunate, you seemed like such a bright boy too.”

???+ note "Stage 22: 1 route"

    1. Talk to [Kaverin](../monsters/kaverin.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) → choose “Anything for the sake of the Shadow.” — **conditions:** reached stage 20 of [Old friends?](../quests/kaverin.md#stage-20) → **stage 22**. NPC: “Good, that's exactly what I wanted to hear.”

???+ note "Stage 25: 1 route"

    1. Talk to [Kaverin](../monsters/kaverin.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) → the conversation leads here automatically — **conditions:** reached stage 22 of [Old friends?](../quests/kaverin.md#stage-22) → **stage 25**; also gives [Kaverin's sealed message](../items/kaverin_message.md). NPC: “[He gives you a sealed message]”

???+ note "Stage 30: 1 route"

    1. Talk to [Unzel](../monsters/unzel.md) ([wild6](../maps/wild6.md)) → choose “Here it is.” — **conditions:** reached stage 61 of [Missing pieces](../quests/vacor.md#stage-61); reached stage 25 of [Old friends?](../quests/kaverin.md#stage-25); carry 1× [Kaverin's sealed message](../items/kaverin_message.md); hand over 1× [Kaverin's sealed message](../items/kaverin_message.md) → **stage 30**. NPC: “Hmm, yes... Let's see... [Unzel opens the sealed message and reads it]”

???+ note "Stage 40: 1 route"

    1. Talk to [Kaverin](../monsters/kaverin.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) → the conversation leads here automatically — **conditions:** reached stage 40 of [Old friends?](../quests/kaverin.md#stage-40) → **stage 40**. NPC: “Thank you, my friend. May you walk in the glow of the Shadow.”

???+ note "Stage 45: 1 route"

    1. Talk to [Kaverin](../monsters/kaverin.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) → the conversation leads here automatically — **conditions:** reached stage 40 of [Old friends?](../quests/kaverin.md#stage-40) → **stage 45**; also gives [Map to Vacor's old hideout](../items/vacor_map.md). NPC: “Take this map as compensation for a job well done.”

???+ note "Stage 60: 1 route"

    1. Talk to [Kaverin](../monsters/kaverin.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) → the conversation leads here automatically — **conditions:** reached stage 60 of [Old friends?](../quests/kaverin.md#stage-60) → **stage 60**. NPC: “Oh yes, I can feel it. You work for Vacor! He must be stopped!”

???+ note "Stage 70: 1 route"

    1. Talk to [Vacor](../monsters/vacor.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) → the conversation leads here automatically — **conditions:** reached stage 60 of [Missing pieces](../quests/vacor.md#stage-60); reached stage 60 of [Old friends?](../quests/kaverin.md#stage-60); carry 1× [Kaverin's sealed message](../items/kaverin_message.md) → **stage 70**. NPC: “What's that in your hands?! ... I recognize that seal!”

???+ note "Stage 75: 1 route"

    1. Talk to [Vacor](../monsters/vacor.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) → choose “Here, have the message.” — **conditions:** reached stage 60 of [Missing pieces](../quests/vacor.md#stage-60); reached stage 60 of [Old friends?](../quests/kaverin.md#stage-60); carry 1× [Kaverin's sealed message](../items/kaverin_message.md); hand over 1× [Kaverin's sealed message](../items/kaverin_message.md) → **stage 75**; also gives [Map to Vacor's old hideout](../items/vacor_map.md). NPC: “Here, take this map as compensation for your troubles.”

???+ note "Stage 90: 2 routes"

    1. Talk to [Kaverin](../monsters/kaverin.md) ([remgard_tavern1](../maps/remgard_tavern1.md)) → the conversation leads here automatically — **conditions:** reached stage 45 of [Old friends?](../quests/kaverin.md#stage-45) → **stage 90**. NPC: “According to the map, the hideout should be just to the northwest of the former prison of Flagstone. Feel free to take…”
    2. Talk to [Vacor](../monsters/vacor.md) ([fallhaven_sw](../maps/fallhaven_sw.md)) → the conversation leads here automatically — **conditions:** reached stage 60 of [Missing pieces](../quests/vacor.md#stage-60); reached stage 75 of [Old friends?](../quests/kaverin.md#stage-75) → **stage 90**. NPC: “[The map shows a location to the northwest of the former prison of Flagstone]”

???+ note "Stage 100: 1 route"

    1. reading a sign on [wild16_cave](../maps/wild16_cave.md) → the conversation leads here automatically → **stage 100**. NPC: “You squeeze through the narrow opening of the cave. The stale air that hangs heavy within the damp cave, with its…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 4 lines changed<br>· text: “(The map shows a location to the northwest of the former prison of Fl…” → “[The map shows a location to the northwest of the former prison of Fl…”<br>· text: “Hmmm, yes... Let's see... (Unzel opens the sealed message and reads i…” → “Hmm, yes... Let's see... [Unzel opens the sealed message and reads it]” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=kaverin.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=kaverin.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=kaverin.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=kaverin.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=kaverin.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `kaverin` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 21, 22, 25, 30, 40, 45, 60, 70, 75, 90, 100 |
    | Dialogue nodes setting stages | 10: `kaverin_4`, 20: `kaverin_8`, 21: `kaverin_decline1`, 22: `kaverin_accept1`, 25: `kaverin_accept3`, 30: `unzel_msg2`, 40: `kaverin_done1`, 45: `kaverin_done2`, 60: `kaverin_fight_1`, 70: `vacor_msg1`, 75: `vacor_msg_8`, 90: `kaverin_done5`, 90: `vacor_msg_10`, 100: `sign_wild16_1` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
