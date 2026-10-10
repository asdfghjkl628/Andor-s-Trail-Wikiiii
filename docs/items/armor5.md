---
description: "Iced leather armor is a extraordinary armor, leather in Andor's Trail (Attack damage -2 to -1, Max HP -5, Max AP 0, Move cost +2). How to get it: monster drops. This armor has a permanent layer of snow and ice which somehow never melts."
---

# ![](../assets/icons/items/items_feygard1_6.png){ .sprite } Iced leather armor

*Extraordinary armor, leather.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/items/items_feygard1_6.png" alt=""></p>

| | |
|---|---|
| **Item ID** | `armor5` |
| **Category** | Armor, leather |
| **Slot** | body |
| **Proficiency** | [Light armor proficiency](../skills/armorProficiencyLight.md) |
| **Rarity** | Extraordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

> This armor has a permanent layer of snow and ice which somehow never melts.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | -2 to -1 |
| Max HP | -5 |
| Max AP | 0 |
| Move cost | +2 |
| Use item cost | +1 |
| Re-equip cost | +2 |
| Attack chance | -5 |
| Critical skill | -10 |
| Block chance | +20 |
| Damage resistance | +2 |
| Grants | immunity to [Ablaze](../conditions/fire.md) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Subdued Feygard mountain scout](../monsters/ortholion_subdued.md) | 20% | 1 | Blackwater Mountain |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=armor5.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=armor5.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=armor5.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=armor5.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `armor5` |
    | Category ID | `bdy_lthr` |
    | Icon | `items_feygard1:6` |
    | Defined in | `res/raw/itemlist_omi2.json` |
    | Loot tables containing it | `ortholion_subdued` |

    Raw data:

    ```json
    {
     "id": "armor5",
     "iconID": "items_feygard1:6",
     "name": "Iced leather armor",
     "displaytype": "extraordinary",
     "category": "bdy_lthr",
     "description": "This armor has a permanent layer of snow and ice which somehow never melts.",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": -2,
       "max": -1
      },
      "increaseMaxHP": -5,
      "increaseMaxAP": 0,
      "increaseMoveCost": 2,
      "increaseUseItemCost": 1,
      "increaseReequipCost": 2,
      "increaseAttackChance": -5,
      "increaseCriticalSkill": -10,
      "increaseBlockChance": 20,
      "increaseDamageResistance": 2,
      "addedConditions": [
       {
        "condition": "fire",
        "magnitude": -99
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
