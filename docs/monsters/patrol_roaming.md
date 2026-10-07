---
description: "Feygard soldier is a non-player character (NPC) in Andor's Trail, found in Brimhaven, Crossroads Guardhouse, Remgard, Remgard."
---

# ![](../assets/icons/monsters/monsters_men_3.png){ .sprite } Feygard soldier

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_3.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Brimhaven, Crossroads Guardhouse, Remgard, Remgard |
| **Entries in game data** | 3 |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

!!! info "3 entries in the game data"
    The game's data files define 3 separate characters named Feygard soldier. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`patrol_roaming`](#v-patrol_roaming) | NPC | Blackwater Mountain: [wild6](../maps/wild6.md#pin-npc-patrol_roaming), Brimhaven: [brimhaven4](../maps/brimhaven4.md#pin-npc-patrol_roaming) (+6 more) | – |
| [`patrol2_captain`](#v-patrol2_captain) | NPC | Remgard: [remgard0](../maps/remgard0.md#pin-npc-patrol2_captain) | – |
| [`patrol2_roaming`](#v-patrol2_roaming) | NPC | Remgard: [remgard0](../maps/remgard0.md#pin-npc-patrol2_roaming) | – |

## Blackwater Mountain, Wild6 and 7 more (patrol_roaming) { #v-patrol_roaming }

**Entry ID:** `patrol_roaming` · **Type:** NPC

**Location:** Blackwater Mountain: [wild6](../maps/wild6.md#pin-npc-patrol_roaming), Brimhaven: [brimhaven4](../maps/brimhaven4.md#pin-npc-patrol_roaming), Crossroads Guardhouse: [crossroads](../maps/crossroads.md#pin-npc-patrol_roaming), Crossroads Guardhouse: [fields6](../maps/fields6.md#pin-npc-patrol_roaming), Fallhaven: [roadbeforecrossroads2](../maps/roadbeforecrossroads2.md#pin-npc-patrol_roaming), Fallhaven: [roadbeforecrossroads6](../maps/roadbeforecrossroads6.md#pin-npc-patrol_roaming) (+2 more)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [brimhaven4](../maps/brimhaven4.md) | Brimhaven | 6 | Appears later, during a quest |
| [crossroads](../maps/crossroads.md) | Crossroads Guardhouse | 6 | Appears later, during a quest |
| [fields6](../maps/fields6.md) | Crossroads Guardhouse | 6 | Appears later, during a quest |
| [remgard0](../maps/remgard0.md) | Remgard | 6 | Appears later, during a quest |
| [road1](../maps/road1.md) | Foaming Flask Tavern | 6 | Appears later, during a quest |
| [roadbeforecrossroads2](../maps/roadbeforecrossroads2.md) | Fallhaven | 6 | Appears later, during a quest |
| [roadbeforecrossroads6](../maps/roadbeforecrossroads6.md) | Fallhaven | 6 | Appears later, during a quest |
| [wild6](../maps/wild6.md) | Blackwater Mountain | 6 | Appears later, during a quest |

### Quests

- [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md): stage 141

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Feygard soldier. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_patrol_roaming.json" data-npc="Feygard soldier" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (9 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-patrol_roaming-brv_patrol_roaming"></span>**`brv_patrol_roaming`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 141 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-141))* → [brv_patrol_roaming_20](#d-patrol_roaming-brv_patrol_roaming_20)
    - branch 2 → [brv_patrol_roaming_10](#d-patrol_roaming-brv_patrol_roaming_10)

    <span id="d-patrol_roaming-brv_patrol_roaming_20"></span>**`brv_patrol_roaming_20`** Feygard soldier: “You again. You have to wait while I check your belongings.”

    - Next → [brv_patrol_roaming_11](#d-patrol_roaming-brv_patrol_roaming_11)

    <span id="d-patrol_roaming-brv_patrol_roaming_10"></span>**`brv_patrol_roaming_10`** Feygard soldier: “You are carrying a lot of gear. Any disallowed substances? You have to wait while I check your belongings.”

    - Next → [brv_patrol_roaming_11](#d-patrol_roaming-brv_patrol_roaming_11)

    <span id="d-patrol_roaming-brv_patrol_roaming_11"></span>**`brv_patrol_roaming_11`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 142 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-142))* → [brv_patrol_roaming_100](#d-patrol_roaming-brv_patrol_roaming_100)
    - branch 2 → [brv_patrol_bonemeals_removed](#d-patrol_roaming-brv_patrol_bonemeals_removed)

    <span id="d-patrol_roaming-brv_patrol_roaming_100"></span>**`brv_patrol_roaming_100`** Feygard soldier: “Everything is OK. Stay clean.” — **effects:** sets stage 141 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-141), clears stage 140 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-140), removes monsters from the map


    <span id="d-patrol_roaming-brv_patrol_bonemeals_removed"></span>**`brv_patrol_bonemeals_removed`** Feygard soldier: “What's this? Smells like Bonemeal! Bonemeal is illegal and forbidden by the law of Feygard. I will have to confiscate it. [He gives you back all your belongings but keeps the Bonemeals] Keep away from illegal stuff. Now go on your way.” — **effects:** sets stage 141 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-141), clears stage 140 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-140), removes monsters from the map

    - “Hey, what the ...?” *(if reached stage 40 of [bwmfill_nondisplay (hidden flag)](../quests/bwmfill_nondisplay.md#stage-40))* → [brv_patrol_bonemeals_removed_bur](#d-patrol_roaming-brv_patrol_bonemeals_removed_bur)
    - “Phew, at least they didn't find my iron reserve in the bonemeal box.” *(if reached stage 42 of [bwmfill_nondisplay (hidden flag)](../quests/bwmfill_nondisplay.md#stage-42))* → *conversation ends*
    - “Phew, at least they had let me go.” *(if NOT reached stage 40 of [bwmfill_nondisplay (hidden flag)](../quests/bwmfill_nondisplay.md#stage-40); NOT reached stage 42 of [bwmfill_nondisplay (hidden flag)](../quests/bwmfill_nondisplay.md#stage-42))* → *conversation ends*

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


??? info "Technical information (patrol_roaming)"

    | | |
    |---|---|
    | Entry ID | `patrol_roaming` |
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


## Remgard, Remgard0 (patrol2_captain) { #v-patrol2_captain }

**Entry ID:** `patrol2_captain` · **Type:** NPC

**Location:** Remgard: [remgard0](../maps/remgard0.md#pin-npc-patrol2_captain)

### Quests

- [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md): stage 141

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Feygard soldier. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_patrol2_roaming.json" data-npc="Feygard soldier" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-patrol2_captain-brv_patrol2_roaming"></span>**`brv_patrol2_roaming`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 141 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-141))* → [brv_patrol2_roaming_20](#d-patrol2_captain-brv_patrol2_roaming_20)
    - branch 2 → [brv_patrol2_roaming_10](#d-patrol2_captain-brv_patrol2_roaming_10)

    <span id="d-patrol2_captain-brv_patrol2_roaming_20"></span>**`brv_patrol2_roaming_20`** Feygard soldier: “You again. You have to wait while I check your belongings.”

    - Next → [brv_patrol2_roaming_11](#d-patrol2_captain-brv_patrol2_roaming_11)

    <span id="d-patrol2_captain-brv_patrol2_roaming_10"></span>**`brv_patrol2_roaming_10`** Feygard soldier: “You are carrying a lot of gear. Any disallowed substances? You have to wait while I check your belongings.”

    - Next → [brv_patrol2_roaming_11](#d-patrol2_captain-brv_patrol2_roaming_11)

    <span id="d-patrol2_captain-brv_patrol2_roaming_11"></span>**`brv_patrol2_roaming_11`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 142 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-142))* → [brv_patrol2_roaming_100](#d-patrol2_captain-brv_patrol2_roaming_100)
    - branch 2 → [brv_patrol2_bonemeals_removed](#d-patrol2_captain-brv_patrol2_bonemeals_removed)

    <span id="d-patrol2_captain-brv_patrol2_roaming_100"></span>**`brv_patrol2_roaming_100`** Feygard soldier: “Everything is OK. Stay clean.” — **effects:** sets stage 141 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-141), clears stage 140 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-140), removes monsters from the map, removes monsters from the map


    <span id="d-patrol2_captain-brv_patrol2_bonemeals_removed"></span>**`brv_patrol2_bonemeals_removed`** Feygard soldier: “What's this? Smells like Bonemeal! Bonemeal is illegal and forbidden by the law of Feygard. I will have to confiscate it. [He gives you back all your belongings but keeps the Bonemeals] And we have to arrest you of course. Report to…” — **effects:** sets stage 141 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-141), clears stage 140 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-140), removes monsters from the map, changes map remgard0, clears stage 138 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-138), clears stage 139 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-139), starts timer “remgard_prison”, removes monsters from remgard_prison




### Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (patrol2_captain)"

    | | |
    |---|---|
    | Entry ID | `patrol2_captain` |
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


## Remgard, Remgard0 (patrol2_roaming) { #v-patrol2_roaming }

**Entry ID:** `patrol2_roaming` · **Type:** NPC

**Location:** Remgard: [remgard0](../maps/remgard0.md#pin-npc-patrol2_roaming)

### Quests

- [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md): stage 141

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Feygard soldier. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_patrol2_roaming.json" data-npc="Feygard soldier" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [brv_patrol2_roaming](#d-patrol2_captain-brv_patrol2_roaming).


### Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (patrol2_roaming)"

    | | |
    |---|---|
    | Entry ID | `patrol2_roaming` |
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
