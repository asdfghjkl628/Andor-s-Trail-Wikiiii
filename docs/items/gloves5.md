# ![](../assets/icons/items/items_omi2_1.png){ .sprite } Iced leather gloves

*Ordinary gloves, leather.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_omi2_1.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `gloves5` |
| **Category** | Gloves, leather |
| **Slot** | hand |
| **Rarity** | Ordinary |
| **Base value** | 524 gold |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

> You wonder how to lift any weapon while wearing them.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | -3 to -2 |
| Max HP | -2 |
| Use item cost | +2 |
| Attack chance | +1 |
| Block chance | +8 |
| setNonWeaponDamageModifier | +100 |

### On hit

| Stat | Value |
|---|---|
| On target | Icy wounds (magnitude 1, 2 rounds, 15% chance) |

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

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=gloves5.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=gloves5.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=gloves5.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=gloves5.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `gloves5` |
    | Category ID | `hnd_lthr` |
    | Icon | `items_omi2:1` |
    | Defined in | `res/raw/itemlist_omi2.json` |
    | Loot tables containing it | `ortholion_subdued` |

    Raw data:

    ```json
    {
     "id": "gloves5",
     "iconID": "items_omi2:1",
     "name": "Iced leather gloves",
     "displaytype": "ordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 524,
     "category": "hnd_lthr",
     "description": "You wonder how to lift any weapon while wearing them.",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": -3,
       "max": -2
      },
      "increaseMaxHP": -2,
      "increaseUseItemCost": 2,
      "increaseAttackChance": 1,
      "increaseBlockChance": 8,
      "setNonWeaponDamageModifier": 100
     },
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "frozen2",
        "magnitude": 1,
        "duration": 2,
        "chance": "15"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
