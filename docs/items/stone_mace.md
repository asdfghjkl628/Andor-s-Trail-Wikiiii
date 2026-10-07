---
description: "Gornaud's stone mace is a extraordinary mace in Andor's Trail (Attack damage 5 to 13, Attack cost +7, Attack chance +10, Block chance 0). How to get it: monster drops."
---

# ![](../assets/icons/items/items_newb_462.png){ .sprite } Gornaud's stone mace

*Extraordinary mace.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_newb_462.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `stone_mace` |
| **Category** | Mace |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [Blunt weapon proficiency](../skills/weaponProficiencyBlunt.md) |
| **Rarity** | Extraordinary |
| **Base value** | 639 gold |
| **Introduced** | [v0.8.10](../versions/0.8.10.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 5 to 13 |
| Attack cost | +7 |
| Attack chance | +10 |
| Block chance | 0 |
| setNonWeaponDamageModifier | +160 |

### On hit

| Stat | Value |
|---|---|
| On target | [Stunned](../conditions/stunned.md) (magnitude 1, 3 rounds, 5% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Gornaud leader](../monsters/gornaud_boss.md) | 100% | 1 | Blackwater Mountain |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.10](../versions/0.8.10.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=stone_mace.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=stone_mace.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=stone_mace.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=stone_mace.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `stone_mace` |
    | Category ID | `mace` |
    | Icon | `items_newb:462` |
    | Defined in | `res/raw/itemlist_bwmfill.json` |
    | Loot tables containing it | `gornaud_boss` |

    Raw data:

    ```json
    {
     "id": "stone_mace",
     "iconID": "items_newb:462",
     "name": "Gornaud's stone mace",
     "displaytype": "extraordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 639,
     "category": "mace",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 5,
       "max": 13
      },
      "increaseAttackCost": 7,
      "increaseAttackChance": 10,
      "increaseBlockChance": 0,
      "setNonWeaponDamageModifier": 160
     },
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "stunned",
        "magnitude": 1,
        "duration": 3,
        "chance": "5"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
