# ![](../assets/icons/items/items_weapons_2_1.png){ .sprite } Two-handed steel sword

*Ordinary two-handed sword.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_2_1.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `clmr_stl` |
| **Category** | Two-handed sword |
| **Slot** | weapon |
| **Hands** | Two-handed |
| **Proficiency** | Two-handed sword |
| **Rarity** | Ordinary |
| **Base value** | 466 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 1 to 6 |
| Attack cost | +5 |
| Attack chance | +12 |
| Critical skill | +1 |
| Block chance | +3 |
| Critical multiplier | 1.5 |
| setNonWeaponDamageModifier | +126 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Agthor](../monsters/agthor.md) (Fallhaven)
- [Cornith](../monsters/stoutford_smith.md) (Stoutford)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | equipEffect: {"increaseAttackChance": 12, "increaseA… → {"increaseAttackChance": 12, "increaseA… |
| [v0.7.10](../versions/0.7.10.md) | equipEffect: {"increaseAttackChance": 12, "increaseA… → {"increaseAttackChance": 12, "increaseA… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clmr_stl.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clmr_stl.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clmr_stl.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clmr_stl.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `clmr_stl` |
    | Category ID | `2hsword` |
    | Icon | `items_weapons_2:1` |
    | Defined in | `res/raw/itemlist_v070.json` |
    | Loot tables containing it | `shop_agthor`, `shop_cornith` |

    Raw data:

    ```json
    {
     "id": "clmr_stl",
     "iconID": "items_weapons_2:1",
     "name": "Two-handed steel sword",
     "baseMarketCost": 466,
     "category": "2hsword",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 1,
       "max": 6
      },
      "increaseAttackCost": 5,
      "increaseAttackChance": 12,
      "increaseCriticalSkill": 1,
      "increaseBlockChance": 3,
      "setCriticalMultiplier": 1.5,
      "setNonWeaponDamageModifier": 126
     }
    }
    ```


<small>Data from v0.8.18</small>
