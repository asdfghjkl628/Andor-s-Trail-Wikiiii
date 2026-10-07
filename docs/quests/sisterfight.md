---
description: "A difference of opinion is a quest in Andor's Trail, started by Ingus (remgard0). 15 stages, 24,000 XP in total. I heard a story about two squabbling sisters in Remgard, Elwel and Elwyl. Apparently they have kept people awake at night with the way they are shouting at each other. I should go visi…"
---

# A difference of opinion

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `sisterfight` |
| **In journal** | Yes |
| **Stages** | 15 (completes at 71) |
| **Started by** | [Ingus](../monsters/ingus.md) ([remgard0](../maps/remgard0.md)) |
| **NPCs involved** | [Elwel](../monsters/elwel.md), [Elwyl](../monsters/elwyl.md), [Hjaldar](../monsters/hjaldar.md), [Ingus](../monsters/ingus.md), [Mazeg](../monsters/mazeg.md) |
| **Locations** | [blackwater_mountain43](../maps/blackwater_mountain43.md), [remgard0](../maps/remgard0.md), [remgard_villager1](../maps/remgard_villager1.md), [remgard_villager5](../maps/remgard_villager5.md) |
| **Total XP** | 24,000 |
| **Related quests** | 2 |

</div>

## Overview

> I heard a story about two squabbling sisters in Remgard, Elwel and Elwyl. Apparently they have kept people awake at night with the way they are shouting at each other. I should go visit them in their house on the southern shore of the city of Remgard.

## Prerequisites to start

Start with [Ingus](../monsters/ingus.md) ([remgard0](../maps/remgard0.md)). Required:

- reached stage 10 of [A difference of opinion](../quests/sisterfight.md#stage-10)
- reached stage 45 of [What is that stench?](../quests/remgard2.md#stage-45)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [The agent and the beast](bwm_agent.md#stage-240) | stage 240 reached, for stages 50, 51, 55 here |
| Requires | [What is that stench?](remgard2.md#stage-45) | stage 45 reached, for stage 10 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I heard a story about two squabbling sisters in Remgard, Elwel and Elwyl. Apparently they have kept people awake at night with the way they are shouting at each other. I should go visit them in their house on the southern shore of the city of Remgard. | [Ingus](../monsters/ingus.md) ([remgard0](../maps/remgard0.md)) | – | – |
| <span id="stage-20"></span>20 | I have talked to Elwyl, one of the Elwille sisters in Remgard. She is furious at her sister for not agreeing on even the most simple of facts. Apparently, they have had their disagreements with each other for several years. | [Elwyl](../monsters/elwyl.md) ([remgard_villager5](../maps/remgard_villager5.md)) | stage 10, stage 31 | – |
| <span id="stage-21"></span>21 | Elwel will not speak to me. | [Elwel](../monsters/elwel.md) ([remgard_villager5](../maps/remgard_villager5.md)) | stage 20, stage 71 | – |
| <span id="stage-30"></span>30 | One matter that the sisters disagree on currently is the color of a certain potion that the town potion-maker Hjaldar used to make. Elwyl says that the potion of accuracy focus that Hjaldar used to make was a blue potion, but Elwel insists that the potion was a green substance. | [Elwyl](../monsters/elwyl.md) ([remgard_villager5](../maps/remgard_villager5.md)) | stage 20 | – |
| <span id="stage-31"></span>31 | Elwyl wants me to get a potion of accuracy focus from Hjaldar here in Remgard so that she can finally prove to Elwel that she is wrong. | [Elwyl](../monsters/elwyl.md) ([remgard_villager5](../maps/remgard_villager5.md)) | stage 20 | – |
| <span id="stage-40"></span>40 | I have talked to Hjaldar in Remgard. Hjaldar no longer makes potions since his supply of Lyson marrow extract has gone dry. | [Hjaldar](../monsters/hjaldar.md) ([remgard_villager1](../maps/remgard_villager1.md)) | – | – |
| <span id="stage-41"></span>41 | Apparently, Hjaldar's old friend Mazeg would surely have some Lyson marrow extract to sell. Unfortunately, he does not know where Mazeg currently lives. He only knows that Mazeg traveled far to the west last time they met. | [Hjaldar](../monsters/hjaldar.md) ([remgard_villager1](../maps/remgard_villager1.md)) | stage 45 | – |
| <span id="stage-45"></span>45 | I should find Mazeg and get some Lyson marrow extract so that Hjaldar can start making potions again. | [Hjaldar](../monsters/hjaldar.md) ([remgard_villager1](../maps/remgard_villager1.md)) | – | – |
| <span id="stage-50"></span>50 | I have talked to Mazeg in the Blackwater mountain settlement. Since I helped the people of the Blackwater mountain before, he is willing to sell me a vial of Lyson marrow extract for only 400 gold. | [Mazeg](../monsters/mazeg.md) ([blackwater_mountain43](../maps/blackwater_mountain43.md)) | stage 45, stage 51 | – |
| <span id="stage-51"></span>51 | I have talked to Mazeg in the Blackwater mountain settlement. He is willing to sell me Lyson marrow extract for 800 gold. | [Mazeg](../monsters/mazeg.md) ([blackwater_mountain43](../maps/blackwater_mountain43.md)) | stage 45 | – |
| <span id="stage-55"></span>55 | I have bought some Lyson marrow extract from Mazeg. I should return to Remgard and give it to Hjaldar.<br><span class="qnote">⚡ A scripted event can now trigger on [Mountainlake13a](../maps/mountainlake13a.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Mountainlake8](../maps/mountainlake8.md).</span> | [Mazeg](../monsters/mazeg.md) ([blackwater_mountain43](../maps/blackwater_mountain43.md)) | pay 400 gold, stage 45, stage 51 | gives [Vial of Lyson marrow extract](../items/lyson_marrow.md) |
| <span id="stage-60"></span>60 | Hjaldar thanked me for bringing him the marrow extract.<br><span class="qnote">⚡ A scripted event can now trigger on [Mountainlake13a](../maps/mountainlake13a.md).</span><br><span class="qnote">⚡ A scripted event can now trigger on [Mountainlake8](../maps/mountainlake8.md).</span> | [Hjaldar](../monsters/hjaldar.md) ([remgard_villager1](../maps/remgard_villager1.md)) | hand over 1× [Vial of Lyson marrow extract](../items/lyson_marrow.md), stage 45 | 15,000 XP |
| <span id="stage-61"></span>61 | Hjaldar can now create potions again, and is willing to trade with me. He even gave me some of the first potions that he made. I should go visit the Elwille sisters here in Remgard again, and show them a potion of accuracy focus. | [Hjaldar](../monsters/hjaldar.md) ([remgard_villager1](../maps/remgard_villager1.md)) | stage 60 | gives [Potion of damage focus](../items/pot_focus_dmg.md), [Potion of accuracy focus](../items/pot_focus_ac.md) |
| <span id="stage-70"></span>70 | I have given a potion of accuracy focus to Elwyl. | [Elwyl](../monsters/elwyl.md) ([remgard_villager5](../maps/remgard_villager5.md)) | hand over 1× [Potion of accuracy focus](../items/pot_focus_ac.md), stage 31 | – |
| <span id="stage-71"></span>71 | Unfortunately, it did not cause their squabbling to diminish. On the contrary, they seem to be even more angry at each other now, since both of them had the color wrong. **(completes quest)** | [Elwyl](../monsters/elwyl.md) ([remgard_villager5](../maps/remgard_villager5.md)) | – | 9,000 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Ingus](../monsters/ingus.md) ([remgard0](../maps/remgard0.md)) → choose “What are they fighting about?” — **conditions:** reached stage 10 of [A difference of opinion](../quests/sisterfight.md#stage-10); reached stage 45 of [What is that stench?](../quests/remgard2.md#stage-45) → **stage 10**. NPC: “They live in one of the cabins on the southern shore. [Ingus points to the south]”

???+ note "Stage 20: 1 route"

    1. Talk to [Elwyl](../monsters/elwyl.md) ([remgard_villager5](../maps/remgard_villager5.md)) → choose “Some people have been complaining that your squabbling has kept them awake at night.” — **conditions:** reached stage 31 of [A difference of opinion](../quests/sisterfight.md#stage-31); reached stage 10 of [A difference of opinion](../quests/sisterfight.md#stage-10) → **stage 20**. NPC: “She doesn't stop either. I can't remember for how long this has been going on, it almost feels like forever.”

???+ note "Stage 21: 2 routes"

    1. Talk to [Elwel](../monsters/elwel.md) ([remgard_villager5](../maps/remgard_villager5.md)) → the conversation leads here automatically — **conditions:** reached stage 20 of [A difference of opinion](../quests/sisterfight.md#stage-20) → **stage 21**. NPC: “I saw you talking to that cursed sister of mine. Don't listen to her, she always tries her best to portray me in the…”
    2. Talk to [Elwel](../monsters/elwel.md) ([remgard_villager5](../maps/remgard_villager5.md)) → the conversation leads here automatically — **conditions:** reached stage 71 of [A difference of opinion](../quests/sisterfight.md#stage-71) → **stage 21**. NPC: “Now look what you did!”

???+ note "Stage 30: 1 route"

    1. Talk to [Elwyl](../monsters/elwyl.md) ([remgard_villager5](../maps/remgard_villager5.md)) → the conversation leads here automatically — **conditions:** reached stage 20 of [A difference of opinion](../quests/sisterfight.md#stage-20) → **stage 30**. NPC: “I can't understand why she would make such a big deal out of it, when the potion was clearly blue. I remember it…”

???+ note "Stage 31: 1 route"

    1. Talk to [Elwyl](../monsters/elwyl.md) ([remgard_villager5](../maps/remgard_villager5.md)) → choose “I'll return with one of those potions.” — **conditions:** reached stage 20 of [A difference of opinion](../quests/sisterfight.md#stage-20) → **stage 31**. NPC: “Good. Maybe when you bring that potion, she will agree to being wrong for once!”

???+ note "Stage 40: 1 route"

    1. Talk to [Hjaldar](../monsters/hjaldar.md) ([remgard_villager1](../maps/remgard_villager1.md)) → the conversation leads here automatically — **conditions:** reached stage 40 of [A difference of opinion](../quests/sisterfight.md#stage-40) → **stage 40**. NPC: “My supply of Lyson marrow extract has gone dry. Without some of that, I can't make potions that are useful for…”

???+ note "Stage 41: 1 route"

    1. Talk to [Hjaldar](../monsters/hjaldar.md) ([remgard_villager1](../maps/remgard_villager1.md)) → choose “Any ideas on where I might find Mazeg?” — **conditions:** reached stage 45 of [A difference of opinion](../quests/sisterfight.md#stage-45) → **stage 41**. NPC: “He even had gear for travelling through colder climates - snow and ice and that sort of thing.”

???+ note "Stage 45: 1 route"

    1. Talk to [Hjaldar](../monsters/hjaldar.md) ([remgard_villager1](../maps/remgard_villager1.md)) → choose “Thanks for the info. I will try to find him.” — **conditions:** reached stage 45 of [A difference of opinion](../quests/sisterfight.md#stage-45) → **stage 45**. NPC: “Good luck finding him. If you do find him, which I doubt you do, please say hello to him from me, and tell him that I…”

???+ note "Stage 50: 1 route"

    1. Talk to [Mazeg](../monsters/mazeg.md) ([blackwater_mountain43](../maps/blackwater_mountain43.md)) → choose “I am looking for some Lyson marrow extract, for Hjaldar in Remgard.” — **conditions:** reached stage 240 of [The agent and the beast](../quests/bwm_agent.md#stage-240); reached stage 45 of [A difference of opinion](../quests/sisterfight.md#stage-45); reached stage 51 of [A difference of opinion](../quests/sisterfight.md#stage-51) → **stage 50**. NPC: “Since you helped us up here in the Blackwater mountain settlement earlier, I am willing to give you a discount on the…”

???+ note "Stage 51: 1 route"

    1. Talk to [Mazeg](../monsters/mazeg.md) ([blackwater_mountain43](../maps/blackwater_mountain43.md)) → choose “I am looking for some Lyson marrow extract, for Hjaldar in Remgard.” — **conditions:** reached stage 240 of [The agent and the beast](../quests/bwm_agent.md#stage-240); reached stage 45 of [A difference of opinion](../quests/sisterfight.md#stage-45); reached stage 51 of [A difference of opinion](../quests/sisterfight.md#stage-51) → **stage 51**. NPC: “For 800 gold, I am willing to sell you some of it for my old friend Hjaldar.”

???+ note "Stage 55: 1 route"

    1. Talk to [Mazeg](../monsters/mazeg.md) ([blackwater_mountain43](../maps/blackwater_mountain43.md)) → choose “Here is 400 gold.” — **conditions:** reached stage 240 of [The agent and the beast](../quests/bwm_agent.md#stage-240); reached stage 45 of [A difference of opinion](../quests/sisterfight.md#stage-45); reached stage 51 of [A difference of opinion](../quests/sisterfight.md#stage-51); pay 400 gold → **stage 55**; also gives [Vial of Lyson marrow extract](../items/lyson_marrow.md). NPC: “Thanks. Here's some of the Lyson marrow extract.”

???+ note "Stage 60: 1 route"

    1. Talk to [Hjaldar](../monsters/hjaldar.md) ([remgard_villager1](../maps/remgard_villager1.md)) → choose “Yes, I brought you some Lyson marrow extract.” — **conditions:** reached stage 45 of [A difference of opinion](../quests/sisterfight.md#stage-45); hand over 1× [Vial of Lyson marrow extract](../items/lyson_marrow.md) → **stage 60**. NPC: “Oh wow. Yes, this is indeed some of that marrow extract. Nice work finding it!”

???+ note "Stage 61: 1 route"

    1. Talk to [Hjaldar](../monsters/hjaldar.md) ([remgard_villager1](../maps/remgard_villager1.md)) → choose “He told me to send you his warmest greetings.” — **conditions:** reached stage 60 of [A difference of opinion](../quests/sisterfight.md#stage-60) → **stage 61**; also gives [Potion of damage focus](../items/pot_focus_dmg.md), [Potion of accuracy focus](../items/pot_focus_ac.md). NPC: “Ah, that should do it. Here you go. One potion of accuracy focus and one potion of damage focus. I hope they will be…”

???+ note "Stage 70: 1 route"

    1. Talk to [Elwyl](../monsters/elwyl.md) ([remgard_villager5](../maps/remgard_villager5.md)) → choose “I have one of those potions of accuracy focus for you.” — **conditions:** reached stage 31 of [A difference of opinion](../quests/sisterfight.md#stage-31); hand over 1× [Potion of accuracy focus](../items/pot_focus_ac.md) → **stage 70**. NPC: “Oh good. Give me that.”

???+ note "Stage 71: 1 route"

    1. Talk to [Elwyl](../monsters/elwyl.md) ([remgard_villager5](../maps/remgard_villager5.md)) → the conversation leads here automatically — **conditions:** reached stage 71 of [A difference of opinion](../quests/sisterfight.md#stage-71) → **stage 71**. NPC: “Hey Elwel, you were wrong all along! Why won't you ever admit it when you are clearly wrong?”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | renamed “A difference in opinion” → “A difference of opinion”; stage 30 journal text changed<br>Dialogue: 2 lines changed<br>· text: “Since you helped us up here in the Blackwater Mountain settlement ear…” → “Since you helped us up here in the Blackwater mountain settlement ear…”<br>· text: “They live in one of the cabins on the southern shore. *Ingus points t…” → “They live in one of the cabins on the southern shore. [Ingus points t…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sisterfight.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sisterfight.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sisterfight.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sisterfight.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=sisterfight.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `sisterfight` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 21, 30, 31, 40, 41, 45, 50, 51, 55, 60, 61, 70, 71 |
    | Dialogue nodes setting stages | 10: `ingus_t6`, 20: `elwyl_11`, 21: `elwel_3`, 21: `elwel_4`, 30: `elwyl_15`, 31: `elwyl_21`, 40: `hjaldar_7`, 41: `hjaldar_13`, 45: `hjaldar_14`, 50: `mazeg_e_7a`, 51: `mazeg_e_7b`, 55: `mazeg_e_9`, 60: `hjaldar_r2`, 61: `hjaldar_r15`, 70: `elwyl_res_1`, 71: `elwyl_res_7` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
