---
description: "Iced broken wooden buckler is a ordinary buckler in Andor's Trail (Attack damage -1, Max HP -2, Max AP 0, Attack chance -6). How to get it: monster drops, containers. Quite resistant despite its apparent frailness and its state. Maybe it's worth fixing."
---

# ![](../assets/icons/items/items_feygard1_7.png){ .sprite } Iced broken wooden buckler

*Ordinary buckler.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_feygard1_7.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `shield8` |
| **Category** | Buckler |
| **Slot** | shield |
| **Proficiency** | [Shield proficiency](../skills/armorProficiencyShield.md) |
| **Rarity** | Ordinary |
| **Base value** | 441 gold |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

> Quite resistant despite its apparent frailness and its state. Maybe it's worth fixing.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | -1 |
| Max HP | -2 |
| Max AP | 0 |
| Attack chance | -6 |
| Critical skill | 0 |
| Block chance | +8 |
| Damage resistance | 0 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Subdued Feygard mountain scout](../monsters/ortholion_subdued.md) | 100% | 1 | Blackwater Mountain |

### Found in containers

- [Elm mine 5](../maps/elm_mine5.md#container-0) (container 1, 1.33333%)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=shield8.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=shield8.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=shield8.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=shield8.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `shield8` |
    | Category ID | `buckler` |
    | Icon | `items_feygard1:7` |
    | Defined in | `res/raw/itemlist_omi2.json` |
    | Loot tables containing it | `ortholion_subdued`, `elm_drop1` |

    Raw data:

    ```json
    {
     "id": "shield8",
     "iconID": "items_feygard1:7",
     "name": "Iced broken wooden buckler",
     "displaytype": "ordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 441,
     "category": "buckler",
     "description": "Quite resistant despite its apparent frailness and its state. Maybe it's worth fixing.",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": -1,
       "max": -1
      },
      "increaseMaxHP": -2,
      "increaseMaxAP": 0,
      "increaseAttackChance": -6,
      "increaseCriticalSkill": 0,
      "increaseBlockChance": 8,
      "increaseDamageResistance": 0
     }
    }
    ```


<small>Data from v0.8.18</small>
