---
description: "hettar_dog_nd is a hidden quest in Andor's Trail, started by stepping on a trigger on blackwater_mountain55. 2 stages. 1=found dog"
---

# hettar_dog_nd

!!! info "Hidden story flag"
    An internal quest the game uses to track progress. It does not appear in the journal. The stage descriptions below are internal notes written by the developers and may be brief.

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `hettar_dog_nd` |
| **In journal** | No (hidden flag) |
| **Stages** | 2 |
| **Started by** | stepping on a trigger on [blackwater_mountain55](../maps/blackwater_mountain55.md), [Wolfhound](../monsters/hettar_dog.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) |
| **NPCs involved** | [Wolfhound](../monsters/hettar_dog.md) |
| **Locations** | [blackwater_mountain55](../maps/blackwater_mountain55.md) |
| **Related quests** | 1 |

</div>

## Overview

> 1=found dog

## Prerequisites to start

**Route 1** (stepping on a trigger on [blackwater_mountain55](../maps/blackwater_mountain55.md)):

- NOT reached stage 2 of [hettar_dog_nd (hidden flag)](../quests/hettar_dog_nd.md#stage-2)

**Route 2** ([Wolfhound](../monsters/hettar_dog.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md))):

- nothing


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>

## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Unlocks | [Where is Norry?](hettar_dog.md#stage-40) | stage 40 there needs stage 2 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-1"></span>1 | 1=found dog<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain55](../maps/blackwater_mountain55.md).</span> | stepping on a trigger on [blackwater_mountain55](../maps/blackwater_mountain55.md)<br>[Wolfhound](../monsters/hettar_dog.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) | – | – |
| <span id="stage-2"></span>2 | 2=picked up bones<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Blackwater mountain55](../maps/blackwater_mountain55.md).</span> | stepping on a trigger on [blackwater_mountain55](../maps/blackwater_mountain55.md)<br>[Wolfhound](../monsters/hettar_dog.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) | hand over 1× [Wyrm meat](../items/hettar_bone.md) | gives 1× [Huge bones from the Blackwater Mountains](../items/bwm_bones.md)<br>sets stage 40 of [Where is Norry?](../quests/hettar_dog.md#stage-40) |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>

## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 1: 2 routes"

    1. stepping on a trigger on [blackwater_mountain55](../maps/blackwater_mountain55.md) → choose “Take the bones.” — **conditions:** NOT reached stage 2 of [hettar_dog_nd (hidden flag)](../quests/hettar_dog_nd.md#stage-2) → **stage 1**. NPC: “GROWL!”
    2. Talk to [Wolfhound](../monsters/hettar_dog.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) → the conversation leads here automatically → **stage 1**. NPC: “Growl!”

???+ note "Stage 2: 2 routes"

    1. stepping on a trigger on [blackwater_mountain55](../maps/blackwater_mountain55.md) → choose “The wolfhound doesn't want you to take 'his' bones. Take them nevertheless.” — **conditions:** NOT reached stage 2 of [hettar_dog_nd (hidden flag)](../quests/hettar_dog_nd.md#stage-2) → **stage 2**; also gives 1× [Huge bones from the Blackwater Mountains](../items/bwm_bones.md)
    2. Talk to [Wolfhound](../monsters/hettar_dog.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) → choose “Hey Norry, look here! I have some much better food for you from Hettar.” — **conditions:** hand over 1× [Wyrm meat](../items/hettar_bone.md); reached stage 2 of [hettar_dog_nd (hidden flag)](../quests/hettar_dog_nd.md#stage-2) → **stage 2**; also sets stage 40 of [Where is Norry?](../quests/hettar_dog.md#stage-40). NPC: “The wolfhound fetched the meat from your hand and devoured it greedily in a few seconds.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=hettar_dog_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=hettar_dog_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=hettar_dog_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=hettar_dog_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=hettar_dog_nd.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `hettar_dog_nd` |
    | showInLog | 0 |
    | Stage IDs | 1, 2 |
    | Dialogue nodes setting stages | 1: `hettar_bones_20`, 1: `hettar_dog`, 2: `hettar_bones_30`, 2: `hettar_dog_10` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
