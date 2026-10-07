# A quick glance

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `quick_glance` |
| **In journal** | Yes |
| **Stages** | 14 (completes at 90) |
| **Started by** | [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)) |
| **NPCs involved** | [Anakis](../monsters/anakis.md), [Fangwurm](../monsters/fangwurm.md) |
| **Locations** | [brimhaven7](../maps/brimhaven7.md), [brimhaven_anakis_house](../maps/brimhaven_anakis_house.md), [brimhaven_church](../maps/brimhaven_church.md) |
| **Total XP** | 1,500 |
| **Related quests** | 2 |

</div>

## Overview

> I talked to Anakis. He told me that his sister, Juttarka, went into the cave and did not come out again.

## Prerequisites to start

Start with [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)). Required:

- NOT reached stage 10 of [A quick glance](../quests/quick_glance.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [quick_glance_hidden_found_statue (hidden flag)](quick_glance_hidden_found_statue.md#stage-10) | stage 10 reached, for stages 40, 50 here |
| Requires | [quick_glance_hidden_found_statue (hidden flag)](quick_glance_hidden_found_statue.md#stage-30) | stage 30 reached, for stage 90 here |
| Blocked by | [quick_glance_hidden_found_statue (hidden flag)](quick_glance_hidden_found_statue.md#stage-10) | stage 10 must NOT be reached, for stage 20 here |
| Blocked by | [quick_glance_hidden_found_statue (hidden flag)](quick_glance_hidden_found_statue.md#stage-30) | stage 30 must NOT be reached, for stages 80, 85 here |
| Unlocks | [quick_glance_hidden_found_statue (hidden flag)](quick_glance_hidden_found_statue.md#stage-20) | stage 20 there needs stage 60 here |
| Unlocks | [quick_glance_hidden_found_statue (hidden flag)](quick_glance_hidden_found_statue.md#stage-30) | stage 30 there needs stage 60 here |
| Unlocks | [quick_glance_hidden_position (hidden flag)](quick_glance_hidden_position.md#stage-110) | stage 110 there needs stage 20 here |
| Blocks | [quick_glance_hidden_position (hidden flag)](quick_glance_hidden_position.md#stage-110) | reaching stages 15, 20, 50 here closes stage 110 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | I talked to Anakis. He told me that his sister, Juttarka, went into the cave and did not come out again. | [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)) | – | – |
| <span id="stage-15"></span>15 | I denied to help Anakis to find his sister, Juttarka. | [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)) | – | – |
| <span id="stage-20"></span>20 | I agreed to help Anakis find his sister, Juttarka. | [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)) | – | – |
| <span id="stage-40"></span>40 | I found a stone statue that looked almost like a real woman. | [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md))<br>walking into a blocked passage on [basiliskcave2](../maps/basiliskcave2.md) | stage 10 | – |
| <span id="stage-50"></span>50 | I told Anakis about the statue. He thinks that it is his sister, Juttarka, and thanked me for helping him. | [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)) | – | 100 XP |
| <span id="stage-60"></span>60 | Anakis asked me if I could avenge his sister. | [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)) | – | – |
| <span id="stage-70"></span>70 | I agreed to avenge Anakis' sister, Juttarka, and kill the Basilisk. | [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)) | – | – |
| <span id="stage-75"></span>75 | I should talk to Fangwurm, the priest of west Brimhaven, to see if he has some information about how it may be possible to help Anakis' sister. | [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)) | – | – |
| <span id="stage-77"></span>77 | Fangwurm told me that the Basilisk's blood has special properties. It can protect against damage if applied to the skin. Fresh, warm, Basilisk's blood might even be able to heal a person that has been turned to stone. | [Fangwurm](../monsters/fangwurm.md) ([brimhaven_church](../maps/brimhaven_church.md)) | – | – |
| <span id="stage-78"></span>78 | The priest Fangwurm told me that the potion maker in Fallhaven sells special crystal vials that are resistent to the blood of a Basilisk, and I will need one to handle it. | [Fangwurm](../monsters/fangwurm.md) ([brimhaven_church](../maps/brimhaven_church.md)) | stage 77 | – |
| <span id="stage-79"></span>79 | I should search the other rooms in this cave for a mirror that I can use to protect me from the glance of the Basilisk. | *no trigger in the game data or code* <sup>[?](#untraced)</sup> | – | – |
| <span id="stage-80"></span>80 | I killed the Basilisk.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Basiliskcave2](../maps/basiliskcave2.md).</span> | stepping on a trigger on [basiliskcave2](../maps/basiliskcave2.md) | stage 60 | – |
| <span id="stage-85"></span>85 | I saved the life of Anakis' sister Juttarka.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Basiliskcave2](../maps/basiliskcave2.md).</span> | stepping on a trigger on [basiliskcave2](../maps/basiliskcave2.md) | carry 1× [Empty crystal vial](../items/empty_crystal_vial.md), stage 60 | 400 XP<br>sets stage 20 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-20)<br>sets stage 30 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-30)<br>spawns monsters on brimhaven_anakis_house |
| <span id="stage-90"></span>90 | I told Anakis that I killed the Basilisk. **(completes quest)** | [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)) | stage 85 | 1,000 XP<br>spawns monsters on brimhaven_anakis_house<br>removes monsters from brimhaven7 |

<span id="untraced"></span>*No trigger*: as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished content, or set in a way this wiki can't trace yet. That doesn't make it a secret: treat anything you hear about it as speculation.

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)) → the conversation leads here automatically — **conditions:** NOT reached stage 10 of [A quick glance](../quests/quick_glance.md#stage-10) → **stage 10**. NPC: “Hello my name is Anakis. I hope you can you help me. Yesterday my sister Juttarka left the city to go up to this hill.…”

???+ note "Stage 15: 1 route"

    1. Talk to [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)) → choose “No, that's none of my business.” — **conditions:** NOT reached stage 10 of [A quick glance](../quests/quick_glance.md#stage-10) → **stage 15**. NPC: “Oh, thats's sad.”

???+ note "Stage 20: 1 route"

    1. Talk to [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)) → choose “Yes, I will search for your sister.” — **conditions:** NOT reached stage 10 of [A quick glance](../quests/quick_glance.md#stage-10); NOT reached stage 10 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-10) → **stage 20**. NPC: “Thank you. My sister has long hair and is wearing a long skirt. Please take care. Fangwurm the priest in western…”

???+ note "Stage 40: 2 routes"

    1. Talk to [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)) → choose “I found a statue that looks almost like a real woman. [Describe the statue to Anakis]” — **conditions:** NOT reached stage 10 of [A quick glance](../quests/quick_glance.md#stage-10); reached stage 10 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-10) → **stage 40**. NPC: “Oh no, that's her! Thank you for helping me to find out what happened to her. I think it was the Basilisk who did that…”
    2. walking into a blocked passage on [basiliskcave2](../maps/basiliskcave2.md) → the conversation leads here automatically — **conditions:** reached stage 10 of [A quick glance](../quests/quick_glance.md#stage-10); NOT reached stage 40 of [A quick glance](../quests/quick_glance.md#stage-40) → **stage 40**

???+ note "Stage 50: 1 route"

    1. Talk to [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)) → choose “I found a statue that looks almost like a real woman. [Describe the statue to Anakis]” — **conditions:** NOT reached stage 10 of [A quick glance](../quests/quick_glance.md#stage-10); reached stage 10 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-10) → **stage 50**. NPC: “Oh no, that's her! Thank you for helping me to find out what happened to her. I think it was the Basilisk who did that…”

???+ note "Stage 60: 1 route"

    1. Talk to [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)) → the conversation leads here automatically — **conditions:** NOT reached stage 60 of [A quick glance](../quests/quick_glance.md#stage-60); NOT reached stage 70 of [A quick glance](../quests/quick_glance.md#stage-70) → **stage 60**. NPC: “Can you find the Basilisk and kill it? And maybe there is a way to help my sister. But take care that the same fate…”

???+ note "Stage 70: 2 routes"

    1. Talk to [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)) → choose “I can't imagine how to help your sister but I will take revenge for her and find a way to kill that Basilisk.” — **conditions:** NOT reached stage 60 of [A quick glance](../quests/quick_glance.md#stage-60); NOT reached stage 70 of [A quick glance](../quests/quick_glance.md#stage-70); NOT killed 1× [Ancient basilisk](../monsters/old_basilisk.md) → **stage 70**
    2. Talk to [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)) → choose “I will take revenge, but first tell me how I might help your sister.” — **conditions:** NOT reached stage 60 of [A quick glance](../quests/quick_glance.md#stage-60); NOT reached stage 70 of [A quick glance](../quests/quick_glance.md#stage-70); NOT killed 1× [Ancient basilisk](../monsters/old_basilisk.md) → **stage 70**. NPC: “I have no idea how to help her. But maybe Fangwurm the priest in western Brimhaven has some information.”

???+ note "Stage 75: 1 route"

    1. Talk to [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)) → choose “I will take revenge, but first tell me how I might help your sister.” — **conditions:** NOT reached stage 60 of [A quick glance](../quests/quick_glance.md#stage-60); NOT reached stage 70 of [A quick glance](../quests/quick_glance.md#stage-70); NOT killed 1× [Ancient basilisk](../monsters/old_basilisk.md) → **stage 75**. NPC: “I have no idea how to help her. But maybe Fangwurm the priest in western Brimhaven has some information.”

???+ note "Stage 77: 1 route"

    1. Talk to [Fangwurm](../monsters/fangwurm.md) ([brimhaven_church](../maps/brimhaven_church.md)) → choose “Can you please tell me again, what you know about the Basilisk's blood?” — **conditions:** reached stage 77 of [A quick glance](../quests/quick_glance.md#stage-77) → **stage 77**. NPC: “The Basilisk's blood has special properties. It can protect against damage if applied to the skin. Fresh, warm,…”

???+ note "Stage 78: 1 route"

    1. Talk to [Fangwurm](../monsters/fangwurm.md) ([brimhaven_church](../maps/brimhaven_church.md)) → choose “I will find a way to kill the Basilisk.” — **conditions:** reached stage 77 of [A quick glance](../quests/quick_glance.md#stage-77) → **stage 78**. NPC: “You would need a special crystal vial that is resistant to the Basilisk's blood to handle it. The potion maker in…”

???+ note "Stage 80: 1 route"

    1. stepping on a trigger on [basiliskcave2](../maps/basiliskcave2.md) → the conversation leads here automatically — **conditions:** killed 1× [Ancient basilisk](../monsters/old_basilisk.md); NOT reached stage 30 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-30); reached stage 60 of [A quick glance](../quests/quick_glance.md#stage-60) → **stage 80**. NPC: “You killed the Basilisk and the blood flows out of its wounds.”

???+ note "Stage 85: 1 route"

    1. stepping on a trigger on [basiliskcave2](../maps/basiliskcave2.md) → choose “I use the crystal vial and pour the blood over the stone statue.” — **conditions:** killed 1× [Ancient basilisk](../monsters/old_basilisk.md); NOT reached stage 30 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-30); reached stage 60 of [A quick glance](../quests/quick_glance.md#stage-60); carry 1× [Empty crystal vial](../items/empty_crystal_vial.md) → **stage 85**; also sets stage 20 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-20), sets stage 30 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-30), spawns monsters on brimhaven_anakis_house. NPC: “Slowly the stone statue gets colorful and starts to move. You healed the woman! After she comes back to life, she…”

???+ note "Stage 90: 3 routes"

    1. Talk to [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)) → choose “I already found the Basilisk and killed it.” — **conditions:** NOT reached stage 60 of [A quick glance](../quests/quick_glance.md#stage-60); NOT reached stage 70 of [A quick glance](../quests/quick_glance.md#stage-70); killed 1× [Ancient basilisk](../monsters/old_basilisk.md) → **stage 90**; also spawns monsters on brimhaven_anakis_house, removes monsters from brimhaven7. NPC: “Thank you for taking revenge for Juttarka. I will go now and mourn for my sister.”
    2. Talk to [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)) → the conversation leads here automatically — **conditions:** NOT reached stage 90 of [A quick glance](../quests/quick_glance.md#stage-90); latest stage of [A quick glance](../quests/quick_glance.md#stage-85) is 85 → **stage 90**; also spawns monsters on brimhaven_anakis_house, removes monsters from brimhaven7. NPC: “Thank you so much for rescuing my sister Juttarka. She just came out of the cave and told me what you did for her. I…”
    3. Talk to [Anakis](../monsters/anakis.md) ([brimhaven7](../maps/brimhaven7.md)) → choose “I found the Basilisk and killed it, but I decided to take the blood for myself.” — **conditions:** NOT reached stage 90 of [A quick glance](../quests/quick_glance.md#stage-90); killed 1× [Ancient basilisk](../monsters/old_basilisk.md); reached stage 30 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-30) → **stage 90**; also spawns monsters on brimhaven_anakis_house, removes monsters from brimhaven7. NPC: “Oh no. Why did you not even try to help her? Now i will go and mourn for my sister.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 15 lines added |
| [v0.7.12](../versions/0.7.12.md) | stage 15 journal text changed; stage 77 journal text changed; stage 79 journal text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=quick_glance.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


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
