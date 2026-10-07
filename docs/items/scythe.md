---
description: "Scythe is a ordinary pole weapon in Andor's Trail (Attack damage 2 to 6, Attack cost +6, Attack chance +11, Block chance +4). How to get it: shops. This looks more suited to farming than fighting"
---

# ![](../assets/icons/items/items_weapons_3_3.png){ .sprite } Scythe

*Ordinary pole weapon.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_3_3.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `scythe` |
| **Category** | Pole weapon |
| **Slot** | weapon |
| **Hands** | Two-handed |
| **Proficiency** | [Pole weapon proficiency](../skills/weaponProficiencyPole.md) |
| **Rarity** | Ordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

> This looks more suited to farming than fighting

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 2 to 6 |
| Attack cost | +6 |
| Attack chance | +11 |
| Block chance | +4 |
| setNonWeaponDamageModifier | +130 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Cornith](../monsters/stoutford_smith.md) (Stoutford)
- [Arlish](../monsters/arlish.md) (Brimhaven)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |
| [v0.7.8](../versions/0.7.8.md) | Category: scythe → pole |
| [v0.7.10](../versions/0.7.10.md) | When equipped, non-weapon damage modifier (%): added (130) |
| [v0.7.13](../versions/0.7.13.md) | When equipped, attack chance: +15 → +11<br>When equipped, attack damage: 2–9 → 2–6 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=scythe.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=scythe.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=scythe.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=scythe.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `scythe` |
    | Category ID | `pole` |
    | Icon | `items_weapons_3:3` |
    | Defined in | `res/raw/itemlist_stoutford_combined.json` |
    | Loot tables containing it | `shop_cornith`, `arlish` |

    Raw data:

    ```json
    {
     "id": "scythe",
     "iconID": "items_weapons_3:3",
     "name": "Scythe",
     "displaytype": "ordinary",
     "category": "pole",
     "description": "This looks more suited to farming than fighting",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 2,
       "max": 6
      },
      "increaseAttackCost": 6,
      "increaseAttackChance": 11,
      "increaseBlockChance": 4,
      "setNonWeaponDamageModifier": 130
     }
    }
    ```


<small>Data from v0.8.18</small>
