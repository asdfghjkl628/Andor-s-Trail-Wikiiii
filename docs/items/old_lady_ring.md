---
description: "Garnet whisper ring is a rare ring in Andor's Trail (Attack damage 0, Max HP +10, Attack chance +10, Block chance +5). How to get it: shops, containers."
---

# ![](../assets/icons/items/items_tometik3_28.png){ .sprite } Garnet whisper ring

*Rare ring.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_tometik3_28.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `old_lady_ring` |
| **Category** | Ring |
| **Slot** | leftring |
| **Rarity** | Rare |
| **Base value** | 0 gold |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 0 |
| Max HP | +10 |
| Attack chance | +10 |
| Block chance | +5 |
| Damage resistance | +1 |
| Grants | Minor weapon feebleness (magnitude 1) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Prowling Arantxa](../monsters/sullengard_arantxa.md) (Sullengard)

### Found in containers

- [thieves_vault](../maps/thieves_vault.md#container-9) (container 10, 100%), Blackwater Mountain


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=old_lady_ring.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=old_lady_ring.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=old_lady_ring.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=old_lady_ring.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `old_lady_ring` |
    | Category ID | `ring` |
    | Icon | `items_tometik3:28` |
    | Defined in | `res/raw/itemlist_sullengard.json` |
    | Loot tables containing it | `sullengard_arantxa_dl`, `thieves_vault_jewelery` |

    Raw data:

    ```json
    {
     "id": "old_lady_ring",
     "iconID": "items_tometik3:28",
     "name": "Garnet whisper ring",
     "displaytype": "rare",
     "category": "ring",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 0,
       "max": 0
      },
      "increaseMaxHP": 10,
      "increaseAttackChance": 10,
      "increaseBlockChance": 5,
      "increaseDamageResistance": 1,
      "addedConditions": [
       {
        "condition": "feebleness_minor",
        "magnitude": 1
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
