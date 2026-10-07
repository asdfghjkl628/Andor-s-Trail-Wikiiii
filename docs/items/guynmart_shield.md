---
description: "Guynmart shield is a ordinary shield, metal (light) in Andor's Trail (Attack cost 0, Attack chance -6, Block chance +10, Damage resistance +1). How to get it: quests and dialogue."
---

# ![](../assets/icons/items/items_armours_12.png){ .sprite } Guynmart shield

*Ordinary shield, metal (light).*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_armours_12.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `guynmart_shield` |
| **Category** | Shield, metal (light) |
| **Slot** | shield |
| **Proficiency** | [Shield proficiency](../skills/armorProficiencyShield.md) |
| **Rarity** | Ordinary |
| **Base value** | 1,000 gold |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack cost | 0 |
| Attack chance | -6 |
| Block chance | +10 |
| Damage resistance | +1 |

### When hit

| Stat | Value |
|---|---|
| On self | [Bark skin](../conditions/barkskin.md) (magnitude 2, 2 rounds, 20% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Quest & dialogue rewards

- From [Armor](../monsters/guynmart_reward3.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) during [guynmart nondisplay (hidden flag)](../quests/guynmart_nondisplay.md#stage-32) (1×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |
| [v0.8.8](../versions/0.8.8.md) | Base value (gold): 0 → 1000 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=guynmart_shield.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=guynmart_shield.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=guynmart_shield.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=guynmart_shield.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `guynmart_shield` |
    | Category ID | `shld_mtl_li` |
    | Icon | `items_armours:12` |
    | Defined in | `res/raw/itemlist_guynmart.json` |
    | Loot tables containing it | – |

    Raw data:

    ```json
    {
     "id": "guynmart_shield",
     "iconID": "items_armours:12",
     "name": "Guynmart shield",
     "hasManualPrice": 1,
     "baseMarketCost": 1000,
     "category": "shld_mtl_li",
     "equipEffect": {
      "increaseAttackCost": 0,
      "increaseAttackChance": -6,
      "increaseBlockChance": 10,
      "increaseDamageResistance": 1
     },
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "barkskin",
        "magnitude": 2,
        "duration": 2,
        "chance": "20"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
