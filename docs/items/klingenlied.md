---
description: "Klingenlied is a rare longsword in Andor's Trail (Attack damage 4 to 8, Max HP +5, Attack cost +4, Attack chance +14). An exotic weapon from a far away land."
---

# ![](../assets/icons/items/items_misc_6_20.png){ .sprite } Klingenlied

*Rare longsword.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_misc_6_20.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `klingenlied` |
| **Category** | Longsword |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [One-handed sword proficiency](../skills/weaponProficiency1hsword.md) |
| **Rarity** | Rare |
| **Base value** | 3,884 gold |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

> An exotic weapon from a far away land.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 4 to 8 |
| Max HP | +5 |
| Attack cost | +4 |
| Attack chance | +14 |
| Critical skill | +8 |
| Block chance | +5 |
| Critical multiplier | 2.0 |
| setNonWeaponDamageModifier | +100 |

### On kill

| Stat | Value |
|---|---|
| On self | Courage (magnitude 1, 2 rounds, 5% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

As of v0.8.18, nothing in the game data gives this item: no monster drops it, no shop sells it, no container holds it and no dialogue hands it out.


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=klingenlied.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=klingenlied.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=klingenlied.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=klingenlied.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `klingenlied` |
    | Category ID | `lsword` |
    | Icon | `items_misc_6:20` |
    | Defined in | `res/raw/itemlist_brightport.json` |
    | Loot tables containing it | – |

    Raw data:

    ```json
    {
     "id": "klingenlied",
     "iconID": "items_misc_6:20",
     "name": "Klingenlied",
     "displaytype": "rare",
     "hasManualPrice": 1,
     "baseMarketCost": 3884,
     "category": "lsword",
     "description": "An exotic weapon from a far away land.",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 4,
       "max": 8
      },
      "increaseMaxHP": 5,
      "increaseAttackCost": 4,
      "increaseAttackChance": 14,
      "increaseCriticalSkill": 8,
      "increaseBlockChance": 5,
      "setCriticalMultiplier": 2.0,
      "setNonWeaponDamageModifier": 100
     },
     "killEffect": {
      "conditionsSource": [
       {
        "condition": "courage",
        "magnitude": 1,
        "duration": 2,
        "chance": "5"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
