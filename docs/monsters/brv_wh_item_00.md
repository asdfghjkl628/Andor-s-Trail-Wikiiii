---
description: "Warehouse storage spot is a non-player character (NPC) in Andor's Trail, found in Brimhaven."
---

# ![](../assets/icons/monsters/monsters_guynmart_8.png){ .sprite } Warehouse storage spot

**Where to find Warehouse storage spot:** [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_00), [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_01), [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_02), [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_03), [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_04), [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_05), [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_06), [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_07), [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_08), [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_09), [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_20), [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_21), [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_22), [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_23), [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_24), [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_25), [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_26), [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_27), [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_28), [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_29)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_guynmart_8.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Brimhaven |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Brimhaven, Brimhaven warehouse { #v-brv_wh_item_00 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_item_00)

### Quests

- [Inventory](../quests/brv_wh.md): stage 100

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse storage spot. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_00.json" data-npc="Warehouse storage spot" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_item_00-brv_wh_item_00"></span>**`brv_wh_item_00`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 120)* → [brv_wh_item_00_1](#d-brv_wh_item_00-brv_wh_item_00_1)
    - branch 2 *(if faction “brv_wh_aln” = 100)* → [brv_wh_item_xx_2](#d-brv_wh_item_00-brv_wh_item_xx_2)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_00-brv_wh_item_xx_3)
    - branch 4 → [brv_wh_item_00_4](#d-brv_wh_item_00-brv_wh_item_00_4)

    <span id="d-brv_wh_item_00-brv_wh_item_00_1"></span>**`brv_wh_item_00_1`** Warehouse storage spot: “You have found the second crystal globe. Now that's a pair!” — **effects:** sets stage 100 of [Inventory](../quests/brv_wh.md#stage-100), gives 2× [Crystal globe](../items/brv_wh_item_00.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse


    <span id="d-brv_wh_item_00-brv_wh_item_xx_2"></span>**`brv_wh_item_xx_2`** Warehouse storage spot: “You put it back to its former place.” — **effects:** faction “brv_wh_aln” set to 0


    <span id="d-brv_wh_item_00-brv_wh_item_xx_3"></span>**`brv_wh_item_xx_3`** Warehouse storage spot: “No, this is not what you're looking for. You put both items back to their bin.” — **effects:** faction “brv_wh_aln” set to 0


    <span id="d-brv_wh_item_00-brv_wh_item_00_4"></span>**`brv_wh_item_00_4`** Warehouse storage spot: “You take the item.” — **effects:** faction “brv_wh_aln” set to 100




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven warehouse (2) { #v-brv_wh_item_01 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_item_01)

### Quests

- [Inventory](../quests/brv_wh.md): stage 101

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse storage spot. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_01.json" data-npc="Warehouse storage spot" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_item_01-brv_wh_item_01"></span>**`brv_wh_item_01`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 121)* → [brv_wh_item_01_1](#d-brv_wh_item_01-brv_wh_item_01_1)
    - branch 2 *(if faction “brv_wh_aln” = 101)* → [brv_wh_item_xx_2](#d-brv_wh_item_00-brv_wh_item_xx_2) (listed above)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_00-brv_wh_item_xx_3) (listed above)
    - branch 4 → [brv_wh_item_01_4](#d-brv_wh_item_01-brv_wh_item_01_4)

    <span id="d-brv_wh_item_01-brv_wh_item_01_1"></span>**`brv_wh_item_01_1`** Warehouse storage spot: “You have found the second plush pillow!” — **effects:** sets stage 101 of [Inventory](../quests/brv_wh.md#stage-101), gives 2× [Plush pillow](../items/brv_wh_item_01.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse


    <span id="d-brv_wh_item_01-brv_wh_item_01_4"></span>**`brv_wh_item_01_4`** Warehouse storage spot: “You take the item.” — **effects:** faction “brv_wh_aln” set to 101




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven warehouse (3) { #v-brv_wh_item_02 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_item_02)

### Quests

- [Inventory](../quests/brv_wh.md): stage 102

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse storage spot. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_02.json" data-npc="Warehouse storage spot" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_item_02-brv_wh_item_02"></span>**`brv_wh_item_02`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 122)* → [brv_wh_item_02_1](#d-brv_wh_item_02-brv_wh_item_02_1)
    - branch 2 *(if faction “brv_wh_aln” = 102)* → [brv_wh_item_xx_2](#d-brv_wh_item_00-brv_wh_item_xx_2) (listed above)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_00-brv_wh_item_xx_3) (listed above)
    - branch 4 → [brv_wh_item_02_4](#d-brv_wh_item_02-brv_wh_item_02_4)

    <span id="d-brv_wh_item_02-brv_wh_item_02_1"></span>**`brv_wh_item_02_1`** Warehouse storage spot: “Great! You have found the second lyre and put it into your bag.” — **effects:** sets stage 102 of [Inventory](../quests/brv_wh.md#stage-102), gives 2× [Lyre](../items/brv_wh_item_02.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse


    <span id="d-brv_wh_item_02-brv_wh_item_02_4"></span>**`brv_wh_item_02_4`** Warehouse storage spot: “You take the item.” — **effects:** faction “brv_wh_aln” set to 102




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven warehouse (4) { #v-brv_wh_item_03 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_item_03)

### Quests

- [Inventory](../quests/brv_wh.md): stage 103

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse storage spot. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_03.json" data-npc="Warehouse storage spot" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_item_03-brv_wh_item_03"></span>**`brv_wh_item_03`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 123)* → [brv_wh_item_03_1](#d-brv_wh_item_03-brv_wh_item_03_1)
    - branch 2 *(if faction “brv_wh_aln” = 103)* → [brv_wh_item_xx_2](#d-brv_wh_item_00-brv_wh_item_xx_2) (listed above)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_00-brv_wh_item_xx_3) (listed above)
    - branch 4 → [brv_wh_item_03_4](#d-brv_wh_item_03-brv_wh_item_03_4)

    <span id="d-brv_wh_item_03-brv_wh_item_03_1"></span>**`brv_wh_item_03_1`** Warehouse storage spot: “You have found the yellow boot!” — **effects:** sets stage 103 of [Inventory](../quests/brv_wh.md#stage-103), gives 2× [Yellow boot](../items/brv_wh_item_03.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse


    <span id="d-brv_wh_item_03-brv_wh_item_03_4"></span>**`brv_wh_item_03_4`** Warehouse storage spot: “You take the item.” — **effects:** faction “brv_wh_aln” set to 103




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven warehouse (5) { #v-brv_wh_item_04 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_item_04)

### Quests

- [Inventory](../quests/brv_wh.md): stage 104

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse storage spot. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_04.json" data-npc="Warehouse storage spot" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_item_04-brv_wh_item_04"></span>**`brv_wh_item_04`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 124)* → [brv_wh_item_04_1](#d-brv_wh_item_04-brv_wh_item_04_1)
    - branch 2 *(if faction “brv_wh_aln” = 104)* → [brv_wh_item_xx_2](#d-brv_wh_item_00-brv_wh_item_xx_2) (listed above)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_00-brv_wh_item_xx_3) (listed above)
    - branch 4 → [brv_wh_item_04_4](#d-brv_wh_item_04-brv_wh_item_04_4)

    <span id="d-brv_wh_item_04-brv_wh_item_04_1"></span>**`brv_wh_item_04_1`** Warehouse storage spot: “You have found the second chandelier!” — **effects:** sets stage 104 of [Inventory](../quests/brv_wh.md#stage-104), gives 2× [Chandelier](../items/brv_wh_item_04.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse


    <span id="d-brv_wh_item_04-brv_wh_item_04_4"></span>**`brv_wh_item_04_4`** Warehouse storage spot: “You take the item.” — **effects:** faction “brv_wh_aln” set to 104




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven warehouse (6) { #v-brv_wh_item_05 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_item_05)

### Quests

- [Inventory](../quests/brv_wh.md): stage 105

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse storage spot. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_05.json" data-npc="Warehouse storage spot" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_item_05-brv_wh_item_05"></span>**`brv_wh_item_05`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 125)* → [brv_wh_item_05_1](#d-brv_wh_item_05-brv_wh_item_05_1)
    - branch 2 *(if faction “brv_wh_aln” = 105)* → [brv_wh_item_xx_2](#d-brv_wh_item_00-brv_wh_item_xx_2) (listed above)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_00-brv_wh_item_xx_3) (listed above)
    - branch 4 → [brv_wh_item_05_4](#d-brv_wh_item_05-brv_wh_item_05_4)

    <span id="d-brv_wh_item_05-brv_wh_item_05_1"></span>**`brv_wh_item_05_1`** Warehouse storage spot: “You have found the second mysterious green something!” — **effects:** sets stage 105 of [Inventory](../quests/brv_wh.md#stage-105), gives 2× [Mysterious green something](../items/brv_wh_item_05.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse


    <span id="d-brv_wh_item_05-brv_wh_item_05_4"></span>**`brv_wh_item_05_4`** Warehouse storage spot: “You take the item.” — **effects:** faction “brv_wh_aln” set to 105




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven warehouse (7) { #v-brv_wh_item_06 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_item_06)

### Quests

- [Inventory](../quests/brv_wh.md): stage 106

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse storage spot. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_06.json" data-npc="Warehouse storage spot" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_item_06-brv_wh_item_06"></span>**`brv_wh_item_06`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 126)* → [brv_wh_item_06_1](#d-brv_wh_item_06-brv_wh_item_06_1)
    - branch 2 *(if faction “brv_wh_aln” = 106)* → [brv_wh_item_xx_2](#d-brv_wh_item_00-brv_wh_item_xx_2) (listed above)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_00-brv_wh_item_xx_3) (listed above)
    - branch 4 → [brv_wh_item_06_4](#d-brv_wh_item_06-brv_wh_item_06_4)

    <span id="d-brv_wh_item_06-brv_wh_item_06_1"></span>**`brv_wh_item_06_1`** Warehouse storage spot: “You have found the second old, worn cape!” — **effects:** sets stage 106 of [Inventory](../quests/brv_wh.md#stage-106), gives 2× [Old, worn cape](../items/brv_wh_item_06.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse


    <span id="d-brv_wh_item_06-brv_wh_item_06_4"></span>**`brv_wh_item_06_4`** Warehouse storage spot: “You take the item.” — **effects:** faction “brv_wh_aln” set to 106




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven warehouse (8) { #v-brv_wh_item_07 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_item_07)

### Quests

- [Inventory](../quests/brv_wh.md): stage 107

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse storage spot. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_07.json" data-npc="Warehouse storage spot" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_item_07-brv_wh_item_07"></span>**`brv_wh_item_07`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 127)* → [brv_wh_item_07_1](#d-brv_wh_item_07-brv_wh_item_07_1)
    - branch 2 *(if faction “brv_wh_aln” = 107)* → [brv_wh_item_xx_2](#d-brv_wh_item_00-brv_wh_item_xx_2) (listed above)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_00-brv_wh_item_xx_3) (listed above)
    - branch 4 → [brv_wh_item_07_4](#d-brv_wh_item_07-brv_wh_item_07_4)

    <span id="d-brv_wh_item_07-brv_wh_item_07_1"></span>**`brv_wh_item_07_1`** Warehouse storage spot: “You have found the second pretty porcelain figure!” — **effects:** sets stage 107 of [Inventory](../quests/brv_wh.md#stage-107), gives 2× [Pretty porcelain figure](../items/brv_wh_item_07.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse


    <span id="d-brv_wh_item_07-brv_wh_item_07_4"></span>**`brv_wh_item_07_4`** Warehouse storage spot: “You take the item.” — **effects:** faction “brv_wh_aln” set to 107




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven warehouse (9) { #v-brv_wh_item_08 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_item_08)

### Quests

- [Inventory](../quests/brv_wh.md): stage 108

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse storage spot. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_08.json" data-npc="Warehouse storage spot" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_item_08-brv_wh_item_08"></span>**`brv_wh_item_08`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 128)* → [brv_wh_item_08_1](#d-brv_wh_item_08-brv_wh_item_08_1)
    - branch 2 *(if faction “brv_wh_aln” = 108)* → [brv_wh_item_xx_2](#d-brv_wh_item_00-brv_wh_item_xx_2) (listed above)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_00-brv_wh_item_xx_3) (listed above)
    - branch 4 → [brv_wh_item_08_4](#d-brv_wh_item_08-brv_wh_item_08_4)

    <span id="d-brv_wh_item_08-brv_wh_item_08_1"></span>**`brv_wh_item_08_1`** Warehouse storage spot: “You have found the second striped hammer!” — **effects:** sets stage 108 of [Inventory](../quests/brv_wh.md#stage-108), gives 2× [Striped hammer](../items/brv_wh_item_08.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse


    <span id="d-brv_wh_item_08-brv_wh_item_08_4"></span>**`brv_wh_item_08_4`** Warehouse storage spot: “You take the item.” — **effects:** faction “brv_wh_aln” set to 108




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven warehouse (10) { #v-brv_wh_item_09 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_item_09)

### Quests

- [Inventory](../quests/brv_wh.md): stage 109

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse storage spot. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_09.json" data-npc="Warehouse storage spot" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_item_09-brv_wh_item_09"></span>**`brv_wh_item_09`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 129)* → [brv_wh_item_09_1](#d-brv_wh_item_09-brv_wh_item_09_1)
    - branch 2 *(if faction “brv_wh_aln” = 109)* → [brv_wh_item_xx_2](#d-brv_wh_item_00-brv_wh_item_xx_2) (listed above)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_00-brv_wh_item_xx_3) (listed above)
    - branch 4 → [brv_wh_item_09_4](#d-brv_wh_item_09-brv_wh_item_09_4)

    <span id="d-brv_wh_item_09-brv_wh_item_09_1"></span>**`brv_wh_item_09_1`** Warehouse storage spot: “You have found the second dusty old book!” — **effects:** sets stage 109 of [Inventory](../quests/brv_wh.md#stage-109), gives 2× [Dusty old book](../items/brv_wh_item_09.md), faction “brv_wh_aln” set to 0, removes monsters from brimhaven_warehouse, removes monsters from brimhaven_warehouse


    <span id="d-brv_wh_item_09-brv_wh_item_09_4"></span>**`brv_wh_item_09_4`** Warehouse storage spot: “You take the item.” — **effects:** faction “brv_wh_aln” set to 109




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven warehouse (11) { #v-brv_wh_item_20 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_item_20)

### Quests

- [Inventory](../quests/brv_wh.md): stage 100

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse storage spot. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_20.json" data-npc="Warehouse storage spot" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_item_20-brv_wh_item_20"></span>**`brv_wh_item_20`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 100)* → [brv_wh_item_00_1](#d-brv_wh_item_00-brv_wh_item_00_1) (listed above)
    - branch 2 *(if faction “brv_wh_aln” = 120)* → [brv_wh_item_xx_2](#d-brv_wh_item_00-brv_wh_item_xx_2) (listed above)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_00-brv_wh_item_xx_3) (listed above)
    - branch 4 → [brv_wh_item_20_4](#d-brv_wh_item_20-brv_wh_item_20_4)

    <span id="d-brv_wh_item_20-brv_wh_item_20_4"></span>**`brv_wh_item_20_4`** Warehouse storage spot: “You take the item.” — **effects:** faction “brv_wh_aln” set to 120




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven warehouse (12) { #v-brv_wh_item_21 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_item_21)

### Quests

- [Inventory](../quests/brv_wh.md): stage 101

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse storage spot. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_21.json" data-npc="Warehouse storage spot" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_item_21-brv_wh_item_21"></span>**`brv_wh_item_21`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 101)* → [brv_wh_item_01_1](#d-brv_wh_item_01-brv_wh_item_01_1) (listed above)
    - branch 2 *(if faction “brv_wh_aln” = 121)* → [brv_wh_item_xx_2](#d-brv_wh_item_00-brv_wh_item_xx_2) (listed above)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_00-brv_wh_item_xx_3) (listed above)
    - branch 4 → [brv_wh_item_21_4](#d-brv_wh_item_21-brv_wh_item_21_4)

    <span id="d-brv_wh_item_21-brv_wh_item_21_4"></span>**`brv_wh_item_21_4`** Warehouse storage spot: “You take the item.” — **effects:** faction “brv_wh_aln” set to 121




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven warehouse (13) { #v-brv_wh_item_22 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_item_22)

### Quests

- [Inventory](../quests/brv_wh.md): stage 102

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse storage spot. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_22.json" data-npc="Warehouse storage spot" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_item_22-brv_wh_item_22"></span>**`brv_wh_item_22`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 102)* → [brv_wh_item_02_1](#d-brv_wh_item_02-brv_wh_item_02_1) (listed above)
    - branch 2 *(if faction “brv_wh_aln” = 122)* → [brv_wh_item_xx_2](#d-brv_wh_item_00-brv_wh_item_xx_2) (listed above)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_00-brv_wh_item_xx_3) (listed above)
    - branch 4 → [brv_wh_item_22_4](#d-brv_wh_item_22-brv_wh_item_22_4)

    <span id="d-brv_wh_item_22-brv_wh_item_22_4"></span>**`brv_wh_item_22_4`** Warehouse storage spot: “You take the item.” — **effects:** faction “brv_wh_aln” set to 122




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven warehouse (14) { #v-brv_wh_item_23 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_item_23)

### Quests

- [Inventory](../quests/brv_wh.md): stage 103

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse storage spot. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_23.json" data-npc="Warehouse storage spot" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_item_23-brv_wh_item_23"></span>**`brv_wh_item_23`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 103)* → [brv_wh_item_03_1](#d-brv_wh_item_03-brv_wh_item_03_1) (listed above)
    - branch 2 *(if faction “brv_wh_aln” = 123)* → [brv_wh_item_xx_2](#d-brv_wh_item_00-brv_wh_item_xx_2) (listed above)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_00-brv_wh_item_xx_3) (listed above)
    - branch 4 → [brv_wh_item_23_4](#d-brv_wh_item_23-brv_wh_item_23_4)

    <span id="d-brv_wh_item_23-brv_wh_item_23_4"></span>**`brv_wh_item_23_4`** Warehouse storage spot: “You take the item.” — **effects:** faction “brv_wh_aln” set to 123




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven warehouse (15) { #v-brv_wh_item_24 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_item_24)

### Quests

- [Inventory](../quests/brv_wh.md): stage 104

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse storage spot. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_24.json" data-npc="Warehouse storage spot" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_item_24-brv_wh_item_24"></span>**`brv_wh_item_24`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 104)* → [brv_wh_item_04_1](#d-brv_wh_item_04-brv_wh_item_04_1) (listed above)
    - branch 2 *(if faction “brv_wh_aln” = 124)* → [brv_wh_item_xx_2](#d-brv_wh_item_00-brv_wh_item_xx_2) (listed above)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_00-brv_wh_item_xx_3) (listed above)
    - branch 4 → [brv_wh_item_24_4](#d-brv_wh_item_24-brv_wh_item_24_4)

    <span id="d-brv_wh_item_24-brv_wh_item_24_4"></span>**`brv_wh_item_24_4`** Warehouse storage spot: “You take the item.” — **effects:** faction “brv_wh_aln” set to 124




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven warehouse (16) { #v-brv_wh_item_25 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_item_25)

### Quests

- [Inventory](../quests/brv_wh.md): stage 105

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse storage spot. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_25.json" data-npc="Warehouse storage spot" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_item_25-brv_wh_item_25"></span>**`brv_wh_item_25`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 105)* → [brv_wh_item_05_1](#d-brv_wh_item_05-brv_wh_item_05_1) (listed above)
    - branch 2 *(if faction “brv_wh_aln” = 125)* → [brv_wh_item_xx_2](#d-brv_wh_item_00-brv_wh_item_xx_2) (listed above)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_00-brv_wh_item_xx_3) (listed above)
    - branch 4 → [brv_wh_item_25_4](#d-brv_wh_item_25-brv_wh_item_25_4)

    <span id="d-brv_wh_item_25-brv_wh_item_25_4"></span>**`brv_wh_item_25_4`** Warehouse storage spot: “You take the item.” — **effects:** faction “brv_wh_aln” set to 125




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven warehouse (17) { #v-brv_wh_item_26 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_item_26)

### Quests

- [Inventory](../quests/brv_wh.md): stage 106

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse storage spot. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_26.json" data-npc="Warehouse storage spot" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_item_26-brv_wh_item_26"></span>**`brv_wh_item_26`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 106)* → [brv_wh_item_06_1](#d-brv_wh_item_06-brv_wh_item_06_1) (listed above)
    - branch 2 *(if faction “brv_wh_aln” = 126)* → [brv_wh_item_xx_2](#d-brv_wh_item_00-brv_wh_item_xx_2) (listed above)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_00-brv_wh_item_xx_3) (listed above)
    - branch 4 → [brv_wh_item_26_4](#d-brv_wh_item_26-brv_wh_item_26_4)

    <span id="d-brv_wh_item_26-brv_wh_item_26_4"></span>**`brv_wh_item_26_4`** Warehouse storage spot: “You take the item.” — **effects:** faction “brv_wh_aln” set to 126




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven warehouse (18) { #v-brv_wh_item_27 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_item_27)

### Quests

- [Inventory](../quests/brv_wh.md): stage 107

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse storage spot. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_27.json" data-npc="Warehouse storage spot" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_item_27-brv_wh_item_27"></span>**`brv_wh_item_27`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 107)* → [brv_wh_item_07_1](#d-brv_wh_item_07-brv_wh_item_07_1) (listed above)
    - branch 2 *(if faction “brv_wh_aln” = 127)* → [brv_wh_item_xx_2](#d-brv_wh_item_00-brv_wh_item_xx_2) (listed above)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_00-brv_wh_item_xx_3) (listed above)
    - branch 4 → [brv_wh_item_27_4](#d-brv_wh_item_27-brv_wh_item_27_4)

    <span id="d-brv_wh_item_27-brv_wh_item_27_4"></span>**`brv_wh_item_27_4`** Warehouse storage spot: “You take the item.” — **effects:** faction “brv_wh_aln” set to 127




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven warehouse (19) { #v-brv_wh_item_28 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_item_28)

### Quests

- [Inventory](../quests/brv_wh.md): stage 108

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse storage spot. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_28.json" data-npc="Warehouse storage spot" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_item_28-brv_wh_item_28"></span>**`brv_wh_item_28`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 108)* → [brv_wh_item_08_1](#d-brv_wh_item_08-brv_wh_item_08_1) (listed above)
    - branch 2 *(if faction “brv_wh_aln” = 128)* → [brv_wh_item_xx_2](#d-brv_wh_item_00-brv_wh_item_xx_2) (listed above)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_00-brv_wh_item_xx_3) (listed above)
    - branch 4 → [brv_wh_item_28_4](#d-brv_wh_item_28-brv_wh_item_28_4)

    <span id="d-brv_wh_item_28-brv_wh_item_28_4"></span>**`brv_wh_item_28_4`** Warehouse storage spot: “You take the item.” — **effects:** faction “brv_wh_aln” set to 128




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Brimhaven, Brimhaven warehouse (20) { #v-brv_wh_item_29 }

**Where:** Brimhaven: [Brimhaven warehouse](../maps/brimhaven_warehouse.md#pin-npc-brv_wh_item_29)

### Quests

- [Inventory](../quests/brv_wh.md): stage 109

### Dialogue simulator

Set your quest stages and items, then talk to Warehouse storage spot. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_wh_item_29.json" data-npc="Warehouse storage spot" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brv_wh_item_29-brv_wh_item_29"></span>**`brv_wh_item_29`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “brv_wh_aln” = 109)* → [brv_wh_item_09_1](#d-brv_wh_item_09-brv_wh_item_09_1) (listed above)
    - branch 2 *(if faction “brv_wh_aln” = 129)* → [brv_wh_item_xx_2](#d-brv_wh_item_00-brv_wh_item_xx_2) (listed above)
    - branch 3 *(if faction “brv_wh_aln” ≥ 1)* → [brv_wh_item_xx_3](#d-brv_wh_item_00-brv_wh_item_xx_3) (listed above)
    - branch 4 → [brv_wh_item_29_4](#d-brv_wh_item_29-brv_wh_item_29_4)

    <span id="d-brv_wh_item_29-brv_wh_item_29_4"></span>**`brv_wh_item_29_4`** Warehouse storage spot: “You take the item.” — **effects:** faction “brv_wh_aln” set to 129




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**20 entries.** The game data defines 20 separate characters named Warehouse storage spot. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation.

| Entry | Type | Section |
|---|---|---|
| `brv_wh_item_00` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_00) |
| `brv_wh_item_01` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_01) |
| `brv_wh_item_02` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_02) |
| `brv_wh_item_03` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_03) |
| `brv_wh_item_04` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_04) |
| `brv_wh_item_05` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_05) |
| `brv_wh_item_06` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_06) |
| `brv_wh_item_07` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_07) |
| `brv_wh_item_08` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_08) |
| `brv_wh_item_09` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_09) |
| `brv_wh_item_20` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_20) |
| `brv_wh_item_21` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_21) |
| `brv_wh_item_22` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_22) |
| `brv_wh_item_23` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_23) |
| `brv_wh_item_24` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_24) |
| `brv_wh_item_25` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_25) |
| `brv_wh_item_26` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_26) |
| `brv_wh_item_27` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_27) |
| `brv_wh_item_28` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_28) |
| `brv_wh_item_29` | NPC | [Brimhaven, Brimhaven warehouse](#v-brv_wh_item_29) |

??? info "Technical information: brv_wh_item_00"

    | | |
    |---|---|
    | Entry ID | `brv_wh_item_00` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_item_00` |
    | Loot table | – |
    | Conversation | `brv_wh_item_00` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_item_00",
     "name": "brv_wh_item_00",
     "iconID": "monsters_guynmart:8",
     "moveCost": 99,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_item_00",
     "phraseID": "brv_wh_item_00"
    }
    ```

??? info "Technical information: brv_wh_item_01"

    | | |
    |---|---|
    | Entry ID | `brv_wh_item_01` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_item_01` |
    | Loot table | – |
    | Conversation | `brv_wh_item_01` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_item_01",
     "name": "brv_wh_item_01",
     "iconID": "monsters_guynmart:8",
     "moveCost": 99,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_item_01",
     "phraseID": "brv_wh_item_01"
    }
    ```

??? info "Technical information: brv_wh_item_02"

    | | |
    |---|---|
    | Entry ID | `brv_wh_item_02` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_item_02` |
    | Loot table | – |
    | Conversation | `brv_wh_item_02` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_item_02",
     "name": "brv_wh_item_02",
     "iconID": "monsters_guynmart:8",
     "moveCost": 99,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_item_02",
     "phraseID": "brv_wh_item_02"
    }
    ```

??? info "Technical information: brv_wh_item_03"

    | | |
    |---|---|
    | Entry ID | `brv_wh_item_03` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_item_03` |
    | Loot table | – |
    | Conversation | `brv_wh_item_03` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_item_03",
     "name": "brv_wh_item_03",
     "iconID": "monsters_guynmart:8",
     "moveCost": 99,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_item_03",
     "phraseID": "brv_wh_item_03"
    }
    ```

??? info "Technical information: brv_wh_item_04"

    | | |
    |---|---|
    | Entry ID | `brv_wh_item_04` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_item_04` |
    | Loot table | – |
    | Conversation | `brv_wh_item_04` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_item_04",
     "name": "brv_wh_item_04",
     "iconID": "monsters_guynmart:8",
     "moveCost": 99,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_item_04",
     "phraseID": "brv_wh_item_04"
    }
    ```

??? info "Technical information: brv_wh_item_05"

    | | |
    |---|---|
    | Entry ID | `brv_wh_item_05` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_item_05` |
    | Loot table | – |
    | Conversation | `brv_wh_item_05` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_item_05",
     "name": "brv_wh_item_05",
     "iconID": "monsters_guynmart:8",
     "moveCost": 99,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_item_05",
     "phraseID": "brv_wh_item_05"
    }
    ```

??? info "Technical information: brv_wh_item_06"

    | | |
    |---|---|
    | Entry ID | `brv_wh_item_06` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_item_06` |
    | Loot table | – |
    | Conversation | `brv_wh_item_06` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_item_06",
     "name": "brv_wh_item_06",
     "iconID": "monsters_guynmart:8",
     "moveCost": 99,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_item_06",
     "phraseID": "brv_wh_item_06"
    }
    ```

??? info "Technical information: brv_wh_item_07"

    | | |
    |---|---|
    | Entry ID | `brv_wh_item_07` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_item_07` |
    | Loot table | – |
    | Conversation | `brv_wh_item_07` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_item_07",
     "name": "brv_wh_item_07",
     "iconID": "monsters_guynmart:8",
     "moveCost": 99,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_item_07",
     "phraseID": "brv_wh_item_07"
    }
    ```

??? info "Technical information: brv_wh_item_08"

    | | |
    |---|---|
    | Entry ID | `brv_wh_item_08` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_item_08` |
    | Loot table | – |
    | Conversation | `brv_wh_item_08` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_item_08",
     "name": "brv_wh_item_08",
     "iconID": "monsters_guynmart:8",
     "moveCost": 99,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_item_08",
     "phraseID": "brv_wh_item_08"
    }
    ```

??? info "Technical information: brv_wh_item_09"

    | | |
    |---|---|
    | Entry ID | `brv_wh_item_09` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_item_09` |
    | Loot table | – |
    | Conversation | `brv_wh_item_09` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_item_09",
     "name": "brv_wh_item_09",
     "iconID": "monsters_guynmart:8",
     "moveCost": 99,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_item_09",
     "phraseID": "brv_wh_item_09"
    }
    ```

??? info "Technical information: brv_wh_item_20"

    | | |
    |---|---|
    | Entry ID | `brv_wh_item_20` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_item_20` |
    | Loot table | – |
    | Conversation | `brv_wh_item_20` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_item_20",
     "name": "brv_wh_item_20",
     "iconID": "monsters_guynmart:8",
     "moveCost": 99,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_item_20",
     "phraseID": "brv_wh_item_20"
    }
    ```

??? info "Technical information: brv_wh_item_21"

    | | |
    |---|---|
    | Entry ID | `brv_wh_item_21` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_item_21` |
    | Loot table | – |
    | Conversation | `brv_wh_item_21` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_item_21",
     "name": "brv_wh_item_21",
     "iconID": "monsters_guynmart:8",
     "moveCost": 99,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_item_21",
     "phraseID": "brv_wh_item_21"
    }
    ```

??? info "Technical information: brv_wh_item_22"

    | | |
    |---|---|
    | Entry ID | `brv_wh_item_22` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_item_22` |
    | Loot table | – |
    | Conversation | `brv_wh_item_22` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_item_22",
     "name": "brv_wh_item_22",
     "iconID": "monsters_guynmart:8",
     "moveCost": 99,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_item_22",
     "phraseID": "brv_wh_item_22"
    }
    ```

??? info "Technical information: brv_wh_item_23"

    | | |
    |---|---|
    | Entry ID | `brv_wh_item_23` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_item_23` |
    | Loot table | – |
    | Conversation | `brv_wh_item_23` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_item_23",
     "name": "brv_wh_item_23",
     "iconID": "monsters_guynmart:8",
     "moveCost": 99,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_item_23",
     "phraseID": "brv_wh_item_23"
    }
    ```

??? info "Technical information: brv_wh_item_24"

    | | |
    |---|---|
    | Entry ID | `brv_wh_item_24` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_item_24` |
    | Loot table | – |
    | Conversation | `brv_wh_item_24` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_item_24",
     "name": "brv_wh_item_24",
     "iconID": "monsters_guynmart:8",
     "moveCost": 99,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_item_24",
     "phraseID": "brv_wh_item_24"
    }
    ```

??? info "Technical information: brv_wh_item_25"

    | | |
    |---|---|
    | Entry ID | `brv_wh_item_25` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_item_25` |
    | Loot table | – |
    | Conversation | `brv_wh_item_25` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_item_25",
     "name": "brv_wh_item_25",
     "iconID": "monsters_guynmart:8",
     "moveCost": 99,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_item_25",
     "phraseID": "brv_wh_item_25"
    }
    ```

??? info "Technical information: brv_wh_item_26"

    | | |
    |---|---|
    | Entry ID | `brv_wh_item_26` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_item_26` |
    | Loot table | – |
    | Conversation | `brv_wh_item_26` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_item_26",
     "name": "brv_wh_item_26",
     "iconID": "monsters_guynmart:8",
     "moveCost": 99,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_item_26",
     "phraseID": "brv_wh_item_26"
    }
    ```

??? info "Technical information: brv_wh_item_27"

    | | |
    |---|---|
    | Entry ID | `brv_wh_item_27` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_item_27` |
    | Loot table | – |
    | Conversation | `brv_wh_item_27` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_item_27",
     "name": "brv_wh_item_27",
     "iconID": "monsters_guynmart:8",
     "moveCost": 99,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_item_27",
     "phraseID": "brv_wh_item_27"
    }
    ```

??? info "Technical information: brv_wh_item_28"

    | | |
    |---|---|
    | Entry ID | `brv_wh_item_28` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_item_28` |
    | Loot table | – |
    | Conversation | `brv_wh_item_28` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_item_28",
     "name": "brv_wh_item_28",
     "iconID": "monsters_guynmart:8",
     "moveCost": 99,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_item_28",
     "phraseID": "brv_wh_item_28"
    }
    ```

??? info "Technical information: brv_wh_item_29"

    | | |
    |---|---|
    | Entry ID | `brv_wh_item_29` |
    | Type (wiki) | NPC |
    | Spawn group | `brv_wh_item_29` |
    | Loot table | – |
    | Conversation | `brv_wh_item_29` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_wh_item_29",
     "name": "brv_wh_item_29",
     "iconID": "monsters_guynmart:8",
     "moveCost": 99,
     "monsterClass": "humanoid",
     "spawnGroup": "brv_wh_item_29",
     "phraseID": "brv_wh_item_29"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_wh_item_00.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_wh_item_00.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_wh_item_00.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_wh_item_00.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
