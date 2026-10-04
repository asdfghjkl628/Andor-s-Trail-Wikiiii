# Brightport jail

<div class="infobox" markdown>

| | |
|---|---|
| **Map ID** | `brightport_jail` |
| **Region** | In Brightport (settlement) |
| **Type** | Indoors / underground |
| **Size** | 16×8 tiles |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |
| **NPCs** | 3 |
| **Quests** | 1 |

</div>

**Brightport jail** is an indoor map, in Brightport (settlement). It has 3 NPCs, and no enemies. Exits lead to Brightport escape cave, Brightport9.

## Map

<div class="map-legend" markdown="0"><label class="lg"><input type="checkbox" data-t="spawn" checked><span class="sw sw-spawn"></span><b>Red</b>&nbsp;Monsters / NPCs</label><label class="lg"><input type="checkbox" data-t="mapchange" checked><span class="sw sw-mapchange"></span><b>Blue</b>&nbsp;Exit to another map</label><label class="lg"><input type="checkbox" data-t="container" checked><span class="sw sw-container"></span><b>Yellow</b>&nbsp;Container (click to see contents)</label><label class="lg"><input type="checkbox" data-t="sign" checked><span class="sw sw-sign"></span><b>Purple</b>&nbsp;Sign</label><label class="lg"><input type="checkbox" data-t="rest" checked><span class="sw sw-rest"></span><b>Green</b>&nbsp;Resting place</label><label class="lg"><input type="checkbox" data-t="key" checked><span class="sw sw-key"></span><b>Orange dashed</b>&nbsp;Blocked until a quest step / item</label><label class="lg"><input type="checkbox" data-t="script"><span class="sw sw-script"></span><b>Grey dotted</b>&nbsp;Scripted event</label><label class="lg"><input type="checkbox" data-t="replace"><span class="sw sw-replace"></span><b>White dotted</b>&nbsp;Changes during a quest</label><label class="lg"><input type="checkbox" data-t="pin" checked><span class="sw sw-pin"></span><b>Numbers</b>&nbsp;Numbered key points (see the key below the map)</label></div>

<div class="map-wrap hide-script hide-replace" markdown="0"><img src="../../assets/maps/brightport_jail.webp" alt="Map of Brightport jail" width="512" height="256" loading="lazy"><a id="place-entrance" class="mo mo-mapchange" href="../brightport9/#place-jail" title="Exit to Brightport9" style="left:18.750%;top:87.500%;width:6.250%;height:12.500%"></a><a id="place-east" class="mo mo-mapchange" href="../brightport_escape_cave/#place-west" title="Exit to Brightport escape cave" style="left:87.500%;top:37.500%;width:6.250%;height:12.500%"></a><a class="mo mo-script" href="../../quests/brightport_nondisplay/#stage-160" title="Scripted event: advances the quest: hidden story flag “brightport_nondisplay” to stage 160 (“arrest escape”)" style="left:56.250%;top:37.500%;width:25.000%;height:25.000%"></a><span id="place-jail" class="mo mo-mapchange" title="Jail" style="left:62.500%;top:37.500%;width:18.750%;height:25.000%"></span><span class="mo mo-spawn" title="Spawns: Brightport guard" style="left:25.000%;top:50.000%;width:18.750%;height:25.000%"></span><span class="mo mo-spawn" title="Spawns: Watchdog" style="left:0.000%;top:0.000%;width:6.250%;height:12.500%"></span><span class="mo mo-spawn" title="Spawns: Nor agent (only appears later, during a quest)" style="left:62.500%;top:37.500%;width:18.750%;height:25.000%"></span><a class="mo mo-key" href="../../quests/brightport_nondisplay/#stage-160" title="Unlocked during the quest: hidden story flag “brightport_nondisplay” (stage 160: “arrest escape”)" style="left:87.500%;top:37.500%;width:6.250%;height:12.500%"></a><a class="mob" href="../../monsters/brightport_jailguard/" title="Brightport guard" style="left:31.250%;top:62.500%;width:6.250%;height:12.500%"><img src="../../assets/icons/monsters/monsters_karvis2_2.png" alt="Brightport guard"></a><a class="mob" href="../../monsters/brightportthieves4/" title="Watchdog" style="left:0.000%;top:0.000%;width:6.250%;height:12.500%"><img src="../../assets/icons/monsters/monsters_ld1_94.png" alt="Watchdog"></a><a class="mob mob-later" href="../../monsters/brightport_agent/" title="Nor agent (appears later in a quest)" style="left:75.000%;top:37.500%;width:6.250%;height:12.500%"><img src="../../assets/icons/monsters/monsters_rltiles1_84.png" alt="Nor agent"></a><a class="pin pin-exit" href="#key-1" style="left:90.625%;top:43.750%" title="Exit (east): to [Brightport escape cave](../brightport_escape_cave.md)">1</a><a class="pin pin-exit" href="#key-2" style="left:21.875%;top:93.750%" title="Exit (south): to [Brightport9](../brightport9.md)">2</a><a class="pin pin-npc" href="#key-3" style="left:34.375%;top:68.750%" title="[Brightport guard](../../monsters/brightport_jailguard.md): NPC">3</a><a class="pin pin-npc" href="#key-4" style="left:78.125%;top:43.750%" title="[Nor agent](../../monsters/brightport_agent.md): 1 quest">4</a><a class="pin pin-npc" href="#key-5" style="left:3.125%;top:6.250%" title="[Watchdog](../../monsters/brightportthieves4.md): NPC">5</a><a class="pin pin-script" href="#key-6" style="left:68.750%;top:50.000%" title="Quest trigger: Scripted event: advances the quest: hidden story flag “brightport_nondisplay” to stage 160 (“arrest escape”)">6</a><a class="pin pin-key" href="#key-7" style="left:91.036%;top:34.376%" title="Blocked passage: Unlocked during the quest: hidden story flag “brightport_nondisplay” (stage 160: “arrest escape”)">7</a></div>

??? abstract "Key to the numbers on the map"

    | # | What | Details |
    |---|---|---|
    | <span id="key-1"></span>1 | Exit (east) | to [Brightport escape cave](../brightport_escape_cave.md) |
    | <span id="key-2"></span>2 | Exit (south) | to [Brightport9](../brightport9.md) |
    | <span id="key-3"></span>3 | [Brightport guard](../monsters/brightport_jailguard.md) | NPC |
    | <span id="key-4"></span>4 | [Nor agent](../monsters/brightport_agent.md) | 1 quest |
    | <span id="key-5"></span>5 | [Watchdog](../monsters/brightportthieves4.md) | NPC |
    | <span id="key-6"></span>6 | Quest trigger | Scripted event: advances the quest: hidden story flag “brightport_nondisplay” to stage 160 (“arrest escape”) |
    | <span id="key-7"></span>7 | Blocked passage | Unlocked during the quest: hidden story flag “brightport_nondisplay” (stage 160: “arrest escape”) |


<p class="verified">Verified against v0.8.18 map data.</p>

## Connections

| Direction | Leads to | Region there | Map # |
|---|---|---|---|
| East | [Brightport escape cave](brightport_escape_cave.md) | Brightport | 1 |
| South | [Brightport9](brightport9.md) | Brightport | 2 |

## NPCs

- [Brightport guard](../monsters/brightport_jailguard.md) (#3)
- [Nor agent](../monsters/brightport_agent.md) — quests: [Boxed in](../quests/brightport_thieves.md) (#4)
- [Watchdog](../monsters/brightportthieves4.md) (#5)

## Quests

- [Boxed in](../quests/brightport_thieves.md): [Nor agent](../monsters/brightport_agent.md) is involved
- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): [Nor agent](../monsters/brightport_agent.md) is involved; blocked passage opens at stage 160; something on this map advances it; stepping on a trigger here sets stage 160

## Points of interest

- **Quest trigger** (#6): Scripted event: advances the quest: hidden story flag “brightport_nondisplay” to stage 160 (“arrest escape”)
- **Blocked passage** (#7): Unlocked during the quest: hidden story flag “brightport_nondisplay” (stage 160: “arrest escape”)


## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added |
| [v0.8.18](../versions/0.8.18.md) | map layout or objects changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=brightport_jail.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=brightport_jail.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=brightport_jail.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=brightport_jail.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Map ID | `brightport_jail` |
    | File | `res/xml/brightport_jail.tmx` |
    | Size | 16×8 tiles (512×256 px) |
    | outdoors property | – |
    | Layers drawn | base, ground, objects, above, top |
    | Tilesets | map_bed_1, map_border_1, map_bridge_1, map_bridge_2, map_broken_1, map_cavewall_1, map_cavewall_2, map_cavewall_3, map_cavewall_4, map_chair_table_1, map_chair_table_2, map_crate_1, map_cupboard_1, map_curtain_1, map_entrance_1, map_entrance_2, map_fence_1, map_fence_2, map_fence_3, map_fence_4, map_ground_1, map_ground_2, map_ground_3, map_ground_4, map_ground_5, map_ground_6, map_ground_7, map_ground_8, map_house_1, map_house_2, map_indoor_1, map_indoor_2, map_kitchen_1, map_outdoor_1, map_pillar_1, map_pillar_2, map_plant_1, map_plant_2, map_rock_1, map_rock_2, map_roof_1, map_roof_2, map_roof_3, map_shop_1, map_sign_ladder_1, map_table_1, map_trail_1, map_transition_1, map_transition_2, map_transition_3, map_transition_4, map_transition_5, map_tree_1, map_tree_2, map_wall_1, map_wall_2, map_wall_3, map_wall_4, map_window_1, map_window_2 |
    | Map objects | mapchange: 3, spawn: 3, script: 1, key: 1 |
    | World map position | – |


<small>Data from v0.8.18</small>
