# Placeholder for hidden quest stages 2 (not displayed)

!!! info "Hidden story flag"
    An internal quest the game uses to track your progress behind the scenes. It never shows up in your journal. The entries below are the developers' notes to themselves, so expect them to be terse.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `nondisplay_2` |
| **In journal** | No (hidden flag) |
| **Stages** | 26 |
| **Started by** | [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) |
| **NPCs involved** | [Aemens](../monsters/aemens.md), [Cithurn](../monsters/waterwayhermit.md), [Cithurn's cat](../monsters/cithurncat.md), [Melona](../monsters/melona.md), [Taret](../monsters/taret.md), [Teksin](../monsters/teksin.md) +1 |
| **Locations** | [brimhaven_inn_east](../maps/brimhaven_inn_east.md), [loneford16](../maps/loneford16.md), [loneford17](../maps/loneford17.md), [stoutford_church](../maps/stoutford_church.md) |
| **Total XP** | 25 |
| **Related quests** | 8 |

</div>

## Overview

> Got Cithurn's talisman

## Prerequisites to start

Start with [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)). Required:

- NOT reached stage 90 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-90)
- NOT reached stage 70 of [Just the beginning](../quests/waterwayacave.md#stage-70)
- reached stage 50 of [Trial by fire](../quests/charwood2.md#stage-50)
- reached stage 35 of [Just the beginning](../quests/waterwayacave.md#stage-35)
- NOT reached stage 10 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Trial by fire](charwood2.md#stage-50) | stage 50 reached, for stage 10 here |
| Requires | [Rumblings](rumblings.md#stage-80) | stage 80 reached, for stages 180, 190 here |
| Requires | [Just the beginning](waterwayacave.md#stage-35) | stage 35 reached, for stage 10 here |
| Requires | [Just the beginning](waterwayacave.md#stage-70) | stage 70 reached, for stage 120 here |
| Mutually exclusive | [Just the beginning](waterwayacave.md#stage-10) | stage 10 must NOT be reached, for stage 90 here |
| Mutually exclusive | [Just the beginning](waterwayacave.md#stage-70) | stage 70 must NOT be reached, for stage 10 here |
| Unlocks | [Unusual experiences and achievements](achievements.md#stage-40) | stage 40 there needs stage 200 here |
| Unlocks | [Search for Andor](andor.md#stage-110) | stage 110 there needs stage 170 here |
| Unlocks | [Ancient secrets](flagstone.md#stage-5) | stage 5 there needs stages 180, 190 here |
| Unlocks | [The odd coin collector](odd_coin_collector.md#stage-12) | stage 12 there needs stage 250 here |
| Unlocks | [The odd coin collector](odd_coin_collector.md#stage-13) | stage 13 there needs stage 250 here |
| Unlocks | [Stoutford's old castle](stoutford_castle.md#stage-10) | stage 10 there needs stages 180, 190 here |
| Unlocks | [Stoutford's old castle](stoutford_castle.md#stage-12) | stage 12 there needs stages 180, 190 here |
| Blocks | [Unusual experiences and achievements](achievements.md#stage-40) | reaching stage 200 here closes stage 40 there |
| Blocks | [The odd coin collector](odd_coin_collector.md#stage-20) | reaching stage 170 here closes stage 20 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Got Cithurn's talisman<br><span class="qnote">⚡ A scripted event can now trigger on [Waterwayacave1](../maps/waterwayacave1.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Waterwayacave1](../maps/waterwayacave1.md).</span> | [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) | – | gives 1× [Cithurn's talisman](../items/cithurn_talisman.md) |
| <span id="stage-20"></span>20 | Found gold on waytolake7b | reading a sign on [waytolake7b](../maps/waytolake7b.md) | – | gives 653× [Gold coins](../items/gold.md) |
| <span id="stage-30"></span>30 | Found gem 1 on waytolake6<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytolake6](../maps/waytolake6.md).</span> | stepping on a trigger on [waytolake6](../maps/waytolake6.md) | – | gives 1× [Sharpened gem](../items/gem4.md) |
| <span id="stage-40"></span>40 | Found gem 2 on waytolake6<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytolake6](../maps/waytolake6.md).</span> | stepping on a trigger on [waytolake6](../maps/waytolake6.md) | – | gives 1× [Polished sparkling gem](../items/gem5.md) |
| <span id="stage-50"></span>50 | Met Aemens | [Aemens](../monsters/aemens.md) ([loneford16](../maps/loneford16.md)) | – | – |
| <span id="stage-60"></span>60 | Was warned about Aemens | [Taret](../monsters/taret.md) ([loneford17](../maps/loneford17.md)) | – | – |
| <span id="stage-70"></span>70 | Told Aemens the neighbor warned you about her | [Aemens](../monsters/aemens.md) ([loneford16](../maps/loneford16.md)) | stage 60 | – |
| <span id="stage-75"></span>75 | Taret tells you to be more careful what you say | [Taret](../monsters/taret.md) ([loneford17](../maps/loneford17.md)) | stage 70 | – |
| <span id="stage-80"></span>80 | Looted corpse in waterway cave | reading a sign on [waterwayacave2](../maps/waterwayacave2.md) | – | gives [Rusted iron sword](../items/rusted_iron_sword.md), [Broken wooden buckler](../items/broken_buckler.md), [Crude ring of block](../items/ring_crude_block.md), [Crude leather cap](../items/hat3.md), [Gold coins](../items/gold.md) |
| <span id="stage-90"></span>90 | Got repreimanded by Cithurn | [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) | – | – |
| <span id="stage-100"></span>100 | Petted Cithurn's cat | [Cithurn's cat](../monsters/cithurncat.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) | – | 25 XP |
| <span id="stage-110"></span>110 | Have discovered hidden room<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waterwayacavex](../maps/waterwayacavex.md).</span> | stepping on a trigger on [waterwayacavex](../maps/waterwayacavex.md) | – | – |
| <span id="stage-120"></span>120 | Returned Cithurn's talisman after initially saying you would keep it. | [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) | hand over 1× [Cithurn's talisman](../items/cithurn_talisman.md) | – |
| <span id="stage-130"></span>130 | Found old clothes<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waterwaya6](../maps/waterwaya6.md).</span> | stepping on a trigger on [waterwaya6](../maps/waterwaya6.md) | – | gives 4× [Old tunic](../items/tunic_old.md) |
| <span id="stage-140"></span>140 | Met Teksin | [Teksin](../monsters/teksin.md) ([waytolake11](../maps/waytolake11.md)) | – | – |
| <span id="stage-150"></span>150 | Purchased potion of lightning attack | [Teksin](../monsters/teksin.md) ([waytolake11](../maps/waytolake11.md)) | pay 4,999 gold, stage 140 | gives 1× [Potion of lightning attack](../items/pot_light_attack.md) |
| <span id="stage-160"></span>160 | Mentioned Remgard - Teksin | [Teksin](../monsters/teksin.md) ([waytolake11](../maps/waytolake11.md)) | stage 140 | – |
| <span id="stage-170"></span>170 | Been to Remgard<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Remgard0](../maps/remgard0.md).</span> | stepping on a trigger on [remgard0](../maps/remgard0.md) | – | – |
| <span id="stage-180"></span>180 | Talked to Yolgen about the castle | [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) | – | – |
| <span id="stage-190"></span>190 | Talked to Yolgen about Flagstone | [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) | – | – |
| <span id="stage-200"></span>200 | Saw bird from lookout | walking into a blocked passage on [waytolake12](../maps/waytolake12.md) | – | – |
| <span id="stage-210"></span>210 | Found opal at lookout | dialogue `lookout_down_3`, which nothing in the data starts directly | – | gives [Shimmering opal](../items/gem7.md) |
| <span id="stage-220"></span>220 | You will never get this quest stage (used for lookout)<br><span class="qnote">🔓 You can finally access a previously blocked area on [Laerothisland3](../maps/laerothisland3.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Mountainlake1](../maps/mountainlake1.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Waytolake12](../maps/waytolake12.md).</span> | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-230"></span>230 | bought Brimhaven bed<br><span class="qnote">🔓 You can finally access a previously blocked area on [Brimhaven inn east](../maps/brimhaven_inn_east.md).</span> | [Melona](../monsters/melona.md) ([brimhaven_inn_east](../maps/brimhaven_inn_east.md)) | pay 90 gold | – |
| <span id="stage-240"></span>240 | Despawned monsters in graveyard<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Graveyard1](../maps/graveyard1.md).</span> | stepping on a trigger on [graveyard1](../maps/graveyard1.md) | hand over 1× [Ancient text](../items/graveyardtext.md) | removes monsters from graveyard1<br>removes monsters from graveyard0 |
| <span id="stage-250"></span>250 | Looted arulir secret room<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Arulircave5](../maps/arulircave5.md).</span> | stepping on a trigger on [arulircave5](../maps/arulircave5.md) | – | gives [Sharpened gem](../items/gem4.md), [Polished sparkling gem](../items/gem5.md), [Gold coins](../items/gold.md), [Polished gem](../items/gem3.md) |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) → choose “I think I need more help to be able to complete my mission.” — **conditions:** NOT reached stage 90 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-90); NOT reached stage 70 of [Just the beginning](../quests/waterwayacave.md#stage-70); reached stage 50 of [Trial by fire](../quests/charwood2.md#stage-50); reached stage 35 of [Just the beginning](../quests/waterwayacave.md#stage-35); NOT reached stage 10 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-10) → **stage 10**; also gives 1× [Cithurn's talisman](../items/cithurn_talisman.md). NPC: “Here. Take this talisman. It does much to dispel evil forces. I acquired it long ago, and it has kept me safe over the…”

???+ note "Stage 20: 1 route"

    1. reading a sign on [waytolake7b](../maps/waytolake7b.md) → the conversation leads here automatically — **conditions:** NOT reached stage 20 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-20) → **stage 20**; also gives 653× [Gold coins](../items/gold.md). NPC: “You found some gold amongst the bones!”

???+ note "Stage 30: 1 route"

    1. stepping on a trigger on [waytolake6](../maps/waytolake6.md) → the conversation leads here automatically — **conditions:** NOT reached stage 30 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-30) → **stage 30**; also gives 1× [Sharpened gem](../items/gem4.md). NPC: “You find a partly visible gem sticking out of the exposed rock.”

???+ note "Stage 40: 1 route"

    1. stepping on a trigger on [waytolake6](../maps/waytolake6.md) → the conversation leads here automatically — **conditions:** NOT reached stage 40 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-40) → **stage 40**; also gives 1× [Polished sparkling gem](../items/gem5.md). NPC: “You find a partly visible gem sticking out of the exposed rock.”

???+ note "Stage 50: 1 route"

    1. Talk to [Aemens](../monsters/aemens.md) ([loneford16](../maps/loneford16.md)) → the conversation leads here automatically → **stage 50**. NPC: “Don't you know that it's rude to walk into someone's house without knocking?”

???+ note "Stage 60: 1 route"

    1. Talk to [Taret](../monsters/taret.md) ([loneford17](../maps/loneford17.md)) → choose “Can you tell me anything about the local area?” → **stage 60**. NPC: “The nastiest person in town is probably my neighbor. *laughs*. Be careful about walking in on her!”

???+ note "Stage 70: 1 route"

    1. Talk to [Aemens](../monsters/aemens.md) ([loneford16](../maps/loneford16.md)) → choose “Your neighbor was right. He said you were not always a nice person.” — **conditions:** reached stage 60 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-60); NOT reached stage 75 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-75) → **stage 70**. NPC: “Did he now! Well, I'll have a word or two to say to him later! What do you want?”

???+ note "Stage 75: 1 route"

    1. Talk to [Taret](../monsters/taret.md) ([loneford17](../maps/loneford17.md)) → choose “You are right. I told her you warned me that she was not always nice to strangers, but I think that just…” — **conditions:** reached stage 70 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-70); NOT reached stage 75 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-75) → **stage 75**. NPC: “Thanks kid. *sigh*. I expect she will be around here later to complain about that. You should be more careful what you…”

???+ note "Stage 80: 1 route"

    1. reading a sign on [waterwayacave2](../maps/waterwayacave2.md) → choose “You decide to take everything.” — **conditions:** NOT reached stage 80 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-80) → **stage 80**; also gives [Rusted iron sword](../items/rusted_iron_sword.md), [Broken wooden buckler](../items/broken_buckler.md), [Crude ring of block](../items/ring_crude_block.md), [Crude leather cap](../items/hat3.md), [Gold coins](../items/gold.md)

???+ note "Stage 90: 1 route"

    1. Talk to [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) → choose “I'm looking for someone.” — **conditions:** NOT reached stage 10 of [Just the beginning](../quests/waterwayacave.md#stage-10); NOT reached stage 90 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-90) → **stage 90**. NPC: “Well I'm the only one here. Perhaps you should leave. Come back when you have learned some manners.”

???+ note "Stage 100: 2 routes"

    1. Talk to [Cithurn's cat](../monsters/cithurncat.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) → choose “[You scratch the cat behind the ear]” — **conditions:** NOT reached stage 100 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-100) → **stage 100**. NPC: “Purr ... Purr.”
    2. Talk to [Cithurn's cat](../monsters/cithurncat.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) → choose “[You stroke the cat]” — **conditions:** NOT reached stage 100 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-100) → **stage 100**. NPC: “Purr ... Purr.”

???+ note "Stage 110: 1 route"

    1. stepping on a trigger on [waterwayacavex](../maps/waterwayacavex.md) → the conversation leads here automatically — **conditions:** NOT reached stage 110 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-110) → **stage 110**. NPC: “You have discovered a hidden room!”

???+ note "Stage 120: 1 route"

    1. Talk to [Cithurn](../monsters/waterwayhermit.md) ([waterwaybhouse](../maps/waterwaybhouse.md)) → choose “Yes. I changed my mind about keeping it.” — **conditions:** reached stage 70 of [Just the beginning](../quests/waterwayacave.md#stage-70); NOT reached stage 120 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-120); hand over 1× [Cithurn's talisman](../items/cithurn_talisman.md) → **stage 120**. NPC: “Thank you. It seems you do have more honor than I thought.”

???+ note "Stage 130: 1 route"

    1. stepping on a trigger on [waterwaya6](../maps/waterwaya6.md) → choose “[Take the clothes]” — **conditions:** NOT reached stage 130 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-130) → **stage 130**; also gives 4× [Old tunic](../items/tunic_old.md). NPC: “The clothes smell musty and are falling apart.”

???+ note "Stage 140: 1 route"

    1. Talk to [Teksin](../monsters/teksin.md) ([waytolake11](../maps/waytolake11.md)) → the conversation leads here automatically — **conditions:** NOT reached stage 140 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-140) → **stage 140**. NPC: “Hello. My name is Teksin. I'm a trader. Who are you?”

???+ note "Stage 150: 1 route"

    1. Talk to [Teksin](../monsters/teksin.md) ([waytolake11](../maps/waytolake11.md)) → choose “OK. I'll take it.” — **conditions:** reached stage 140 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-140); NOT reached stage 150 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-150); pay 4,999 gold → **stage 150**; also gives 1× [Potion of lightning attack](../items/pot_light_attack.md). NPC: “Use it wisely. Such a potion is very hard to obtain. It is unlikely I will have any more to sell in the future.”

???+ note "Stage 160: 1 route"

    1. Talk to [Teksin](../monsters/teksin.md) ([waytolake11](../maps/waytolake11.md)) → choose “I'm looking for my brother, Andor. He looks a bit like me.” — **conditions:** reached stage 140 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-140) → **stage 160**. NPC: “This is as close as I can get coming this way. I am an experienced traveler, and I know that Remgard is close. It's…”

???+ note "Stage 170: 1 route"

    1. stepping on a trigger on [remgard0](../maps/remgard0.md) → the conversation leads here automatically → **stage 170**

???+ note "Stage 180: 1 route"

    1. Talk to [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “Can you tell me more about Mt. Galmore?” — **conditions:** reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80) → **stage 180**. NPC: “However, recently more and more of the most foul monsters are coming from the mountain and we have to fend them off.…”

???+ note "Stage 190: 1 route"

    1. Talk to [Yolgen](../monsters/yolgen.md) ([stoutford_church](../maps/stoutford_church.md)) → choose “Can you tell me more about Flagstone?” — **conditions:** reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80) → **stage 190**. NPC: “Flagstone Prison was built four hundred years ago by house Gorland of Stoutford, and was used until the Noble Wars,…”

???+ note "Stage 200: 1 route"

    1. walking into a blocked passage on [waytolake12](../maps/waytolake12.md) → choose “Look up at the sky.” — **conditions:** NOT reached stage 200 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-200) → **stage 200**. NPC: “You see a bird, perhaps a hawk, high in the sky.”

???+ note "Stage 230: 1 route"

    1. Talk to [Melona](../monsters/melona.md) ([brimhaven_inn_east](../maps/brimhaven_inn_east.md)) → choose “I'll take it.” — **conditions:** NOT reached stage 230 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-230); pay 90 gold → **stage 230**. NPC: “Thank you for your patronage. You can use any available bed.”

???+ note "Stage 240: 4 routes"

    1. stepping on a trigger on [graveyard1](../maps/graveyard1.md) → the conversation leads here automatically — **conditions:** killed 1× [Graveyard king](../monsters/graveyardking.md); NOT reached stage 240 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-240); hand over 1× [Ancient text](../items/graveyardtext.md) → **stage 240**; also removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard0, removes monsters from graveyard1, removes monsters from graveyard1. NPC: “The ancient text crumbles and turns to dust. The defeat of the undead master seems to have lifted the spell animating…”
    2. stepping on a trigger on [graveyard1](../maps/graveyard1.md) → the conversation leads here automatically — **conditions:** killed 1× [Graveyard king](../monsters/graveyardking.md); NOT reached stage 240 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-240) → **stage 240**; also removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard0, removes monsters from graveyard1, removes monsters from graveyard1. NPC: “The defeat of the undead master seems to have lifted the spell animating the remaining corpses and they return to…”
    3. stepping on a trigger on [graveyard1](../maps/graveyard1.md) → the conversation leads here automatically — **conditions:** killed 1× [Graveyard king](../monsters/graveyardking.md) → **stage 240**
    4. stepping on a trigger on [graveyard1](../maps/graveyard1.md) → the conversation leads here automatically — **conditions:** killed 1× [Graveyard king](../monsters/graveyardking.md); NOT reached stage 240 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-240) → **stage 240**; also removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard0, removes monsters from graveyard1, removes monsters from graveyard1. NPC: “The defeat of the undead master seems to have lifted the spell animating the remaining corpses and they return to…”

???+ note "Stage 250: 1 route"

    1. stepping on a trigger on [arulircave5](../maps/arulircave5.md) → choose “[Plunder the loot]” — **conditions:** NOT reached stage 250 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-250) → **stage 250**; also gives [Sharpened gem](../items/gem4.md), [Polished sparkling gem](../items/gem5.md), [Gold coins](../items/gold.md), [Polished gem](../items/gem3.md). NPC: “You have 'acquired' some gold and other valuable gems!”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 22 lines added |
| [v0.7.4](../versions/0.7.4.md) | stages added: 200, 210, 220<br>Dialogue: 2 lines added, 1 line changed<br>· text: “Flagstone Prison was built four hundred years ago by house Gorland of…” → “Flagstone Prison was built four hundred years ago by house Gorland of…” |
| [v0.7.11](../versions/0.7.11.md) | stages added: 230<br>Dialogue: 1 line added |
| [v0.7.12](../versions/0.7.12.md) | stages added: 240<br>Dialogue: 3 lines added, 1 line changed |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 1 line changed |
| [v0.8.11](../versions/0.8.11.md) | stages added: 250<br>Dialogue: 1 line added |
| [v0.8.14](../versions/0.8.14.md) | Dialogue: 1 line changed<br>· text: “However, recently more and more of the most foul monsters are coming …” → “However, recently more and more of the most foul monsters are coming …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=nondisplay_2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=nondisplay_2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=nondisplay_2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=nondisplay_2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=nondisplay_2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `nondisplay_2` |
    | showInLog | 0 |
    | Stage IDs | 10, 20, 30, 40, 50, 60, 70, 75, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250 |
    | Dialogue nodes setting stages | 10: `cithurn_51`, 20: `sign_waytolake7b_1`, 30: `lostfound1`, 40: `lostfound2`, 50: `aemens_0`, 60: `taret_3`, 70: `aemens_3`, 75: `taret_5`, 80: `waterwatcaveloot2`, 90: `cithurn_80`, 100: `cithurncatmeow_1`, 100: `cithurncatmeow_2`, 110: `waterwaycavex_1`, 120: `cithurn_111`, 130: `old_clothes_2`, 140: `teksin12`, 150: `teksin110`, 160: `teksin50`, 170: `been_to_remgard`, 180: `yolgen_surroundings_2c`, 190: `yolgen_surroundings_1`, 200: `lookout_up_1`, 210: `lookout_down_3`, 230: `melona_2a`, 240: `graveyardday2`, 240: `graveyardday2a`, 240: `boss_killed1`, 250: `arulir_secret_room_loot_2` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
