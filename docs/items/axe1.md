---
description: "Woodcutter's axe is a ordinary axe in Andor's Trail (Attack damage 6 to 12, Attack cost +7, Attack chance +5, setNonWeaponDamageModifier +187). How to get it: shops."
---

# ![](../assets/icons/items/items_weapons_56.png){ .sprite } Woodcutter's axe

*Ordinary axe.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/items/items_weapons_56.png" alt=""></p>

| | |
|---|---|
| **Item ID** | `axe1` |
| **Category** | Axe |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [Axe proficiency](../skills/weaponProficiencyAxe.md) |
| **Rarity** | Ordinary |
| **Base value** | 24 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 6 to 12 |
| Attack cost | +7 |
| Attack chance | +5 |
| setNonWeaponDamageModifier | +187 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Jakrar](../monsters/jakrar.md) (Fallhaven)
- [Hadracor](../monsters/hadracor.md) (Crossroads Guardhouse)
- [Wood craftsman](../monsters/brv_woodcraftsman.md) (Brimhaven)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.10](../versions/0.7.10.md) | When equipped, attack cost: +5 → +7<br>When equipped, attack damage: 1–3 → 6–12<br>When equipped, non-weapon damage modifier (%): added (187)<br>Renamed “Woodcutter axe” → “Woodcutter's axe” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=axe1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=axe1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=axe1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=axe1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `axe1` |
    | Category ID | `axe` |
    | Icon | `items_weapons:56` |
    | Defined in | `res/raw/itemlist_weapons.json` |
    | Loot tables containing it | `shop_hadracor`, `shop_fallhaven_lumberjack`, `brv_woodcraft` |

    Raw data:

    ```json
    {
     "id": "axe1",
     "iconID": "items_weapons:56",
     "name": "Woodcutter's axe",
     "baseMarketCost": 24,
     "category": "axe",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 6,
       "max": 12
      },
      "increaseAttackCost": 7,
      "increaseAttackChance": 5,
      "setNonWeaponDamageModifier": 187
     }
    }
    ```


<small>Data from v0.8.18</small>
