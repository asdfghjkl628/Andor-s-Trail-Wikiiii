---
description: "Bogsten1 is an indoor location in Andor's Trail. NPCs: Bogsten. Exits to Bogsten0."
---

# Bogsten1

<div class="infobox" markdown>

| | |
|---|---|
| **Map ID** | `bogsten1` |
| **Type** | Indoors / underground |
| **Size** | 12×7 tiles |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |
| **NPCs** | 1 |
| **Quests** | 1 |

</div>

**Bogsten1** is an indoor map. It has 1 NPC, and no enemies. Exits lead to Bogsten0.

## Map

<div class="map-legend" markdown="0"><label class="lg"><input type="checkbox" data-t="spawn" checked><span class="sw sw-spawn"></span><b>Red</b>&nbsp;Monsters / NPCs</label><label class="lg"><input type="checkbox" data-t="mapchange" checked><span class="sw sw-mapchange"></span><b>Blue</b>&nbsp;Exit to another map</label><label class="lg"><input type="checkbox" data-t="container" checked><span class="sw sw-container"></span><b>Yellow</b>&nbsp;Container (click to see contents)</label><label class="lg"><input type="checkbox" data-t="sign" checked><span class="sw sw-sign"></span><b>Purple</b>&nbsp;Sign</label><label class="lg"><input type="checkbox" data-t="rest" checked><span class="sw sw-rest"></span><b>Green</b>&nbsp;Resting place</label><label class="lg"><input type="checkbox" data-t="key" checked><span class="sw sw-key"></span><b>Orange dashed</b>&nbsp;Blocked until a quest step / item</label><label class="lg"><input type="checkbox" data-t="script"><span class="sw sw-script"></span><b>Grey dotted</b>&nbsp;Scripted event</label><label class="lg"><input type="checkbox" data-t="replace"><span class="sw sw-replace"></span><b>White dotted</b>&nbsp;Changes during a quest</label><label class="lg"><input type="checkbox" data-t="pin" checked><span class="sw sw-pin"></span><b>Numbers</b>&nbsp;Numbered key points (see the key below the map)</label></div>

<div class="map-wrap hide-script hide-replace" markdown="0"><img src="../../assets/maps/bogsten1.webp" alt="Map of Bogsten1" width="384" height="224" loading="lazy"><a id="place-exit_south" class="mo mo-mapchange" href="../bogsten0/#place-house_entrance" title="Exit to Bogsten0" style="left:66.667%;top:85.714%;width:8.333%;height:14.286%"></a><a id="place-exit_north" class="mo mo-mapchange" href="../bogsten0/#place-backyard_entrance" title="Exit to Bogsten0" style="left:58.333%;top:28.571%;width:8.333%;height:14.286%"></a><a class="mo mo-script" href="../../quests/fungi_panic_nondisplayed/#stage-35" title="Scripted event: advances the quest: hidden story flag “fungi_panic_nondisplayed” to stage 35 (“35=I opened Bogsten&#x27;s backyard door.”)" style="left:50.000%;top:42.857%;width:25.000%;height:14.286%"></a><span class="mo mo-spawn" title="Spawns: Bogsten" style="left:25.000%;top:42.857%;width:25.000%;height:42.857%"></span><a class="mo mo-key" href="../../quests/fungi_panic_nondisplayed/#stage-35" title="Unlocked during the quest: hidden story flag “fungi_panic_nondisplayed” (stage 35: “35=I opened Bogsten&#x27;s backyard door.”)" style="left:58.333%;top:28.571%;width:8.333%;height:14.286%"></a><span class="mo mo-replace" title="This area changes when a scripted event activates it" style="left:58.333%;top:14.286%;width:8.333%;height:28.571%"></span><a class="mob" href="../../monsters/bogsten/" title="Bogsten" style="left:41.667%;top:57.143%;width:8.333%;height:14.286%"><img src="../../assets/icons/monsters/monsters_rltiles1_77.png" alt="Bogsten"></a><a class="pin pin-exit" href="#key-1" style="left:70.833%;top:92.857%" title="Exit (south): to [Bogsten0](bogsten0.md)">1</a><a class="pin pin-exit" href="#key-2" style="left:62.500%;top:35.714%" title="Exit (stairs / passage): to [Bogsten0](bogsten0.md)">2</a><a id="pin-npc-bogsten" class="pin pin-npc" href="#key-3" style="left:45.833%;top:64.286%" title="[Bogsten](../../monsters/bogsten.md): 1 quest">3</a><a class="pin pin-script" href="#key-4" style="left:62.500%;top:50.000%" title="Quest trigger: Scripted event: advances the quest: hidden story flag “fungi_panic_nondisplayed” to stage 35 (“35=I opened Bogsten&#x27;s backyard door.”)">4</a><a class="pin pin-key" href="#key-5" style="left:63.048%;top:25.001%" title="Blocked passage: Unlocked during the quest: hidden story flag “fungi_panic_nondisplayed” (stage 35: “35=I opened Bogsten&#x27;s backyard door.”)">5</a></div>

??? abstract "Key to the numbers on the map"

    | # | What | Details |
    |---|---|---|
    | <span id="key-1"></span>1 | Exit (south) | to [Bogsten0](bogsten0.md) |
    | <span id="key-2"></span>2 | Exit (stairs / passage) | to [Bogsten0](bogsten0.md) |
    | <span id="key-3"></span>3 | [Bogsten](../monsters/bogsten.md) | 1 quest |
    | <span id="key-4"></span>4 | Quest trigger | Scripted event: advances the quest: hidden story flag “fungi_panic_nondisplayed” to stage 35 (“35=I opened Bogsten's backyard door.”) |
    | <span id="key-5"></span>5 | Blocked passage | Unlocked during the quest: hidden story flag “fungi_panic_nondisplayed” (stage 35: “35=I opened Bogsten's backyard door.”) |


<p class="verified">Verified against v0.8.18 map data.</p>

## Connections

| Direction | Leads to | Region there | Map # |
|---|---|---|---|
| South | [Bogsten0](bogsten0.md) | Fallhaven | 1 |
| Stairs / passage | [Bogsten0](bogsten0.md) | Fallhaven | 2 |

## NPCs

- [Bogsten](../monsters/bogsten.md) — can be fought — quests: [Fungi panic](../quests/fungi_panic.md) (#3)

## Quests

- [Fungi panic](../quests/fungi_panic.md): [Bogsten](../monsters/bogsten.md) is involved
- [Fungi Panic - non displayed (hidden flag)](../quests/fungi_panic_nondisplayed.md): blocked passage opens at stage 35; something on this map advances it; stepping on a trigger here sets stage 35

## Points of interest

- **Quest trigger** (#4): Scripted event: advances the quest: hidden story flag “fungi_panic_nondisplayed” to stage 35 (“35=I opened Bogsten's backyard door.”)
- **Blocked passage** (#5): Unlocked during the quest: hidden story flag “fungi_panic_nondisplayed” (stage 35: “35=I opened Bogsten's backyard door.”)


## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=bogsten1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=bogsten1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=bogsten1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=bogsten1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Map ID | `bogsten1` |
    | File | `res/xml/bogsten1.tmx` |
    | Size | 12×7 tiles (384×224 px) |
    | outdoors property | – |
    | Layers drawn | ground, objects, above |
    | Tilesets | map_bed_1, map_border_1, map_bridge_1, map_broken_1, map_cavewall_1, map_cavewall_2, map_cavewall_3, map_chair_table_1, map_crate_1, map_cupboard_1, map_curtain_1, map_entrance_1, map_fence_1, map_fence_2, map_ground_1, map_ground_2, map_ground_3, map_ground_4, map_ground_5, map_ground_6, map_ground_7, map_ground_8, map_indoor_1, map_kitchen_1, map_outdoor_1, map_pillar_1, map_plant_1, map_rock_1, map_roof_1, map_roof_2, map_shop_1, map_sign_ladder_1, map_table_1, map_trail_1, map_tree_1, map_wall_1, map_wall_2, map_wall_3, map_window_1, map_window_2 |
    | Map objects | mapchange: 2, script: 1, spawn: 1, key: 1, replace: 1 |
    | World map position | – |


<small>Data from v0.8.18</small>
