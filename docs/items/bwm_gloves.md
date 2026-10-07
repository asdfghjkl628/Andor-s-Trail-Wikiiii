---
description: "Blackwater gloves is a rare gloves, leather in Andor's Trail (Max HP +2, Attack chance -5, Block chance +14, Grants Blackwater misery (magnitude 1)). How to get it: shops."
---

# ![](../assets/icons/items/items_armours_38.png){ .sprite } Blackwater gloves

*Rare gloves, leather.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_armours_38.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `bwm_gloves` |
| **Category** | Gloves, leather |
| **Slot** | hand |
| **Proficiency** | [Light armor proficiency](../skills/armorProficiencyLight.md) |
| **Rarity** | Rare |
| **Base value** | 0 gold |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Max HP | +2 |
| Attack chance | -5 |
| Block chance | +14 |
| Grants | Blackwater misery (magnitude 1) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Teksin](../monsters/teksin.md) (waytolake11)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bwm_gloves.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bwm_gloves.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bwm_gloves.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bwm_gloves.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `bwm_gloves` |
    | Category ID | `hnd_lthr` |
    | Icon | `items_armours:38` |
    | Defined in | `res/raw/itemlist_trader_teksin.json` |
    | Loot tables containing it | `teksin` |

    Raw data:

    ```json
    {
     "id": "bwm_gloves",
     "iconID": "items_armours:38",
     "name": "Blackwater gloves",
     "displaytype": "rare",
     "category": "hnd_lthr",
     "equipEffect": {
      "increaseMaxHP": 2,
      "increaseAttackChance": -5,
      "increaseBlockChance": 14,
      "addedConditions": [
       {
        "condition": "blackwater_misery",
        "magnitude": 1
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
