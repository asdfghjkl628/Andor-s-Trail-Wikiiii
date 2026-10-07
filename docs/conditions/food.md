---
description: "Sustenance is a beneficial physical condition in Andor's Trail: +1 HP per round. Caused by: items, enemies, dialogue and events."
---

# ![](../assets/icons/conditions/actorconditions_1_35.png){ .sprite } Sustenance

*Beneficial physical condition.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/conditions/actorconditions_1_35.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Beneficial |
| **Category** | [Physical](index.md#categories-and-resistance) |
| **Affects** | You and enemies |
| **Stacking** | No |
| **Resisted by** | [Enduring Body](../skills/resistancePhysical.md) |
| **Condition ID** | `food` |

</div>

## Effects

| Effect | Per magnitude level |
|---|---|
| HP every round | +1 |

All values are multiplied by the condition's magnitude. Round effects apply once per round: each turn in combat, and every 6 seconds outside combat.

**Stacking:** No. A new application replaces the current one only if it has a higher magnitude, or the same magnitude and a longer duration.


<p class="verified">Verified against v0.8.18 condition data and game code (`ActorStatsController.java`).</p>

## How you get it

**Items**

| Item | When | Magnitude | Duration | Chance |
|---|---|---|---|---|
| [Apple juice](../items/drink_applej.md) | When used | 1 | 15 rounds | 100% |
| [Apple pie](../items/brightport_bakery2.md) | When used | 3 | 7 rounds | 100% |
| [Bandit's Brew](../items/sullengrad_bandit_brew.md) | When used | 2 | 3 rounds | 100% |
| [Berry pie](../items/brightport_bakery1.md) | When used | 3 | 8 rounds | 100% |
| [Blue cheese](../items/cheese_blue.md) | When used | 2 | 4 rounds | 100% |
| [Bogsten's mushroom](../items/mushroom_bogsten.md) | When used | 1 | 3 rounds | 50% |
| [Boiled tripe](../items/tripe_boiled.md) | When used | 1 | 9 rounds | 100% |
| [Boletus spelunca](../items/elm_mushroom1.md) | When used | 1 | 30 rounds | 100% |
| [Bramblefin](../items/bramblefin_fish.md) | When used | 2 | 12 rounds | 100% |
| [Bread](../items/bread.md) | When used | 1 | 10 rounds | 100% |
| [Brightport bread](../items/brightport_bakery.md) | When used | 2 | 10 rounds | 100% |
| [Broccoli](../items/broccoli.md) | When used | 2 | 5 rounds | 100% |
| [Cake](../items/cake.md) | When used | 5 | 16 rounds | 100% |
| [Carrot](../items/carrot.md) | When used | 1 | 8 rounds | 100% |
| [Carrots](../items/carrots.md) | When used | 1 | 10 rounds | 100% |
| [Charwood cheddar](../items/charwood_cheddar.md) | When used | 2 | 6 rounds | 100% |
| [Cheese](../items/cheese.md) | When used | 2 | 4 rounds | 100% |
| [Coconut](../items/coconut.md) | When used | 2 | 30 rounds | 100% |
| [Concentrated charwood sap](../items/drink_charwood2.md) | When used | 3 | 15 rounds | 100% |
| [Cooked chicken leg](../items/chkn_leg.md) | When used | 4 | 6 rounds | 100% |
| [Cooked inkyfish](../items/bwm_fish2.md) | When used | 3 | 9 rounds | 100% |
| [Cooked lamb meat](../items/lamb_meat.md) | When used | 3 | 10 rounds | 100% |
| [Cooked meat](../items/meat_cooked.md) | When used | 3 | 11 rounds | 100% |
| [Cooked perch](../items/cookperch.md) | When used | 4 | 8 rounds | 100% |
| [Cooked snake meat](../items/snake_meat_cooked.md) | When used | 4 | 8 rounds | 100% |
| [Cooked venison](../items/brightport_meat.md) | When used | 4 | 10 rounds | 100% |
| [Corn](../items/corn.md) | When used | 1 | 11 rounds | 100% |
| [Cured ham](../items/cured_ham.md) | When used | 3 | 10 rounds | 100% |
| [Dark Beer Sour](../items/sullengard_dark_beer_sour.md) | When used | 2 | 3 rounds | 100% |
| [Deebo's apple cider](../items/apple_orchard_cider.md) | When used | 2 | 14 rounds | 100% |
| [Deebo's apple juice](../items/apple_orchard_juice.md) | When used | 2 | 12 rounds | 100% |
| [Deebo's apple pie](../items/apple_orchard_pie.md) | When used | 3 | 10 rounds | 100% |
| [Dried goat meat](../items/goat_meat_dried.md) | When used | 3 | 10 rounds | 100% |
| [Duck eggs](../items/eggs_duck.md) | When used | 1 | 7 rounds | 100% |
| [Durian fruit](../items/durian.md) | When used | 5 | 6 rounds | 100% |
| [Eggs](../items/eggs.md) | When used | 1 | 6 rounds | 100% |
| [Especially sweet cherries](../items/esp_sweet_cherries.md) | When used | 7 | 6 rounds | 100% |
| [Especially sweet ice berries](../items/wild_berry2a.md) | When used | 6 | 5 rounds | 100% |
| [Especially sweet red berries](../items/wild_berry3a.md) | When used | 6 | 5 rounds | 100% |
| [Especially sweet wild berries](../items/wild_berry1a.md) | When used | 4 | 5 rounds | 100% |
| [Feline milk](../items/feline_milk.md) | When used | 2 | 3 rounds | 90% |
| [Fermented garlic](../items/ferm-garlic.md) | When used | 1 | 2 rounds | 100% |
| [Feydelight](../items/feydelight.md) | When used | 3 | 35 rounds | 100% |
| [Fig](../items/fig_fruit.md) | When used | 3 | 3 rounds | 100% |
| [Forest Ale](../items/sullengard_forest_ale.md) | When used | 2 | 2 rounds | 100% |
| [Fruit assortment](../items/brightport_fruit2.md) | When used | 4 | 15 rounds | 100% |
| [Fungi potion](../items/liquid_fungi.md) | When used | 5 | 15 rounds | 100% |
| [Gison and Nimael's soup of the forest](../items/soup_forest.md) | When used | 3 | 7 rounds | 100% |
| [Goat cheese](../items/cheese_goat.md) | When used | 2 | 5 rounds | 100% |
| [Green apple](../items/apple_green.md) | When used | 1 | 8 rounds | 100% |
| [Green Pepper](../items/green_pepper.md) | When used | 3 | 4 rounds | 100% |
| [Hannah's lunch](../items/guynmart_lunch.md) | When used | 5 | 10 rounds | 100% |
| [Hard biscuits](../items/biscuit_hard.md) | When used | 2 | 11 rounds | 100% |
| [Headless fish](../items/headless_fish.md) | When used | 1 | 10 rounds | 50% |
| [Healthier worm meat](../items/better_worm_meat.md) | When used | 6 | 4 rounds | 100% |
| [Hexi egg](../items/hexi_egg.md) | When used | 4 | 5 rounds | 100% |
| [Honey](../items/honey.md) | When used | 1 | 4 rounds | 100% |
| [Ice berries](../items/wild_berry2.md) | When used | 2 | 5 rounds | 100% |
| [Izthiel claw](../items/izthiel_claw.md) | When used | 3 | 6 rounds | 100% |
| [Lowyna's foul brew](../items/drink_lowyn1.md) | When used | 2 | 5 rounds | 100% |

*50 further items are not listed.*

**Dialogue and scripted events**

| From | Quest | Duration |
|---|---|---|
| walking into a blocked passage on [ratdom_maze_632](../maps/ratdom_maze_632.md) | – | 10 rounds |
| [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)) | – | 3 rounds |

## Applied to enemies

**Enemies**

| Enemy | When | Magnitude | Duration | Chance | Found in |
|---|---|---|---|---|---|
| [Yczorah](../monsters/elm_yzczorah2.md) | On itself, when it hits you | 3 | 2 rounds | 20% | elm5f_1, elm5f_2 |
| [Yczorah marauder](../monsters/elm_yczorah1.md) | On itself, when it hits you | 2 | 2 rounds | 20% | elm5f_1, elm5f_2 |


<p class="verified">Verified against v0.8.18 item, monster, dialogue and skill data.</p>

## Removal and protection

- **Resistance:** each level of [Enduring Body](../skills/resistancePhysical.md) reduces the chance of receiving this condition by 10% of its value (for example, a 30% chance becomes 27% at level 1). Effects with a 100% chance cannot be resisted. Note that resistance also applies to beneficial conditions: it lowers the chance of receiving this one from sources with a chance below 100%.
- **[Dark blessing of the Shadow](../skills/shadowBless.md)** reduces the chance of receiving any condition by 5% of its value per level.
- **Duration and rest:** timed applications end when their duration runs out, and resting removes them earlier.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Observations**: what players notice in-game · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=food.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=food.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/conditions?filename=food.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Condition ID | `food` |
    | Category (internal) | `physical` |
    | Icon | `actorconditions_1:35` |
    | Defined in | `res/raw/actorconditions_v0612_2.json` |

    Raw data:

    ```json
    {
     "id": "food",
     "iconID": "actorconditions_1:35",
     "name": "Sustenance",
     "category": "physical",
     "isPositive": 1,
     "roundEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 1
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
