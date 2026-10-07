# ![](../assets/icons/items/items_misc_5_40.png){ .sprite } Xul'viir

*Extraordinary two-handed sword.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_misc_5_40.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `xulviir` |
| **Category** | Two-handed sword |
| **Slot** | weapon |
| **Hands** | Two-handed |
| **Proficiency** | Two-handed sword |
| **Rarity** | Extraordinary |
| **Base value** | 5,045 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 4 to 15 |
| Max HP | -2 |
| Attack cost | +6 |
| Attack chance | +32 |
| Critical skill | +3 |
| Block chance | +12 |
| Critical multiplier | 2.0 |
| setNonWeaponDamageModifier | +173 |

### On hit

| Stat | Value |
|---|---|
| On target | Bleeding wound (magnitude 3, 3 rounds, 15% chance); Dazed (magnitude 1, 2 rounds, 10% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Quest & dialogue rewards

- From [Vilegard smith](../monsters/vilegard_smith.md) ([vilegard_smith](../maps/vilegard_smith.md)) during [A creeping fear](../quests/xulviir.md#stage-20) (100%)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | hitEffect: {"conditionsTarget": [{"chance": 15, "c… → {"conditionsTarget": [{"chance": "15", … |
| [v0.7.10](../versions/0.7.10.md) | equipEffect: {"increaseAttackChance": 32, "increaseA… → {"increaseAttackChance": 32, "increaseA… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=xulviir.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=xulviir.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=xulviir.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=xulviir.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `xulviir` |
    | Category ID | `2hsword` |
    | Icon | `items_misc_5:40` |
    | Defined in | `res/raw/itemlist_v070.json` |
    | Loot tables containing it | `xulviir` |

    Raw data:

    ```json
    {
     "id": "xulviir",
     "iconID": "items_misc_5:40",
     "name": "Xul'viir",
     "displaytype": "extraordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 5045,
     "category": "2hsword",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 4,
       "max": 15
      },
      "increaseMaxHP": -2,
      "increaseAttackCost": 6,
      "increaseAttackChance": 32,
      "increaseCriticalSkill": 3,
      "increaseBlockChance": 12,
      "setCriticalMultiplier": 2.0,
      "setNonWeaponDamageModifier": 173
     },
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 3,
        "duration": 3,
        "chance": "15"
       },
       {
        "condition": "dazed",
        "magnitude": 1,
        "duration": 2,
        "chance": "10"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
