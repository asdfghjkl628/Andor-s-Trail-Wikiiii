---
description: "Prim arming sword is a ordinary rapier in Andor's Trail (Attack damage 2 to 6, Max HP -2, Attack cost +5, Attack chance +13). How to get it: monster drops."
---

# ![](../assets/icons/items/items_japozero_53.png){ .sprite } Prim arming sword

*Ordinary rapier.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_japozero_53.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `kamelio_drop1` |
| **Category** | Rapier |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [One-handed sword proficiency](../skills/weaponProficiency1hsword.md) |
| **Rarity** | Ordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 2 to 6 |
| Max HP | -2 |
| Attack cost | +5 |
| Attack chance | +13 |
| Critical skill | +8 |
| Block chance | +8 |
| Critical multiplier | 1.5 |
| setNonWeaponDamageModifier | +113 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Undead Kamelio](../monsters/kamelio2.md) | 100% | 1 | elm5f_2 |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=kamelio_drop1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=kamelio_drop1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=kamelio_drop1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=kamelio_drop1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `kamelio_drop1` |
    | Category ID | `rapier` |
    | Icon | `items_japozero:53` |
    | Defined in | `res/raw/itemlist_omi2.json` |
    | Loot tables containing it | `kamelio2` |

    Raw data:

    ```json
    {
     "id": "kamelio_drop1",
     "iconID": "items_japozero:53",
     "name": "Prim arming sword",
     "displaytype": "ordinary",
     "category": "rapier",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 2,
       "max": 6
      },
      "increaseMaxHP": -2,
      "increaseAttackCost": 5,
      "increaseAttackChance": 13,
      "increaseCriticalSkill": 8,
      "increaseBlockChance": 8,
      "setCriticalMultiplier": 1.5,
      "setNonWeaponDamageModifier": 113
     }
    }
    ```


<small>Data from v0.8.18</small>
