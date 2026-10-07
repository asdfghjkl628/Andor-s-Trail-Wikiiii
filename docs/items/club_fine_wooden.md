---
description: "Fine wooden club is a ordinary club in Andor's Trail (Attack damage 0 to 7, Attack cost +5, Attack chance +12, setNonWeaponDamageModifier +122). How to get it: monster drops, shops."
---

# ![](../assets/icons/items/items_weapons_42.png){ .sprite } Fine wooden club

*Ordinary club.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_42.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `club_fine_wooden` |
| **Category** | Club |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [Blunt weapon proficiency](../skills/weaponProficiencyBlunt.md) |
| **Rarity** | Ordinary |
| **Base value** | 245 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 0 to 7 |
| Attack cost | +5 |
| Attack chance | +12 |
| setNonWeaponDamageModifier | +122 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [River troll](../monsters/rivertroll.md) | 100% | 1 | Flagstone Prison, Crossroads Guardhouse |

### Sold by

- [Vilegard smith](../monsters/vilegard_smith.md) (Vilegard)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.10](../versions/0.7.10.md) | equipEffect: {"increaseAttackChance": 12, "increaseA… → {"increaseAttackChance": 12, "increaseA… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=club_fine_wooden.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=club_fine_wooden.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=club_fine_wooden.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=club_fine_wooden.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `club_fine_wooden` |
    | Category ID | `club` |
    | Icon | `items_weapons:42` |
    | Defined in | `res/raw/itemlist_v0610_1.json` |
    | Loot tables containing it | `shop_vg_smith`, `rivertroll` |

    Raw data:

    ```json
    {
     "id": "club_fine_wooden",
     "iconID": "items_weapons:42",
     "name": "Fine wooden club",
     "hasManualPrice": 0,
     "baseMarketCost": 245,
     "category": "club",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 0,
       "max": 7
      },
      "increaseAttackCost": 5,
      "increaseAttackChance": 12,
      "setNonWeaponDamageModifier": 122
     }
    }
    ```


<small>Data from v0.8.18</small>
