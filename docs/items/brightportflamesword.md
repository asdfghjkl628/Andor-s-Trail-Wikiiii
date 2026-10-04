# ![](../assets/icons/items/items_weapons_41.png){ .sprite } Flaming greatsword

*Extraordinary two-handed sword.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_41.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `brightportflamesword` |
| **Category** | Two-handed sword |
| **Slot** | weapon |
| **Hands** | Two-handed |
| **Proficiency** | Two-handed sword |
| **Rarity** | Extraordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

> Sizzling the flesh of evil beasts, and your hands alike.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 6 to 12 |
| Attack cost | +6 |
| Attack chance | +20 |
| Block chance | +5 |
| Critical multiplier | 0.0 |
| setNonWeaponDamageModifier | +140 |

### On hit

| Stat | Value |
|---|---|
| On self | Searing burn (magnitude 1, 2 rounds, 40% chance) |
| On target | Searing burn (magnitude 2, 2 rounds, 30% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Quest & dialogue rewards

- From [Fiamma](../monsters/brightportsmith.md) ([brightport_weapon](../maps/brightport_weapon.md)) during [Too hot to handle](../quests/brightport_fiamma.md#stage-50) (1×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brightportflamesword.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brightportflamesword.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brightportflamesword.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brightportflamesword.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `brightportflamesword` |
    | Category ID | `2hsword` |
    | Icon | `items_weapons:41` |
    | Defined in | `res/raw/itemlist_brightport.json` |
    | Loot tables containing it | – |

    Raw data:

    ```json
    {
     "id": "brightportflamesword",
     "iconID": "items_weapons:41",
     "name": "Flaming greatsword",
     "displaytype": "extraordinary",
     "category": "2hsword",
     "description": "Sizzling the flesh of evil beasts, and your hands alike.",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 6,
       "max": 12
      },
      "increaseAttackCost": 6,
      "increaseAttackChance": 20,
      "increaseBlockChance": 5,
      "setCriticalMultiplier": 0.0,
      "setNonWeaponDamageModifier": 140
     },
     "hitEffect": {
      "conditionsSource": [
       {
        "condition": "brightportflame",
        "magnitude": 1,
        "duration": 2,
        "chance": "40"
       }
      ],
      "conditionsTarget": [
       {
        "condition": "brightportflame",
        "magnitude": 2,
        "duration": 2,
        "chance": "30"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
