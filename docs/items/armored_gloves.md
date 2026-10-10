---
description: "Armored gloves is a ordinary gloves, metal (heavy) in Andor's Trail (Use item cost +1, Attack cost +1, Block chance +10). How to get it: shops."
---

# ![](../assets/icons/items/items_newb_5.png){ .sprite } Armored gloves

*Ordinary gloves, metal (heavy).*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/items/items_newb_5.png" alt=""></p>

| | |
|---|---|
| **Item ID** | `armored_gloves` |
| **Category** | Gloves, metal (heavy) |
| **Slot** | hand |
| **Proficiency** | [Heavy armor proficiency](../skills/armorProficiencyHeavy.md) |
| **Rarity** | Ordinary |
| **Base value** | 1,868 gold |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Use item cost | +1 |
| Attack cost | +1 |
| Block chance | +10 |

### When hit

| Stat | Value |
|---|---|
| On self | [Minor increased defense](../conditions/minor_increased_defense.md) (magnitude 1, 2 rounds, 3% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Odirath](../monsters/stoutford_armorer.md) (Stoutford)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=armored_gloves.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=armored_gloves.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=armored_gloves.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=armored_gloves.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `armored_gloves` |
    | Category ID | `hnd_mtl_hv` |
    | Icon | `items_newb:5` |
    | Defined in | `res/raw/itemlist_feygard_1.json` |
    | Loot tables containing it | `shop_odirath` |

    Raw data:

    ```json
    {
     "id": "armored_gloves",
     "iconID": "items_newb:5",
     "name": "Armored gloves",
     "displaytype": "ordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 1868,
     "category": "hnd_mtl_hv",
     "equipEffect": {
      "increaseUseItemCost": 1,
      "increaseAttackCost": 1,
      "increaseBlockChance": 10
     },
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "minor_increased_defense",
        "magnitude": 1,
        "duration": 2,
        "chance": "3"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
