# ![](../assets/icons/items/items_weapons_7.png){ .sprite } Balanced steel sword

*Ordinary longsword.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_7.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `sword_balanced_steel` |
| **Category** | Longsword |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | One-handed sword |
| **Rarity** | Ordinary |
| **Base value** | 2,797 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 3 to 7 |
| Attack cost | +4 |
| Attack chance | +25 |
| setNonWeaponDamageModifier | +97 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Minarra](../monsters/minarra.md) (houseatcrossroads4)
- [Teksin](../monsters/teksin.md) (waytolake11)

### Quest & dialogue rewards

- From stepping on a trigger on [laerothbasement0](../maps/laerothbasement0.md) during [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-140) (1×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.10](../versions/0.7.10.md) | equipEffect: {"increaseAttackChance": 32, "increaseA… → {"increaseAttackChance": 32, "increaseA… |
| [v0.8.13](../versions/0.8.13.md) | equipEffect: {"increaseAttackChance": 32, "increaseA… → {"increaseAttackChance": 25, "increaseA… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sword_balanced_steel.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sword_balanced_steel.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sword_balanced_steel.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sword_balanced_steel.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `sword_balanced_steel` |
    | Category ID | `lsword` |
    | Icon | `items_weapons:7` |
    | Defined in | `res/raw/itemlist_v0610_1.json` |
    | Loot tables containing it | `shop_minarra`, `teksin` |

    Raw data:

    ```json
    {
     "id": "sword_balanced_steel",
     "iconID": "items_weapons:7",
     "name": "Balanced steel sword",
     "hasManualPrice": 0,
     "baseMarketCost": 2797,
     "category": "lsword",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 3,
       "max": 7
      },
      "increaseAttackCost": 4,
      "increaseAttackChance": 25,
      "setNonWeaponDamageModifier": 97
     }
    }
    ```


<small>Data from v0.8.18</small>
