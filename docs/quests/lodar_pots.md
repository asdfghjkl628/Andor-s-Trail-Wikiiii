---
description: "Lodar's potions is a quest in Andor's Trail, started by Lodar (lodarhouse1). 7 stages, 2,000 XP in total. Lodar says that he can make potions from some animal remains, if I first bring him some Spotted Hornbeam fungus. Apparently, the potion-maker in Fallhaven has a stock of it, if you know enoug…"
---

# Lodar's potions

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `lodar_pots` |
| **In journal** | Yes |
| **Stages** | 7 (completes at 40) |
| **Started by** | [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) |
| **NPCs involved** | [Lodar](../monsters/lodar.md), [Potion merchant](../monsters/potion_merchant.md) |
| **Locations** | [fallhaven_potions](../maps/fallhaven_potions.md), [lodarhouse1](../maps/lodarhouse1.md) |
| **Total XP** | 2,000 |
| **Related quests** | 1 |

</div>

## Overview

> Lodar says that he can make potions from some animal remains, if I first bring him some Spotted Hornbeam fungus. Apparently, the potion-maker in Fallhaven has a stock of it, if you know enough to ask.

## Prerequisites to start

Start with [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)). Required:

- reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Searching for madness](lodar2.md#stage-60) | stage 60 reached, for stages 10, 30, 40, 41, 42, 43 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Lodar says that he can make potions from some animal remains, if I first bring him some Spotted Hornbeam fungus. Apparently, the potion-maker in Fallhaven has a stock of it, if you know enough to ask. | [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) | – | – |
| <span id="stage-20"></span>20 | I have retrieved some Spotted Hornbeam fungus from the potion-maker in Fallhaven. I should return to Lodar with it as soon as possible. | [Potion merchant](../monsters/potion_merchant.md) ([fallhaven_potions](../maps/fallhaven_potions.md)) | stage 10 | gives [Spotted Hornbeam fungus](../items/hornbeam.md) |
| <span id="stage-30"></span>30 | I have given the Spotted Hornbeam fungus to Lodar. | [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) | hand over 1× [Spotted Hornbeam fungus](../items/hornbeam.md), stage 10 | – |
| <span id="stage-40"></span>40 | Lodar thanked me for bringing him the fungus. In return, he can now create his special potions for me. **(completes quest)** | [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) | stage 30 | 2,000 XP |
| <span id="stage-41"></span>41 | Lodar can create a defensive potion if I bring him two White wyrm claws and a Ruby gem. | [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) | stage 40 | – |
| <span id="stage-42"></span>42 | Lodar can create a potion of strength if I bring him a dead spider and the wings of an insect. | [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) | stage 40 | – |
| <span id="stage-43"></span>43 | Lodar can create a potent defensive potion if I bring him two arulir skins and a claw from some monster. The arulir beasts can be found somewhere up in the north, and the claws can apparently be found from creatures that dwell underground and in caves somewhere outside Fallhaven. | [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) | stage 40 | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. Talk to [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) → choose “Fallhaven? The potion maker in Fallhaven?” — **conditions:** reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60) → **stage 10**. NPC: “Yes, that's what I was looking for. Fallhaven. Go visit him and ask him if he has some. I am sure he has some, if you…”

???+ note "Stage 20: 1 route"

    1. Talk to [Potion merchant](../monsters/potion_merchant.md) ([fallhaven_potions](../maps/fallhaven_potions.md)) → choose “I was told that I can get some Spotted Hornbeam fungus from you.” — **conditions:** reached stage 10 of [Lodar's potions](../quests/lodar_pots.md#stage-10) → **stage 20**; also gives [Spotted Hornbeam fungus](../items/hornbeam.md). NPC: “Here, have some. I don't have that much, so don't lose it!”

???+ note "Stage 30: 1 route"

    1. Talk to [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) → choose “Yes, here it is.” — **conditions:** reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60); reached stage 10 of [Lodar's potions](../quests/lodar_pots.md#stage-10); hand over 1× [Spotted Hornbeam fungus](../items/hornbeam.md) → **stage 30**. NPC: “Oh yes, this will do nicely. Good, good. Thank you, my friend.”

???+ note "Stage 40: 1 route"

    1. Talk to [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) → choose “I'd like to talk about your potions.” — **conditions:** reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60); reached stage 30 of [Lodar's potions](../quests/lodar_pots.md#stage-30) → **stage 40**. NPC: “With your help, I can now create additional potions from the remains of certain animals if you would like.”

???+ note "Stage 41: 1 route"

    1. Talk to [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) → choose “What about the resistance potion?” — **conditions:** reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60); reached stage 40 of [Lodar's potions](../quests/lodar_pots.md#stage-40) → **stage 41**. NPC: “I have discovered that if you mix some ground up claws from a beast called the white wyrm, together with a slight…”

???+ note "Stage 42: 1 route"

    1. Talk to [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) → choose “What about the strength potion?” — **conditions:** reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60); reached stage 40 of [Lodar's potions](../quests/lodar_pots.md#stage-40) → **stage 42**. NPC: “Have you ever noticed how insects are able to lift things that are much larger than themselves? As it turns out, I…”

???+ note "Stage 43: 1 route"

    1. Talk to [Lodar](../monsters/lodar.md) ([lodarhouse1](../maps/lodarhouse1.md)) → choose “What about the hardening potion?” — **conditions:** reached stage 60 of [Searching for madness](../quests/lodar2.md#stage-60); reached stage 40 of [Lodar's potions](../quests/lodar_pots.md#stage-40) → **stage 43**. NPC: “Up in the north, I have heard tales of beast called the arulir. Their skin is thick as bark due to the interesting…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.1](../versions/0.7.1.md) | Stage 43 journal text changed<br>Dialogue: 1 line changed<br>· text: “Up in the north, I have heard tales of beast called the Arulir. Their…” → “Up in the north, I have heard tales of beast called the Arulir. Their…” |
| [v0.7.2](../versions/0.7.2.md) | Stage 43 journal text changed<br>Dialogue: 2 lines changed<br>· text: “I have discovered that if you mix some ground up claws from a beast c…” → “I have discovered that if you mix some ground up claws from a beast c…”<br>· text: “Up in the north, I have heard tales of beast called the Arulir. Their…” → “Up in the north, I have heard tales of beast called the arulir. Their…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lodar_pots.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lodar_pots.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lodar_pots.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lodar_pots.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=lodar_pots.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `lodar_pots` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 41, 42, 43 |
    | Dialogue nodes setting stages | 10: `lodar_pq5`, 20: `fallhaven_potions3`, 30: `lodar_pots5`, 40: `lodar_pots7`, 41: `lodar_spo2_0`, 42: `lodar_spo1_0`, 43: `lodar_spo3_0` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
