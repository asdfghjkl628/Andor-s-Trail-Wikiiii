---
description: "Elm steel mace is a ordinary mace in Andor's Trail (Attack damage 6 to 7, Max HP 0, Max AP 0, Attack cost +6). How to get it: containers. Elm steel is usually too coarse to make sharp weapons with it, but blunt ones are robust and durable."
---

# ![](../assets/icons/items/items_omi2_24.png){ .sprite } Elm steel mace

*Ordinary mace.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_omi2_24.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `mace2` |
| **Category** | Mace |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [Blunt weapon proficiency](../skills/weaponProficiencyBlunt.md) |
| **Rarity** | Ordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

> Elm steel is usually too coarse to make sharp weapons with it, but blunt ones are robust and durable.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 6 to 7 |
| Max HP | 0 |
| Max AP | 0 |
| Attack cost | +6 |
| Attack chance | +16 |
| Critical skill | -5 |
| Block chance | +1 |
| Critical multiplier | 0.0 |
| setNonWeaponDamageModifier | +161 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Found in containers

- [elm_2f_2](../maps/elm_2f_2.md#container-1) (container 2, 100%)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=mace2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=mace2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=mace2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=mace2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `mace2` |
    | Category ID | `mace` |
    | Icon | `items_omi2:24` |
    | Defined in | `res/raw/itemlist_omi2.json` |
    | Loot tables containing it | `elm2f2_chest` |

    Raw data:

    ```json
    {
     "id": "mace2",
     "iconID": "items_omi2:24",
     "name": "Elm steel mace",
     "displaytype": "ordinary",
     "category": "mace",
     "description": "Elm steel is usually too coarse to make sharp weapons with it, but blunt ones are robust and durable.",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 6,
       "max": 7
      },
      "increaseMaxHP": 0,
      "increaseMaxAP": 0,
      "increaseAttackCost": 6,
      "increaseAttackChance": 16,
      "increaseCriticalSkill": -5,
      "increaseBlockChance": 1,
      "setCriticalMultiplier": 0.0,
      "setNonWeaponDamageModifier": 161
     }
    }
    ```


<small>Data from v0.8.18</small>
