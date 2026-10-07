---
description: "Destined for great things is a quest in Andor's Trail, started by Lethenlor (tradehouse1). 31 stages, 3,000 XP in total. I heard a rumor that some mining town in the Charwood forest, northwest of the Foaming Flask tavern, has had some troubles recently. I should try to find the Charwood cabin and…"
---

# Destined for great things

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `charwood1` |
| **In journal** | Yes |
| **Stages** | 31 (completes at 115) |
| **Started by** | [Lethenlor](../monsters/lethenlor.md) ([tradehouse1](../maps/tradehouse1.md)) |
| **NPCs involved** | [Charwood goblin](../monsters/charwdg4.md#v-charwdgg), [Drashad](../monsters/drashad.md), [Erethori](../monsters/erethori.md), [Falothen](../monsters/falothen0.md#v-falothen1), [Falothen](../monsters/falothen0.md), [Fayvara](../monsters/fayvara0.md) +6 |
| **Locations** | [minerhouse0](../maps/minerhouse0.md), [minerhouse7](../maps/minerhouse7.md), [tradehouse0](../maps/tradehouse0.md), [tradehouse0a](../maps/tradehouse0a.md) |
| **Total XP** | 3,000 |
| **Related quests** | 4 |

</div>

## Overview

> I heard a rumor that some mining town in the Charwood forest, northwest of the Foaming Flask tavern, has had some troubles recently. I should try to find the Charwood cabin and find out what has happened.

## Prerequisites to start

None: talk to [Lethenlor](../monsters/lethenlor.md) ([tradehouse1](../maps/tradehouse1.md)) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [brightport_nondisplay (hidden flag)](brightport_nondisplay.md#stage-233) | stage 233 there needs stage 115 here |
| Unlocks | [Trial by fire](charwood2.md#stage-10) | stage 10 there needs stage 50 here |
| Unlocks | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-1) | stage 1 there needs stage 115 here |
| Unlocks | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-2) | stage 2 there needs stage 115 here |
| Unlocks | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-10) | stage 10 there needs stage 115 here |
| Unlocks | [Yellow is it](ratdom_quest.md#stage-10) | stage 10 there needs stage 115 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I heard a rumor that some mining town in the Charwood forest, northwest of the Foaming Flask tavern, has had some troubles recently. I should try to find the Charwood cabin and find out what has happened. | [Lethenlor](../monsters/lethenlor.md) ([tradehouse1](../maps/tradehouse1.md)) | – | – |
| <span id="stage-11"></span>11 | I heard someone mention that the mining town of Charwood heights has had some troubles recently. I should search for the Charwood cabin in the forest northwest of the Foaming Flask tavern. | [Erethori](../monsters/erethori.md) ([waytominingtown1a](../maps/waytominingtown1a.md)) | – | – |
| <span id="stage-19"></span>19 | I have found the Charwood cabin in the forest northwest of the Foaming Flask tavern. | [Guard](../monsters/guard.md#v-charwd_guard) ([waytominingtown2](../maps/waytominingtown2.md))<br>[Drashad](../monsters/drashad.md) ([tradehouse0](../maps/tradehouse0.md))<br>[Khorailla](../monsters/khorailla.md) ([tradehouse0](../maps/tradehouse0.md))<br>+2 more | – | – |
| <span id="stage-20"></span>20 | Maevalia in the Charwood cabin told me a story about how their mining settlement was attacked by some monsters, forcing them to flee down the mountain. They are still missing several of their friends and relatives from the Charwood heights, either killed or captured by the monsters. | [Maevalia](../monsters/maevalia.md) ([tradehouse0](../maps/tradehouse0.md)) | stage 30 | – |
| <span id="stage-21"></span>21 | In particular, Maevalia mentions four people that are greatly missed; their former leader Morenavia, their weapons trainer Falothen, the healer Ayell and their armorer Fayvara. | [Maevalia](../monsters/maevalia.md) ([tradehouse0](../maps/tradehouse0.md)) | stage 30 | – |
| <span id="stage-30"></span>30 | I have agreed to help the people of Charwood find their missing people. | [Maevalia](../monsters/maevalia.md) ([tradehouse0](../maps/tradehouse0.md)) | – | – |
| <span id="stage-35"></span>35 | The guard outside the Charwood cabin allowed me to enter the hills ahead. I should keep to the east and then head north. | [Guard](../monsters/guard.md#v-charwd_guard) ([waytominingtown2](../maps/waytominingtown2.md)) | – | – |
| <span id="stage-40"></span>40 | I encountered one of the monsters that Maevalia spoke of. The monster spoke of someone or something called 'The Thukuzun'. | [Charwood goblin](../monsters/charwdg4.md#v-charwdgg) ([waytolostmine0](../maps/waytolostmine0.md)) | – | – |
| <span id="stage-41"></span>41 | I have found Falothen, the weapons trainer of the Charwood heights, and freed him from the restraints that held him. He will try to make his way back to the Charwood cabin himself. | [Falothen](../monsters/falothen0.md) ([minerhouse0](../maps/minerhouse0.md)) | – | – |
| <span id="stage-42"></span>42 | I have found some skeletal remains, containing a ring with the insignia 'Morenavia'. This must be the former leader of the Charwood hills. | reading a sign on [minerhouse4](../maps/minerhouse4.md) | – | – |
| <span id="stage-43"></span>43 | I have found the armorer Fayvara, and freed her from the restraints that held her. She will try to make her way back to the Charwood cabin herself. | [Fayvara](../monsters/fayvara0.md) ([minerhouse7](../maps/minerhouse7.md)) | – | – |
| <span id="stage-44"></span>44 | I have found some skeletal remains, containing a ring with the insignia 'Ayell'. This must be the remains of the Charwood hills healer that Maevalia mentioned. | reading a sign on [minerhouse5](../maps/minerhouse5.md) | – | – |
| <span id="stage-50"></span>50 | Maevalia thanked me for finding out what happened to the four people that she told me about, but was really sad to hear about the fate of Morenavia and Ayell. Both the weapons trainer Falothen and the armorer Fayvara made it back to the Charwood cabin safely. | [Maevalia](../monsters/maevalia.md) ([tradehouse0](../maps/tradehouse0.md)) | stage 60 | – |
| <span id="stage-60"></span>60 | She told me that both Falothen and Fayvara are anxious to see me, in the basement of the Charwood cabin. I should go see them at once. | [Maevalia](../monsters/maevalia.md) ([tradehouse0](../maps/tradehouse0.md)) | – | – |
| <span id="stage-65"></span>65 | Falothen was happy to see me again, and in return offered to train me in better handling of one weapon type. He can teach me better handling of one or two handed swords, daggers, blunt weapons, axes, or unarmed combat. I'll have to chose my preference and let him know. | [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) | – | – |
| <span id="stage-70"></span>70 | Falothen has taught me how to better handle one handed swords. | [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) | carry 2× [Oegyth crystal](../items/oegyth.md), hand over 2× [Oegyth crystal](../items/oegyth.md), have 5,000 gold, pay 5,000 gold, stage 91 | +1 [One-handed sword proficiency](../skills/weaponProficiency1hsword.md) |
| <span id="stage-71"></span>71 | Falothen has taught me how to better handle two handed swords. | [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) | carry 2× [Oegyth crystal](../items/oegyth.md), hand over 2× [Oegyth crystal](../items/oegyth.md), have 5,000 gold, pay 5,000 gold, stage 70, stage 91 | +1 [Two-handed sword proficiency](../skills/weaponProficiency2hsword.md) |
| <span id="stage-72"></span>72 | Falothen has taught me how to better handle daggers. | [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) | carry 2× [Oegyth crystal](../items/oegyth.md), hand over 2× [Oegyth crystal](../items/oegyth.md), have 5,000 gold, pay 5,000 gold, stage 70, stage 91 | +1 [Dagger proficiency](../skills/weaponProficiencyDagger.md) |
| <span id="stage-73"></span>73 | Falothen has taught me how to better handle blunt weapons. | [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) | carry 2× [Oegyth crystal](../items/oegyth.md), hand over 2× [Oegyth crystal](../items/oegyth.md), have 5,000 gold, pay 5,000 gold, stage 70, stage 91 | +1 [Blunt weapon proficiency](../skills/weaponProficiencyBlunt.md) |
| <span id="stage-74"></span>74 | Falothen has taught me how to better handle axes. | [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) | carry 2× [Oegyth crystal](../items/oegyth.md), hand over 2× [Oegyth crystal](../items/oegyth.md), have 5,000 gold, pay 5,000 gold, stage 70, stage 91 | +1 [Axe proficiency](../skills/weaponProficiencyAxe.md) |
| <span id="stage-75"></span>75 | Falothen has taught me how to be better at fighting unarmed, without weapons. | [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) | carry 2× [Oegyth crystal](../items/oegyth.md), hand over 2× [Oegyth crystal](../items/oegyth.md), have 5,000 gold, pay 5,000 gold, stage 70, stage 91 | +1 [Unarmed fighting](../skills/weaponProficiencyUnarmed.md) |
| <span id="stage-76"></span>76 | Falothen has taught me how to better handle polearms. | [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) | carry 2× [Oegyth crystal](../items/oegyth.md), hand over 2× [Oegyth crystal](../items/oegyth.md), have 5,000 gold, pay 5,000 gold, stage 70, stage 91 | +1 [Pole weapon proficiency](../skills/weaponProficiencyPole.md) |
| <span id="stage-80"></span>80 | Falothen offered me the chance to learn about the other weapon types, but to teach me, he needs 5000 gold and two Oegyth crystals for each skill that I want to get better at. | [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) | stage 70, stage 91 | – |
| <span id="stage-90"></span>90 | Fayvara thanked me for rescuing her, and in return offered to train me in better handling of one type of armor. She can teach me better handling of shields, light armor, heavy armor or or unarmored combat. I'll have to chose my preference and let her know. | [Fayvara](../monsters/fayvara0.md#v-fayvara1) ([tradehouse0a](../maps/tradehouse0a.md)) | – | – |
| <span id="stage-91"></span>91 | Fayvara has taught me how to better handle shields. | [Fayvara](../monsters/fayvara0.md#v-fayvara1) ([tradehouse0a](../maps/tradehouse0a.md)) | carry 2× [Oegyth crystal](../items/oegyth.md), hand over 2× [Oegyth crystal](../items/oegyth.md), have 6,000 gold, pay 6,000 gold, stage 70 | +1 [Shield proficiency](../skills/armorProficiencyShield.md) |
| <span id="stage-92"></span>92 | Fayvara has taught me how to better handle light armor. | [Fayvara](../monsters/fayvara0.md#v-fayvara1) ([tradehouse0a](../maps/tradehouse0a.md)) | carry 2× [Oegyth crystal](../items/oegyth.md), hand over 2× [Oegyth crystal](../items/oegyth.md), have 6,000 gold, pay 6,000 gold, stage 70, stage 91 | +1 [Light armor proficiency](../skills/armorProficiencyLight.md) |
| <span id="stage-93"></span>93 | Fayvara has taught me how to better handle heavy armor. | [Fayvara](../monsters/fayvara0.md#v-fayvara1) ([tradehouse0a](../maps/tradehouse0a.md)) | carry 2× [Oegyth crystal](../items/oegyth.md), hand over 2× [Oegyth crystal](../items/oegyth.md), have 6,000 gold, pay 6,000 gold, stage 70, stage 91 | +1 [Heavy armor proficiency](../skills/armorProficiencyHeavy.md) |
| <span id="stage-94"></span>94 | Fayvara has taught me how to better fighting unarmored, without wearing any armor. | [Fayvara](../monsters/fayvara0.md#v-fayvara1) ([tradehouse0a](../maps/tradehouse0a.md)) | carry 2× [Oegyth crystal](../items/oegyth.md), hand over 2× [Oegyth crystal](../items/oegyth.md), have 6,000 gold, pay 6,000 gold, stage 70, stage 91 | +1 [Unarmored fighting](../skills/armorProficiencyUnarmored.md) |
| <span id="stage-100"></span>100 | Fayvara offered me the chance to learn about the other armor types, but to teach me, she needs 6000 gold and two Oegyth crystals for each skill that I want to get better at. | [Fayvara](../monsters/fayvara0.md#v-fayvara1) ([tradehouse0a](../maps/tradehouse0a.md)) | stage 70, stage 91 | – |
| <span id="stage-110"></span>110 | I have been taught one weapon type skill and one armor type skill from Falothen and Fayvara. I should go see Maevalia again. | [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md))<br>[Fayvara](../monsters/fayvara0.md#v-fayvara1) ([tradehouse0a](../maps/tradehouse0a.md)) | stage 70, stage 91 | – |
| <span id="stage-115"></span>115 | Maevalia thanked me for helping the people of Charwood. **(completes quest)**<br><span class="qnote">🔓 You can finally access a previously blocked area on [Tradehouse0](../maps/tradehouse0.md).</span> | [Maevalia](../monsters/maevalia.md) ([tradehouse0](../maps/tradehouse0.md)) | stage 60, stage 65, stage 90 | 3,000 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Lethenlor](../monsters/lethenlor.md) ([tradehouse1](../maps/tradehouse1.md)) → choose “Charwood, where's that?” → **stage 10**. NPC: “It's just northeast of here. Look for the Charwood cabin north of here.”

???+ note "Stage 11: 1 route"

    1. Talk to [Erethori](../monsters/erethori.md) ([waytominingtown1a](../maps/waytominingtown1a.md)) → choose “Charwood, where is that?” → **stage 11**. NPC: “It's just north of here. Take the path west of our camp here, and head straight north. It's just around the bend there…”

???+ note "Stage 19: 5 routes"

    1. Talk to [Guard](../monsters/guard.md#v-charwd_guard) ([waytominingtown2](../maps/waytominingtown2.md)) → the conversation leads here automatically → **stage 19**
    2. Talk to [Drashad](../monsters/drashad.md) ([tradehouse0](../maps/tradehouse0.md)) → the conversation leads here automatically → **stage 19**
    3. Talk to [Khorailla](../monsters/khorailla.md) ([tradehouse0](../maps/tradehouse0.md)) → the conversation leads here automatically → **stage 19**
    4. Talk to [Kantya](../monsters/kantya.md) ([tradehouse0](../maps/tradehouse0.md)) → the conversation leads here automatically → **stage 19**
    5. Talk to [Maevalia](../monsters/maevalia.md) ([tradehouse0](../maps/tradehouse0.md)) → the conversation leads here automatically → **stage 19**

???+ note "Stage 20: 1 route"

    1. Talk to [Maevalia](../monsters/maevalia.md) ([tradehouse0](../maps/tradehouse0.md)) → choose “What do you think has happened to them?” — **conditions:** reached stage 30 of [Destined for great things](../quests/charwood1.md#stage-30) → **stage 20**. NPC: “I don't know what that net was for though. I wonder if he was supposed to capture some of us.”

???+ note "Stage 21: 1 route"

    1. Talk to [Maevalia](../monsters/maevalia.md) ([tradehouse0](../maps/tradehouse0.md)) → choose “Who were the people that I was supposed to look for, again?” — **conditions:** reached stage 30 of [Destined for great things](../quests/charwood1.md#stage-30) → **stage 21**. NPC: “There's also Ayell, our healer, and Fayvara, our armorer. They always stayed together, those two. We don't know what…”

???+ note "Stage 30: 1 route"

    1. Talk to [Maevalia](../monsters/maevalia.md) ([tradehouse0](../maps/tradehouse0.md)) → choose “OK, I'll try to find your missing people.” — **conditions:** reached stage 30 of [Destined for great things](../quests/charwood1.md#stage-30) → **stage 30**. NPC: “Thank you. The path up to Charwood heights is just east of here.”

???+ note "Stage 35: 1 route"

    1. Talk to [Guard](../monsters/guard.md#v-charwd_guard) ([waytominingtown2](../maps/waytominingtown2.md)) → the conversation leads here automatically — **conditions:** reached stage 35 of [Destined for great things](../quests/charwood1.md#stage-35) → **stage 35**. NPC: “I'll let you enter the hills. Keep heading east, and then turn north once you see the mountain side.”

???+ note "Stage 40: 1 route"

    1. Talk to [Charwood goblin](../monsters/charwdg4.md#v-charwdgg) ([waytolostmine0](../maps/waytolostmine0.md)) → the conversation leads here automatically → **stage 40**. NPC: “Bow before the might of the Thukuzun!”

???+ note "Stage 41: 1 route"

    1. Talk to [Falothen](../monsters/falothen0.md) ([minerhouse0](../maps/minerhouse0.md)) → choose “[Untie the ropes]” → **stage 41**

???+ note "Stage 42: 1 route"

    1. reading a sign on [minerhouse4](../maps/minerhouse4.md) → choose “[Examine the remains]” → **stage 42**. NPC: “Among the remains, you find a ring with the insignia 'Morenavia'. This must be what's left of the former leader of the…”

???+ note "Stage 43: 1 route"

    1. Talk to [Fayvara](../monsters/fayvara0.md) ([minerhouse7](../maps/minerhouse7.md)) → choose “[Untie the ropes]” → **stage 43**

???+ note "Stage 44: 1 route"

    1. reading a sign on [minerhouse5](../maps/minerhouse5.md) → choose “[Examine the pile]” → **stage 44**. NPC: “Among the remains, you find a ring with the insignia 'Ayell'. This must be what's left of the former healer of the…”

???+ note "Stage 50: 1 route"

    1. Talk to [Maevalia](../monsters/maevalia.md) ([tradehouse0](../maps/tradehouse0.md)) → the conversation leads here automatically — **conditions:** reached stage 60 of [Destined for great things](../quests/charwood1.md#stage-60) → **stage 50**. NPC: “It is at least some comfort to know that we still have Falothen and Fayvara with us.”

???+ note "Stage 60: 1 route"

    1. Talk to [Maevalia](../monsters/maevalia.md) ([tradehouse0](../maps/tradehouse0.md)) → the conversation leads here automatically — **conditions:** reached stage 60 of [Destined for great things](../quests/charwood1.md#stage-60) → **stage 60**. NPC: “I hear they are both anxious to talk to you now that they're safe. You should go meet them downstairs in the basement.”

???+ note "Stage 65: 1 route"

    1. Talk to [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “What weapon types can you teach me?” → **stage 65**. NPC: “I only have time to teach you about one type of weapon, so make sure you pick the one that suits you best.”

???+ note "Stage 70: 2 routes"

    1. Talk to [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me how to fight with one-handed swords.” → **stage 70**; also +1 [One-handed sword proficiency](../skills/weaponProficiency1hsword.md). NPC: “[Falothen teaches you the one-handed sword skill]”
    2. Talk to [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me how to fight with one-handed swords. Here are two Oegyth crystals and 5,000 gold as…” — **conditions:** reached stage 70 of [Destined for great things](../quests/charwood1.md#stage-70); reached stage 91 of [Destined for great things](../quests/charwood1.md#stage-91); carry 2× [Oegyth crystal](../items/oegyth.md); have 5,000 gold; hand over 2× [Oegyth crystal](../items/oegyth.md); pay 5,000 gold → **stage 70**; also +1 [One-handed sword proficiency](../skills/weaponProficiency1hsword.md). NPC: “[Falothen teaches you the one-handed sword skill]”

???+ note "Stage 71: 2 routes"

    1. Talk to [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me two-handed sword fighting.” → **stage 71**; also +1 [Two-handed sword proficiency](../skills/weaponProficiency2hsword.md). NPC: “[Falothen teaches you the two-handed sword skill]”
    2. Talk to [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me two-handed sword fighting. Here are two Oegyth crystals and 5,000 gold as payment.” — **conditions:** reached stage 70 of [Destined for great things](../quests/charwood1.md#stage-70); reached stage 91 of [Destined for great things](../quests/charwood1.md#stage-91); carry 2× [Oegyth crystal](../items/oegyth.md); have 5,000 gold; hand over 2× [Oegyth crystal](../items/oegyth.md); pay 5,000 gold → **stage 71**; also +1 [Two-handed sword proficiency](../skills/weaponProficiency2hsword.md). NPC: “[Falothen teaches you the two-handed sword skill]”

???+ note "Stage 72: 2 routes"

    1. Talk to [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me how to fight with daggers.” → **stage 72**; also +1 [Dagger proficiency](../skills/weaponProficiencyDagger.md). NPC: “[Falothen teaches you the dagger skill]”
    2. Talk to [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me how to fight with daggers. Here are two Oegyth crystals and 5,000 gold as payment.” — **conditions:** reached stage 70 of [Destined for great things](../quests/charwood1.md#stage-70); reached stage 91 of [Destined for great things](../quests/charwood1.md#stage-91); carry 2× [Oegyth crystal](../items/oegyth.md); have 5,000 gold; hand over 2× [Oegyth crystal](../items/oegyth.md); pay 5,000 gold → **stage 72**; also +1 [Dagger proficiency](../skills/weaponProficiencyDagger.md). NPC: “[Falothen teaches you the dagger skill]”

???+ note "Stage 73: 2 routes"

    1. Talk to [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me how to fight with blunt weapons.” → **stage 73**; also +1 [Blunt weapon proficiency](../skills/weaponProficiencyBlunt.md). NPC: “[Falothen teaches you the blunt weapons skill]”
    2. Talk to [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me how to fight with blunt weapons. Here are two Oegyth crystals and 5,000 gold as payment.” — **conditions:** reached stage 70 of [Destined for great things](../quests/charwood1.md#stage-70); reached stage 91 of [Destined for great things](../quests/charwood1.md#stage-91); carry 2× [Oegyth crystal](../items/oegyth.md); have 5,000 gold; hand over 2× [Oegyth crystal](../items/oegyth.md); pay 5,000 gold → **stage 73**; also +1 [Blunt weapon proficiency](../skills/weaponProficiencyBlunt.md). NPC: “[Falothen teaches you the blunt weapons skill]”

???+ note "Stage 74: 2 routes"

    1. Talk to [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me how to fight with axes.” → **stage 74**; also +1 [Axe proficiency](../skills/weaponProficiencyAxe.md). NPC: “[Falothen teaches you the axe skill]”
    2. Talk to [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me how to fight with axes. Here are two Oegyth crystals and 5,000 gold as payment.” — **conditions:** reached stage 70 of [Destined for great things](../quests/charwood1.md#stage-70); reached stage 91 of [Destined for great things](../quests/charwood1.md#stage-91); carry 2× [Oegyth crystal](../items/oegyth.md); have 5,000 gold; hand over 2× [Oegyth crystal](../items/oegyth.md); pay 5,000 gold → **stage 74**; also +1 [Axe proficiency](../skills/weaponProficiencyAxe.md). NPC: “[Falothen teaches you the axe skill]”

???+ note "Stage 75: 2 routes"

    1. Talk to [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me how to be better at unarmed fighting.” → **stage 75**; also +1 [Unarmed fighting](../skills/weaponProficiencyUnarmed.md). NPC: “[Falothen teaches you the unarmed fighting skill]”
    2. Talk to [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me how to be better at unarmed fighting. Here are two Oegyth crystals and 5,000 gold as…” — **conditions:** reached stage 70 of [Destined for great things](../quests/charwood1.md#stage-70); reached stage 91 of [Destined for great things](../quests/charwood1.md#stage-91); carry 2× [Oegyth crystal](../items/oegyth.md); have 5,000 gold; hand over 2× [Oegyth crystal](../items/oegyth.md); pay 5,000 gold → **stage 75**; also +1 [Unarmed fighting](../skills/weaponProficiencyUnarmed.md). NPC: “[Falothen teaches you the unarmed fighting skill]”

???+ note "Stage 76: 2 routes"

    1. Talk to [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me how to fight with polearms.” → **stage 76**; also +1 [Pole weapon proficiency](../skills/weaponProficiencyPole.md). NPC: “[Falothen teaches you the polearm skill]”
    2. Talk to [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me how to better fight with polearms. Here are two Oegyth crystals and 5,000 gold as…” — **conditions:** reached stage 70 of [Destined for great things](../quests/charwood1.md#stage-70); reached stage 91 of [Destined for great things](../quests/charwood1.md#stage-91); carry 2× [Oegyth crystal](../items/oegyth.md); have 5,000 gold; hand over 2× [Oegyth crystal](../items/oegyth.md); pay 5,000 gold → **stage 76**; also +1 [Pole weapon proficiency](../skills/weaponProficiencyPole.md). NPC: “[Falothen teaches you the polearm skill]”

???+ note "Stage 80: 1 route"

    1. Talk to [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “What sort of payment?” — **conditions:** reached stage 70 of [Destined for great things](../quests/charwood1.md#stage-70); reached stage 91 of [Destined for great things](../quests/charwood1.md#stage-91) → **stage 80**. NPC: “Seeing as you saved me, I think it's reasonable to only require two of those crystals from you. I still have expenses…”

???+ note "Stage 90: 1 route"

    1. Talk to [Fayvara](../monsters/fayvara0.md#v-fayvara1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “What armor types can you teach me?” → **stage 90**. NPC: “We only have time for one type of armor right now though, so think carefully on which one will suit you best.”

???+ note "Stage 91: 2 routes"

    1. Talk to [Fayvara](../monsters/fayvara0.md#v-fayvara1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me about shields and parrying weapons.” → **stage 91**; also +1 [Shield proficiency](../skills/armorProficiencyShield.md). NPC: “[Fayvara teaches you the shield skill]”
    2. Talk to [Fayvara](../monsters/fayvara0.md#v-fayvara1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me about shields. Here are two Oegyth crystals and 6,000 gold as payment.” — **conditions:** reached stage 91 of [Destined for great things](../quests/charwood1.md#stage-91); reached stage 70 of [Destined for great things](../quests/charwood1.md#stage-70); carry 2× [Oegyth crystal](../items/oegyth.md); have 6,000 gold; hand over 2× [Oegyth crystal](../items/oegyth.md); pay 6,000 gold → **stage 91**; also +1 [Shield proficiency](../skills/armorProficiencyShield.md). NPC: “[Fayvara teaches you the shield skill]”

???+ note "Stage 92: 2 routes"

    1. Talk to [Fayvara](../monsters/fayvara0.md#v-fayvara1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me about light armors.” → **stage 92**; also +1 [Light armor proficiency](../skills/armorProficiencyLight.md). NPC: “[Fayvara teaches you the light armor skill]”
    2. Talk to [Fayvara](../monsters/fayvara0.md#v-fayvara1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me about light armors. Here are two Oegyth crystals and 6,000 gold as payment.” — **conditions:** reached stage 91 of [Destined for great things](../quests/charwood1.md#stage-91); reached stage 70 of [Destined for great things](../quests/charwood1.md#stage-70); carry 2× [Oegyth crystal](../items/oegyth.md); have 6,000 gold; hand over 2× [Oegyth crystal](../items/oegyth.md); pay 6,000 gold → **stage 92**; also +1 [Light armor proficiency](../skills/armorProficiencyLight.md). NPC: “[Fayvara teaches you the light armor skill]”

???+ note "Stage 93: 2 routes"

    1. Talk to [Fayvara](../monsters/fayvara0.md#v-fayvara1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me about heavy armors.” → **stage 93**; also +1 [Heavy armor proficiency](../skills/armorProficiencyHeavy.md). NPC: “[Fayvara teaches you the heavy armor skill]”
    2. Talk to [Fayvara](../monsters/fayvara0.md#v-fayvara1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me about heavy armors. Here are two Oegyth crystals and 6,000 gold as payment.” — **conditions:** reached stage 91 of [Destined for great things](../quests/charwood1.md#stage-91); reached stage 70 of [Destined for great things](../quests/charwood1.md#stage-70); carry 2× [Oegyth crystal](../items/oegyth.md); have 6,000 gold; hand over 2× [Oegyth crystal](../items/oegyth.md); pay 6,000 gold → **stage 93**; also +1 [Heavy armor proficiency](../skills/armorProficiencyHeavy.md). NPC: “[Fayvara teaches you the heavy armor skill]”

???+ note "Stage 94: 2 routes"

    1. Talk to [Fayvara](../monsters/fayvara0.md#v-fayvara1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me about unarmored combat.” → **stage 94**; also +1 [Unarmored fighting](../skills/armorProficiencyUnarmored.md). NPC: “[Fayvara teaches you the unarmored combat skill]”
    2. Talk to [Fayvara](../monsters/fayvara0.md#v-fayvara1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “Sounds good. Teach me about unarmored combat. Here are two Oegyth crystals and 6,000 gold as payment.” — **conditions:** reached stage 91 of [Destined for great things](../quests/charwood1.md#stage-91); reached stage 70 of [Destined for great things](../quests/charwood1.md#stage-70); carry 2× [Oegyth crystal](../items/oegyth.md); have 6,000 gold; hand over 2× [Oegyth crystal](../items/oegyth.md); pay 6,000 gold → **stage 94**; also +1 [Unarmored fighting](../skills/armorProficiencyUnarmored.md). NPC: “[Fayvara teaches you the unarmored combat skill]”

???+ note "Stage 100: 1 route"

    1. Talk to [Fayvara](../monsters/fayvara0.md#v-fayvara1) ([tradehouse0a](../maps/tradehouse0a.md)) → choose “What sort of payment?” — **conditions:** reached stage 91 of [Destined for great things](../quests/charwood1.md#stage-91); reached stage 70 of [Destined for great things](../quests/charwood1.md#stage-70) → **stage 100**. NPC: “So I'm thinking something similar would suffice. Since as you're my friend, I won't charge as much as Falothen did but…”

???+ note "Stage 110: 2 routes"

    1. Talk to [Falothen](../monsters/falothen0.md#v-falothen1) ([tradehouse0a](../maps/tradehouse0a.md)) → the conversation leads here automatically — **conditions:** reached stage 70 of [Destined for great things](../quests/charwood1.md#stage-70); reached stage 91 of [Destined for great things](../quests/charwood1.md#stage-91) → **stage 110**
    2. Talk to [Fayvara](../monsters/fayvara0.md#v-fayvara1) ([tradehouse0a](../maps/tradehouse0a.md)) → the conversation leads here automatically — **conditions:** reached stage 91 of [Destined for great things](../quests/charwood1.md#stage-91); reached stage 70 of [Destined for great things](../quests/charwood1.md#stage-70) → **stage 110**

???+ note "Stage 115: 1 route"

    1. Talk to [Maevalia](../monsters/maevalia.md) ([tradehouse0](../maps/tradehouse0.md)) → choose “I've spoken to them both.” — **conditions:** reached stage 60 of [Destined for great things](../quests/charwood1.md#stage-60); reached stage 65 of [Destined for great things](../quests/charwood1.md#stage-65); reached stage 90 of [Destined for great things](../quests/charwood1.md#stage-90) → **stage 115**. NPC: “Good. We are truly grateful for the help that you have provided to us from the Charwood heights.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Stage 10 journal text changed<br>Stage 11 journal text changed<br>Stage 41 journal text changed<br>Stage 43 journal text changed<br>Stage 65 journal text changed<br>Dialogue: 10 lines changed<br>· text: “We only have time for one type of armor right now though, so think ca…” → “We only have time for one type of armor right now though, so think ca…”<br>· text: “It's just north of here. Take the path west of our camp here, and hea…” → “It's just north of here. Take the path west of our camp here, and hea…” |
| [v0.7.11](../versions/0.7.11.md) | Dialogue: 1 line changed |
| [v0.7.12](../versions/0.7.12.md) | Stages added: 76<br>Dialogue: 2 lines added, 1 line changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “So I'm thinking something similar would suffice. Since as you're my f…” → “So I'm thinking something similar would suffice. Since as you're my f…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=charwood1.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=charwood1.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=charwood1.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=charwood1.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=charwood1.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `charwood1` |
    | showInLog | 1 |
    | Stage IDs | 10, 11, 19, 20, 21, 30, 35, 40, 41, 42, 43, 44, 50, 60, 65, 70, 71, 72, 73, 74, 75, 76, 80, 90, 91, 92, 93, 94, 100, 110, 115 |
    | Dialogue nodes setting stages | 10: `lethenlor7`, 11: `erethori6`, 19: `charwd_guard`, 19: `drashad`, 19: `khorailla`, 20: `maevalia15`, 21: `maevalia20`, 30: `maevalia28`, 35: `charwd_guard2`, 40: `charwoodm`, 41: `falothen0_2`, 42: `morenavia_1`, 43: `fayvara0_2`, 44: `ayell_1`, 50: `maevalia_r8`, 60: `maevalia_r9`, 65: `falothen1_6`, 70: `falothen1_7_1hs2`, 70: `falothen1_2nd_1hs3`, 71: `falothen1_7_2hs2`, 71: `falothen1_2nd_2hs3`, 72: `falothen1_7_d2`, 72: `falothen1_2nd_d3`, 73: `falothen1_7_b2`, 73: `falothen1_2nd_b3`, 74: `falothen1_7_a2`, 74: `falothen1_2nd_a3`, 75: `falothen1_7_f2`, 75: `falothen1_2nd_f3`, 76: `falothen_1_pa2`, 76: `falothen1_2nd_pa3`, 80: `falothen1_11`, 90: `fayvara1_6`, 91: `fayvara1_7_s2`, 91: `fayvara1_2nd_s3`, 92: `fayvara1_7_l2`, 92: `fayvara1_2nd_l3`, 93: `fayvara1_7_h2`, 93: `fayvara1_2nd_h3`, 94: `fayvara1_7_u2`, 94: `fayvara1_2nd_u3`, 100: `fayvara1_11`, 110: `falothen1_s0`, 110: `fayvara1_s0`, 115: `maevalia_r10` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
