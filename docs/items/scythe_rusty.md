# ![](../assets/icons/items/items_weapons_3_2.png){ .sprite } Rusty scythe

*Ordinary pole weapon.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_3_2.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `scythe_rusty` |
| **Category** | Pole weapon |
| **Slot** | weapon |
| **Hands** | Two-handed |
| **Proficiency** | Pole weapon |
| **Rarity** | Ordinary |
| **Base value** | 464 gold |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

> This looks more suited to farming than fighting

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 1 to 3 |
| Attack cost | +6 |
| Attack chance | +8 |
| Block chance | +1 |
| setNonWeaponDamageModifier | +135 |

### On hit

| Stat | Value |
|---|---|
| On target | Blood poisoning (magnitude 1, 3 rounds, 7% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Cornith](../monsters/stoutford_smith.md) (Stoutford)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |
| [v0.7.8](../versions/0.7.8.md) | category: scythe → pole |
| [v0.7.10](../versions/0.7.10.md) | equipEffect: {"increaseAttackChance": 8, "increaseAt… → {"increaseAttackChance": 8, "increaseAt… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=scythe_rusty.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=scythe_rusty.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=scythe_rusty.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=scythe_rusty.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `scythe_rusty` |
    | Category ID | `pole` |
    | Icon | `items_weapons_3:2` |
    | Defined in | `res/raw/itemlist_stoutford_combined.json` |
    | Loot tables containing it | `shop_cornith` |

    Raw data:

    ```json
    {
     "id": "scythe_rusty",
     "iconID": "items_weapons_3:2",
     "name": "Rusty scythe",
     "displaytype": "ordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 464,
     "category": "pole",
     "description": "This looks more suited to farming than fighting",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 1,
       "max": 3
      },
      "increaseAttackCost": 6,
      "increaseAttackChance": 8,
      "increaseBlockChance": 1,
      "setNonWeaponDamageModifier": 135
     },
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "poison_blood",
        "magnitude": 1,
        "duration": 3,
        "chance": "7"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
