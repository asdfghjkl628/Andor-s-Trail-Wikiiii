---
description: "Blackwater iron longsword is a rare longsword in Andor's Trail (Attack damage 4 to 9, Attack cost +4, Attack chance +55, Block chance 0). How to get it: containers."
---

# ![](../assets/icons/items/items_weapons_7.png){ .sprite } Blackwater iron longsword

*Rare longsword.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/items/items_weapons_7.png" alt=""></p>

| | |
|---|---|
| **Item ID** | `bwm_longsword` |
| **Category** | Longsword |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [One-handed sword proficiency](../skills/weaponProficiency1hsword.md) |
| **Rarity** | Rare |
| **Base value** | 1,699 gold |
| **Introduced** | [v0.8.10](../versions/0.8.10.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 4 to 9 |
| Attack cost | +4 |
| Attack chance | +55 |
| Block chance | 0 |
| setNonWeaponDamageModifier | +110 |
| Grants | [Blackwater misery](../conditions/blackwater_misery.md) (magnitude 1) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Found in containers

- [Bwmfill 6](../maps/bwmfill6.md#container-0) (container 1, 100%), Blackwater Mountain


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.10](../versions/0.8.10.md) | Added |
| [v0.8.12.1](../versions/0.8.12.1.md) | When equipped, non-weapon damage modifier (%): 122 → 110 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bwm_longsword.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bwm_longsword.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bwm_longsword.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bwm_longsword.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `bwm_longsword` |
    | Category ID | `lsword` |
    | Icon | `items_weapons:7` |
    | Defined in | `res/raw/itemlist_bwmfill.json` |
    | Loot tables containing it | `bwmfill6_container` |

    Raw data:

    ```json
    {
     "id": "bwm_longsword",
     "iconID": "items_weapons:7",
     "name": "Blackwater iron longsword",
     "displaytype": "rare",
     "hasManualPrice": 1,
     "baseMarketCost": 1699,
     "category": "lsword",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 4,
       "max": 9
      },
      "increaseAttackCost": 4,
      "increaseAttackChance": 55,
      "increaseBlockChance": 0,
      "setNonWeaponDamageModifier": 110,
      "addedConditions": [
       {
        "condition": "blackwater_misery",
        "magnitude": 1
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
