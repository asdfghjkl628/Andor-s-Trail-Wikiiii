---
description: "Guard is a non-player character (NPC) in Andor's Trail, found in Fallhaven, Brimhaven, Foaming Flask Tavern, Crossroads Guardhouse, Flagstone Prison, Loneford, Remgard. Starts Fair play?."
---

# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Guard

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Starts [Fair play?](../quests/brv_blackjack.md) |
| **Found in** | Fallhaven, Brimhaven, Foaming Flask Tavern, Crossroads Guardhouse, Flagstone Prison, Loneford, Remgard |
| **Entries in game data** | 16 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "16 entries in the game data"
    The game's data files define 16 separate characters named Guard. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location, appearance. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`guard`](#v-guard) | NPC | Fallhaven: [fallhaven_nw](../maps/fallhaven_nw.md#pin-npc-guard), Fallhaven: [fallhaven_prison](../maps/fallhaven_prison.md#pin-npc-guard) (+1 more) | – |
| [`brv_exit_guard`](#v-brv_exit_guard) | NPC | Brimhaven: [brimhaven3](../maps/brimhaven3.md#pin-npc-brv_exit_guard), Brimhaven: [brimhaven4](../maps/brimhaven4.md#pin-npc-brv_exit_guard) | – |
| [`brv_prison_guard`](#v-brv_prison_guard) | NPC | Brimhaven: [brimhaven_prison](../maps/brimhaven_prison.md#pin-npc-brv_prison_guard) | – |
| [`brv_shop_guard`](#v-brv_shop_guard) | NPC | Brimhaven: [brimhaven4](../maps/brimhaven4.md#pin-npc-brv_shop_guard) | – |
| [`brv_tavern_west_guard`](#v-brv_tavern_west_guard) | NPC | Brimhaven: [brimhaven_tavern_west](../maps/brimhaven_tavern_west.md#pin-npc-brv_tavern_west_guard) | starts [Fair play?](../quests/brv_blackjack.md) |
| [`charwd_guard`](#v-charwd_guard) | NPC | Foaming Flask Tavern: [waytominingtown2](../maps/waytominingtown2.md#pin-npc-charwd_guard) | – |
| [`crossroads_backguard`](#v-crossroads_backguard) | NPC | Crossroads Guardhouse: [houseatcrossroads1](../maps/houseatcrossroads1.md#pin-npc-crossroads_backguard) | – |
| [`crossroads_guard`](#v-crossroads_guard) | NPC | Crossroads Guardhouse: [crossroads](../maps/crossroads.md#pin-npc-crossroads_guard), Crossroads Guardhouse: [houseatcrossroads2](../maps/houseatcrossroads2.md#pin-npc-crossroads_guard) (+1 more) | – |
| [`crossroads_sleepguard`](#v-crossroads_sleepguard) | NPC | Crossroads Guardhouse: [houseatcrossroads1](../maps/houseatcrossroads1.md#pin-npc-crossroads_sleepguard) | – |
| [`flagstone_guard`](#v-flagstone_guard) | NPC | Flagstone Prison: [flagstone0](../maps/flagstone0.md#pin-npc-flagstone_guard) | – |
| [`guard_advent`](#v-guard_advent) | NPC | Brimhaven: [brimhaven3](../maps/brimhaven3.md#pin-npc-guard_advent) | – |
| [`loneford_guard0`](#v-loneford_guard0) | NPC | Loneford: [loneford10](../maps/loneford10.md#pin-npc-loneford_guard0), Loneford: [loneford2](../maps/loneford2.md#pin-npc-loneford_guard0) | – |
| [`loneford_wellguard`](#v-loneford_wellguard) | NPC | Loneford: [loneford2](../maps/loneford2.md#pin-npc-loneford_wellguard) | – |
| [`remgard_g1`](#v-remgard_g1) | NPC | Remgard: [remgard_church](../maps/remgard_church.md#pin-npc-remgard_g1), Remgard: [remgard_tavern1](../maps/remgard_tavern1.md#pin-npc-remgard_g1) | – |
| [`remgard_g2`](#v-remgard_g2) | NPC | Remgard: [remgard_church](../maps/remgard_church.md#pin-npc-remgard_g2), Remgard: [remgard_tavern1](../maps/remgard_tavern1.md#pin-npc-remgard_g2) | – |
| [`remgard_g3`](#v-remgard_g3) | NPC | Remgard: [remgard_tavern1](../maps/remgard_tavern1.md#pin-npc-remgard_g3) | – |

## Fallhaven, Fallhaven north-west and 2 more (guard) { #v-guard }

**Entry ID:** `guard` · **Type:** NPC

**Location:** Fallhaven: [fallhaven_nw](../maps/fallhaven_nw.md#pin-npc-guard), Fallhaven: [fallhaven_prison](../maps/fallhaven_prison.md#pin-npc-guard), Fallhaven: [gapfiller4](../maps/gapfiller4.md#pin-npc-guard)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [fallhaven_nw](../maps/fallhaven_nw.md) | Fallhaven | 1 | – |
| [fallhaven_prison](../maps/fallhaven_prison.md) | Fallhaven | 2 | – |
| [gapfiller4](../maps/gapfiller4.md) | Fallhaven | 1 | – |

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/fallhaven_guard.json" data-npc="Guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guard-fallhaven_guard"></span>**`fallhaven_guard`** Guard: “Keep out of trouble.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guard)"

    | | |
    |---|---|
    | Entry ID | `guard` |
    | Spawn group | `fallhaven_guard` |
    | Loot table | – |
    | Conversation | `fallhaven_guard` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles3:14` |
    | Defined in | `res/raw/monsterlist_fallhaven_npcs.json` |

    Raw data:

    ```json
    {
     "id": "guard",
     "name": "Guard",
     "iconID": "monsters_rltiles3:14",
     "monsterClass": "humanoid",
     "spawnGroup": "fallhaven_guard",
     "phraseID": "fallhaven_guard"
    }
    ```


## Brimhaven, Brimhaven3 and 1 more (brv_exit_guard) { #v-brv_exit_guard }

**Entry ID:** `brv_exit_guard` · **Type:** NPC

**Location:** Brimhaven: [brimhaven3](../maps/brimhaven3.md#pin-npc-brv_exit_guard), Brimhaven: [brimhaven4](../maps/brimhaven4.md#pin-npc-brv_exit_guard)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [brimhaven3](../maps/brimhaven3.md) | Brimhaven | 1 | Appears later, during a quest |
| [brimhaven4](../maps/brimhaven4.md) | Brimhaven | 2 | Appears later, during a quest |

### Quests

- [Much water](../quests/brv_flood.md): stage 100

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_exit_forbidden_10.json" data-npc="Guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brv_exit_guard-brv_exit_forbidden_10"></span>**`brv_exit_forbidden_10`** [Guard](../monsters/guard.md#v-brv_exit_guard): “Stop! All foreigners have to stay in town until we have investigated who destroyed the great dam.” — **effects:** sets stage 100 of [Much water](../quests/brv_flood.md#stage-100)

    - “Who gave this order?” → [brv_exit_forbidden_20](#d-brv_exit_guard-brv_exit_forbidden_20)

    <span id="d-brv_exit_guard-brv_exit_forbidden_20"></span>**`brv_exit_forbidden_20`** Guard: “Mustura, the captain of the guard, gave the order. Usually you can find her in front of the warehouse in the center of the town, north of the church.”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_exit_guard)"

    | | |
    |---|---|
    | Entry ID | `brv_exit_guard` |
    | Spawn group | `brv_exit_guard` |
    | Loot table | – |
    | Conversation | `brv_exit_forbidden_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:41` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_exit_guard",
     "name": "Guard",
     "iconID": "monsters_ld1:41",
     "phraseID": "brv_exit_forbidden_10"
    }
    ```


## Brimhaven, Brimhaven prison (brv_prison_guard) { #v-brv_prison_guard }

**Entry ID:** `brv_prison_guard` · **Type:** NPC

**Location:** Brimhaven: [brimhaven_prison](../maps/brimhaven_prison.md#pin-npc-brv_prison_guard)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_prison_guard.json" data-npc="Guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brv_prison_guard-brv_prison_guard"></span>**`brv_prison_guard`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 200 of [Much water](../quests/brv_flood.md#stage-200))* → [brv_prison_guard_20](#d-brv_prison_guard-brv_prison_guard_20)
    - branch 2 *(if reached stage 220 of [A strange looking dagger](../quests/brv_dagger.md#stage-220))* → [brv_prison_guard_30](#d-brv_prison_guard-brv_prison_guard_30)
    - branch 3 → [brv_prison_guard_10](#d-brv_prison_guard-brv_prison_guard_10)

    <span id="d-brv_prison_guard-brv_prison_guard_20"></span>**`brv_prison_guard_20`** Guard: “Are you looking for the captain? She has been gone for a while now, arresting the person that destroyed the dam.”


    <span id="d-brv_prison_guard-brv_prison_guard_30"></span>**`brv_prison_guard_30`** Guard: “After all this long time I finally have a resident here again.”


    <span id="d-brv_prison_guard-brv_prison_guard_10"></span>**`brv_prison_guard_10`** Guard: “The prison is currently vacant and I hope you don't give me a reason to change this.”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 3 lines added |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line added, 2 lines changed<br>· text: “Are you looking for the captain? He has been gone for a while now, ar…” → “Are you looking for the captain? She has been gone for a while now, a…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_prison_guard)"

    | | |
    |---|---|
    | Entry ID | `brv_prison_guard` |
    | Spawn group | `brv_prison_guard` |
    | Loot table | – |
    | Conversation | `brv_prison_guard` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:41` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_prison_guard",
     "name": "Guard",
     "iconID": "monsters_ld1:41",
     "phraseID": "brv_prison_guard"
    }
    ```


## Brimhaven, Brimhaven4 (brv_shop_guard) { #v-brv_shop_guard }

**Entry ID:** `brv_shop_guard` · **Type:** NPC

**Location:** Brimhaven: [brimhaven4](../maps/brimhaven4.md#pin-npc-brv_shop_guard)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_shop_guard_select.json" data-npc="Guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brv_shop_guard-brv_shop_guard_select"></span>**`brv_shop_guard_select`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 130 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-130))* → [brv_shop_guard_20](#d-brv_shop_guard-brv_shop_guard_20)
    - Next → [brv_shop_guard_10](#d-brv_shop_guard-brv_shop_guard_10)

    <span id="d-brv_shop_guard-brv_shop_guard_20"></span>**`brv_shop_guard_20`** Guard: “Hello again, traveler.”


    <span id="d-brv_shop_guard-brv_shop_guard_10"></span>**`brv_shop_guard_10`** Guard: “I will keep an eye on you.”




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 3 lines added |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “Hello again, Sir.” → “Hello again, traveler.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_shop_guard)"

    | | |
    |---|---|
    | Entry ID | `brv_shop_guard` |
    | Spawn group | `brv_shop_guard` |
    | Loot table | – |
    | Conversation | `brv_shop_guard_select` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles3:14` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_shop_guard",
     "name": "Guard",
     "iconID": "monsters_rltiles3:14",
     "phraseID": "brv_shop_guard_select"
    }
    ```


## Brimhaven, Brimhaven tavern west (brv_tavern_west_guard) { #v-brv_tavern_west_guard }

**Entry ID:** `brv_tavern_west_guard` · **Type:** NPC · **Role:** Starts [Fair play?](../quests/brv_blackjack.md)

**Location:** Brimhaven: [brimhaven_tavern_west](../maps/brimhaven_tavern_west.md#pin-npc-brv_tavern_west_guard)

### Quests

- [Fair play?](../quests/brv_blackjack.md): stages 10, 40, 60
- [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md): stage 150

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_tavern_west_guard_select.json" data-npc="Guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brv_tavern_west_guard-brv_tavern_west_guard_select"></span>**`brv_tavern_west_guard_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 60 of [Fair play?](../quests/brv_blackjack.md#stage-60))* → [brv_tavern_west_guard_100](#d-brv_tavern_west_guard-brv_tavern_west_guard_100)
    - branch 2 *(if reached stage 50 of [Fair play?](../quests/brv_blackjack.md#stage-50); killed 1× [Dealer](../monsters/brv_blackjack_dealer.md#v-brv_blackjack_dealer_evil); killed 1× [Gambler](../monsters/brv_blackjack_gambler1.md#v-brv_blackjack_gambler1_evil); killed 1× [Gambler](../monsters/brv_blackjack_gambler1.md#v-brv_blackjack_gambler1_evil))* → [brv_tavern_west_guard_90](#d-brv_tavern_west_guard-brv_tavern_west_guard_90)
    - branch 3 *(if reached stage 40 of [Fair play?](../quests/brv_blackjack.md#stage-40))* → [brv_tavern_west_guard_20](#d-brv_tavern_west_guard-brv_tavern_west_guard_20)
    - branch 4 → [brv_tavern_west_backroom_5](#d-brv_tavern_west_guard-brv_tavern_west_backroom_5)

    <span id="d-brv_tavern_west_guard-brv_tavern_west_guard_100"></span>**`brv_tavern_west_guard_100`** [Guard](../monsters/guard.md#v-brv_tavern_west_guard): “You are not welcome anymore.”

    - “Sure I am. I'm on official Alkapoan business.” *(if latest stage of [A place to forge](../quests/place_to_forge.md#stage-40) is 40)* → [brv_tavern_west_guard_alkapaon_business_10](#d-brv_tavern_west_guard-brv_tavern_west_guard_alkapaon_business_10)
    - “Ah, right. I forgot.” → *conversation ends*

    <span id="d-brv_tavern_west_guard-brv_tavern_west_guard_90"></span>**`brv_tavern_west_guard_90`** [Guard](../monsters/guard.md#v-brv_tavern_west_guard): “I heard you fighting in there. Lucky for you that no one got killed. You are not welcome anymore.” — **effects:** sets stage 60 of [Fair play?](../quests/brv_blackjack.md#stage-60), clears stage 150 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-150)

    - “Sure I am. I'm on official Alkapoan business.” *(if latest stage of [A place to forge](../quests/place_to_forge.md#stage-40) is 40)* → [brv_tavern_west_guard_alkapaon_business_10](#d-brv_tavern_west_guard-brv_tavern_west_guard_alkapaon_business_10)
    - “Calm down! I'm leaving right now.” → *conversation ends*

    <span id="d-brv_tavern_west_guard-brv_tavern_west_guard_20"></span>**`brv_tavern_west_guard_20`** Guard: “I wish you good luck. [Laughs]” — **effects:** sets stage 150 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-150), sets stage 40 of [Fair play?](../quests/brv_blackjack.md#stage-40)


    <span id="d-brv_tavern_west_guard-brv_tavern_west_backroom_5"></span>**`brv_tavern_west_backroom_5`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 20 of [Fair play?](../quests/brv_blackjack.md#stage-20))* → [brv_tavern_west_guard_10](#d-brv_tavern_west_guard-brv_tavern_west_guard_10)
    - branch 2 → [brv_tavern_west_backroom_6](#d-brv_tavern_west_guard-brv_tavern_west_backroom_6)

    <span id="d-brv_tavern_west_guard-brv_tavern_west_guard_alkapaon_business_10"></span>**`brv_tavern_west_guard_alkapaon_business_10`** Guard: “Oh, sorry. Please don't tell Alkapoan that I hassled you.” — **effects:** sets stage 150 of [brv_blackjack_hidden (hidden flag)](../quests/brv_blackjack_hidden.md#stage-150), spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back, spawns monsters on brimhaven_tavern_west_back

    - “Now that's the attitude I like to see.” → *conversation ends*

    <span id="d-brv_tavern_west_guard-brv_tavern_west_guard_10"></span>**`brv_tavern_west_guard_10`** [Guard](../monsters/guard.md#v-brv_tavern_west_guard): “[You hear noises from the back room...] Stop! Tell me the password, if you want to enter.” — **effects:** sets stage 10 of [Fair play?](../quests/brv_blackjack.md#stage-10)

    - “I don't know the password.” → *conversation ends*
    - “[Tell him the password]” *(if reached stage 30 of [Fair play?](../quests/brv_blackjack.md#stage-30))* → [brv_tavern_west_guard_20](#d-brv_tavern_west_guard-brv_tavern_west_guard_20)

    <span id="d-brv_tavern_west_guard-brv_tavern_west_backroom_6"></span>**`brv_tavern_west_backroom_6`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 10 of [Fair play?](../quests/brv_blackjack.md#stage-10)

    - branch 1 → [brv_tavern_west_guard_10](#d-brv_tavern_west_guard-brv_tavern_west_guard_10)



### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 7 lines added |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line added, 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brv_tavern_west_guard)"

    | | |
    |---|---|
    | Entry ID | `brv_tavern_west_guard` |
    | Spawn group | `brv_tavern_west_guard` |
    | Loot table | – |
    | Conversation | `brv_tavern_west_guard_select` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:69` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "brv_tavern_west_guard",
     "name": "Guard",
     "iconID": "monsters_rltiles1:69",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_tavern_west_guard",
     "phraseID": "brv_tavern_west_guard_select"
    }
    ```


## Foaming Flask Tavern, Waytominingtown2 (charwd_guard) { #v-charwd_guard }

**Entry ID:** `charwd_guard` · **Type:** NPC

**Location:** Foaming Flask Tavern: [waytominingtown2](../maps/waytominingtown2.md#pin-npc-charwd_guard)

### Quests

- [Destined for great things](../quests/charwood1.md): stages 19, 35

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/charwd_guard.json" data-npc="Guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-charwd_guard-charwd_guard"></span>**`charwd_guard`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 19 of [Destined for great things](../quests/charwood1.md#stage-19)

    - branch 1 *(if reached stage 35 of [Destined for great things](../quests/charwood1.md#stage-35))* → [charwd_guard2](#d-charwd_guard-charwd_guard2)
    - branch 2 → [charwd_guard0](#d-charwd_guard-charwd_guard0)

    <span id="d-charwd_guard-charwd_guard2"></span>**`charwd_guard2`** Guard: “I'll let you enter the hills. Keep heading east, and then turn north once you see the mountain side.” — **effects:** sets stage 35 of [Destined for great things](../quests/charwood1.md#stage-35)

    - “Thank you.” → *NPC leaves*
    - “I sure hope there's some reward for all of this later.” → *NPC leaves*

    <span id="d-charwd_guard-charwd_guard0"></span>**`charwd_guard0`** Guard: “You better talk to Maevalia.”

    - “I've already talked to her, and I have agreed to help find your missing people.” *(if reached stage 30 of [Destined for great things](../quests/charwood1.md#stage-30))* → [charwd_guard1](#d-charwd_guard-charwd_guard1)
    - “What's back here?” → [charwd_guard4](#d-charwd_guard-charwd_guard4)
    - “OK, I'll go talk to her.” → [charwd_guard3](#d-charwd_guard-charwd_guard3)

    <span id="d-charwd_guard-charwd_guard1"></span>**`charwd_guard1`** Guard: “Good. We need all the help we can get.”

    - Next → [charwd_guard2](#d-charwd_guard-charwd_guard2)

    <span id="d-charwd_guard-charwd_guard4"></span>**`charwd_guard4`** Guard: “Behind me is the path up to the Charwood mining town. You really should go talk to Maevalia though. She's inside the cabin.”

    - “OK, I'll go talk to her.” → [charwd_guard3](#d-charwd_guard-charwd_guard3)
    - “I've already talked to her, and I have agreed to help find your missing people.” *(if reached stage 30 of [Destined for great things](../quests/charwood1.md#stage-30))* → [charwd_guard1](#d-charwd_guard-charwd_guard1)

    <span id="d-charwd_guard-charwd_guard3"></span>**`charwd_guard3`** Guard: “Yes, you do that.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (charwd_guard)"

    | | |
    |---|---|
    | Entry ID | `charwd_guard` |
    | Spawn group | `charwd_guard` |
    | Loot table | – |
    | Conversation | `charwd_guard` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:114` |
    | Defined in | `res/raw/monsterlist_v070_npcs.json` |

    Raw data:

    ```json
    {
     "id": "charwd_guard",
     "name": "Guard",
     "iconID": "monsters_ld1:114",
     "unique": 1,
     "phraseID": "charwd_guard"
    }
    ```


## Crossroads Guardhouse, Houseatcrossroads1 (crossroads_backguard) { #v-crossroads_backguard }

**Entry ID:** `crossroads_backguard` · **Type:** NPC

**Location:** Crossroads Guardhouse: [houseatcrossroads1](../maps/houseatcrossroads1.md#pin-npc-crossroads_backguard)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/crossroads_backguard.json" data-npc="Guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (11 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-crossroads_backguard-crossroads_backguard"></span>**`crossroads_backguard`** Guard: “Uh, hello.”

    - “Hello. What's back there?” → [crossroads_backguard_1](#d-crossroads_backguard-crossroads_backguard_1)

    <span id="d-crossroads_backguard-crossroads_backguard_1"></span>**`crossroads_backguard_1`** Guard: “Back there? Oh, nothing.”

    - “OK, never mind then.” → *conversation ends*
    - “But there's a hole in the wall there. Where does it lead?” → [crossroads_backguard_2](#d-crossroads_backguard-crossroads_backguard_2)

    <span id="d-crossroads_backguard-crossroads_backguard_2"></span>**`crossroads_backguard_2`** Guard: “Lead? Oh nowhere. Nothing back there at all.”

    - “OK, never mind then.” → *conversation ends*
    - “There's something you are not telling me.” → [crossroads_backguard_3](#d-crossroads_backguard-crossroads_backguard_3)

    <span id="d-crossroads_backguard-crossroads_backguard_3"></span>**`crossroads_backguard_3`** Guard: “Oh no, no. Nothing interesting here. Move along now.”

    - “OK, never mind then.” → *conversation ends*
    - “How about I pay you 100 gold to move out of the way?” → [crossroads_backguard_4](#d-crossroads_backguard-crossroads_backguard_4)

    <span id="d-crossroads_backguard-crossroads_backguard_4"></span>**`crossroads_backguard_4`** Guard: “You would do that? Hmm, let me think.”

    - Next → [crossroads_backguard_5](#d-crossroads_backguard-crossroads_backguard_5)

    <span id="d-crossroads_backguard-crossroads_backguard_5"></span>**`crossroads_backguard_5`** Guard: “No.”

    - “OK, never mind then.” → *conversation ends*
    - “200 gold then?” → [crossroads_backguard_6](#d-crossroads_backguard-crossroads_backguard_6)

    <span id="d-crossroads_backguard-crossroads_backguard_6"></span>**`crossroads_backguard_6`** Guard: “No.”

    - “OK, never mind then.” → *conversation ends*
    - “400 gold then?” → [crossroads_backguard_7](#d-crossroads_backguard-crossroads_backguard_7)

    <span id="d-crossroads_backguard-crossroads_backguard_7"></span>**`crossroads_backguard_7`** Guard: “Look, you are not getting back there, and there is nothing to see back there.”

    - “OK, never mind then.” → *conversation ends*
    - “OK, final offer, 800 gold? That's a fortune.” → [crossroads_backguard_8](#d-crossroads_backguard-crossroads_backguard_8)

    <span id="d-crossroads_backguard-crossroads_backguard_8"></span>**`crossroads_backguard_8`** Guard: “Hmm, 800 gold you say? Well, why didn't you say so from the start? Sure, that could work.”

    - Next → [crossroads_backguard_9](#d-crossroads_backguard-crossroads_backguard_9)

    <span id="d-crossroads_backguard-crossroads_backguard_9"></span>**`crossroads_backguard_9`** Guard: “I should tell you however, that there is something in there that we won't dare go near. I just guard here to make sure it doesn't get out, and that no one goes in.”

    - Next → [crossroads_backguard_10](#d-crossroads_backguard-crossroads_backguard_10)

    <span id="d-crossroads_backguard-crossroads_backguard_10"></span>**`crossroads_backguard_10`** Guard: “Some other guards went in there earlier, and came back screaming. Enter at your own risk, but don't say I didn't warn you.”

    - “Never mind, I was just kidding.” → *conversation ends*
    - “Here is the gold, now get out of the way.” *(if pay 800 gold)* → *NPC leaves*



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 8 lines changed<br>· text: “You would do that? Hm, let me think.” → “You would do that? Hmm, let me think.”<br>· text: “Hm, 800 gold you say? Well, why didn't you say so from the start? Sur…” → “Hmm, 800 gold you say? Well, why didn't you say so from the start? Su…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (crossroads_backguard)"

    | | |
    |---|---|
    | Entry ID | `crossroads_backguard` |
    | Spawn group | `crossroads_backguard` |
    | Loot table | – |
    | Conversation | `crossroads_backguard` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:76` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "crossroads_backguard",
     "name": "Guard",
     "iconID": "monsters_rltiles1:76",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "crossroads_backguard",
     "phraseID": "crossroads_backguard"
    }
    ```


## Crossroads Guardhouse, Crossroads and 2 more (crossroads_guard) { #v-crossroads_guard }

**Entry ID:** `crossroads_guard` · **Type:** NPC

**Location:** Crossroads Guardhouse: [crossroads](../maps/crossroads.md#pin-npc-crossroads_guard), Crossroads Guardhouse: [houseatcrossroads2](../maps/houseatcrossroads2.md#pin-npc-crossroads_guard), Crossroads Guardhouse: [houseatcrossroads3](../maps/houseatcrossroads3.md#pin-npc-crossroads_guard)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [crossroads](../maps/crossroads.md) | Crossroads Guardhouse | 2 | – |
| [houseatcrossroads2](../maps/houseatcrossroads2.md) | Crossroads Guardhouse | 1 | – |
| [houseatcrossroads3](../maps/houseatcrossroads3.md) | Crossroads Guardhouse | 1 | – |

### Quests

- [The ruthless Crackshot](../quests/Thieves03.md): stage 15

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/crossroads_guard.json" data-npc="Guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (10 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-crossroads_guard-crossroads_guard"></span>**`crossroads_guard`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 10 of [The ruthless Crackshot](../quests/Thieves03.md#stage-10); NOT reached stage 15 of [The ruthless Crackshot](../quests/Thieves03.md#stage-15))* → [crossroads_guild03_1](#d-crossroads_guard-crossroads_guild03_1)
    - branch 2 *(if reached stage 90 of [Night visit](../quests/farrik.md#stage-90))* → [crossroads_guard_r_1](#d-crossroads_guard-crossroads_guard_r_1)
    - branch 3 → [crossroads_guard_1](#d-crossroads_guard-crossroads_guard_1)

    <span id="d-crossroads_guard-crossroads_guild03_1"></span>**`crossroads_guild03_1`** Guard: “Aren't you a bit young to be travelling around here all by yourself?”

    - “Sorry, have you heard anything about a murder?” → [crossroads_guild03_2](#d-crossroads_guard-crossroads_guild03_2)

    <span id="d-crossroads_guard-crossroads_guard_r_1"></span>**`crossroads_guard_r_1`** Guard: “Did you hear? Some thieves down in Fallhaven were planning an escape for one of the imprisoned thieves in the prison there.”

    - Next → [crossroads_guard_r_2](#d-crossroads_guard-crossroads_guard_r_2)

    <span id="d-crossroads_guard-crossroads_guard_1"></span>**`crossroads_guard_1`** Guard: “Aren't you a bit young to be traveling around here all by yourself?”

    - Next → [crossroads_guard_2](#d-crossroads_guard-crossroads_guard_2)

    <span id="d-crossroads_guard-crossroads_guild03_2"></span>**`crossroads_guild03_2`** Guard: “Yeah, Feygard authorities have sent more patrols to the south. Apparently there is a group of criminals hiding in the forest” — **effects:** sets stage 15 of [The ruthless Crackshot](../quests/Thieves03.md#stage-15)

    - Next → [crossroads_guild03_3](#d-crossroads_guard-crossroads_guild03_3)

    <span id="d-crossroads_guard-crossroads_guard_r_2"></span>**`crossroads_guard_r_2`** Guard: “Luckily, someone got wind of it and told the guard captain.”

    - Next → [crossroads_guard_r_3](#d-crossroads_guard-crossroads_guard_r_3)

    <span id="d-crossroads_guard-crossroads_guard_2"></span>**`crossroads_guard_2`** Guard: “I sure hope you are not another one of those types trying to sell me your cheap junk.”

    - Next → [crossroads_guard_3](#d-crossroads_guard-crossroads_guard_3)

    <span id="d-crossroads_guard-crossroads_guild03_3"></span>**`crossroads_guild03_3`** Guard: “Now go away kid, I'm working!”


    <span id="d-crossroads_guard-crossroads_guard_r_3"></span>**`crossroads_guard_r_3`** Guard: “It's good to know that there are at least a few decent people still around.”


    <span id="d-crossroads_guard-crossroads_guard_3"></span>**`crossroads_guard_3`** Guard: “Go away, kid.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 3 lines added, 2 lines changed<br>· text: “Aren't you a bit young to be travelling around here all by yourself?” → “Aren't you a bit young to be traveling around here all by yourself?” |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 1 line changed<br>· text: “Yeah, Feygard authorities have sent more patrols to the south. Appear…” → “Yeah, Feygard authorities have sent more patrols to the south. Appare…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (crossroads_guard)"

    | | |
    |---|---|
    | Entry ID | `crossroads_guard` |
    | Spawn group | `crossroads_guard` |
    | Loot table | – |
    | Conversation | `crossroads_guard` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:76` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "crossroads_guard",
     "name": "Guard",
     "iconID": "monsters_rltiles1:76",
     "monsterClass": "humanoid",
     "spawnGroup": "crossroads_guard",
     "phraseID": "crossroads_guard"
    }
    ```


## Crossroads Guardhouse, Houseatcrossroads1 (crossroads_sleepguard) { #v-crossroads_sleepguard }

**Entry ID:** `crossroads_sleepguard` · **Type:** NPC

**Location:** Crossroads Guardhouse: [houseatcrossroads1](../maps/houseatcrossroads1.md#pin-npc-crossroads_sleepguard)

### Quests

- [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md): stage 17

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/crossroads_sleepguard.json" data-npc="Guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-crossroads_sleepguard-crossroads_sleepguard"></span>**`crossroads_sleepguard`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 17 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-17))* → [crossroads_sleepguard_2](#d-crossroads_sleepguard-crossroads_sleepguard_2)
    - branch 2 → [crossroads_sleepguard_1](#d-crossroads_sleepguard-crossroads_sleepguard_1)

    <span id="d-crossroads_sleepguard-crossroads_sleepguard_2"></span>**`crossroads_sleepguard_2`** Guard: “Hello again. I hope the bed is comfortable enough. Use it as much as you like.”


    <span id="d-crossroads_sleepguard-crossroads_sleepguard_1"></span>**`crossroads_sleepguard_1`** Guard: “Hello there. Can I help you?”

    - “No. Goodbye.” → *conversation ends*
    - “Mind if I use one of the beds over there?” → [crossroads_sleepguard_3](#d-crossroads_sleepguard-crossroads_sleepguard_3)

    <span id="d-crossroads_sleepguard-crossroads_sleepguard_3"></span>**`crossroads_sleepguard_3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 90 of [Night visit](../quests/farrik.md#stage-90))* → [crossroads_sleepguard_5](#d-crossroads_sleepguard-crossroads_sleepguard_5)
    - branch 2 → [crossroads_sleepguard_4](#d-crossroads_sleepguard-crossroads_sleepguard_4)

    <span id="d-crossroads_sleepguard-crossroads_sleepguard_5"></span>**`crossroads_sleepguard_5`** Guard: “Say, aren't you that kid that helped the guards down in Fallhaven? With the thieves that were planning an escape?”

    - “Yes, I helped the guards in the prison find out about some plans that the thieves had.” → [crossroads_sleepguard_6](#d-crossroads_sleepguard-crossroads_sleepguard_6)

    <span id="d-crossroads_sleepguard-crossroads_sleepguard_4"></span>**`crossroads_sleepguard_4`** Guard: “No, sorry. These beds are for guards and allies of Feygard only.”


    <span id="d-crossroads_sleepguard-crossroads_sleepguard_6"></span>**`crossroads_sleepguard_6`** Guard: “I knew I had heard about you somewhere. You are always welcome by us guards. You can use that second bed over there to the left if you need to rest.” — **effects:** sets stage 17 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-17)




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (crossroads_sleepguard)"

    | | |
    |---|---|
    | Entry ID | `crossroads_sleepguard` |
    | Spawn group | `crossroads_sleepguard` |
    | Loot table | – |
    | Conversation | `crossroads_sleepguard` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:76` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "crossroads_sleepguard",
     "name": "Guard",
     "iconID": "monsters_rltiles1:76",
     "monsterClass": "humanoid",
     "spawnGroup": "crossroads_sleepguard",
     "phraseID": "crossroads_sleepguard"
    }
    ```


## Flagstone Prison, Flagstone0 (flagstone_guard) { #v-flagstone_guard }

**Entry ID:** `flagstone_guard` · **Type:** NPC

**Location:** Flagstone Prison: [flagstone0](../maps/flagstone0.md#pin-npc-flagstone_guard)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/flagstone_guard.json" data-npc="Guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-flagstone_guard-flagstone_guard"></span>**`flagstone_guard`** Guard: “I hate this place. It rains all the time and I can't stand the eerie screams of the undead!”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (flagstone_guard)"

    | | |
    |---|---|
    | Entry ID | `flagstone_guard` |
    | Spawn group | `flagstone_guard` |
    | Loot table | – |
    | Conversation | `flagstone_guard` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:44` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "flagstone_guard",
     "name": "Guard",
     "iconID": "monsters_tometik2:44",
     "spawnGroup": "flagstone_guard",
     "phraseID": "flagstone_guard"
    }
    ```


## Brimhaven, Brimhaven3 (guard_advent) { #v-guard_advent }

**Entry ID:** `guard_advent` · **Type:** NPC

**Location:** Brimhaven: [brimhaven3](../maps/brimhaven3.md#pin-npc-guard_advent)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/guard_advent.json" data-npc="Guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (19 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guard_advent-guard_advent"></span>**`guard_advent`** Guard: “I used to be an adventurer like you,”

    - Next → [guard_advent_2](#d-guard_advent-guard_advent_2)

    <span id="d-guard_advent-guard_advent_2"></span>**`guard_advent_2`** Guard: “Then I took an arrow in the knee.”

    - “Sorry for you.” → *conversation ends*
    - “That reminds me of a song.” *(if random chance (20%))* → [guard_advent_4](#d-guard_advent-guard_advent_4)
    - “I'm wondering, do you know anything about Lawellyn's death?” *(if reached stage 130 of [A strange looking dagger](../quests/brv_dagger.md#stage-130); NOT reached stage 200 of [A strange looking dagger](../quests/brv_dagger.md#stage-200); NOT reached stage 230 of [A strange looking dagger](../quests/brv_dagger.md#stage-230))* → [guard_advent_asd_10](#d-guard_advent-guard_advent_asd_10)

    <span id="d-guard_advent-guard_advent_4"></span>**`guard_advent_4`** Guard: “I think I know which song you are thinking of.”

    - “Shall we sing it together?” → [guard_advent_10](#d-guard_advent-guard_advent_10)

    <span id="d-guard_advent-guard_advent_asd_10"></span>**`guard_advent_asd_10`** Guard: “Death? The last I knew was that Arlish reported him missing.”


    <span id="d-guard_advent-guard_advent_10"></span>**`guard_advent_10`** Guard: “Mahna.”

    - “Mahna mahna?” → [guard_advent_12](#d-guard_advent-guard_advent_12)

    <span id="d-guard_advent-guard_advent_12"></span>**`guard_advent_12`** Guard: “I took an arrow ...”

    - “You took an arrow” → [guard_advent_14](#d-guard_advent-guard_advent_14)

    <span id="d-guard_advent-guard_advent_14"></span>**`guard_advent_14`** Guard: “... right in the knee.”

    - “right in your knee” → [guard_advent_16](#d-guard_advent-guard_advent_16)

    <span id="d-guard_advent-guard_advent_16"></span>**`guard_advent_16`** Guard: “I took an arrow.”

    - “You took an arrow, an arrow, an arrow, an evil dirty arrow in your knee.” → [guard_advent_20](#d-guard_advent-guard_advent_20)

    <span id="d-guard_advent-guard_advent_20"></span>**`guard_advent_20`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (50%))* → [guard_advent_22](#d-guard_advent-guard_advent_22)
    - branch 2 → [guard_advent_30](#d-guard_advent-guard_advent_30)

    <span id="d-guard_advent-guard_advent_22"></span>**`guard_advent_22`** Guard: “-”

    - “What?” → [guard_advent_30](#d-guard_advent-guard_advent_30)

    <span id="d-guard_advent-guard_advent_30"></span>**`guard_advent_30`** Guard: “I took an arrow ...”

    - “He took an arrow” → [guard_advent_32](#d-guard_advent-guard_advent_32)

    <span id="d-guard_advent-guard_advent_32"></span>**`guard_advent_32`** Guard: “... right in the knee.”

    - “right in his knee” → [guard_advent_34](#d-guard_advent-guard_advent_34)

    <span id="d-guard_advent-guard_advent_34"></span>**`guard_advent_34`** Guard: “I took an arrow.”

    - “He took an arrow, an arrow, an arrow, an evil dirty arrow in his knee.” → [guard_advent_40](#d-guard_advent-guard_advent_40)

    <span id="d-guard_advent-guard_advent_40"></span>**`guard_advent_40`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (25%))* → [guard_advent_12](#d-guard_advent-guard_advent_12)
    - branch 2 → [guard_advent_50](#d-guard_advent-guard_advent_50)

    <span id="d-guard_advent-guard_advent_50"></span>**`guard_advent_50`** Guard: “An adventurer like you,”

    - Next → [guard_advent_52](#d-guard_advent-guard_advent_52)

    <span id="d-guard_advent-guard_advent_52"></span>**`guard_advent_52`** Guard: “I took an arrow in the knee!”

    - Next → [guard_advent_54](#d-guard_advent-guard_advent_54)

    <span id="d-guard_advent-guard_advent_54"></span>**`guard_advent_54`** Guard: “adventunarrow, In the knee the arrow”

    - Next → [guard_advent_56](#d-guard_advent-guard_advent_56)

    <span id="d-guard_advent-guard_advent_56"></span>**`guard_advent_56`** Guard: “La be di bap bap ...”

    - Next → [guard_advent_58](#d-guard_advent-guard_advent_58)

    <span id="d-guard_advent-guard_advent_58"></span>**`guard_advent_58`** Guard: “Die be die be boo mbie La be di bap bap ...”

    - “What??” → [guard_advent_12](#d-guard_advent-guard_advent_12)



### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 18 lines added |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guard_advent)"

    | | |
    |---|---|
    | Entry ID | `guard_advent` |
    | Spawn group | `guard_advent` |
    | Loot table | – |
    | Conversation | `guard_advent` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:41` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "guard_advent",
     "name": "Guard",
     "iconID": "monsters_ld1:41",
     "phraseID": "guard_advent"
    }
    ```


## Loneford, Loneford10 and 1 more (loneford_guard0) { #v-loneford_guard0 }

**Entry ID:** `loneford_guard0` · **Type:** NPC

**Location:** Loneford: [loneford10](../maps/loneford10.md#pin-npc-loneford_guard0), Loneford: [loneford2](../maps/loneford2.md#pin-npc-loneford_guard0)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [loneford10](../maps/loneford10.md) | Loneford | 2 | – |
| [loneford2](../maps/loneford2.md) | Loneford | 1 | – |

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/loneford_guard0.json" data-npc="Guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-loneford_guard0-loneford_guard0"></span>**`loneford_guard0`** Guard: “We keep the order around here. I wonder what the people of Loneford would do without us guards from Feygard. Poor things.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (loneford_guard0)"

    | | |
    |---|---|
    | Entry ID | `loneford_guard0` |
    | Spawn group | `loneford_guard0` |
    | Loot table | – |
    | Conversation | `loneford_guard0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles3:14` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "loneford_guard0",
     "name": "Guard",
     "iconID": "monsters_rltiles3:14",
     "monsterClass": "humanoid",
     "spawnGroup": "loneford_guard0",
     "phraseID": "loneford_guard0"
    }
    ```


## Loneford, Loneford2 (loneford_wellguard) { #v-loneford_wellguard }

**Entry ID:** `loneford_wellguard` · **Type:** NPC

**Location:** Loneford: [loneford2](../maps/loneford2.md#pin-npc-loneford_wellguard)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/loneford_wellguard.json" data-npc="Guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-loneford_wellguard-loneford_wellguard"></span>**`loneford_wellguard`** Guard: “Please report any suspicious behavior you might see to Kuldan.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (loneford_wellguard)"

    | | |
    |---|---|
    | Entry ID | `loneford_wellguard` |
    | Spawn group | `loneford_wellguard` |
    | Loot table | – |
    | Conversation | `loneford_wellguard` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:72` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "loneford_wellguard",
     "name": "Guard",
     "iconID": "monsters_rltiles1:72",
     "monsterClass": "humanoid",
     "spawnGroup": "loneford_wellguard",
     "phraseID": "loneford_wellguard"
    }
    ```


## Remgard, Remgard church and 1 more (remgard_g1) { #v-remgard_g1 }

**Entry ID:** `remgard_g1` · **Type:** NPC

**Location:** Remgard: [remgard_church](../maps/remgard_church.md#pin-npc-remgard_g1), Remgard: [remgard_tavern1](../maps/remgard_tavern1.md#pin-npc-remgard_g1)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [remgard_church](../maps/remgard_church.md) | Remgard | 1 | – |
| [remgard_tavern1](../maps/remgard_tavern1.md) | Remgard | 1 | – |

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/fallhaven_guard.json" data-npc="Guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [fallhaven_guard](#d-guard-fallhaven_guard).


### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (remgard_g1)"

    | | |
    |---|---|
    | Entry ID | `remgard_g1` |
    | Spawn group | `remgard_guard` |
    | Loot table | – |
    | Conversation | `fallhaven_guard` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:4` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "remgard_g1",
     "name": "Guard",
     "iconID": "monsters_ld1:4",
     "monsterClass": "humanoid",
     "spawnGroup": "remgard_guard",
     "phraseID": "fallhaven_guard"
    }
    ```


## Remgard, Remgard church and 1 more (remgard_g2) { #v-remgard_g2 }

**Entry ID:** `remgard_g2` · **Type:** NPC

**Location:** Remgard: [remgard_church](../maps/remgard_church.md#pin-npc-remgard_g2), Remgard: [remgard_tavern1](../maps/remgard_tavern1.md#pin-npc-remgard_g2)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [remgard_church](../maps/remgard_church.md) | Remgard | 1 | – |
| [remgard_tavern1](../maps/remgard_tavern1.md) | Remgard | 1 | – |

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/blackwater_guard1.json" data-npc="Guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-remgard_g2-blackwater_guard1"></span>**`blackwater_guard1`** Guard: “Stay out of trouble and trouble will stay away from you.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (remgard_g2)"

    | | |
    |---|---|
    | Entry ID | `remgard_g2` |
    | Spawn group | `remgard_guard` |
    | Loot table | – |
    | Conversation | `blackwater_guard1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:5` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "remgard_g2",
     "name": "Guard",
     "iconID": "monsters_ld1:5",
     "monsterClass": "humanoid",
     "spawnGroup": "remgard_guard",
     "phraseID": "blackwater_guard1"
    }
    ```


## Remgard, Remgard tavern1 (remgard_g3) { #v-remgard_g3 }

**Entry ID:** `remgard_g3` · **Type:** NPC

**Location:** Remgard: [remgard_tavern1](../maps/remgard_tavern1.md#pin-npc-remgard_g3)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/remgard_guard1.json" data-npc="Guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-remgard_g3-remgard_guard1"></span>**`remgard_guard1`** Guard: “I've got my eye on you. Don't do anything stupid.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (remgard_g3)"

    | | |
    |---|---|
    | Entry ID | `remgard_g3` |
    | Spawn group | `remgard_guard2` |
    | Loot table | – |
    | Conversation | `remgard_guard1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:67` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "remgard_g3",
     "name": "Guard",
     "iconID": "monsters_ld1:67",
     "monsterClass": "humanoid",
     "spawnGroup": "remgard_guard2",
     "phraseID": "remgard_guard1"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
