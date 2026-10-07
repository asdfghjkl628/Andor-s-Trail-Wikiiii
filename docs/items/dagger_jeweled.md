---
description: "Jeweled dagger is a ordinary dagger in Andor's Trail (Attack damage 1 to 4, Attack cost +4, Attack chance +19, Critical skill +1). How to get it: shops. A dagger that is meant to impress. Unless you are trying to impress an opponent in a fight."
---

# ![](../assets/icons/items/items_weapons_3_46.png){ .sprite } Jeweled dagger

*Ordinary dagger.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_3_46.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `dagger_jeweled` |
| **Category** | Dagger |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [Dagger proficiency](../skills/weaponProficiencyDagger.md) |
| **Rarity** | Ordinary |
| **Base value** | 2,942 gold |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

> A dagger that is meant to impress. Unless you are trying to impress an opponent in a fight.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 1 to 4 |
| Attack cost | +4 |
| Attack chance | +19 |
| Critical skill | +1 |
| Critical multiplier | 1.1 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Edrin](../monsters/brv_metalsmith.md) (Brimhaven)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=dagger_jeweled.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=dagger_jeweled.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=dagger_jeweled.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=dagger_jeweled.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `dagger_jeweled` |
    | Category ID | `dagger` |
    | Icon | `items_weapons_3:46` |
    | Defined in | `res/raw/itemlist_brimhaven.json` |
    | Loot tables containing it | `edrin` |

    Raw data:

    ```json
    {
     "id": "dagger_jeweled",
     "iconID": "items_weapons_3:46",
     "name": "Jeweled dagger",
     "displaytype": "ordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 2942,
     "category": "dagger",
     "description": "A dagger that is meant to impress. Unless you are trying to impress an opponent in a fight.",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 1,
       "max": 4
      },
      "increaseAttackCost": 4,
      "increaseAttackChance": 19,
      "increaseCriticalSkill": 1,
      "setCriticalMultiplier": 1.1
     }
    }
    ```


<small>Data from v0.8.18</small>
