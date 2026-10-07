---
description: "Ring of far lesser Shadow is a legendary ring in Andor's Trail (Attack damage 5 to 8, Attack chance +26, Critical skill +7, Block chance +6). How to get it: quests and dialogue. The glow of the Shadow guides my path. It follows me wherever I go, and aids the dangers against me that others might…"
---

# ![](../assets/icons/items/items_jewelry_2.png){ .sprite } Ring of far lesser Shadow

*Legendary ring.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_jewelry_2.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `ring_shadow1` |
| **Category** | Ring |
| **Slot** | leftring |
| **Rarity** | Legendary |
| **Base value** | 0 gold |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

> The glow of the Shadow guides my path. It follows me wherever I go, and aids the dangers against me that others might not see. I am Shadow, and Shadow is in me.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 5 to 8 |
| Attack chance | +26 |
| Critical skill | +7 |
| Block chance | +6 |
| Grants | [Shadow Degeneration](../conditions/regenNeg.md) (magnitude 1) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Quest & dialogue rewards

- From [Rorthron](../monsters/guynmart_wizard.md) ([guynmart_tower_4](../maps/guynmart_tower_4.md)) during [Ringmaker (hidden flag)](../quests/guynmart_quest_wizard.md#stage-1) (100%)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ring_shadow1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ring_shadow1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ring_shadow1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ring_shadow1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `ring_shadow1` |
    | Category ID | `ring` |
    | Icon | `items_jewelry:2` |
    | Defined in | `res/raw/itemlist_guynmart.json` |
    | Loot tables containing it | `guynmart_drp_wizard` |

    Raw data:

    ```json
    {
     "id": "ring_shadow1",
     "iconID": "items_jewelry:2",
     "name": "Ring of far lesser Shadow",
     "displaytype": "legendary",
     "hasManualPrice": 1,
     "baseMarketCost": 0,
     "category": "ring",
     "description": "The glow of the Shadow guides my path. It follows me wherever I go, and aids the dangers against me that others might not see. I am Shadow, and Shadow is in me.",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 5,
       "max": 8
      },
      "increaseAttackChance": 26,
      "increaseCriticalSkill": 7,
      "increaseBlockChance": 6,
      "addedConditions": [
       {
        "condition": "regenNeg",
        "magnitude": 1
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
