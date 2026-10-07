# ![](../assets/icons/items/items_weapons_14.png){ .sprite } Feygard iron dagger

*Ordinary dagger.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_14.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `feygard_iron_dagger` |
| **Category** | Dagger |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | Dagger |
| **Rarity** | Ordinary |
| **Base value** | 567 gold |
| **Introduced** | [v0.7.8](../versions/0.7.8.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 2 to 5 |
| Re-equip cost | 0 |
| Attack cost | +4 |
| Attack chance | +15 |
| Critical skill | +10 |
| Block chance | +2 |
| Critical multiplier | 2.5 |
| setNonWeaponDamageModifier | +96 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Feygard scout](../monsters/feygard_scout.md) | 100% | 1 | Crossroads Guardhouse |
| [Subdued Feygard mountain scout](../monsters/ortholion_subdued.md) | 50% | 1 | Blackwater Mountain |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added |
| [v0.7.10](../versions/0.7.10.md) | equipEffect: {"increaseAttackChance": 15, "increaseA… → {"increaseAttackChance": 15, "increaseA… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=feygard_iron_dagger.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=feygard_iron_dagger.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=feygard_iron_dagger.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=feygard_iron_dagger.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `feygard_iron_dagger` |
    | Category ID | `dagger` |
    | Icon | `items_weapons:14` |
    | Defined in | `res/raw/itemlist_omicronrg9.json` |
    | Loot tables containing it | `Feygard_scout`, `ortholion_subdued` |

    Raw data:

    ```json
    {
     "id": "feygard_iron_dagger",
     "iconID": "items_weapons:14",
     "name": "Feygard iron dagger",
     "displaytype": "ordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 567,
     "category": "dagger",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 2,
       "max": 5
      },
      "increaseReequipCost": 0,
      "increaseAttackCost": 4,
      "increaseAttackChance": 15,
      "increaseCriticalSkill": 10,
      "increaseBlockChance": 2,
      "setCriticalMultiplier": 2.5,
      "setNonWeaponDamageModifier": 96
     }
    }
    ```


<small>Data from v0.8.18</small>
