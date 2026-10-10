---
description: "Salamander gloves is a rare gloves, leather in Andor's Trail (Block chance +3, Damage resistance +1, Grants immunity to Searing burn). How to get it: quests and dialogue. Fire-proof gloves crafted out of arulir skin. somehow named after a lizard instead."
---

# ![](../assets/icons/items/items_omi2_5.png){ .sprite } Salamander gloves

*Rare gloves, leather.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/items/items_omi2_5.png" alt=""></p>

| | |
|---|---|
| **Item ID** | `brightport_glove` |
| **Category** | Gloves, leather |
| **Slot** | hand |
| **Proficiency** | [Light armor proficiency](../skills/armorProficiencyLight.md) |
| **Rarity** | Rare |
| **Base value** | 455 gold |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

> Fire-proof gloves crafted out of arulir skin. somehow named after a lizard instead.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Block chance | +3 |
| Damage resistance | +1 |
| Grants | immunity to [Searing burn](../conditions/brightportflame.md) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Quest & dialogue rewards

- From [Fiamma](../monsters/brightportsmith.md) ([Brightport weapon](../maps/brightport_weapon.md)) during [Too hot to handle](../quests/brightport_fiamma.md#stage-50) (1×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brightport_glove.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brightport_glove.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brightport_glove.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brightport_glove.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `brightport_glove` |
    | Category ID | `hnd_lthr` |
    | Icon | `items_omi2:5` |
    | Defined in | `res/raw/itemlist_brightport.json` |
    | Loot tables containing it | – |

    Raw data:

    ```json
    {
     "id": "brightport_glove",
     "iconID": "items_omi2:5",
     "name": "Salamander gloves",
     "displaytype": "rare",
     "hasManualPrice": 1,
     "baseMarketCost": 455,
     "category": "hnd_lthr",
     "description": "Fire-proof gloves crafted out of arulir skin. somehow named after a lizard instead.",
     "equipEffect": {
      "increaseBlockChance": 3,
      "increaseDamageResistance": 1,
      "addedConditions": [
       {
        "condition": "brightportflame",
        "magnitude": -99
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
