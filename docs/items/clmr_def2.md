# ![](../assets/icons/items/items_weapons_3_26.png){ .sprite } Superior defender's claymore

*Ordinary two-handed sword.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_3_26.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `clmr_def2` |
| **Category** | Two-handed sword |
| **Slot** | weapon |
| **Hands** | Two-handed |
| **Proficiency** | Two-handed sword |
| **Rarity** | Ordinary |
| **Base value** | 1,019 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 1 to 6 |
| Max HP | +4 |
| Attack cost | +6 |
| Attack chance | +10 |
| Critical skill | +2 |
| Block chance | +15 |
| Damage resistance | -2 |
| Critical multiplier | 1.5 |
| setNonWeaponDamageModifier | +175 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Lleglaris](../monsters/lleglaris.md) (Foaming Flask Tavern)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | equipEffect: {"increaseAttackChance": 10, "increaseA… → {"increaseAttackChance": 10, "increaseA… |
| [v0.7.10](../versions/0.7.10.md) | equipEffect: {"increaseAttackChance": 10, "increaseA… → {"increaseAttackChance": 10, "increaseA… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clmr_def2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clmr_def2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clmr_def2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clmr_def2.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `clmr_def2` |
    | Category ID | `2hsword` |
    | Icon | `items_weapons_3:26` |
    | Defined in | `res/raw/itemlist_v070.json` |
    | Loot tables containing it | `shop_lleglaris` |

    Raw data:

    ```json
    {
     "id": "clmr_def2",
     "iconID": "items_weapons_3:26",
     "name": "Superior defender's claymore",
     "baseMarketCost": 1019,
     "category": "2hsword",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 1,
       "max": 6
      },
      "increaseMaxHP": 4,
      "increaseAttackCost": 6,
      "increaseAttackChance": 10,
      "increaseCriticalSkill": 2,
      "increaseBlockChance": 15,
      "increaseDamageResistance": -2,
      "setCriticalMultiplier": 1.5,
      "setNonWeaponDamageModifier": 175
     }
    }
    ```


<small>Data from v0.8.18</small>
