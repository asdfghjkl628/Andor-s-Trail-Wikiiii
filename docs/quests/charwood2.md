---
description: "Trial by fire is a quest in Andor's Trail, started by Kantya (tradehouse0). 6 stages, 7,000 XP in total. I've heard a story that the whole reason for the Charwood hills being invaded by the monsters in the first place was that something had been awoken deep in the Charwood mine. The people in the…"
---

# Trial by fire

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `charwood2` |
| **In journal** | Yes |
| **Stages** | 6 (completes at 50) |
| **Started by** | [Kantya](../monsters/kantya.md) ([Tradehouse 0](../maps/tradehouse0.md)) |
| **NPCs involved** | [Kantya](../monsters/kantya.md), [Maevalia](../monsters/maevalia.md), [Thukuzun](../monsters/thukuzun.md) |
| **Locations** | [Lostmine 11](../maps/lostmine11.md), [Tradehouse 0](../maps/tradehouse0.md) |
| **Total XP** | 7,000 |
| **Related quests** | 3 |

</div>

## Overview

> I've heard a story that the whole reason for the Charwood hills being invaded by the monsters in the first place was that something had been awoken deep in the Charwood mine. The people in the Charwood cabin say that the miners uncovered some sort of marking on the ground in a cave, with strange noises coming from below it. When they finally broke through the ground around the markings, all the…

## Prerequisites to start

Start with [Kantya](../monsters/kantya.md) ([Tradehouse 0](../maps/tradehouse0.md)). Required:

- reached stage 50 of [Destined for great things](../quests/charwood1.md#stage-50)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Destined for great things](charwood1.md#stage-50) | stage 50 reached, for stage 10 here |
| Unlocks | [General story flags 2 (hidden flag)](nondisplay_2.md#stage-10) | stage 10 there needs stage 50 here |
| Unlocks | [Just the beginning](waterwayacave.md#stage-15) | stage 15 there needs stage 50 here |
| Unlocks | [Just the beginning](waterwayacave.md#stage-20) | stage 20 there needs stage 50 here |
| Unlocks | [Just the beginning](waterwayacave.md#stage-25) | stage 25 there needs stage 50 here |
| Unlocks | [Just the beginning](waterwayacave.md#stage-30) | stage 30 there needs stage 50 here |
| Unlocks | [Just the beginning](waterwayacave.md#stage-35) | stage 35 there needs stage 50 here |
| Blocks | [Just the beginning](waterwayacave.md#stage-12) | reaching stage 50 here closes stage 12 there |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">I've heard a story that the whole reason for the Charwood hills… ▸</span><span class="l">▴ less</span></summary>I've heard a story that the whole reason for the Charwood hills being invaded by the monsters in the first place was that something had been awoken deep in the Charwood mine. The people in the Charwood cabin say that the miners uncovered some sort of marking on the ground in a cave, with strange noises coming from below it. When they finally broke through the ground around the markings, all the troubles started. I should talk to Maevalia again.</details> | [Kantya](../monsters/kantya.md) | – |
| <span id="stage-15"></span>[15](#route-15) | <details class="jt"><summary><span class="s">I've promised Maevalia to investigate the deeper parts of the… ▸</span><span class="l">▴ less</span></summary>I've promised Maevalia to investigate the deeper parts of the Charwood mine. I should be on the lookout for the dangerous monsters that inhabit the mine.</details><br><span class="qnote">🔓 You can finally access a previously blocked area on [Lostmine 0](../maps/lostmine0.md).</span> | [Maevalia](../monsters/maevalia.md) | – |
| <span id="stage-20"></span>[20](#route-20) | <details class="jt"><summary><span class="s">I've reached the part of the mine that was broken into. The air… ▸</span><span class="l">▴ less</span></summary>I've reached the part of the mine that was broken into. The air around here seems to get hotter as I get deeper into the mine.</details> | reading a sign on [Lostmine 4](../maps/lostmine4.md) | – |
| <span id="stage-30"></span>[30](#route-30) | <details class="jt"><summary><span class="s">Among the fires in the lower parts of the mine, I've encountered… ▸</span><span class="l">▴ less</span></summary>Among the fires in the lower parts of the mine, I've encountered some type of dragon-like creature. I guess this is the source of all the chaos in the mine. I should attempt to kill it and then venture back to Maevalia to tell her about it once I'm victorious.</details> | [Thukuzun](../monsters/thukuzun.md) | – |
| <span id="stage-40"></span>[40](#route-40) | I have presented one of the bones from the corpse of the Thukuzun to Maevalia. | [Maevalia](../monsters/maevalia.md) | – |
| <span id="stage-50"></span>[50](#route-50) | Maevalia was happy to hear that I killed the source of the monster invasion. **(ends quest)** | [Maevalia](../monsters/maevalia.md) | 7,000 XP; varies by route (see below) |

</div>

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Kantya · 1 way"

    **Way 1:** Talk to [Kantya](../monsters/kantya.md), choose “Is there anything I can do?”

    - **Needs:** reached stage 50 of [Destined for great things](../quests/charwood1.md#stage-50)
    - *“You've helped us this far. Talk to Maevalia again, she might have something else for you.”*


<span id="route-15"></span>

??? note "Stage 15 · Maevalia · 1 way"

    **Way 1:** Talk to [Maevalia](../monsters/maevalia.md), choose “I'll go down into the Charwood mine and investigate.”

    - **Needs:** stage 15
    - *“Thank you.”*


<span id="route-20"></span>

??? note "Stage 20 · reading a sign on lostmine4 · 1 way"

    **Way 1:** Reading a sign on [Lostmine 4](../maps/lostmine4.md)

    - *“The air around here is much hotter around the hole in the ground here than in the rest of this room. This must be where the miners found…”*


<span id="route-30"></span>

??? note "Stage 30 · Thukuzun · 1 way"

    **Way 1:** Talk to [Thukuzun](../monsters/thukuzun.md), automatic

    - *“Ah, another mortal that has come to bow before the might of Thukuzun.”*


<span id="route-40"></span>

??? note "Stage 40 · Maevalia · 1 way"

    **Way 1:** Talk to [Maevalia](../monsters/maevalia.md), automatic

    - **Needs:** stage 40
    - *“You actually killed it?”*


<span id="route-50"></span>

??? note "Stage 50 · Maevalia · 3 ways"

    **Way 1:** Talk to [Maevalia](../monsters/maevalia.md), choose “I'm just happy to help.”

    - **Needs:** stage 40
    - *“You are truly our hero. Thank you yet again.”*

    **Way 2:** Talk to [Maevalia](../monsters/maevalia.md), choose “How about some gold for all my troubles?”

    - **Needs:** stage 40
    - **Gives:** [Gold coins](../items/gold.md)
    - *“Certainly. Here is what we can spare. Thank you yet again.”*

    **Way 3:** Talk to [Maevalia](../monsters/maevalia.md), choose “I think that one of your most precious items will suffice as payment.”

    - **Needs:** stage 40
    - **Gives:** [Worn iron boots](../items/hboot_wirn.md), [Ring of surehit](../items/ring_atkch1.md)
    - *“I guess we have no choice but to agree. Here, take these. They used to belong to my mother.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=charwood2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=charwood2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=charwood2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=charwood2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=charwood2.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `charwood2` |
    | showInLog | 1 |
    | Stage IDs | 10, 15, 20, 30, 40, 50 |
    | Dialogue nodes setting stages | 10: `kantya23`, 15: `maevalia_d10`, 20: `sign_lostmine4`, 30: `thukuzun`, 40: `maevalia_h5`, 50: `maevalia_h9`, 50: `maevalia_h10`, 50: `maevalia_h12` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
