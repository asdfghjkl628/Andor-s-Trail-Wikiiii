---
description: "A quick glance is a quest in Andor's Trail, started by Anakis (brimhaven7). 14 stages, 1,500 XP in total. I talked to Anakis. He told me that his sister, Juttarka, went into the cave and did not come out again."
---

# A quick glance

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `quick_glance` |
| **In journal** | Yes |
| **Stages** | 14 (completes at 90) |
| **Started by** | [Anakis](../monsters/anakis.md) ([Brimhaven 7](../maps/brimhaven7.md)) |
| **NPCs involved** | [Anakis](../monsters/anakis.md), [Fangwurm](../monsters/fangwurm.md) |
| **Locations** | [Brimhaven 7](../maps/brimhaven7.md), [Brimhaven anakis house](../maps/brimhaven_anakis_house.md), [Brimhaven church](../maps/brimhaven_church.md) |
| **Total XP** | 1,500 |
| **Related quests** | 2 |

</div>

## Overview

> I talked to Anakis. He told me that his sister, Juttarka, went into the cave and did not come out again.

## Prerequisites to start

Start with [Anakis](../monsters/anakis.md) ([Brimhaven 7](../maps/brimhaven7.md)). Required:

- NOT reached stage 10 of [A quick glance](../quests/quick_glance.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Quick glance: statue found (hidden flag)](quick_glance_hidden_found_statue.md#stage-10) | stage 10 reached, for stages 40, 50 here |
| Requires | [Quick glance: statue found (hidden flag)](quick_glance_hidden_found_statue.md#stage-30) | stage 30 reached, for stage 90 here |
| Blocked by | [Quick glance: statue found (hidden flag)](quick_glance_hidden_found_statue.md#stage-10) | stage 10 must NOT be reached, for stage 20 here |
| Blocked by | [Quick glance: statue found (hidden flag)](quick_glance_hidden_found_statue.md#stage-30) | stage 30 must NOT be reached, for stages 80, 85 here |
| Unlocks | [Quick glance: statue found (hidden flag)](quick_glance_hidden_found_statue.md#stage-20) | stage 20 there needs stage 60 here |
| Unlocks | [Quick glance: statue found (hidden flag)](quick_glance_hidden_found_statue.md#stage-30) | stage 30 there needs stage 60 here |
| Unlocks | [Quick glance: position (hidden flag)](quick_glance_hidden_position.md#stage-110) | stage 110 there needs stage 20 here |
| Blocks | [Quick glance: position (hidden flag)](quick_glance_hidden_position.md#stage-110) | reaching stages 15, 20, 50 here closes stage 110 there |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>[10](#route-10) | <details class="jt"><summary><span class="s">I talked to Anakis. He told me that his sister, Juttarka, went into… ▸</span><span class="l">▴ less</span></summary>I talked to Anakis. He told me that his sister, Juttarka, went into the cave and did not come out again.</details> | [Anakis](../monsters/anakis.md) | – |
| <span id="stage-15"></span>[15](#route-15) | I denied to help Anakis to find his sister, Juttarka. | [Anakis](../monsters/anakis.md) | – |
| <span id="stage-20"></span>[20](#route-20) | I agreed to help Anakis find his sister, Juttarka. | [Anakis](../monsters/anakis.md) | – |
| <span id="stage-40"></span>[40](#route-40) | I found a stone statue that looked almost like a real woman. | [Anakis](../monsters/anakis.md), walking into a blocked passage on [Basiliskcave 2](../maps/basiliskcave2.md) | – |
| <span id="stage-50"></span>[50](#route-50) | <details class="jt"><summary><span class="s">I told Anakis about the statue. He thinks that it is his sister,… ▸</span><span class="l">▴ less</span></summary>I told Anakis about the statue. He thinks that it is his sister, Juttarka, and thanked me for helping him.</details> | [Anakis](../monsters/anakis.md) | 100 XP |
| <span id="stage-60"></span>[60](#route-60) | Anakis asked me if I could avenge his sister. | [Anakis](../monsters/anakis.md) | – |
| <span id="stage-70"></span>[70](#route-70) | I agreed to avenge Anakis' sister, Juttarka, and kill the Basilisk. | [Anakis](../monsters/anakis.md) | – |
| <span id="stage-75"></span>[75](#route-75) | <details class="jt"><summary><span class="s">I should talk to Fangwurm, the priest of west Brimhaven, to see if… ▸</span><span class="l">▴ less</span></summary>I should talk to Fangwurm, the priest of west Brimhaven, to see if he has some information about how it may be possible to help Anakis' sister.</details> | [Anakis](../monsters/anakis.md) | – |
| <span id="stage-77"></span>[77](#route-77) | <details class="jt"><summary><span class="s">Fangwurm told me that the Basilisk's blood has special properties.… ▸</span><span class="l">▴ less</span></summary>Fangwurm told me that the Basilisk's blood has special properties. It can protect against damage if applied to the skin. Fresh, warm, Basilisk's blood might even be able to heal a person that has been turned to stone.</details> | [Fangwurm](../monsters/fangwurm.md) | – |
| <span id="stage-78"></span>[78](#route-78) | <details class="jt"><summary><span class="s">The priest Fangwurm told me that the potion maker in Fallhaven sells… ▸</span><span class="l">▴ less</span></summary>The priest Fangwurm told me that the potion maker in Fallhaven sells special crystal vials that are resistent to the blood of a Basilisk, and I will need one to handle it.</details> | [Fangwurm](../monsters/fangwurm.md) | – |
| <span id="stage-79"></span>79 | <details class="jt"><summary><span class="s">I should search the other rooms in this cave for a mirror that I can… ▸</span><span class="l">▴ less</span></summary>I should search the other rooms in this cave for a mirror that I can use to protect me from the glance of the Basilisk.</details> | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-80"></span>[80](#route-80) | I killed the Basilisk.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Basiliskcave 2](../maps/basiliskcave2.md).</span> | stepping on a trigger on [Basiliskcave 2](../maps/basiliskcave2.md) | – |
| <span id="stage-85"></span>[85](#route-85) | I saved the life of Anakis' sister Juttarka.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Basiliskcave 2](../maps/basiliskcave2.md).</span> | stepping on a trigger on [Basiliskcave 2](../maps/basiliskcave2.md) | 400 XP, spawns monsters on brimhaven_anakis_house |
| <span id="stage-90"></span>[90](#route-90) | I told Anakis that I killed the Basilisk. **(ends quest)** | [Anakis](../monsters/anakis.md) | 1,000 XP, spawns monsters on brimhaven_anakis_house, removes monsters from brimhaven7 |

</div>

<span id="untraced"></span>*No trigger found:* as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished.

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-10"></span>

??? note "Stage 10 · Anakis · 1 way"

    **Way 1:** Talk to [Anakis](../monsters/anakis.md), automatic

    - **Needs:** not yet stage 10
    - *“Hello my name is Anakis. I hope you can you help me. Yesterday my sister Juttarka left the city to go up to this hill. She did not come…”*


<span id="route-15"></span>

??? note "Stage 15 · Anakis · 1 way"

    **Way 1:** Talk to [Anakis](../monsters/anakis.md), choose “No, that's none of my business.”

    - **Needs:** not yet stage 10
    - *“Oh, thats's sad.”*


<span id="route-20"></span>

??? note "Stage 20 · Anakis · 1 way"

    **Way 1:** Talk to [Anakis](../monsters/anakis.md), choose “Yes, I will search for your sister.”

    - **Needs:** not yet stage 10; not reached stage 10 of [Quick glance: statue found (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-10)
    - *“Thank you. My sister has long hair and is wearing a long skirt. Please take care. Fangwurm the priest in western Brimhaven told us about a…”*


<span id="route-40"></span>

??? note "Stage 40 · Anakis, walking into a blocked passage on basiliskcave2 · 2 ways"

    **Way 1:** Talk to [Anakis](../monsters/anakis.md), choose “I found a statue that looks almost like a real woman. [Describe the statue to Anakis]”

    - **Needs:** not yet stage 10; reached stage 10 of [Quick glance: statue found (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-10)
    - *“Oh no, that's her! Thank you for helping me to find out what happened to her. I think it was the Basilisk who did that to her.”*

    **Way 2:** Walking into a blocked passage on [Basiliskcave 2](../maps/basiliskcave2.md)

    - **Needs:** stage 10; not yet stage 40


<span id="route-50"></span>

??? note "Stage 50 · Anakis · 1 way"

    **Way 1:** Talk to [Anakis](../monsters/anakis.md), choose “I found a statue that looks almost like a real woman. [Describe the statue to Anakis]”

    - **Needs:** not yet stage 10; reached stage 10 of [Quick glance: statue found (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-10)
    - *“Oh no, that's her! Thank you for helping me to find out what happened to her. I think it was the Basilisk who did that to her.”*


<span id="route-60"></span>

??? note "Stage 60 · Anakis · 1 way"

    **Way 1:** Talk to [Anakis](../monsters/anakis.md), automatic

    - **Needs:** not yet stage 60, 70
    - *“Can you find the Basilisk and kill it? And maybe there is a way to help my sister. But take care that the same fate that happened to my…”*


<span id="route-70"></span>

??? note "Stage 70 · Anakis · 2 ways"

    **Way 1:** Talk to [Anakis](../monsters/anakis.md), choose “I can't imagine how to help your sister but I will take revenge for her and find a way to kill that Basilisk.”

    - **Needs:** not yet stage 60, 70; not killed 1× [Ancient basilisk](../monsters/old_basilisk.md)

    **Way 2:** Talk to [Anakis](../monsters/anakis.md), choose “I will take revenge, but first tell me how I might help your sister.”

    - **Needs:** not yet stage 60, 70; not killed 1× [Ancient basilisk](../monsters/old_basilisk.md)
    - *“I have no idea how to help her. But maybe Fangwurm the priest in western Brimhaven has some information.”*


<span id="route-75"></span>

??? note "Stage 75 · Anakis · 1 way"

    **Way 1:** Talk to [Anakis](../monsters/anakis.md), choose “I will take revenge, but first tell me how I might help your sister.”

    - **Needs:** not yet stage 60, 70; not killed 1× [Ancient basilisk](../monsters/old_basilisk.md)
    - *“I have no idea how to help her. But maybe Fangwurm the priest in western Brimhaven has some information.”*


<span id="route-77"></span>

??? note "Stage 77 · Fangwurm · 1 way"

    **Way 1:** Talk to [Fangwurm](../monsters/fangwurm.md), choose “Can you please tell me again, what you know about the Basilisk's blood?”

    - **Needs:** stage 77
    - *“The Basilisk's blood has special properties. It can protect against damage if applied to the skin. Fresh, warm, Basilisks blood might even…”*


<span id="route-78"></span>

??? note "Stage 78 · Fangwurm · 1 way"

    **Way 1:** Talk to [Fangwurm](../monsters/fangwurm.md), choose “I will find a way to kill the Basilisk.”

    - **Needs:** stage 77
    - *“You would need a special crystal vial that is resistant to the Basilisk's blood to handle it. The potion maker in Fallhaven might sell…”*


<span id="route-80"></span>

??? note "Stage 80 · stepping on a trigger on basiliskcave2 · 1 way"

    **Way 1:** Stepping on a trigger on [Basiliskcave 2](../maps/basiliskcave2.md)

    - **Needs:** stage 60; killed 1× [Ancient basilisk](../monsters/old_basilisk.md); not reached stage 30 of [Quick glance: statue found (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-30)
    - *“You killed the Basilisk and the blood flows out of its wounds.”*


<span id="route-85"></span>

??? note "Stage 85 · stepping on a trigger on basiliskcave2 · 1 way"

    **Way 1:** Stepping on a trigger on [Basiliskcave 2](../maps/basiliskcave2.md), choose “I use the crystal vial and pour the blood over the stone statue.”

    - **Needs:** stage 60; killed 1× [Ancient basilisk](../monsters/old_basilisk.md); not reached stage 30 of [Quick glance: statue found (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-30); carry 1× [Empty crystal vial](../items/empty_crystal_vial.md)
    - **Gives:** spawns monsters on brimhaven_anakis_house
    - <small>Also: sets stage 20 of [Quick glance: statue found (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-20), sets stage 30 of [Quick glance: statue found (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-30)</small>
    - *“Slowly the stone statue gets colorful and starts to move. You healed the woman! After she comes back to life, she thanks you and tells you…”*


<span id="route-90"></span>

??? note "Stage 90 · Anakis · 3 ways"

    **Way 1:** Talk to [Anakis](../monsters/anakis.md), choose “I already found the Basilisk and killed it.”

    - **Needs:** not yet stage 60, 70; killed 1× [Ancient basilisk](../monsters/old_basilisk.md)
    - **Gives:** spawns monsters on brimhaven_anakis_house, removes monsters from brimhaven7
    - *“Thank you for taking revenge for Juttarka. I will go now and mourn for my sister.”*

    **Way 2:** Talk to [Anakis](../monsters/anakis.md), automatic

    - **Needs:** not yet stage 90; latest stage of [A quick glance](../quests/quick_glance.md#stage-85) is 85
    - **Gives:** spawns monsters on brimhaven_anakis_house, removes monsters from brimhaven7
    - *“Thank you so much for rescuing my sister Juttarka. She just came out of the cave and told me what you did for her. I will now go home, too.”*

    **Way 3:** Talk to [Anakis](../monsters/anakis.md), choose “I found the Basilisk and killed it, but I decided to take the blood for myself.”

    - **Needs:** not yet stage 90; killed 1× [Ancient basilisk](../monsters/old_basilisk.md); reached stage 30 of [Quick glance: statue found (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-30)
    - **Gives:** spawns monsters on brimhaven_anakis_house, removes monsters from brimhaven7
    - *“Oh no. Why did you not even try to help her? Now i will go and mourn for my sister.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 15 lines added |
| [v0.7.12](../versions/0.7.12.md) | Stage 15 journal text changed<br>Stage 77 journal text changed<br>Stage 79 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `quick_glance` |
    | showInLog | 1 |
    | Stage IDs | 10, 15, 20, 40, 50, 60, 70, 75, 77, 78, 79, 80, 85, 90 |
    | Dialogue nodes setting stages | 10: `anakis_help_find_sister`, 15: `anakis_deny_help`, 20: `anakis_agreed_find_sister`, 40: `anakis_thank_finding_sister`, 40: `basiliskcave2_sister_statue_questprogress`, 50: `anakis_thank_finding_sister`, 60: `anakis_can_you_take_revenge`, 70: `anakis_agreed_take_revenge`, 70: `anakis_talk_to_priest`, 75: `anakis_talk_to_priest`, 77: `fangwurm_info_about_blood`, 78: `fangwurm_info_vial`, 80: `basiliskcave2_ask_heal_sister`, 85: `basiliskcave2_decided_to_heal`, 90: `anakis_thank_taking_revenge`, 90: `anakis_thank_healing_sister`, 90: `anakis_sad_blood_not_use_for_sister` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
