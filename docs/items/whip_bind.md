# ![](../assets/icons/items/items_weapons_3_57.png){ .sprite } Whip of binding

*Extraordinary whip.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_3_57.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `whip_bind` |
| **Category** | Whip |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Rarity** | Extraordinary |
| **Base value** | 6,700 gold |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

> When you hold it, it almost feels like it's moving on its own, as though it were alive.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 2 to 5 |
| Attack cost | +5 |
| Attack chance | +10 |
| Critical skill | +5 |
| Block chance | +8 |
| Critical multiplier | 1.5 |
| setNonWeaponDamageModifier | +127 |

### On hit

| Stat | Value |
|---|---|
| On target | Entanglement (magnitude 1, 2 rounds, 25% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Revenant](../monsters/revenant.md) | 0.1% | 1 | waterwayacave2, waterwayacave3, waterwayacave4 |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=whip_bind.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=whip_bind.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=whip_bind.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=whip_bind.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `whip_bind` |
    | Category ID | `whip` |
    | Icon | `items_weapons_3:57` |
    | Defined in | `res/raw/itemlist_brimhaven.json` |
    | Loot tables containing it | `revenant_2` |

    Raw data:

    ```json
    {
     "id": "whip_bind",
     "iconID": "items_weapons_3:57",
     "name": "Whip of binding",
     "displaytype": "extraordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 6700,
     "category": "whip",
     "description": "When you hold it, it almost feels like it's moving on its own, as though it were alive.",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 2,
       "max": 5
      },
      "increaseAttackCost": 5,
      "increaseAttackChance": 10,
      "increaseCriticalSkill": 5,
      "increaseBlockChance": 8,
      "setCriticalMultiplier": 1.5,
      "setNonWeaponDamageModifier": 127
     },
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "entanglement",
        "magnitude": 1,
        "duration": 2,
        "chance": "25"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
