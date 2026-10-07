---
description: "Shield of the undead is a extraordinary shield, metal (light) in Andor's Trail (Attack chance -5, Block chance +12, Damage resistance +1, Grants Curse of the Undead (magnitude 1)). How to get it: monster drops. This shield calls for death, and yours will do."
---

# ![](../assets/icons/items/items_armours_4.png){ .sprite } Shield of the undead

*Extraordinary shield, metal (light).*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_armours_4.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `shield_of_undead` |
| **Category** | Shield, metal (light) |
| **Slot** | shield |
| **Proficiency** | [Shield proficiency](../skills/armorProficiencyShield.md) |
| **Rarity** | Extraordinary |
| **Base value** | 11,155 gold |
| **Introduced** | [v0.8.3](../versions/0.8.3.md) |

</div>

> This shield calls for death, and yours will do.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack chance | -5 |
| Block chance | +12 |
| Damage resistance | +1 |
| Grants | Curse of the Undead (magnitude 1) |

### On kill

| Stat | Value |
|---|---|
| Heal HP | 3 to 5 |

### When hit

| Stat | Value |
|---|---|
| increaseAttackerCurrentHP | -3 to -1 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Benzimos](../monsters/haunted_benzimos.md) | 100% | 1 | haunted_house_basement |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.3](../versions/0.8.3.md) | Added |
| [v0.8.4](../versions/0.8.4.md) | baseMarketCost added (11155); hasManualPrice added (1) |
| [v0.8.5](../versions/0.8.5.md) | category: shld_wd_li → shld_mtl_li |
| [v0.8.12.1](../versions/0.8.12.1.md) | hitReceivedEffect: {"increaseAttackerCurrentHP": {"max": -… → {"increaseAttackerCurrentHP": {"max": -… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=shield_of_undead.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=shield_of_undead.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=shield_of_undead.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=shield_of_undead.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `shield_of_undead` |
    | Category ID | `shld_mtl_li` |
    | Icon | `items_armours:4` |
    | Defined in | `res/raw/itemlist_haunted_forest.json` |
    | Loot tables containing it | `benzimos_dl` |

    Raw data:

    ```json
    {
     "id": "shield_of_undead",
     "iconID": "items_armours:4",
     "name": "Shield of the undead",
     "displaytype": "extraordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 11155,
     "category": "shld_mtl_li",
     "description": "This shield calls for death, and yours will do.",
     "equipEffect": {
      "increaseAttackChance": -5,
      "increaseBlockChance": 12,
      "increaseDamageResistance": 1,
      "addedConditions": [
       {
        "condition": "curse_undead",
        "magnitude": 1
       }
      ]
     },
     "hitReceivedEffect": {
      "increaseAttackerCurrentHP": {
       "min": -3,
       "max": -1
      }
     },
     "killEffect": {
      "increaseCurrentHP": {
       "min": 3,
       "max": 5
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
