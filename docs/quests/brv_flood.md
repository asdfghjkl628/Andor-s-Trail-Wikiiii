---
description: "Much water is a quest in Andor's Trail, started by walking into a blocked passage on brimhaven_brother1_to_2. 17 stages, 1,500 XP in total. I found two not very bright brothers in a cellar of their house. They seemed to be talking about some sinister plan."
---

# Much water

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `brv_flood` |
| **In journal** | Yes |
| **Stages** | 17 (completes at 200) |
| **Started by** | walking into a blocked passage on [Brimhaven brother 1 to 2](../maps/brimhaven_brother1_to_2.md) |
| **NPCs involved** | [Alkapoan](../monsters/brv_richman.md), [Alvies](../monsters/brv_alvies.md), [Attohead](../monsters/brv_attohead.md), [Guard](../monsters/guard.md#v-brv_exit_guard), [Mustura](../monsters/brv_guard_captain.md) |
| **Locations** | [Brimhaven 3](../maps/brimhaven3.md), [Brimhaven 4](../maps/brimhaven4.md), [Brimhaven brother 1 to 2](../maps/brimhaven_brother1_to_2.md), [Brimhaven house 1](../maps/brimhaven_house1.md) |
| **Total XP** | 1,500 |
| **Related quests** | 5 |

</div>

## Overview

> I found two not very bright brothers in a cellar of their house. They seemed to be talking about some sinister plan.

## Prerequisites to start

None: talk to walking into a blocked passage on [Brimhaven brother 1 to 2](../maps/brimhaven_brother1_to_2.md) to begin.


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Brimhaven story flags (hidden flag)](brv_nondisplay.md#stage-100) | stage 100 reached, for stages 100, 110 here |
| Unlocks | [Search for Andor](andor.md#stage-65) | stage 65 there needs stages 120, 130 here |
| Unlocks | [Search for Andor](andor.md#stage-910) | stage 910 there needs stage 200 here |
| Unlocks | [Brimhaven story flags (hidden flag)](brv_nondisplay.md#stage-71) | stage 71 there needs stages 52, 70 here |
| Unlocks | [Brimhaven story flags (hidden flag)](brv_nondisplay.md#stage-81) | stage 81 there needs stages 52, 70 here |
| Unlocks | [Brimhaven story flags (hidden flag)](brv_nondisplay.md#stage-100) | stage 100 there needs stages 52, 70 here |
| Unlocks | [Brimhaven story flags (hidden flag)](brv_nondisplay.md#stage-110) | stage 110 there needs stage 200 here |
| Unlocks | [Brimhaven story flags (hidden flag)](brv_nondisplay.md#stage-120) | stage 120 there needs stage 200 here |
| Unlocks | [Galmore story flags (hidden flag)](galmore_nondisplayed.md#stage-20) | stage 20 there needs stage 200 here |
| Unlocks | [Galmore story flags (hidden flag)](galmore_nondisplayed.md#stage-21) | stage 21 there needs stage 200 here |
| Unlocks | [A place to forge](place_to_forge.md#stage-20) | stage 20 there needs stage 130 here |
| Unlocks | [A place to forge](place_to_forge.md#stage-30) | stage 30 there needs stage 200 here |
| Unlocks | [A place to forge](place_to_forge.md#stage-35) | stage 35 there needs stage 200 here |
| Unlocks | [A place to forge](place_to_forge.md#stage-40) | stage 40 there needs stage 200 here |
| Unlocks | [A place to forge](place_to_forge.md#stage-50) | stage 50 there needs stage 200 here |
| Unlocks | [Undertell story flags (hidden flag)](undertell_hidden.md#stage-15) | stage 15 there needs stage 200 here |
| Blocks | [Brimhaven story flags (hidden flag)](brv_nondisplay.md#stage-71) | reaching stages 54, 70, 80 here closes stage 71 there |
| Blocks | [Brimhaven story flags (hidden flag)](brv_nondisplay.md#stage-81) | reaching stages 54, 70, 80 here closes stage 81 there |
| Blocks | [Brimhaven story flags (hidden flag)](brv_nondisplay.md#stage-100) | reaching stages 54, 70, 80 here closes stage 100 there |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">I found two not very bright brothers in a cellar of their house.… ▸</span><span class="l">▴ less</span></summary>I found two not very bright brothers in a cellar of their house. They seemed to be talking about some sinister plan.</details><br><span class="qnote">🔓 You can finally access a previously blocked area on [Brimhaven brother 1 to 2](../maps/brimhaven_brother1_to_2.md).</span> | walking into a blocked passage on [Brimhaven brother 1 to 2](../maps/brimhaven_brother1_to_2.md) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">They were planning to destroy the great dam of Brimhaven. They just… ▸</span><span class="l">▴ less</span></summary>They were planning to destroy the great dam of Brimhaven. They just could not agree how they would do it.</details> | [Alvies](../monsters/brv_alvies.md) | – |
| <span id="stage-30"></span>[30](#route-30) | They asked me to help them. | [Alvies](../monsters/brv_alvies.md) | removes monsters from brimhaven1 |
| <span id="stage-50"></span>[50](#route-50) | I have agreed to destroy the dam for them. | [Alvies](../monsters/brv_alvies.md) | 1× [Hand Axe](../items/hand_axe.md) |
| <span id="stage-52"></span>[52](#route-52) | The brothers gave me a hand axe that could weaken the dam in a vulnerable place. | [Alvies](../monsters/brv_alvies.md) | 1× [Hand Axe](../items/hand_axe.md) |
| <span id="stage-53"></span>[53](#route-53) | I took another hand axe. This time I shouldn't lose it.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven brother 1 to 2](../maps/brimhaven_brother1_to_2.md).</span> | stepping on a trigger on [Brimhaven brother 1 to 2](../maps/brimhaven_brother1_to_2.md) | 1× [Hand Axe](../items/hand_axe.md) |
| <span id="stage-54"></span>[54](#route-54) | I found the weak spot in the dam and started hacking at the wood.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven 1](../maps/brimhaven1.md).</span> | stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md) | 500 XP, spawns monsters on brimhaven3, spawns monsters on brimhaven4, spawns monsters on brimhaven4 |
| <span id="stage-56"></span>[56](#route-56) | Water came pouring through the hole in the dam. A lot of water!<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven 1](../maps/brimhaven1.md).</span> | stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md) | spawns monsters on brimhaven3, spawns monsters on brimhaven4, spawns monsters on brimhaven4 |
| <span id="stage-70"></span>[70](#route-70) | I refused to destroy the dam for the brothers. | [Alvies](../monsters/brv_alvies.md) | faction “brv_brothers” set to -1 |
| <span id="stage-72"></span>[72](#route-72) | <details class="jt"><summary><span class="s">Given what I overheard, I was not allowed to leave. The two brothers… ▸</span><span class="l">▴ less</span></summary>Given what I overheard, I was not allowed to leave. The two brothers attacked me.</details> | [Alvies](../monsters/brv_alvies.md) | faction “brv_brothers” set to -1 |
| <span id="stage-75"></span>[75](#route-75) | <br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven brother 1 to 2](../maps/brimhaven_brother1_to_2.md).</span> | stepping on a trigger on [Brimhaven brother 1 to 2](../maps/brimhaven_brother1_to_2.md) | – |
| <span id="stage-80"></span>[80](#route-80) | <details class="jt"><summary><span class="s">Someone else destroyed the dam and water came pouring through a hole… ▸</span><span class="l">▴ less</span></summary>Someone else destroyed the dam and water came pouring through a hole in the dam. A lot of water!</details><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Brimhaven 1](../maps/brimhaven1.md).</span> | stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md) | spawns monsters on brimhaven3, spawns monsters on brimhaven4, spawns monsters on brimhaven4 |
| <span id="stage-100"></span>[100](#route-100) | <details class="jt"><summary><span class="s">The Brimhaven guards have informed me that I may not leave the town… ▸</span><span class="l">▴ less</span></summary>The Brimhaven guards have informed me that I may not leave the town until they have investigated who destroyed the dam.</details> | [Guard](../monsters/guard.md#v-brv_exit_guard), [Mustura](../monsters/brv_guard_captain.md) | – |
| <span id="stage-110"></span>[110](#route-110) | <details class="jt"><summary><span class="s">I have promised to track down the real perpetrators. However, I… ▸</span><span class="l">▴ less</span></summary>I have promised to track down the real perpetrators. However, I still cannot leave the town.</details> | [Mustura](../monsters/brv_guard_captain.md) | – |
| <span id="stage-120"></span>[120](#route-120) | <details class="jt"><summary><span class="s">The two brothers did not know their boss's name, but he seemed to… ▸</span><span class="l">▴ less</span></summary>The two brothers did not know their boss's name, but he seemed to have a lot of gold.</details> | [Alvies](../monsters/brv_alvies.md) | – |
| <span id="stage-130"></span>[130](#route-130) | <details class="jt"><summary><span class="s">The rich man living up on the hill of Brimhaven seemed to know more… ▸</span><span class="l">▴ less</span></summary>The rich man living up on the hill of Brimhaven seemed to know more than he admitted.</details> | [Alkapoan](../monsters/brv_richman.md) | – |
| <span id="stage-150"></span>[150](#route-150) | <details class="jt"><summary><span class="s">The rich man boasted that he had been bribed by an important man in… ▸</span><span class="l">▴ less</span></summary>The rich man boasted that he had been bribed by an important man in Loneford to sabotage the dam.</details> | [Alkapoan](../monsters/brv_richman.md) | 1× [Alkapoans's letters](../items/alkapoans_letters.md), sets stage 65 of [Search for Andor](../quests/andor.md#stage-65) |
| <span id="stage-200"></span>[200](#route-200) | <details class="jt"><summary><span class="s">I gave the letters as a piece of evidence to the captain of the… ▸</span><span class="l">▴ less</span></summary>I gave the letters as a piece of evidence to the captain of the guard. Now it is up to them to deal with the rich man.</details> **(ends quest)** | [Mustura](../monsters/brv_guard_captain.md) | 1,000 XP, removes monsters from brimhaven4, removes monsters from brimhaven4, removes monsters from brimhaven4, removes monsters from brimhaven3, removes monsters from brimhaven_house1, spawns monsters on brimhaven1, spawns monsters on brimhaven_house1, spawns monsters on brimhaven_house1 |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · walking into a blocked passage on brimhaven_brother1_to_2 · 1 way"

    **Way 1:** Walking into a blocked passage on [Brimhaven brother 1 to 2](../maps/brimhaven_brother1_to_2.md)

    - *“[You eavesdrop on the middle of the conversation. ] ... have to make sure no one finds out what we are going to do.”*


<span id="route-20"></span>

??? note "Stage 20 · Alvies · 1 way"

    **Way 1:** Talk to [Alvies](../monsters/brv_alvies.md), automatic

    - *“[It seems they still have not seen you, because they have their backs turned to you.] Your way of destroying the dam will not work. Better…”*


<span id="route-30"></span>

??? note "Stage 30 · Alvies · 1 way"

    **Way 1:** Talk to [Alvies](../monsters/brv_alvies.md), automatic

    - **Needs:** stage 30
    - **Gives:** removes monsters from brimhaven1
    - *“Would you assist us in destroying the dam?”*


<span id="route-50"></span>

??? note "Stage 50 · Alvies · 1 way"

    **Way 1:** Talk to [Alvies](../monsters/brv_alvies.md), choose “OK, I would like to help you destroy the dam.”

    - **Needs:** stage 30
    - **Gives:** 1× [Hand Axe](../items/hand_axe.md)
    - *“To not attract attention the best way to destroy the dam would be to take this small axe. Use it at the weak point of the dam in the dry…”*


<span id="route-52"></span>

??? note "Stage 52 · Alvies · 1 way"

    **Way 1:** Talk to [Alvies](../monsters/brv_alvies.md), choose “OK, I would like to help you destroy the dam.”

    - **Needs:** stage 30
    - **Gives:** 1× [Hand Axe](../items/hand_axe.md)
    - *“To not attract attention the best way to destroy the dam would be to take this small axe. Use it at the weak point of the dam in the dry…”*


<span id="route-53"></span>

??? note "Stage 53 · stepping on a trigger on brimhaven_brother1_to_2 · 1 way"

    **Way 1:** Stepping on a trigger on [Brimhaven brother 1 to 2](../maps/brimhaven_brother1_to_2.md)

    - **Gives:** 1× [Hand Axe](../items/hand_axe.md)
    - *“So lucky! Another small hand axe lies here.”*


<span id="route-54"></span>

??? note "Stage 54 · stepping on a trigger on brimhaven1 · 1 way"

    **Way 1:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md), choose “Start hacking on the wood.”

    - **Needs:** stage 52; not yet stage 54, 70; wearing [Hand Axe](../items/hand_axe.md)
    - **Gives:** spawns monsters on brimhaven3, spawns monsters on brimhaven4, spawns monsters on brimhaven4
    - <small>Also: sets stage 71 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-71), sets stage 81 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-81), sets stage 100 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-100)</small>
    - *“Water comes pouring through the hole in the dam. A lot of water!”*


<span id="route-56"></span>

??? note "Stage 56 · stepping on a trigger on brimhaven1 · 1 way"

    **Way 1:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md), choose “Start hacking on the wood.”

    - **Needs:** stage 52; not yet stage 54, 70; wearing [Hand Axe](../items/hand_axe.md)
    - **Gives:** spawns monsters on brimhaven3, spawns monsters on brimhaven4, spawns monsters on brimhaven4
    - <small>Also: sets stage 71 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-71), sets stage 81 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-81), sets stage 100 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-100)</small>
    - *“Water comes pouring through the hole in the dam. A lot of water!”*


<span id="route-70"></span>

??? note "Stage 70 · Alvies · 1 way"

    **Way 1:** Talk to [Alvies](../monsters/brv_alvies.md), choose “No, I will never do that!”

    - **Needs:** stage 30
    - **Gives:** faction “brv_brothers” set to -1
    - *“Then we have to shut you up and do it ourselves.”*


<span id="route-72"></span>

??? note "Stage 72 · Alvies · 1 way"

    **Way 1:** Talk to [Alvies](../monsters/brv_alvies.md), choose “No, I will never do that!”

    - **Needs:** stage 30
    - **Gives:** faction “brv_brothers” set to -1
    - *“Then we have to shut you up and do it ourselves.”*


<span id="route-75"></span>

??? note "Stage 75 · stepping on a trigger on brimhaven_brother1_to_2 · 1 way"

    **Way 1:** Stepping on a trigger on [Brimhaven brother 1 to 2](../maps/brimhaven_brother1_to_2.md)

    - **Needs:** carry 1× [Coin bag (with the name "Alkapoan" on it)](../items/brv_richmans_coin_bag.md)


<span id="route-80"></span>

??? note "Stage 80 · stepping on a trigger on brimhaven1 · 1 way"

    **Way 1:** Stepping on a trigger on [Brimhaven 1](../maps/brimhaven1.md)

    - **Needs:** stage 70; not yet stage 80
    - **Gives:** spawns monsters on brimhaven3, spawns monsters on brimhaven4, spawns monsters on brimhaven4
    - <small>Also: sets stage 71 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-71), sets stage 81 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-81), sets stage 100 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-100)</small>
    - *“Water comes pouring through a hole in the dam. A lot of water! If not the brothers, then someone else destroyed the dam.”*


<span id="route-100"></span>

??? note "Stage 100 · Guard, Mustura · 3 ways"

    **Way 1:** Talk to [Guard](../monsters/guard.md#v-brv_exit_guard), automatic

    - *“Stop! All foreigners have to stay in town until we have investigated who destroyed the great dam.”*

    **Way 2:** Talk to [Mustura](../monsters/brv_guard_captain.md), choose “[Lie] I have no idea, but I will try to help you.”

    - **Needs:** reached stage 100 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-100)
    - *“Thank you. But be aware that you are not allowed to leave the town until we have found out how the dam was destroyed.”*

    **Way 3:** Talk to [Mustura](../monsters/brv_guard_captain.md), choose “No, not yet, but I will try to help you.”

    - **Needs:** stage 110
    - *“Come back when you have a proof, and until then stop accusing people. In the meantime, you are not allowed to leave the city.”*


<span id="route-110"></span>

??? note "Stage 110 · Mustura · 2 ways"

    **Way 1:** Talk to [Mustura](../monsters/brv_guard_captain.md), choose “[Lie] I have no idea, but I will try to help you.”

    - **Needs:** reached stage 100 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-100)
    - *“Thank you. But be aware that you are not allowed to leave the town until we have found out how the dam was destroyed.”*

    **Way 2:** Talk to [Mustura](../monsters/brv_guard_captain.md), choose “No, not yet, but I will try to help you.”

    - **Needs:** stage 110
    - *“Come back when you have a proof, and until then stop accusing people. In the meantime, you are not allowed to leave the city.”*


<span id="route-120"></span>

??? note "Stage 120 · Alvies · 1 way"

    **Way 1:** Talk to [Alvies](../monsters/brv_alvies.md), choose “Can you tell me who is your boss?”

    - **Needs:** stage 56, 110
    - *“We don't know him by name. He looked very rich and I think he lives in the western town alone in a big house.”*


<span id="route-130"></span>

??? note "Stage 130 · Alkapoan · 1 way"

    **Way 1:** Talk to [Alkapoan](../monsters/brv_richman.md), choose “Are you sure?”

    - **Needs:** stage 110, 120; not yet stage 150
    - *“I... I.... know nothing. Really, it is the truth!”*


<span id="route-150"></span>

??? note "Stage 150 · Alkapoan · 1 way"

    **Way 1:** Talk to [Alkapoan](../monsters/brv_richman.md), choose “I don't believe a word you say. [Half-lie] The two brothers told me that you paid them for destroying the dam.”

    - **Needs:** stage 120, 130
    - **Gives:** 1× [Alkapoans's letters](../items/alkapoans_letters.md), sets stage 65 of [Search for Andor](../quests/andor.md#stage-65)
    - *“[Breaks down] I was bribed by the people of Loneford to sabotage the dam. Here are some letters I exchanged with them, that prove what I…”*


<span id="route-200"></span>

??? note "Stage 200 · Mustura · 1 way"

    **Way 1:** Talk to [Mustura](../monsters/brv_guard_captain.md), choose “Alkapoan was behind it. Here are letters proving his guilt. He is waiting at his home for you to arrest him.”

    - **Needs:** stage 110; hand over 1× [Alkapoans's letters](../items/alkapoans_letters.md)
    - **Gives:** removes monsters from brimhaven4, removes monsters from brimhaven4, removes monsters from brimhaven4, removes monsters from brimhaven3, removes monsters from brimhaven_house1, spawns monsters on brimhaven1, spawns monsters on brimhaven_house1, spawns monsters on brimhaven_house1
    - <small>Also: clears stage 100 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-100)</small>
    - *“We will check this and if it is true then you can leave the town.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 15 lines added |
| [v0.7.12](../versions/0.7.12.md) | Stage 10 journal text changed<br>Stage 30 journal text changed<br>Stage 50 journal text changed<br>Stage 52 journal text changed<br>Stage 54 journal text changed<br>Stage 70 journal text changed<br>Stage 72 journal text changed<br>Stage 100 journal text changed<br>Stage 110 journal text changed<br>Stage 200 journal text changed |
| [v0.7.13](../versions/0.7.13.md) | Stages added: 53<br>Dialogue: 1 line added, 1 line changed<br>· text: “[Breaks down] I was bribed by the people of Loneford to sabotage the …” → “[Breaks down] I was bribed by the people of Loneford to sabotage the …” |
| [v0.8.14](../versions/0.8.14.md) | Stage 100 journal text changed<br>Stage 110 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_flood.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_flood.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_flood.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_flood.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=brv_flood.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `brv_flood` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 50, 52, 53, 54, 56, 70, 72, 75, 80, 100, 110, 120, 130, 150, 200 |
    | Dialogue nodes setting stages | 10: `brv_brothers_0`, 20: `brv_brothers_6`, 30: `brv_brothers_10`, 50: `brv_brothers_12`, 52: `brv_brothers_12`, 53: `brv_brothers_another_axe_10`, 54: `brv_flood_0_10`, 56: `brv_flood_0_10`, 70: `brv_brothers_11`, 72: `brv_brothers_11`, 75: `brv_brothers_found_coin_bag`, 80: `brv_flood_20_10`, 100: `brv_exit_forbidden_10`, 100: `brv_guard_captain_40`, 100: `brv_guard_captain_23`, 110: `brv_guard_captain_40`, 110: `brv_guard_captain_23`, 120: `brv_brothers_15`, 130: `brv_richman_10`, 150: `brv_richman_20`, 200: `brv_guard_captain_30` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
