# ![](../assets/icons/items/items_misc_6_7.png){ .sprite } Branch of twilight

*Rare scepter.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_misc_6_7.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `branch_of_twilight` |
| **Category** | Scepter |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | Blunt |
| **Rarity** | Rare |
| **Base value** | 4,387 gold |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 2 |
| Attack cost | +5 |
| Attack chance | +5 |
| Critical skill | 0 |
| Critical multiplier | 0.0 |

### On hit

| Stat | Value |
|---|---|
| On target | Putrefaction (magnitude 1, 2 rounds, 3% chance); Chaotic grip (magnitude 3, 2 rounds, 25% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Prowling Arantxa](../monsters/sullengard_arantxa.md) (Sullengard)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |
| [v0.8.4](../versions/0.8.4.md) | hitEffect: {"conditionsTarget": [{"chance": "3", "… → {"conditionsTarget": [{"chance": "3", "… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=branch_of_twilight.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=branch_of_twilight.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=branch_of_twilight.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=branch_of_twilight.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `branch_of_twilight` |
    | Category ID | `scepter` |
    | Icon | `items_misc_6:7` |
    | Defined in | `res/raw/itemlist_sullengard.json` |
    | Loot tables containing it | `sullengard_arantxa_dl` |

    Raw data:

    ```json
    {
     "id": "branch_of_twilight",
     "iconID": "items_misc_6:7",
     "name": "Branch of twilight",
     "displaytype": "rare",
     "hasManualPrice": 1,
     "baseMarketCost": 4387,
     "category": "scepter",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 2,
       "max": 2
      },
      "increaseAttackCost": 5,
      "increaseAttackChance": 5,
      "increaseCriticalSkill": 0,
      "setCriticalMultiplier": 0.0
     },
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "putrefaction",
        "magnitude": 1,
        "duration": 2,
        "chance": "3"
       },
       {
        "condition": "chaotic_grip",
        "magnitude": 3,
        "duration": 2,
        "chance": "25"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
