---
description: "Iced leather boots is a ordinary footwear, leather in Andor's Trail (Attack damage -1 to 0, Max HP -3, Move cost 0, Use item cost 0). How to get it: monster drops. These leather boots bright like if they were metallic."
---

# ![](../assets/icons/items/items_omi2_7.png){ .sprite } Iced leather boots

*Ordinary footwear, leather.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_omi2_7.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `boots7` |
| **Category** | Footwear, leather |
| **Slot** | feet |
| **Proficiency** | [Light armor proficiency](../skills/armorProficiencyLight.md) |
| **Rarity** | Ordinary |
| **Base value** | 788 gold |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

> These leather boots bright like if they were metallic.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | -1 to 0 |
| Max HP | -3 |
| Move cost | 0 |
| Use item cost | 0 |
| Re-equip cost | 0 |
| Attack cost | 0 |
| Attack chance | -9 |
| Block chance | +6 |
| Damage resistance | 0 |
| Grants | Minor freeze (magnitude 1) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Subdued Feygard mountain scout](../monsters/ortholion_subdued.md) | 100% | 1 | Blackwater Mountain |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=boots7.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=boots7.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=boots7.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=boots7.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `boots7` |
    | Category ID | `feet_lthr` |
    | Icon | `items_omi2:7` |
    | Defined in | `res/raw/itemlist_omi2.json` |
    | Loot tables containing it | `ortholion_subdued` |

    Raw data:

    ```json
    {
     "id": "boots7",
     "iconID": "items_omi2:7",
     "name": "Iced leather boots",
     "displaytype": "ordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 788,
     "category": "feet_lthr",
     "description": "These leather boots bright like if they were metallic.",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": -1,
       "max": 0
      },
      "increaseMaxHP": -3,
      "increaseMoveCost": 0,
      "increaseUseItemCost": 0,
      "increaseReequipCost": 0,
      "increaseAttackCost": 0,
      "increaseAttackChance": -9,
      "increaseBlockChance": 6,
      "increaseDamageResistance": 0,
      "addedConditions": [
       {
        "condition": "frozen1",
        "magnitude": 1
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
