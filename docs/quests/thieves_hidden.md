---
description: "Thieves story flags is a hidden quest in Andor's Trail, started by Ambelie (foaming_flask). 11 stages. Must be never fulfilled"
---

# Thieves story flags

!!! info "Hidden story flag"
    An internal quest the game uses to track progress. It does not appear in the journal. The stage descriptions below are internal notes written by the developers and may be brief.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `thieves_hidden` |
| **In journal** | No (hidden flag) |
| **Stages** | 11 |
| **Started by** | [Ambelie](../monsters/ambelie.md) ([Foaming flask](../maps/foaming_flask.md)), [Ambelie](../monsters/ambelie.md) ([Foaming flask](../maps/foaming_flask.md)) |
| **NPCs involved** | [Ambelie](../monsters/ambelie.md), [Dying Patrol](../monsters/g03_deadpatrol_2.md), [Dying patrol](../monsters/g03_deadpatrol_1.md), [Feygard patrol sergeant](../monsters/g03_sergeant.md), [Thoronir](../monsters/thoronir.md), [Troublemaker](../monsters/troublemaker.md) |
| **Locations** | [Crackshot hideout 2](../maps/crackshot_hideout2.md), [Crackshot hideout 3](../maps/crackshot_hideout3.md), [Fallhaven church](../maps/fallhaven_church.md), [Fallhaven derelict 2](../maps/fallhaven_derelict2.md) |
| **Related quests** | 6 |

</div>

## Overview

> Must be never fulfilled

## Prerequisites to start

**Route 1** ([Ambelie](../monsters/ambelie.md) ([Foaming flask](../maps/foaming_flask.md))):

- reached stage 15 of [Immaculate kidnapping](../quests/Thieves02.md#stage-15)

**Route 2** ([Ambelie](../monsters/ambelie.md) ([Foaming flask](../maps/foaming_flask.md))):

- reached stage 21 of [Immaculate kidnapping](../quests/Thieves02.md#stage-21)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Thief apprentice](Thieves01.md#stage-20) | stage 20 reached, for stages 100, 110 here |
| Requires | [Thief apprentice](Thieves01.md#stage-45) | stage 45 reached, for stage 80 here |
| Requires | [Thief apprentice](Thieves01.md#stage-51) | stage 51 reached, for stage 100 here |
| Requires | [Thief apprentice](Thieves01.md#stage-55) | stage 55 reached, for stage 100 here |
| Requires | [Immaculate kidnapping](Thieves02.md#stage-15) | stage 15 reached, for stage 20 here |
| Requires | [Immaculate kidnapping](Thieves02.md#stage-21) | stage 21 reached, for stage 20 here |
| Requires | [Disallowed substance](bonemeal.md#stage-100) | stage 100 reached, for stage 80 here |
| Requires | [Score counters (hidden flag)](scores.md#stage-18) | stage 18 reached, for stage 80 here |
| Mutually exclusive | [Thief apprentice](Thieves01.md#stage-50) | stage 50 must NOT be reached, for stage 80 here |
| Mutually exclusive | [Thief apprentice](Thieves01.md#stage-60) | stage 60 must NOT be reached, for stages 100, 110 here |
| Mutually exclusive | [The ruthless Crackshot](Thieves03.md#stage-40) | stage 40 must NOT be reached, for stage 30 here |
| Blocked by | [Troubling times](troubling_times.md#stage-210) | stage 210 must NOT be reached, for stage 70 here |
| Unlocks | [Thief apprentice](Thieves01.md#stage-60) | stage 60 there needs stage 100 here |
| Unlocks | [The ruthless Crackshot](Thieves03.md#stage-26) | stage 26 there needs stage 40 here |

## Stages

<div class="stages" markdown>

| Stage | Journal entry | From | Rewards |
|---|---|---|---|
| <span id="stage-10"></span>10 | Must be never fulfilled<br><span class="qnote">🔓 You can finally access a previously blocked area on [Fallhaven gravedigger](../maps/fallhaven_gravedigger.md).</span> | *no trigger found* <sup>[?](#untraced)</sup> | – |
| <span id="stage-20"></span>[20](#route-20) | Block road1 | [Ambelie](../monsters/ambelie.md) | varies by route (see below) |
| <span id="stage-30"></span>[30](#route-30) | Spoke to dying Crackshot. Remove block road1<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crackshot hideout 3](../maps/crackshot_hideout3.md).</span><br><span class="qnote">🗺️ Part of [Road 1](../maps/road1.md) visibly changes.</span> | stepping on a trigger on [Crackshot hideout 3](../maps/crackshot_hideout3.md) | sets stage 40 of [The ruthless Crackshot](../quests/Thieves03.md#stage-40), removes monsters from road1 |
| <span id="stage-40"></span>[40](#route-40) | thieves3 - Found patrol 1<br><span class="qnote">🔓 You can finally access a previously blocked area on [Crackshot hideout 2](../maps/crackshot_hideout2.md).</span> | [Dying patrol](../monsters/g03_deadpatrol_1.md) | removes monsters from crackshot_hideout2 |
| <span id="stage-50"></span>[50](#route-50) | thieves3 - Found patrol 2<br><span class="qnote">🔓 You can finally access a previously blocked area on [Crackshot hideout 2](../maps/crackshot_hideout2.md).</span> | [Dying Patrol](../monsters/g03_deadpatrol_2.md) | removes monsters from crackshot_hideout2 |
| <span id="stage-60"></span>[60](#route-60) | thieves3 - Open chest<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crackshot hideout 3](../maps/crackshot_hideout3.md).</span> | stepping on a trigger on [Crackshot hideout 3](../maps/crackshot_hideout3.md) | – |
| <span id="stage-70"></span>[70](#route-70) | <details class="jt"><summary><span class="s">thieves3 - Open door (can currently not be fulfilled, beause the… ▸</span><span class="l">▴ less</span></summary>thieves3 - Open door (can currently not be fulfilled, beause the blessed key of luthor can't be obtained in the game)</details> | walking into a blocked passage on [Crackshot hideout 3](../maps/crackshot_hideout3.md) | – |
| <span id="stage-80"></span>[80](#route-80) | Talked about thieves to Thoronir | [Thoronir](../monsters/thoronir.md) | – |
| <span id="stage-90"></span>[90](#route-90) | Sergeant died. | [Feygard patrol sergeant](../monsters/g03_sergeant.md) | removes monsters from crackshot_hideout3 |
| <span id="stage-100"></span>[100](#route-100) | Gave journals | [Troublemaker](../monsters/troublemaker.md) | – |
| <span id="stage-110"></span>[110](#route-110) | Got reward | [Troublemaker](../monsters/troublemaker.md) | sets stage 60 of [Thief apprentice](../quests/Thieves01.md#stage-60), 900× [Gold coins](../items/gold.md) |

</div>

<span id="untraced"></span>*No trigger found:* as of v0.8.18, nothing in the game's dialogue, maps or code sets this stage. It may be unused or unfinished.

<small>Click a stage number for how to reach it, or a long journal entry to expand it.</small>

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How to reach each stage

Every route in the game data, including alternatives. To try a specific situation, use the **dialogue simulator** on the NPC's page.

<span id="route-20"></span>

??? note "Stage 20 · Ambelie · 2 ways"

    **Way 1:** Talk to [Ambelie](../monsters/ambelie.md), choose “(Knock her out) Time to sleep!”

    - **Needs:** reached stage 15 of [Immaculate kidnapping](../quests/Thieves02.md#stage-15)
    - **Gives:** sets stage 20 of [Immaculate kidnapping](../quests/Thieves02.md#stage-20), removes monsters from foaming_flask, spawns monsters on road1, applies condition carrying_ambelie
    - *“(You tap her on the back of the head with the handle of your weapon, and she falls unconscious)”*

    **Way 2:** Talk to [Ambelie](../monsters/ambelie.md), choose “Give me something of value, and you won't see me again.”

    - **Needs:** reached stage 21 of [Immaculate kidnapping](../quests/Thieves02.md#stage-21)
    - **Gives:** 1× [Sapphire Necklace](../items/g02_ambelie.md), sets stage 24 of [Immaculate kidnapping](../quests/Thieves02.md#stage-24), spawns monsters on road1
    - *“Take this and leave me, please.”*


<span id="route-30"></span>

??? note "Stage 30 · stepping on a trigger on crackshot_hideout3 · 1 way"

    **Way 1:** Stepping on a trigger on [Crackshot hideout 3](../maps/crackshot_hideout3.md), choose “What are you talking about?”

    - **Needs:** killed 1× [Crackshot](../monsters/g03_crackshot.md); not reached stage 40 of [The ruthless Crackshot](../quests/Thieves03.md#stage-40)
    - **Gives:** sets stage 40 of [The ruthless Crackshot](../quests/Thieves03.md#stage-40), removes monsters from road1
    - <small>Also: clears stage 20 of [Thieves story flags (hidden flag)](../quests/thieves_hidden.md#stage-20)</small>
    - *“The key is cursed .... She ... I am ... (Crackshot finally dies, emitting a soft bluish breath)”*


<span id="route-40"></span>

??? note "Stage 40 · Dying patrol · 1 way"

    **Way 1:** Talk to [Dying patrol](../monsters/g03_deadpatrol_1.md), automatic

    - **Needs:** not yet stage 50
    - **Gives:** removes monsters from crackshot_hideout2
    - *“(You see, horrified, how this man is bleeding out rapidly. He has countless cuts and his face is mutilated. You can almost hear his gasps.)”*


<span id="route-50"></span>

??? note "Stage 50 · Dying Patrol · 1 way"

    **Way 1:** Talk to [Dying Patrol](../monsters/g03_deadpatrol_2.md), choose “What guy?”

    - **Needs:** stage 40
    - **Gives:** removes monsters from crackshot_hideout2
    - *“No ... he's not .... Agggh! [He has stopped breathing. I cannot do anything for him. Better to move on.]”*


<span id="route-60"></span>

??? note "Stage 60 · stepping on a trigger on crackshot_hideout3 · 1 way"

    **Way 1:** Stepping on a trigger on [Crackshot hideout 3](../maps/crackshot_hideout3.md)



<span id="route-70"></span>

??? note "Stage 70 · walking into a blocked passage on crackshot_hideout3 · 1 way"

    **Way 1:** Walking into a blocked passage on [Crackshot hideout 3](../maps/crackshot_hideout3.md), choose “Insert the blessed key of Luthor into the lock.”

    - **Needs:** not reached stage 210 of [Troubling times](../quests/troubling_times.md#stage-210); carry 1× [Blessed key of luthor](../items/g03_luthor2.md)
    - *“The door opens.”*


<span id="route-80"></span>

??? note "Stage 80 · Thoronir · 1 way"

    **Way 1:** Talk to [Thoronir](../monsters/thoronir.md), choose “Fanamor, a member of Thieves' Guild, is severely wounded. Please give me a bandage for her!”

    - **Needs:** reached stage 18 of [Score counters (hidden flag)](../quests/scores.md#stage-18); reached stage 45 of [Thief apprentice](../quests/Thieves01.md#stage-45); reached stage 100 of [Disallowed substance](../quests/bonemeal.md#stage-100); not reached stage 50 of [Thief apprentice](../quests/Thieves01.md#stage-50)


<span id="route-90"></span>

??? note "Stage 90 · Feygard patrol sergeant · 1 way"

    **Way 1:** Talk to [Feygard patrol sergeant](../monsters/g03_sergeant.md), automatic

    - **Needs:** killed 1× [Crackshot](../monsters/g03_crackshot.md)
    - **Gives:** removes monsters from crackshot_hideout3
    - *“You ... Argh ... [The sergeant takes one final breath and then dies. You should have come earlier. Now you will never get to know what he…”*


<span id="route-100"></span>

??? note "Stage 100 · Troublemaker · 2 ways"

    **Way 1:** Talk to [Troublemaker](../monsters/troublemaker.md), choose “I've brought all the journals.”

    - **Needs:** reached stage 20 of [Thief apprentice](../quests/Thieves01.md#stage-20); not reached stage 60 of [Thief apprentice](../quests/Thieves01.md#stage-60); reached stage 55 of [Thief apprentice](../quests/Thieves01.md#stage-55); hand over 1× [Dunla's Journal](../items/Dunla_journal.md); hand over 1× [Fanamor's Journal](../items/Fanamor_journal.md); hand over 1× [Leta's Journal](../items/Leta_journal.md)
    - *“Well done kid! You can now consider yourself skilled enough to be a part of this guild.”*

    **Way 2:** Talk to [Troublemaker](../monsters/troublemaker.md), choose “I have the journals, but one of your spies, Fanamor, was killed by a Feygard scout.”

    - **Needs:** reached stage 20 of [Thief apprentice](../quests/Thieves01.md#stage-20); not reached stage 60 of [Thief apprentice](../quests/Thieves01.md#stage-60); latest stage of [Thief apprentice](../quests/Thieves01.md#stage-51) is 51; hand over 1× [Dunla's Journal](../items/Dunla_journal.md); hand over 1× [Fanamor's Journal](../items/Fanamor_journal.md); hand over 1× [Leta's Journal](../items/Leta_journal.md)
    - *“Well, that is the price of being one of us. There's always risk.”*


<span id="route-110"></span>

??? note "Stage 110 · Troublemaker · 1 way"

    **Way 1:** Talk to [Troublemaker](../monsters/troublemaker.md), choose “I gave you the journals, so where's my reward?”

    - **Needs:** stage 100; not yet stage 110; reached stage 20 of [Thief apprentice](../quests/Thieves01.md#stage-20); not reached stage 60 of [Thief apprentice](../quests/Thieves01.md#stage-60)
    - **Gives:** sets stage 60 of [Thief apprentice](../quests/Thieves01.md#stage-60), 900× [Gold coins](../items/gold.md)
    - *“You should talk with Umar. Maybe he has another task ... one that's more in your line of work, you know.”*



<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 12 lines added |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 1 line changed<br>· text: “(You tap her on the back of the head with the handle of your weapon, …” → “(You tap her on the back of the head with the handle of your weapon, …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=thieves_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=thieves_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=thieves_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=thieves_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=thieves_hidden.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `thieves_hidden` |
    | Name in game data | `Thieves Hidden` |
    | showInLog | 0 |
    | Stage IDs | 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110 |
    | Dialogue nodes setting stages | 20: `ambelie_guild02_4b`, 20: `ambelie_guild02_19`, 30: `guild03_hideout3_exit_3`, 40: `guild03_deadpatrol_1_1`, 50: `guild03_deadpatrol_2_3`, 60: `guild03_hideout3_open_chest`, 70: `guild03_hideout3_unlock`, 80: `thoronir_guild_2`, 90: `FeygardSerg_guild03_dead`, 100: `troublemaker_guild_11a`, 100: `troublemaker_guild_11b`, 110: `troublemaker_guild_12a` |
    | Dialogue nodes clearing stages | 20: `guild03_hideout3_exit_3` |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
