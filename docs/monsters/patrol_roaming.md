---
description: "Feygard soldier is a non-player character (NPC) in Andor's Trail, found in Brimhaven, Crossroads Guardhouse, Remgard, Remgard."
---

# ![](../assets/icons/monsters/monsters_men_3.png){ .sprite } Feygard soldier

**Where to find Feygard soldier:** [Blackwater Mountain, Wild 6 and 7 more](#v-patrol_roaming), [Remgard, Remgard 0](#v-patrol2_captain), [Remgard, Remgard 0](#v-patrol2_roaming)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_3.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Brimhaven, Crossroads Guardhouse, Remgard, Remgard |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Blackwater Mountain, Wild 6 and 7 more { #v-patrol_roaming }

**Where:** Blackwater Mountain: [Wild 6](../maps/wild6.md#pin-npc-patrol_roaming), Brimhaven: [Brimhaven 4](../maps/brimhaven4.md#pin-npc-patrol_roaming), Crossroads Guardhouse: [Crossroads](../maps/crossroads.md#pin-npc-patrol_roaming), Crossroads Guardhouse: [Fields 6](../maps/fields6.md#pin-npc-patrol_roaming), Fallhaven: [Roadbeforecrossroads 2](../maps/roadbeforecrossroads2.md#pin-npc-patrol_roaming), Fallhaven: [Roadbeforecrossroads 6](../maps/roadbeforecrossroads6.md#pin-npc-patrol_roaming) (+2 more)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Brimhaven 4](../maps/brimhaven4.md) | Brimhaven | 6 | Appears later, during a quest |
| [Crossroads](../maps/crossroads.md) | Crossroads Guardhouse | 6 | Appears later, during a quest |
| [Fields 6](../maps/fields6.md) | Crossroads Guardhouse | 6 | Appears later, during a quest |
| [Remgard 0](../maps/remgard0.md) | Remgard | 6 | Appears later, during a quest |
| [Road 1](../maps/road1.md) | Foaming Flask Tavern | 6 | Appears later, during a quest |
| [Roadbeforecrossroads 2](../maps/roadbeforecrossroads2.md) | Fallhaven | 6 | Appears later, during a quest |
| [Roadbeforecrossroads 6](../maps/roadbeforecrossroads6.md) | Fallhaven | 6 | Appears later, during a quest |
| [Wild 6](../maps/wild6.md) | Blackwater Mountain | 6 | Appears later, during a quest |

### Quests

- [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md): stage 141

### Dialogue simulator

Set your quest stages and items, then talk to Feygard soldier. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_patrol_roaming.json" data-npc="Feygard soldier" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (9 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-patrol_roaming-brv_patrol_roaming"></span>**`brv_patrol_roaming`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 141 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-141))* → [brv_patrol_roaming_20](#d-patrol_roaming-brv_patrol_roaming_20)
    - branch 2 → [brv_patrol_roaming_10](#d-patrol_roaming-brv_patrol_roaming_10)

    <span id="d-patrol_roaming-brv_patrol_roaming_20"></span>**`brv_patrol_roaming_20`** Feygard soldier: “You again. You have to wait while I check your belongings.”

    - Next → [brv_patrol_roaming_11](#d-patrol_roaming-brv_patrol_roaming_11)

    <span id="d-patrol_roaming-brv_patrol_roaming_10"></span>**`brv_patrol_roaming_10`** Feygard soldier: “You are carrying a lot of gear. Any disallowed substances? You have to wait while I check your belongings.”

    - Next → [brv_patrol_roaming_11](#d-patrol_roaming-brv_patrol_roaming_11)

    <span id="d-patrol_roaming-brv_patrol_roaming_11"></span>**`brv_patrol_roaming_11`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 142 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-142))* → [brv_patrol_roaming_100](#d-patrol_roaming-brv_patrol_roaming_100)
    - branch 2 → [brv_patrol_bonemeals_removed](#d-patrol_roaming-brv_patrol_bonemeals_removed)

    <span id="d-patrol_roaming-brv_patrol_roaming_100"></span>**`brv_patrol_roaming_100`** Feygard soldier: “Everything is OK. Stay clean.” — **effects:** sets stage 141 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-141), clears stage 140 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-140), removes monsters from the map


    <span id="d-patrol_roaming-brv_patrol_bonemeals_removed"></span>**`brv_patrol_bonemeals_removed`** Feygard soldier: “What's this? Smells like Bonemeal! Bonemeal is illegal and forbidden by the law of Feygard. I will have to confiscate it. [He gives you back all your belongings but keeps the Bonemeals] Keep away from illegal stuff. Now go on your way.” — **effects:** sets stage 141 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-141), clears stage 140 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-140), removes monsters from the map

    - “Hey, what the ...?” *(if reached stage 40 of [Blackwater Mountain story flags (hidden flag)](../quests/bwmfill_nondisplay.md#stage-40))* → [brv_patrol_bonemeals_removed_bur](#d-patrol_roaming-brv_patrol_bonemeals_removed_bur)
    - “Phew, at least they didn't find my iron reserve in the bonemeal box.” *(if reached stage 42 of [Blackwater Mountain story flags (hidden flag)](../quests/bwmfill_nondisplay.md#stage-42))* → *conversation ends*
    - “Phew, at least they had let me go.” *(if NOT reached stage 40 of [Blackwater Mountain story flags (hidden flag)](../quests/bwmfill_nondisplay.md#stage-40); NOT reached stage 42 of [Blackwater Mountain story flags (hidden flag)](../quests/bwmfill_nondisplay.md#stage-42))* → *conversation ends*

    <span id="d-patrol_roaming-brv_patrol_bonemeals_removed_bur"></span>**`brv_patrol_bonemeals_removed_bur`** [Dummy NPC](../monsters/none.md): “One of the guards winks at you while putting the confiscated bonemeal potions back in your pouch.”

    - “???” → [brv_patrol_bonemeals_removed_bur_10](#d-patrol_roaming-brv_patrol_bonemeals_removed_bur_10)

    <span id="d-patrol_roaming-brv_patrol_bonemeals_removed_bur_10"></span>**`brv_patrol_bonemeals_removed_bur_10`** Feygard soldier: “You'll be speechless - the guard is Burhczyd in the uniform of the Feygard Guard!”

    - Next → [brv_patrol_bonemeals_removed_bur_20](#d-patrol_roaming-brv_patrol_bonemeals_removed_bur_20)

    <span id="d-patrol_roaming-brv_patrol_bonemeals_removed_bur_20"></span>**`brv_patrol_bonemeals_removed_bur_20`** Feygard soldier: “Before you react, the guards have moved on.”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 6 lines added |
| [v0.8.10](../versions/0.8.10.md) | Dialogue: 3 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Remgard, Remgard 0 { #v-patrol2_captain }

**Where:** Remgard: [Remgard 0](../maps/remgard0.md#pin-npc-patrol2_captain)

### Quests

- [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md): stage 141

### Dialogue simulator

Set your quest stages and items, then talk to Feygard soldier. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_patrol2_roaming.json" data-npc="Feygard soldier" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-patrol2_captain-brv_patrol2_roaming"></span>**`brv_patrol2_roaming`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 141 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-141))* → [brv_patrol2_roaming_20](#d-patrol2_captain-brv_patrol2_roaming_20)
    - branch 2 → [brv_patrol2_roaming_10](#d-patrol2_captain-brv_patrol2_roaming_10)

    <span id="d-patrol2_captain-brv_patrol2_roaming_20"></span>**`brv_patrol2_roaming_20`** Feygard soldier: “You again. You have to wait while I check your belongings.”

    - Next → [brv_patrol2_roaming_11](#d-patrol2_captain-brv_patrol2_roaming_11)

    <span id="d-patrol2_captain-brv_patrol2_roaming_10"></span>**`brv_patrol2_roaming_10`** Feygard soldier: “You are carrying a lot of gear. Any disallowed substances? You have to wait while I check your belongings.”

    - Next → [brv_patrol2_roaming_11](#d-patrol2_captain-brv_patrol2_roaming_11)

    <span id="d-patrol2_captain-brv_patrol2_roaming_11"></span>**`brv_patrol2_roaming_11`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 142 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-142))* → [brv_patrol2_roaming_100](#d-patrol2_captain-brv_patrol2_roaming_100)
    - branch 2 → [brv_patrol2_bonemeals_removed](#d-patrol2_captain-brv_patrol2_bonemeals_removed)

    <span id="d-patrol2_captain-brv_patrol2_roaming_100"></span>**`brv_patrol2_roaming_100`** Feygard soldier: “Everything is OK. Stay clean.” — **effects:** sets stage 141 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-141), clears stage 140 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-140), removes monsters from the map, removes monsters from the map


    <span id="d-patrol2_captain-brv_patrol2_bonemeals_removed"></span>**`brv_patrol2_bonemeals_removed`** Feygard soldier: “What's this? Smells like Bonemeal! Bonemeal is illegal and forbidden by the law of Feygard. I will have to confiscate it. [He gives you back all your belongings but keeps the Bonemeals] And we have to arrest you of course. Report to…” — **effects:** sets stage 141 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-141), clears stage 140 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-140), removes monsters from the map, changes map remgard0, clears stage 138 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-138), clears stage 139 of [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md#stage-139), starts timer “remgard_prison”, removes monsters from remgard_prison




### Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Remgard, Remgard 0 (2) { #v-patrol2_roaming }

**Where:** Remgard: [Remgard 0](../maps/remgard0.md#pin-npc-patrol2_roaming)

### Quests

- [Brimhaven story flags (hidden flag)](../quests/brv_nondisplay.md): stage 141

### Dialogue simulator

Set your quest stages and items, then talk to Feygard soldier. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_patrol2_roaming.json" data-npc="Feygard soldier" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [brv_patrol2_roaming](#d-patrol2_captain-brv_patrol2_roaming).


### Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**3 entries.** The game data defines 3 separate characters named Feygard soldier. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location.

| Entry | Type | Section |
|---|---|---|
| `patrol_roaming` | NPC | [Blackwater Mountain, Wild 6 and 7 more](#v-patrol_roaming) |
| `patrol2_captain` | NPC | [Remgard, Remgard 0](#v-patrol2_captain) |
| `patrol2_roaming` | NPC | [Remgard, Remgard 0](#v-patrol2_roaming) |

??? info "Technical information: patrol_roaming"

    | | |
    |---|---|
    | Entry ID | `patrol_roaming` |
    | Type (wiki) | NPC |
    | Spawn group | `patrol_roaming` |
    | Loot table | – |
    | Conversation | `brv_patrol_roaming` |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_men:3` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "patrol_roaming",
     "name": "Feygard soldier",
     "iconID": "monsters_men:3",
     "moveCost": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "protectSpawn",
     "spawnGroup": "patrol_roaming",
     "phraseID": "brv_patrol_roaming"
    }
    ```

??? info "Technical information: patrol2_captain"

    | | |
    |---|---|
    | Entry ID | `patrol2_captain` |
    | Type (wiki) | NPC |
    | Spawn group | `patrol2_captain` |
    | Loot table | – |
    | Conversation | `brv_patrol2_roaming` |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_men:3` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "patrol2_captain",
     "name": "Feygard soldier",
     "iconID": "monsters_men:3",
     "moveCost": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "protectSpawn",
     "spawnGroup": "patrol2_captain",
     "phraseID": "brv_patrol2_roaming"
    }
    ```

??? info "Technical information: patrol2_roaming"

    | | |
    |---|---|
    | Entry ID | `patrol2_roaming` |
    | Type (wiki) | NPC |
    | Spawn group | `patrol2_roaming` |
    | Loot table | – |
    | Conversation | `brv_patrol2_roaming` |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_men:3` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "patrol2_roaming",
     "name": "Feygard soldier",
     "iconID": "monsters_men:3",
     "moveCost": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "protectSpawn",
     "spawnGroup": "patrol2_roaming",
     "phraseID": "brv_patrol2_roaming"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=patrol_roaming.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=patrol_roaming.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=patrol_roaming.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=patrol_roaming.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
