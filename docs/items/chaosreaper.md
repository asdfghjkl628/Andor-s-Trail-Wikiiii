# ![](../assets/icons/items/items_weapons_49.png){ .sprite } Chaosreaper

*Extraordinary scepter.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_49.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `chaosreaper` |
| **Category** | Scepter |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | Blunt |
| **Rarity** | Extraordinary |
| **Base value** | 339 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 0 to 2 |
| Attack cost | +4 |
| Attack chance | -10 |
| Critical skill | +1 |
| Critical multiplier | 1.5 |
| setNonWeaponDamageModifier | +102 |

### On hit

| Stat | Value |
|---|---|
| On target | Chaotic grip (magnitude 5, 3 rounds, 50% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Iqhan chaos beast](../monsters/iqhan_chb_1a.md) | 0.1% | 1 | pwcave2a, pwcave4 |
| [Iqhan chaos beast](../monsters/iqhan_chb_1b.md) | 0.1% | 1 | pwcave2a, pwcave4 |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | hitEffect: {"conditionsTarget": [{"chance": 50, "c… → {"conditionsTarget": [{"chance": "50", … |
| [v0.7.10](../versions/0.7.10.md) | equipEffect: {"increaseAttackChance": -30, "increase… → {"increaseAttackChance": -30, "increase… |
| [v0.7.12](../versions/0.7.12.md) | equipEffect: {"increaseAttackChance": -30, "increase… → {"increaseAttackChance": -10, "increase… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=chaosreaper.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=chaosreaper.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=chaosreaper.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=chaosreaper.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `chaosreaper` |
    | Category ID | `scepter` |
    | Icon | `items_weapons:49` |
    | Defined in | `res/raw/itemlist_v0610_2.json` |
    | Loot tables containing it | `iqhan_beast` |

    Raw data:

    ```json
    {
     "id": "chaosreaper",
     "iconID": "items_weapons:49",
     "name": "Chaosreaper",
     "displaytype": "extraordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 339,
     "category": "scepter",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 0,
       "max": 2
      },
      "increaseAttackCost": 4,
      "increaseAttackChance": -10,
      "increaseCriticalSkill": 1,
      "setCriticalMultiplier": 1.5,
      "setNonWeaponDamageModifier": 102
     },
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "chaotic_grip",
        "magnitude": 5,
        "duration": 3,
        "chance": "50"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
