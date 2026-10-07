---
description: "General story flags 2 is a hidden quest in Andor's Trail, started by Cithurn (waterwaybhouse). 26 stages, 25 XP in total. Got Cithurn's talisman"
---

# General story flags 2

!!! info "Hidden story flag"
    An internal quest the game uses to track progress. It does not appear in the journal. The stage descriptions below are internal notes written by the developers and may be brief.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `nondisplay_2` |
| **In journal** | No (hidden flag) |
| **Stages** | 26 |
| **Started by** | [Cithurn](../monsters/waterwayhermit.md) ([Waterwaybhouse](../maps/waterwaybhouse.md)) |
| **NPCs involved** | [Aemens](../monsters/aemens.md), [Cithurn](../monsters/waterwayhermit.md), [Cithurn's cat](../monsters/cithurncat.md), [Melona](../monsters/melona.md), [Taret](../monsters/taret.md), [Teksin](../monsters/teksin.md) +1 |
| **Locations** | [Brimhaven inn east](../maps/brimhaven_inn_east.md), [Loneford 16](../maps/loneford16.md), [Loneford 17](../maps/loneford17.md), [Stoutford church](../maps/stoutford_church.md) |
| **Total XP** | 25 |
| **Related quests** | 8 |

</div>

## Overview

> Got Cithurn's talisman

## Prerequisites to start

Start with [Cithurn](../monsters/waterwayhermit.md) ([Waterwaybhouse](../maps/waterwaybhouse.md)). Required:

- NOT reached stage 90 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-90)
- NOT reached stage 70 of [Just the beginning](../quests/waterwayacave.md#stage-70)
- reached stage 50 of [Trial by fire](../quests/charwood2.md#stage-50)
- reached stage 35 of [Just the beginning](../quests/waterwayacave.md#stage-35)
- NOT reached stage 10 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-10)


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

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | Got Cithurn's talisman<br><span class="qnote">⚡ A scripted event can now trigger on [Waterwayacave 1](../maps/waterwayacave1.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Waterwayacave 1](../maps/waterwayacave1.md).</span> | [Cithurn](../monsters/waterwayhermit.md) | 1× [Cithurn's talisman](../items/cithurn_talisman.md) |
| <span id="stage-20"></span>[20](#route-20) | Found gold on waytolake7b | reading a sign on [Waytolake 7b](../maps/waytolake7b.md) | 653× [Gold coins](../items/gold.md) |
| <span id="stage-30"></span>[30](#route-30) | Found gem 1 on waytolake6<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytolake 6](../maps/waytolake6.md).</span> | stepping on a trigger on [Waytolake 6](../maps/waytolake6.md) | 1× [Sharpened gem](../items/gem4.md) |
| <span id="stage-40"></span>[40](#route-40) | Found gem 2 on waytolake6<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waytolake 6](../maps/waytolake6.md).</span> | stepping on a trigger on [Waytolake 6](../maps/waytolake6.md) | 1× [Polished sparkling gem](../items/gem5.md) |
| <span id="stage-50"></span>[50](#route-50) | Met Aemens | [Aemens](../monsters/aemens.md) | – |
| <span id="stage-60"></span>[60](#route-60) | Was warned about Aemens | [Taret](../monsters/taret.md) | – |
| <span id="stage-70"></span>[70](#route-70) | Told Aemens the neighbor warned you about her | [Aemens](../monsters/aemens.md) | – |
| <span id="stage-75"></span>[75](#route-75) | Taret tells you to be more careful what you say | [Taret](../monsters/taret.md) | – |
| <span id="stage-80"></span>[80](#route-80) | Looted corpse in waterway cave | reading a sign on [Waterwayacave 2](../maps/waterwayacave2.md) | [Rusted iron sword](../items/rusted_iron_sword.md), [Broken wooden buckler](../items/broken_buckler.md), [Crude ring of block](../items/ring_crude_block.md), [Crude leather cap](../items/hat3.md), [Gold coins](../items/gold.md) |
| <span id="stage-90"></span>[90](#route-90) | Got repreimanded by Cithurn | [Cithurn](../monsters/waterwayhermit.md) | – |
| <span id="stage-100"></span>[100](#route-100) | Petted Cithurn's cat | [Cithurn's cat](../monsters/cithurncat.md) | 25 XP |
| <span id="stage-110"></span>[110](#route-110) | Have discovered hidden room<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waterwayacavex](../maps/waterwayacavex.md).</span> | stepping on a trigger on [Waterwayacavex](../maps/waterwayacavex.md) | – |
| <span id="stage-120"></span>[120](#route-120) | Returned Cithurn's talisman after initially saying you would keep it. | [Cithurn](../monsters/waterwayhermit.md) | – |
| <span id="stage-130"></span>[130](#route-130) | Found old clothes<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Waterwaya 6](../maps/waterwaya6.md).</span> | stepping on a trigger on [Waterwaya 6](../maps/waterwaya6.md) | 4× [Old tunic](../items/tunic_old.md) |
| <span id="stage-140"></span>[140](#route-140) | Met Teksin | [Teksin](../monsters/teksin.md) | – |
| <span id="stage-150"></span>[150](#route-150) | Purchased potion of lightning attack | [Teksin](../monsters/teksin.md) | 1× [Potion of lightning attack](../items/pot_light_attack.md) |
| <span id="stage-160"></span>[160](#route-160) | Mentioned Remgard - Teksin | [Teksin](../monsters/teksin.md) | – |
| <span id="stage-170"></span>[170](#route-170) | Been to Remgard<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Remgard 0](../maps/remgard0.md).</span> | stepping on a trigger on [Remgard 0](../maps/remgard0.md) | – |
| <span id="stage-180"></span>[180](#route-180) | Talked to Yolgen about the castle | [Yolgen](../monsters/yolgen.md) | – |
| <span id="stage-190"></span>[190](#route-190) | Talked to Yolgen about Flagstone | [Yolgen](../monsters/yolgen.md) | – |
| <span id="stage-200"></span>[200](#route-200) | Saw bird from lookout | walking into a blocked passage on [Waytolake 12](../maps/waytolake12.md) | – |
| <span id="stage-210"></span>210 | Found opal at lookout | dialogue `lookout_down_3`, never started directly | – |
| <span id="stage-220"></span>220 | You will never get this quest stage (used for lookout)<br><span class="qnote">🔓 You can finally access a previously blocked area on [Laerothisland 3](../maps/laerothisland3.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Mountainlake 1](../maps/mountainlake1.md).</span><br><span class="qnote">🔓 You can finally access a previously blocked area on [Waytolake 12](../maps/waytolake12.md).</span> | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-230"></span>[230](#route-230) | bought Brimhaven bed<br><span class="qnote">🔓 You can finally access a previously blocked area on [Brimhaven inn east](../maps/brimhaven_inn_east.md).</span> | [Melona](../monsters/melona.md) | – |
| <span id="stage-240"></span>[240](#route-240) | Despawned monsters in graveyard<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Graveyard 1](../maps/graveyard1.md).</span> | stepping on a trigger on [Graveyard 1](../maps/graveyard1.md) | varies by route (see below) |
| <span id="stage-250"></span>[250](#route-250) | Looted arulir secret room<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Arulircave 5](../maps/arulircave5.md).</span> | stepping on a trigger on [Arulircave 5](../maps/arulircave5.md) | [Sharpened gem](../items/gem4.md), [Polished sparkling gem](../items/gem5.md), [Gold coins](../items/gold.md), [Polished gem](../items/gem3.md) |

</div>

<span id="untraced"></span>*No trigger found:* as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished.

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Cithurn · 1 way"

    **Way 1:** Talk to [Cithurn](../monsters/waterwayhermit.md), choose “I think I need more help to be able to complete my mission.”

    - **Needs:** not yet stage 10, 90; not reached stage 70 of [Just the beginning](../quests/waterwayacave.md#stage-70); reached stage 50 of [Trial by fire](../quests/charwood2.md#stage-50); reached stage 35 of [Just the beginning](../quests/waterwayacave.md#stage-35)
    - **Gives:** 1× [Cithurn's talisman](../items/cithurn_talisman.md)
    - *“Here. Take this talisman. It does much to dispel evil forces. I acquired it long ago, and it has kept me safe over the years. Since you…”*


<span id="route-20"></span>

??? note "Stage 20 · reading a sign on waytolake7b · 1 way"

    **Way 1:** Reading a sign on [Waytolake 7b](../maps/waytolake7b.md)

    - **Needs:** not yet stage 20
    - **Gives:** 653× [Gold coins](../items/gold.md)
    - *“You found some gold amongst the bones!”*


<span id="route-30"></span>

??? note "Stage 30 · stepping on a trigger on waytolake6 · 1 way"

    **Way 1:** Stepping on a trigger on [Waytolake 6](../maps/waytolake6.md)

    - **Needs:** not yet stage 30
    - **Gives:** 1× [Sharpened gem](../items/gem4.md)
    - *“You find a partly visible gem sticking out of the exposed rock.”*


<span id="route-40"></span>

??? note "Stage 40 · stepping on a trigger on waytolake6 · 1 way"

    **Way 1:** Stepping on a trigger on [Waytolake 6](../maps/waytolake6.md)

    - **Needs:** not yet stage 40
    - **Gives:** 1× [Polished sparkling gem](../items/gem5.md)
    - *“You find a partly visible gem sticking out of the exposed rock.”*


<span id="route-50"></span>

??? note "Stage 50 · Aemens · 1 way"

    **Way 1:** Talk to [Aemens](../monsters/aemens.md), automatic

    - *“Don't you know that it's rude to walk into someone's house without knocking?”*


<span id="route-60"></span>

??? note "Stage 60 · Taret · 1 way"

    **Way 1:** Talk to [Taret](../monsters/taret.md), choose “Can you tell me anything about the local area?”

    - *“The nastiest person in town is probably my neighbor. *laughs*. Be careful about walking in on her!”*


<span id="route-70"></span>

??? note "Stage 70 · Aemens · 1 way"

    **Way 1:** Talk to [Aemens](../monsters/aemens.md), choose “Your neighbor was right. He said you were not always a nice person.”

    - **Needs:** stage 60; not yet stage 75
    - *“Did he now! Well, I'll have a word or two to say to him later! What do you want?”*


<span id="route-75"></span>

??? note "Stage 75 · Taret · 1 way"

    **Way 1:** Talk to [Taret](../monsters/taret.md), choose “You are right. I told her you warned me that she was not always nice to strangers, but I think that just…”

    - **Needs:** stage 70; not yet stage 75
    - *“Thanks kid. *sigh*. I expect she will be around here later to complain about that. You should be more careful what you say to people.”*


<span id="route-80"></span>

??? note "Stage 80 · reading a sign on waterwayacave2 · 1 way"

    **Way 1:** Reading a sign on [Waterwayacave 2](../maps/waterwayacave2.md), choose “You decide to take everything.”

    - **Needs:** not yet stage 80
    - **Gives:** [Rusted iron sword](../items/rusted_iron_sword.md), [Broken wooden buckler](../items/broken_buckler.md), [Crude ring of block](../items/ring_crude_block.md), [Crude leather cap](../items/hat3.md), [Gold coins](../items/gold.md)


<span id="route-90"></span>

??? note "Stage 90 · Cithurn · 1 way"

    **Way 1:** Talk to [Cithurn](../monsters/waterwayhermit.md), choose “I'm looking for someone.”

    - **Needs:** not yet stage 90; not reached stage 10 of [Just the beginning](../quests/waterwayacave.md#stage-10)
    - *“Well I'm the only one here. Perhaps you should leave. Come back when you have learned some manners.”*


<span id="route-100"></span>

??? note "Stage 100 · Cithurn's cat · 2 ways"

    **Way 1:** Talk to [Cithurn's cat](../monsters/cithurncat.md), choose “[You scratch the cat behind the ear]”

    - **Needs:** not yet stage 100
    - *“Purr ... Purr.”*

    **Way 2:** Talk to [Cithurn's cat](../monsters/cithurncat.md), choose “[You stroke the cat]”

    - **Needs:** not yet stage 100
    - *“Purr ... Purr.”*


<span id="route-110"></span>

??? note "Stage 110 · stepping on a trigger on waterwayacavex · 1 way"

    **Way 1:** Stepping on a trigger on [Waterwayacavex](../maps/waterwayacavex.md)

    - **Needs:** not yet stage 110
    - *“You have discovered a hidden room!”*


<span id="route-120"></span>

??? note "Stage 120 · Cithurn · 1 way"

    **Way 1:** Talk to [Cithurn](../monsters/waterwayhermit.md), choose “Yes. I changed my mind about keeping it.”

    - **Needs:** not yet stage 120; reached stage 70 of [Just the beginning](../quests/waterwayacave.md#stage-70); hand over 1× [Cithurn's talisman](../items/cithurn_talisman.md)
    - *“Thank you. It seems you do have more honor than I thought.”*


<span id="route-130"></span>

??? note "Stage 130 · stepping on a trigger on waterwaya6 · 1 way"

    **Way 1:** Stepping on a trigger on [Waterwaya 6](../maps/waterwaya6.md), choose “[Take the clothes]”

    - **Needs:** not yet stage 130
    - **Gives:** 4× [Old tunic](../items/tunic_old.md)
    - *“The clothes smell musty and are falling apart.”*


<span id="route-140"></span>

??? note "Stage 140 · Teksin · 1 way"

    **Way 1:** Talk to [Teksin](../monsters/teksin.md), automatic

    - **Needs:** not yet stage 140
    - *“Hello. My name is Teksin. I'm a trader. Who are you?”*


<span id="route-150"></span>

??? note "Stage 150 · Teksin · 1 way"

    **Way 1:** Talk to [Teksin](../monsters/teksin.md), choose “OK. I'll take it.”

    - **Needs:** stage 140; not yet stage 150; pay 4,999 gold
    - **Gives:** 1× [Potion of lightning attack](../items/pot_light_attack.md)
    - *“Use it wisely. Such a potion is very hard to obtain. It is unlikely I will have any more to sell in the future.”*


<span id="route-160"></span>

??? note "Stage 160 · Teksin · 1 way"

    **Way 1:** Talk to [Teksin](../monsters/teksin.md), choose “I'm looking for my brother, Andor. He looks a bit like me.”

    - **Needs:** stage 140
    - *“This is as close as I can get coming this way. I am an experienced traveler, and I know that Remgard is close. It's north across this…”*


<span id="route-170"></span>

??? note "Stage 170 · stepping on a trigger on remgard0 · 1 way"

    **Way 1:** Stepping on a trigger on [Remgard 0](../maps/remgard0.md)



<span id="route-180"></span>

??? note "Stage 180 · Yolgen · 1 way"

    **Way 1:** Talk to [Yolgen](../monsters/yolgen.md), choose “Can you tell me more about Mt. Galmore?”

    - **Needs:** reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80)
    - *“However, recently more and more of the most foul monsters are coming from the mountain and we have to fend them off. There are rumors that…”*


<span id="route-190"></span>

??? note "Stage 190 · Yolgen · 1 way"

    **Way 1:** Talk to [Yolgen](../monsters/yolgen.md), choose “Can you tell me more about Flagstone?”

    - **Needs:** reached stage 80 of [Rumblings](../quests/rumblings.md#stage-80)
    - *“Flagstone Prison was built four hundred years ago by house Gorland of Stoutford, and was used until the Noble Wars, when the house was…”*


<span id="route-200"></span>

??? note "Stage 200 · walking into a blocked passage on waytolake12 · 1 way"

    **Way 1:** Walking into a blocked passage on [Waytolake 12](../maps/waytolake12.md), choose “Look up at the sky.”

    - **Needs:** not yet stage 200
    - *“You see a bird, perhaps a hawk, high in the sky.”*


<span id="route-230"></span>

??? note "Stage 230 · Melona · 1 way"

    **Way 1:** Talk to [Melona](../monsters/melona.md), choose “I'll take it.”

    - **Needs:** not yet stage 230; pay 90 gold
    - *“Thank you for your patronage. You can use any available bed.”*


<span id="route-240"></span>

??? note "Stage 240 · stepping on a trigger on graveyard1 · 4 ways"

    **Way 1:** Stepping on a trigger on [Graveyard 1](../maps/graveyard1.md)

    - **Needs:** not yet stage 240; killed 1× [Graveyard king](../monsters/graveyardking.md); hand over 1× [Ancient text](../items/graveyardtext.md)
    - **Gives:** removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard0, removes monsters from graveyard1, removes monsters from graveyard1
    - *“The ancient text crumbles and turns to dust. The defeat of the undead master seems to have lifted the spell animating the remaining…”*

    **Way 2:** Stepping on a trigger on [Graveyard 1](../maps/graveyard1.md)

    - **Needs:** not yet stage 240; killed 1× [Graveyard king](../monsters/graveyardking.md)
    - **Gives:** removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard0, removes monsters from graveyard1, removes monsters from graveyard1
    - *“The defeat of the undead master seems to have lifted the spell animating the remaining corpses and they return to their graves.”*

    **Way 3:** Stepping on a trigger on [Graveyard 1](../maps/graveyard1.md)

    - **Needs:** killed 1× [Graveyard king](../monsters/graveyardking.md)

    **Way 4:** Stepping on a trigger on [Graveyard 1](../maps/graveyard1.md)

    - **Needs:** not yet stage 240; killed 1× [Graveyard king](../monsters/graveyardking.md)
    - **Gives:** removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard1, removes monsters from graveyard0, removes monsters from graveyard1, removes monsters from graveyard1
    - *“The defeat of the undead master seems to have lifted the spell animating the remaining corpses and they return to their graves.”*


<span id="route-250"></span>

??? note "Stage 250 · stepping on a trigger on arulircave5 · 1 way"

    **Way 1:** Stepping on a trigger on [Arulircave 5](../maps/arulircave5.md), choose “[Plunder the loot]”

    - **Needs:** not yet stage 250
    - **Gives:** [Sharpened gem](../items/gem4.md), [Polished sparkling gem](../items/gem5.md), [Gold coins](../items/gold.md), [Polished gem](../items/gem3.md)
    - *“You have 'acquired' some gold and other valuable gems!”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 22 lines added |
| [v0.7.4](../versions/0.7.4.md) | Stages added: 200, 210, 220<br>Dialogue: 2 lines added, 1 line changed<br>· text: “Flagstone Prison was built four hundred years ago by house Gorland of…” → “Flagstone Prison was built four hundred years ago by house Gorland of…” |
| [v0.7.11](../versions/0.7.11.md) | Stages added: 230<br>Dialogue: 1 line added |
| [v0.7.12](../versions/0.7.12.md) | Stages added: 240<br>Dialogue: 3 lines added, 1 line changed |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 1 line changed |
| [v0.8.11](../versions/0.8.11.md) | Stages added: 250<br>Dialogue: 1 line added |
| [v0.8.14](../versions/0.8.14.md) | Dialogue: 1 line changed<br>· text: “However, recently more and more of the most foul monsters are coming …” → “However, recently more and more of the most foul monsters are coming …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=nondisplay_2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=nondisplay_2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=nondisplay_2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=nondisplay_2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=nondisplay_2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `nondisplay_2` |
    | Name in game data | `Placeholder for hidden quest stages 2 (not displayed)` |
    | showInLog | 0 |
    | Stage IDs | 10, 20, 30, 40, 50, 60, 70, 75, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250 |
    | Dialogue nodes setting stages | 10: `cithurn_51`, 20: `sign_waytolake7b_1`, 30: `lostfound1`, 40: `lostfound2`, 50: `aemens_0`, 60: `taret_3`, 70: `aemens_3`, 75: `taret_5`, 80: `waterwatcaveloot2`, 90: `cithurn_80`, 100: `cithurncatmeow_1`, 100: `cithurncatmeow_2`, 110: `waterwaycavex_1`, 120: `cithurn_111`, 130: `old_clothes_2`, 140: `teksin12`, 150: `teksin110`, 160: `teksin50`, 170: `been_to_remgard`, 180: `yolgen_surroundings_2c`, 190: `yolgen_surroundings_1`, 200: `lookout_up_1`, 210: `lookout_down_3`, 230: `melona_2a`, 240: `graveyardday2`, 240: `graveyardday2a`, 240: `boss_killed1`, 250: `arulir_secret_room_loot_2` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
