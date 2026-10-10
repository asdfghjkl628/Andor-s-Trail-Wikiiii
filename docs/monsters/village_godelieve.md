---
description: "Godelieve is a non-player character (NPC) in Andor's Trail, found in Wexlow Village, Gamjee well jail cells."
---

# ![](../assets/icons/monsters/monsters_ld1_144.png){ .sprite } Godelieve

**Where to find Godelieve:** [Wexlow Village, Wexlow village north-west house](#v-village_godelieve), [Gamjee well jail cells](#v-troll_hollow_godelieve), [Wexlow Village, Wexlow village](#v-village_godelieve_hidden)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld1_144.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Wexlow Village, Gamjee well jail cells |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

## Wexlow Village, Wexlow village north-west house { #v-village_godelieve }

**Where:** Wexlow Village: [Wexlow village north-west house](../maps/wexlow_village_nw_house.md#pin-npc-village_godelieve)

### Quests

- [Echoes of enchantment](../quests/echoes_of_enchantment.md): stage 14
- [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md): stage 9

### Dialogue simulator

Talk to Godelieve as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/village_godelieve_selector.json" data-npc="Godelieve" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-village_godelieve-village_godelieve_selector"></span>**`village_godelieve_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 14 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-14))* → [village_godelieve_1](#d-village_godelieve-village_godelieve_1)
    - Next → [village_godelieve_generic](#d-village_godelieve-village_godelieve_generic)

    <span id="d-village_godelieve-village_godelieve_1"></span>**`village_godelieve_1`** Godelieve: “Oh, our hero returns to us.”

    - “I'm just happy to see you guys safe.” → [village_godelieve_2](#d-village_godelieve-village_godelieve_2)

    <span id="d-village_godelieve-village_godelieve_generic"></span>**`village_godelieve_generic`** Godelieve: “It's very nice to see you again.”

    - “Would it be OK with you if I slept here? I'm pretty tired.” *(if reached stage 12 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-12))* → [village_godelieve_bed](#d-village_godelieve-village_godelieve_bed)

    <span id="d-village_godelieve-village_godelieve_2"></span>**`village_godelieve_2`** Godelieve: “I'm just happy to curl up with Godwin in our own bed tonight.” — **effects:** sets stage 14 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-14)


    <span id="d-village_godelieve-village_godelieve_bed"></span>**`village_godelieve_bed`** Godelieve: “Of course. Just use the mat over there in the corner.” — **effects:** sets stage 9 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-9)




### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Gamjee well jail cells { #v-troll_hollow_godelieve }

**Where:** [Gamjee well jail cells](../maps/gamjee_well_jail_cells.md)


### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Wexlow Village, Wexlow village { #v-village_godelieve_hidden }

**Where:** Wexlow Village: [Wexlow village](../maps/wexlow_village.md)


### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**3 entries.** The game data defines 3 separate characters named Godelieve. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location.

| Entry | Type | Section |
|---|---|---|
| `village_godelieve` | NPC | [Wexlow Village, Wexlow village north-west house](#v-village_godelieve) |
| `troll_hollow_godelieve` | Scenery | [Gamjee well jail cells](#v-troll_hollow_godelieve) |
| `village_godelieve_hidden` | Scenery | [Wexlow Village, Wexlow village](#v-village_godelieve_hidden) |

- `troll_hollow_godelieve` has no conversation and no combat statistics. Other conversations use it as their speaker (the `switchToNPC` field), which is how its name and picture appear in dialogue. The game data also places it on [Gamjee well jail cells](../maps/gamjee_well_jail_cells.md).
- `village_godelieve_hidden` has no conversation and no combat statistics. Other conversations use it as their speaker (the `switchToNPC` field), which is how its name and picture appear in dialogue. The game data also places it on Wexlow Village: [Wexlow village](../maps/wexlow_village.md).

??? info "Technical information: village_godelieve"

    | | |
    |---|---|
    | Entry ID | `village_godelieve` |
    | Type (wiki) | NPC |
    | Spawn group | `village_godelieve` |
    | Loot table | – |
    | Conversation | `village_godelieve_selector` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_ld1:144` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "village_godelieve",
     "name": "Godelieve",
     "iconID": "monsters_ld1:144",
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "phraseID": "village_godelieve_selector"
    }
    ```

??? info "Technical information: troll_hollow_godelieve"

    | | |
    |---|---|
    | Entry ID | `troll_hollow_godelieve` |
    | Type (wiki) | Scenery |
    | Spawn group | `troll_hollow_godelieve` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_ld1:144` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "troll_hollow_godelieve",
     "name": "Godelieve",
     "iconID": "monsters_ld1:144",
     "moveCost": 3,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none"
    }
    ```

??? info "Technical information: village_godelieve_hidden"

    | | |
    |---|---|
    | Entry ID | `village_godelieve_hidden` |
    | Type (wiki) | Scenery |
    | Spawn group | `village_godelieve_hidden` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_ld1:144` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "village_godelieve_hidden",
     "name": "Godelieve",
     "iconID": "monsters_ld1:144",
     "moveCost": 5,
     "monsterClass": "humanoid",
     "movementAggressionType": "none"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_godelieve.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_godelieve.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_godelieve.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_godelieve.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
