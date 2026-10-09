---
description: "Sword of Shadow's rage is a extraordinary rapier in Andor's Trail (Attack damage 3 to 6, Attack cost +5, Attack chance +21, Block chance +5). How to get it: quests and dialogue."
---

# ![](../assets/icons/items/items_weapons_71.png){ .sprite } Sword of Shadow's rage

*Extraordinary rapier.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_71.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `clouded_rage` |
| **Category** | Rapier |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [One-handed sword proficiency](../skills/weaponProficiency1hsword.md) |
| **Rarity** | Extraordinary |
| **Base value** | 0 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 3 to 6 |
| Attack cost | +5 |
| Attack chance | +21 |
| Block chance | +5 |
| setNonWeaponDamageModifier | +115 |

### On kill

| Stat | Value |
|---|---|
| On self | [Minor berserker rage](../conditions/rage_minor.md) (magnitude 1, 1 round, 50% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Quest & dialogue rewards

- From [Harlenn](../monsters/harlenn.md) ([Blackwater mountain 45](../maps/blackwater_mountain45.md)) during [The agent and the beast](../quests/bwm_agent.md#stage-150) (100%)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On kill, condition on self: [Minor berserker rage](../conditions/rage_minor.md) (magnitude 1, 1 rounds, 50% chance) → (magnitude 1, 1 rounds, 50% chance) |
| [v0.7.10](../versions/0.7.10.md) | When equipped, non-weapon damage modifier (%): added (115) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clouded_rage.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clouded_rage.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clouded_rage.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=clouded_rage.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `clouded_rage` |
    | Category ID | `rapier` |
    | Icon | `items_weapons:71` |
    | Defined in | `res/raw/itemlist_v069.json` |
    | Loot tables containing it | `harlenn_reward` |

    Raw data:

    ```json
    {
     "id": "clouded_rage",
     "iconID": "items_weapons:71",
     "name": "Sword of Shadow's rage",
     "displaytype": "extraordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 0,
     "category": "rapier",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 3,
       "max": 6
      },
      "increaseAttackCost": 5,
      "increaseAttackChance": 21,
      "increaseBlockChance": 5,
      "setNonWeaponDamageModifier": 115
     },
     "killEffect": {
      "conditionsSource": [
       {
        "condition": "rage_minor",
        "magnitude": 1,
        "duration": 1,
        "chance": "50"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
