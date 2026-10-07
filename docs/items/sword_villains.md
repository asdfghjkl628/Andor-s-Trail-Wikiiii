---
description: "Villain's blade is a ordinary shortsword in Andor's Trail (Attack damage 1 to 2, Attack cost +4, Attack chance +20, Critical skill +5). How to get it: shops."
---

# ![](../assets/icons/items/items_weapons_16.png){ .sprite } Villain's blade

*Ordinary shortsword.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_16.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `sword_villains` |
| **Category** | Shortsword |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [Dagger proficiency](../skills/weaponProficiencyDagger.md) |
| **Rarity** | Ordinary |
| **Base value** | 1,665 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 1 to 2 |
| Attack cost | +4 |
| Attack chance | +20 |
| Critical skill | +5 |
| Critical multiplier | 3.0 |
| setNonWeaponDamageModifier | +96 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Dunla](../monsters/dunla.md) (Vilegard)
- [Oseanpry](../monsters/Brightportthieves5.md) (Brightport)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | minor data change |
| [v0.7.10](../versions/0.7.10.md) | equipEffect: {"increaseAttackChance": 20, "increaseA… → {"increaseAttackChance": 20, "increaseA… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sword_villains.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sword_villains.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sword_villains.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sword_villains.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `sword_villains` |
    | Category ID | `ssword` |
    | Icon | `items_weapons:16` |
    | Defined in | `res/raw/itemlist_v0610_1.json` |
    | Loot tables containing it | `shop_dunla`, `brightport_oseanpry` |

    Raw data:

    ```json
    {
     "id": "sword_villains",
     "iconID": "items_weapons:16",
     "name": "Villain's blade",
     "hasManualPrice": 0,
     "baseMarketCost": 1665,
     "category": "ssword",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 1,
       "max": 2
      },
      "increaseAttackCost": 4,
      "increaseAttackChance": 20,
      "increaseCriticalSkill": 5,
      "setCriticalMultiplier": 3.0,
      "setNonWeaponDamageModifier": 96
     }
    }
    ```


<small>Data from v0.8.18</small>
