# More rats!

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `ratdom_mikhail` |
| **In journal** | Yes |
| **Stages** | 10 (completes at 90) |
| **Started by** | [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)), [Gruiik](../monsters/ratdom_mikhail.md) ([home](../maps/home.md)) |
| **NPCs involved** | [Gruiik](../monsters/ratdom_mikhail.md), [Mikhail](../monsters/mikhail.md) |
| **Locations** | [home](../maps/home.md), [waytogalmore0](../maps/waytogalmore0.md) |
| **Total XP** | 1,200 |
| **Related quests** | 2 |

</div>

## Overview

> A huge rat called Gruiik told me that they drove all the people out of this village.

## Prerequisites to start

**Route 1** ([Mikhail](../monsters/mikhail.md) ([home](../maps/home.md))):

- reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1)

**Route 2** ([Gruiik](../monsters/ratdom_mikhail.md) ([home](../maps/home.md))):

- nothing

**Route 3** (stepping on a trigger on [home](../maps/home.md)):

- reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1)
- reached stage 950 of [Yellow is it](../quests/ratdom_quest.md#stage-950)
- NOT reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-1) | stage 1 reached, for stages 10, 20, 52, 54, 70, 74, 90 here |
| Requires | [Yellow is it](ratdom_quest.md#stage-950) | stage 950 reached, for stages 10, 20, 52, 54, 70, 74, 90 here |
| Blocked by | [Yellow is it](ratdom_quest.md#stage-999) | stage 999 must NOT be reached, for stages 10, 20, 52, 54, 70, 74, 90 here |
| Unlocks | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-13) | stage 13 there needs stage 90 here |
| Unlocks | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-21) | stage 21 there needs stage 90 here |
| Unlocks | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-22) | stage 22 there needs stage 90 here |
| Unlocks | [ratdom_nondisplay (hidden flag)](ratdom_nondisplay.md#stage-23) | stage 23 there needs stage 90 here |
| Unlocks | [Yellow is it](ratdom_quest.md#stage-50) | stage 50 there needs stage 10 here |
| Unlocks | [Yellow is it](ratdom_quest.md#stage-940) | stage 940 there needs stage 90 here |
| Unlocks | [Yellow is it](ratdom_quest.md#stage-999) | stage 999 there needs stage 90 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | A huge rat called Gruiik told me that they drove all the people out of this village.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Home](../maps/home.md).</span> | [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md))<br>[Gruiik](../monsters/ratdom_mikhail.md) ([home](../maps/home.md))<br>stepping on a trigger on [home](../maps/home.md) | – | – |
| <span id="stage-20"></span>20 | Some two-legs were running around in the garden again. I should kill them.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Home](../maps/home.md).</span> | [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md))<br>[Gruiik](../monsters/ratdom_mikhail.md) ([home](../maps/home.md))<br>stepping on a trigger on [home](../maps/home.md) | – | – |
| <span id="stage-30"></span>30 | I have killed Mara.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossglen](../maps/crossglen.md).</span> | stepping on a trigger on [crossglen](../maps/crossglen.md) | – | removes monsters from crossglen_hall |
| <span id="stage-32"></span>32 | I have killed Tharal.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Crossglen](../maps/crossglen.md).</span> | stepping on a trigger on [crossglen](../maps/crossglen.md) | – | removes monsters from crossglen_hall |
| <span id="stage-52"></span>52 | I told Gruiik that I have killed Mara and Tharal.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Home](../maps/home.md).</span> | [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md))<br>[Gruiik](../monsters/ratdom_mikhail.md) ([home](../maps/home.md))<br>stepping on a trigger on [home](../maps/home.md) | stage 20 | 500 XP |
| <span id="stage-54"></span>54 | I lied to Gruiik that I have killed Mara and Tharal.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Home](../maps/home.md).</span> | [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md))<br>[Gruiik](../monsters/ratdom_mikhail.md) ([home](../maps/home.md))<br>stepping on a trigger on [home](../maps/home.md) | stage 20 | 500 XP |
| <span id="stage-70"></span>70 | Gruiik was hungry and asked to bring him bread.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Home](../maps/home.md).</span> | [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md))<br>[Gruiik](../monsters/ratdom_mikhail.md) ([home](../maps/home.md))<br>stepping on a trigger on [home](../maps/home.md) | stage 20 | – |
| <span id="stage-72"></span>72 | I found a bread in a bag hanging at the door of the Crossglen town hall. | walking into a blocked passage on [crossglen](../maps/crossglen.md) | – | gives 1× [Bread](../items/bread.md) |
| <span id="stage-74"></span>74 | I gave a bread to Gruiik.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Home](../maps/home.md).</span> | [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md))<br>[Gruiik](../monsters/ratdom_mikhail.md) ([home](../maps/home.md))<br>stepping on a trigger on [home](../maps/home.md) | hand over 1× [Bread](../items/bread.md), stage 20, stage 70 | 200 XP |
| <span id="stage-90"></span>90 | The huge rat ignored me after he had got the bread. **(completes quest)**<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Home](../maps/home.md).</span> | [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md))<br>[Gruiik](../monsters/ratdom_mikhail.md) ([home](../maps/home.md))<br>stepping on a trigger on [home](../maps/home.md) | stage 70, stage 74 | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 3 routes"

    1. Talk to [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) → choose “What are you doing in my house? Where is Mikhail?” — **conditions:** reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1) → **stage 10**. NPC: “We rats took over this village. I am Gruiik, their leader.”
    2. Talk to [Gruiik](../monsters/ratdom_mikhail.md) ([home](../maps/home.md)) → choose “What are you doing in my house? Where is Mikhail?” → **stage 10**. NPC: “We rats took over this village. I am Gruiik, their leader.”
    3. stepping on a trigger on [home](../maps/home.md) → choose “What are you doing in my house? Where is Mikhail?” — **conditions:** reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 950 of [Yellow is it](../quests/ratdom_quest.md#stage-950); NOT reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999) → **stage 10**. NPC: “We rats took over this village. I am Gruiik, their leader.”

???+ note "Stage 20: 3 routes"

    1. Talk to [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) → choose “What are you doing in my house? Where is Mikhail?” — **conditions:** reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1) → **stage 20**. NPC: “However, there are two-legs running around in my garden again. Go and kill them.”
    2. Talk to [Gruiik](../monsters/ratdom_mikhail.md) ([home](../maps/home.md)) → choose “What are you doing in my house? Where is Mikhail?” → **stage 20**. NPC: “However, there are two-legs running around in my garden again. Go and kill them.”
    3. stepping on a trigger on [home](../maps/home.md) → choose “What are you doing in my house? Where is Mikhail?” — **conditions:** reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 950 of [Yellow is it](../quests/ratdom_quest.md#stage-950); NOT reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999) → **stage 20**. NPC: “However, there are two-legs running around in my garden again. Go and kill them.”

???+ note "Stage 30: 1 route"

    1. stepping on a trigger on [crossglen](../maps/crossglen.md) → the conversation leads here automatically — **conditions:** killed 1× [Mara](../monsters/ratdom_mara.md); NOT reached stage 30 of [More rats!](../quests/ratdom_mikhail.md#stage-30) → **stage 30**; also removes monsters from crossglen_hall

???+ note "Stage 32: 1 route"

    1. stepping on a trigger on [crossglen](../maps/crossglen.md) → the conversation leads here automatically — **conditions:** killed 1× [Tharal](../monsters/ratdom_tharal.md); NOT reached stage 32 of [More rats!](../quests/ratdom_mikhail.md#stage-32) → **stage 32**; also removes monsters from crossglen_hall

???+ note "Stage 52: 3 routes"

    1. Talk to [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) → choose “Yes, I killed Mara and Tharal in the garden for you.” — **conditions:** reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 20 of [More rats!](../quests/ratdom_mikhail.md#stage-20); NOT reached stage 52 of [More rats!](../quests/ratdom_mikhail.md#stage-52); NOT reached stage 54 of [More rats!](../quests/ratdom_mikhail.md#stage-54); killed 1× [Mara](../monsters/ratdom_mara.md); killed 1× [Tharal](../monsters/ratdom_tharal.md) → **stage 52**
    2. Talk to [Gruiik](../monsters/ratdom_mikhail.md) ([home](../maps/home.md)) → choose “Yes, I killed Mara and Tharal in the garden for you.” — **conditions:** reached stage 20 of [More rats!](../quests/ratdom_mikhail.md#stage-20); NOT reached stage 52 of [More rats!](../quests/ratdom_mikhail.md#stage-52); NOT reached stage 54 of [More rats!](../quests/ratdom_mikhail.md#stage-54); killed 1× [Mara](../monsters/ratdom_mara.md); killed 1× [Tharal](../monsters/ratdom_tharal.md) → **stage 52**
    3. stepping on a trigger on [home](../maps/home.md) → choose “Yes, I killed Mara and Tharal in the garden for you.” — **conditions:** reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 950 of [Yellow is it](../quests/ratdom_quest.md#stage-950); NOT reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999); reached stage 20 of [More rats!](../quests/ratdom_mikhail.md#stage-20); NOT reached stage 52 of [More rats!](../quests/ratdom_mikhail.md#stage-52); NOT reached stage 54 of [More rats!](../quests/ratdom_mikhail.md#stage-54); killed 1× [Mara](../monsters/ratdom_mara.md); killed 1× [Tharal](../monsters/ratdom_tharal.md) → **stage 52**

???+ note "Stage 54: 3 routes"

    1. Talk to [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) → choose “(lie) I killed Mara and Tharal in the garden for you.” — **conditions:** reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 20 of [More rats!](../quests/ratdom_mikhail.md#stage-20); NOT reached stage 52 of [More rats!](../quests/ratdom_mikhail.md#stage-52); NOT reached stage 54 of [More rats!](../quests/ratdom_mikhail.md#stage-54); NOT killed 1× [Mara](../monsters/ratdom_mara.md); killed 1× [Tharal](../monsters/ratdom_tharal.md) → **stage 54**
    2. Talk to [Gruiik](../monsters/ratdom_mikhail.md) ([home](../maps/home.md)) → choose “(lie) I killed Mara and Tharal in the garden for you.” — **conditions:** reached stage 20 of [More rats!](../quests/ratdom_mikhail.md#stage-20); NOT reached stage 52 of [More rats!](../quests/ratdom_mikhail.md#stage-52); NOT reached stage 54 of [More rats!](../quests/ratdom_mikhail.md#stage-54); NOT killed 1× [Mara](../monsters/ratdom_mara.md); killed 1× [Tharal](../monsters/ratdom_tharal.md) → **stage 54**
    3. stepping on a trigger on [home](../maps/home.md) → choose “(lie) I killed Mara and Tharal in the garden for you.” — **conditions:** reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 950 of [Yellow is it](../quests/ratdom_quest.md#stage-950); NOT reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999); reached stage 20 of [More rats!](../quests/ratdom_mikhail.md#stage-20); NOT reached stage 52 of [More rats!](../quests/ratdom_mikhail.md#stage-52); NOT reached stage 54 of [More rats!](../quests/ratdom_mikhail.md#stage-54); NOT killed 1× [Mara](../monsters/ratdom_mara.md); killed 1× [Tharal](../monsters/ratdom_tharal.md) → **stage 54**

???+ note "Stage 70: 3 routes"

    1. Talk to [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) → the conversation leads here automatically — **conditions:** reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 20 of [More rats!](../quests/ratdom_mikhail.md#stage-20); NOT reached stage 70 of [More rats!](../quests/ratdom_mikhail.md#stage-70) → **stage 70**. NPC: “And I am hungry. Go to the town hall and bring me some bread.”
    2. Talk to [Gruiik](../monsters/ratdom_mikhail.md) ([home](../maps/home.md)) → the conversation leads here automatically — **conditions:** reached stage 20 of [More rats!](../quests/ratdom_mikhail.md#stage-20); NOT reached stage 70 of [More rats!](../quests/ratdom_mikhail.md#stage-70) → **stage 70**. NPC: “And I am hungry. Go to the town hall and bring me some bread.”
    3. stepping on a trigger on [home](../maps/home.md) → choose “Oh. Hello Gruiik.” — **conditions:** reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 950 of [Yellow is it](../quests/ratdom_quest.md#stage-950); NOT reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999); reached stage 20 of [More rats!](../quests/ratdom_mikhail.md#stage-20); NOT reached stage 70 of [More rats!](../quests/ratdom_mikhail.md#stage-70) → **stage 70**. NPC: “And I am hungry. Go to the town hall and bring me some bread.”

???+ note "Stage 72: 1 route"

    1. walking into a blocked passage on [crossglen](../maps/crossglen.md) → choose “Oh, what's this?” — **conditions:** NOT reached stage 72 of [More rats!](../quests/ratdom_mikhail.md#stage-72) → **stage 72**; also gives 1× [Bread](../items/bread.md). NPC: “A bag of freshly baked bread is dangling at the door.”

???+ note "Stage 74: 6 routes"

    1. Talk to [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) → choose “Here I have some bread for you.” — **conditions:** reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 20 of [More rats!](../quests/ratdom_mikhail.md#stage-20); NOT reached stage 70 of [More rats!](../quests/ratdom_mikhail.md#stage-70); hand over 1× [Bread](../items/bread.md) → **stage 74**. NPC: “It's about time.”
    2. Talk to [Gruiik](../monsters/ratdom_mikhail.md) ([home](../maps/home.md)) → choose “Here I have some bread for you.” — **conditions:** reached stage 20 of [More rats!](../quests/ratdom_mikhail.md#stage-20); NOT reached stage 70 of [More rats!](../quests/ratdom_mikhail.md#stage-70); hand over 1× [Bread](../items/bread.md) → **stage 74**. NPC: “It's about time.”
    3. stepping on a trigger on [home](../maps/home.md) → choose “Here I have some bread for you.” — **conditions:** reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 950 of [Yellow is it](../quests/ratdom_quest.md#stage-950); NOT reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999); reached stage 20 of [More rats!](../quests/ratdom_mikhail.md#stage-20); NOT reached stage 70 of [More rats!](../quests/ratdom_mikhail.md#stage-70); hand over 1× [Bread](../items/bread.md) → **stage 74**. NPC: “It's about time.”
    4. Talk to [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) → choose “Here I have some bread for you.” — **conditions:** reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 70 of [More rats!](../quests/ratdom_mikhail.md#stage-70); hand over 1× [Bread](../items/bread.md) → **stage 74**
    5. Talk to [Gruiik](../monsters/ratdom_mikhail.md) ([home](../maps/home.md)) → choose “Here I have some bread for you.” — **conditions:** reached stage 70 of [More rats!](../quests/ratdom_mikhail.md#stage-70); hand over 1× [Bread](../items/bread.md) → **stage 74**
    6. stepping on a trigger on [home](../maps/home.md) → choose “Here I have some bread for you.” — **conditions:** reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 950 of [Yellow is it](../quests/ratdom_quest.md#stage-950); NOT reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999); reached stage 70 of [More rats!](../quests/ratdom_mikhail.md#stage-70); hand over 1× [Bread](../items/bread.md) → **stage 74**

???+ note "Stage 90: 3 routes"

    1. Talk to [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)) → choose “Hey - I have brought some bread already.” — **conditions:** reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 70 of [More rats!](../quests/ratdom_mikhail.md#stage-70); reached stage 74 of [More rats!](../quests/ratdom_mikhail.md#stage-74) → **stage 90**. NPC: “Good! Now I don't need you anymore!”
    2. Talk to [Gruiik](../monsters/ratdom_mikhail.md) ([home](../maps/home.md)) → choose “Hey - I have brought some bread already.” — **conditions:** reached stage 70 of [More rats!](../quests/ratdom_mikhail.md#stage-70); reached stage 74 of [More rats!](../quests/ratdom_mikhail.md#stage-74) → **stage 90**. NPC: “Good! Now I don't need you anymore!”
    3. stepping on a trigger on [home](../maps/home.md) → choose “Hey - I have brought some bread already.” — **conditions:** reached stage 1 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-1); reached stage 950 of [Yellow is it](../quests/ratdom_quest.md#stage-950); NOT reached stage 999 of [Yellow is it](../quests/ratdom_quest.md#stage-999); reached stage 70 of [More rats!](../quests/ratdom_mikhail.md#stage-70); reached stage 74 of [More rats!](../quests/ratdom_mikhail.md#stage-74) → **stage 90**. NPC: “Good! Now I don't need you anymore!”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 11 lines added |
| [v0.8.6.1](../versions/0.8.6.1.md) | Dialogue: 1 line changed |
| [v0.8.12.1](../versions/0.8.12.1.md) | stage 10 journal text changed; stage 20 journal text changed; stage 30 journal text changed; stage 32 journal text changed; stage 52 journal text changed; stage 54 journal text changed (+3 more) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_mikhail.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_mikhail.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_mikhail.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_mikhail.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=ratdom_mikhail.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `ratdom_mikhail` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 32, 52, 54, 70, 72, 74, 90 |
    | Dialogue nodes setting stages | 10: `ratdom_mikhail_04`, 20: `ratdom_mikhail_10`, 30: `ratdom_check_kills_mara`, 32: `ratdom_check_kills_tharal`, 52: `ratdom_mikhail_50_2`, 54: `ratdom_mikhail_50_4`, 70: `ratdom_mikhail_10_10`, 72: `crossglen_ratdom_key_3_20`, 74: `ratdom_mikhail_10_20`, 74: `ratdom_mikhail_74`, 90: `ratdom_mikhail_80` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
