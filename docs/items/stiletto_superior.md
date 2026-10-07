---
description: "Superior stiletto is a ordinary dagger in Andor's Trail (Attack damage 1 to 4, Attack cost +4, Attack chance +17, Critical skill +15). How to get it: containers."
---

# ![](../assets/icons/items/items_tometik3_33.png){ .sprite } Superior stiletto

*Ordinary dagger.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_tometik3_33.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `stiletto_superior` |
| **Category** | Dagger |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [Dagger proficiency](../skills/weaponProficiencyDagger.md) |
| **Rarity** | Ordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 1 to 4 |
| Attack cost | +4 |
| Attack chance | +17 |
| Critical skill | +15 |
| Critical multiplier | 2.5 |
| setNonWeaponDamageModifier | +105 |

### On hit

| Stat | Value |
|---|---|
| On self | Minor speed (magnitude 2, 2 rounds, 1% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Found in containers

- [galmore_37](../maps/galmore_37.md#container-0) (container 1, 100%)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=stiletto_superior.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=stiletto_superior.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=stiletto_superior.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=stiletto_superior.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `stiletto_superior` |
    | Category ID | `dagger` |
    | Icon | `items_tometik3:33` |
    | Defined in | `res/raw/itemlist_mt_galmore2.json` |
    | Loot tables containing it | `galmore_37_treasure` |

    Raw data:

    ```json
    {
     "id": "stiletto_superior",
     "iconID": "items_tometik3:33",
     "name": "Superior stiletto",
     "displaytype": "ordinary",
     "category": "dagger",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 1,
       "max": 4
      },
      "increaseAttackCost": 4,
      "increaseAttackChance": 17,
      "increaseCriticalSkill": 15,
      "setCriticalMultiplier": 2.5,
      "setNonWeaponDamageModifier": 105
     },
     "hitEffect": {
      "conditionsSource": [
       {
        "condition": "speed_minor",
        "magnitude": 2,
        "duration": 2,
        "chance": "1"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
