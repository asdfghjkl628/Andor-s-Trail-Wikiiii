---
description: "Blackwater misery is a harmful blood condition in Andor's Trail: attack chance −50, critical skill −50, attack cost +1. Caused by: items."
---

# ![](../assets/icons/conditions/actorconditions_1_58.png){ .sprite } Blackwater misery

*Harmful blood condition.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/conditions/actorconditions_1_58.png" alt=""></p>

| | |
|---|---|
| **Type** | Harmful |
| **Category** | [Blood](index.md#categories-and-resistance) |
| **Affects** | You |
| **Stacking** | No |
| **Resisted by** | [Pure Blood](../skills/resistanceBlood.md) |
| **Condition ID** | `blackwater_misery` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| Attack chance | −50 |
| Critical skill | −50 |
| Attack cost (AP) | +1 |

Values are per magnitude level. A round is one combat turn, or 6 seconds outside combat.

**Stacking:** No (only a stronger or longer application replaces it).


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Blackwater boots](../items/bwm_boots.md) | While equipped | 1 | While equipped | – |
| [Blackwater dagger](../items/bwm_dagger.md) | While equipped | 1 | While equipped | – |
| [Blackwater gloves](../items/bwm_gloves.md) | While equipped | 1 | While equipped | – |
| [Blackwater iron longsword](../items/bwm_longsword.md) | While equipped | 1 | While equipped | – |
| [Blackwater iron sword](../items/bwm_ironsword.md) | While equipped | 1 | While equipped | – |
| [Blackwater leather armor](../items/bwm_leather_armour.md) | While equipped | 1 | While equipped | – |
| [Blackwater leather cap](../items/bwm_leather_cap.md) | While equipped | 1 | While equipped | – |
| [Blackwater poisoned dagger](../items/bwm_dagger_venom.md) | While equipped | 1 | While equipped | – |
| [Blackwater ring of combat](../items/bwm_combat_ring.md) | While equipped | 1 | While equipped | – |
| [Blackwater rusted pickaxe](../items/bwm_pick.md) | While equipped | 1 | While equipped | – |
| [Blackwater shield](../items/bwm_shield.md) | While equipped | 1 | While equipped | – |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Duration and rest:** permanent ones (equipment, story events) stay through rest.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=blackwater_misery.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=blackwater_misery.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=blackwater_misery.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `blackwater_misery` |
    | Category (internal) | `blood` |
    | Icon | `actorconditions_1:58` |
    | Defined in | `res/raw/actorconditions_v069_bwm.json` |

    Raw data:

    ```json
    {
     "id": "blackwater_misery",
     "iconID": "actorconditions_1:58",
     "name": "Blackwater misery",
     "category": "blood",
     "abilityEffect": {
      "increaseAttackChance": -50,
      "increaseAttackCost": 1,
      "increaseCriticalSkill": -50
     }
    }
    ```


<small>Data from v0.8.18</small>
