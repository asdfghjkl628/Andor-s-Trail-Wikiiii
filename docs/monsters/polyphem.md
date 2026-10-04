# ![](../assets/icons/monsters/monsters_ld1_36.png){ .sprite } Polyphem

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_36.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `polyphem` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | ll2_cyclops_cave |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ll2_cyclops_cave](../maps/ll2_cyclops_cave.md) | – | 1 | appears later in a quest |


## Quests

- [A map of the Great Lake Laeroth](../quests/lake_map.md): stages 52, 54, 56, 57

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Polyphem. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/polyphem.json" data-npc="Polyphem" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (56 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-polyphem"></span>**`polyphem`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 57 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-57))* → [polyphem_57](#d-polyphem_57)
    - branch 2 *(if reached stage 56 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-56))* → [polyphem_105](#d-polyphem_105)
    - branch 3 *(if reached stage 55 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-55))* → [polyphem_55](#d-polyphem_55)
    - branch 4 *(if reached stage 54 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-54))* → [polyphem_54](#d-polyphem_54)
    - branch 5 *(if reached stage 52 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-52))* → [polyphem_52](#d-polyphem_52)
    - branch 6 → [polyphem_10](#d-polyphem_10)

    <span id="d-polyphem_57"></span>**`polyphem_57`** [Polyphem](../monsters/polyphem_door.md): “It's a good thing sheep are so easy to distinguish from humans.”

    - “Baaah.” *(if NOT reached stage 58 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-58))* → [polyphem_57_10](#d-polyphem_57_10)
    - “Baaah.” *(if reached stage 58 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-58))* → [polyphem_58](#d-polyphem_58)

    <span id="d-polyphem_105"></span>**`polyphem_105`** Polyphem: “[angry] YOU! Little one! WHERE ARE YOU?!”

    - Next → [polyphem_106](#d-polyphem_106)

    <span id="d-polyphem_55"></span>**`polyphem_55`** Polyphem: “Hmmm? [Polyphem opens his eye for a brief moment, but long enough for you.]”

    - “You pour the harsh soapy water directly into Polyphem's eye.” → [polyphem_100](#d-polyphem_100)

    <span id="d-polyphem_54"></span>**`polyphem_54`** Polyphem: “Hmmm? [Polyphem opens his eye for a brief moment.]”


    <span id="d-polyphem_52"></span>**`polyphem_52`** Polyphem: “Without another word, Polyphem falls onto his bed and immediately begins to snore loudly.” — **effects:** removes monsters from ll2_cyclops_cave, spawns monsters on ll2_cyclops_cave, sets stage 54 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-54)


    <span id="d-polyphem_10"></span>**`polyphem_10`** [Polyphem](../monsters/polyphem.md): “Ah. Good. Nice. Home.”

    - Next → [polyphem_11](#d-polyphem_11)

    <span id="d-polyphem_57_10"></span>**`polyphem_57_10`** Polyphem: “HA! Are you trying to sneak your way through here acting like a sheep?!”

    - “Does it really catch the eye?” → *conversation ends*

    <span id="d-polyphem_58"></span>**`polyphem_58`** Polyphem: “My favorite sheep! Your bleating sounds a bit unusual today. But I recognize you among hundreds by your wool.”

    - Next → [polyphem_58_10](#d-polyphem_58_10)

    <span id="d-polyphem_106"></span>**`polyphem_106`** Polyphem: “Calm down. Stay calm.”

    - Next → [polyphem_107](#d-polyphem_107)

    <span id="d-polyphem_100"></span>**`polyphem_100`** Polyphem: “AAAAH - MY EYE!” — **effects:** sets stage 56 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-56)

    - Next → [polyphem_101](#d-polyphem_101)

    <span id="d-polyphem_11"></span>**`polyphem_11`** Polyphem: “[sniffs] Hm. The cave smells... strange today.”

    - Next → [polyphem_12](#d-polyphem_12)

    <span id="d-polyphem_58_10"></span>**`polyphem_58_10`** Polyphem: “Hop, hop, run outside and enjoy the delicious grass.”


    <span id="d-polyphem_107"></span>**`polyphem_107`** Polyphem: “I'll see you again in a minute.”

    - Next → [polyphem_108](#d-polyphem_108)

    <span id="d-polyphem_101"></span>**`polyphem_101`** Polyphem: “MY GOOD EYE!”

    - Next → [polyphem_102](#d-polyphem_102)

    <span id="d-polyphem_12"></span>**`polyphem_12`** Polyphem: “Oh, a guest! How unusual.”

    - Next → [polyphem_13](#d-polyphem_13)

    <span id="d-polyphem_108"></span>**`polyphem_108`** Polyphem: “I CAN'T SEE ANYTHING ANYMORE!”

    - Next → [polyphem_109](#d-polyphem_109)

    <span id="d-polyphem_102"></span>**`polyphem_102`** Polyphem: “[staggers backward, flailing blindly] That burns!”

    - Next → [polyphem_103](#d-polyphem_103)

    <span id="d-polyphem_13"></span>**`polyphem_13`** Polyphem: “Don't be alarmed. I'm not alarmed by myself either.”

    - Next → [polyphem_14](#d-polyphem_14)

    <span id="d-polyphem_109"></span>**`polyphem_109`** Polyphem: “[yells outside] BROTHERS! HELP!”

    - Next → [polyphem_110](#d-polyphem_110)

    <span id="d-polyphem_103"></span>**`polyphem_103`** Polyphem: “That's cheating!”

    - Next → [polyphem_105](#d-polyphem_105)

    <span id="d-polyphem_14"></span>**`polyphem_14`** Polyphem: “[looking in the mirror] I just look dangerous.”

    - Next → [polyphem_15](#d-polyphem_15)

    <span id="d-polyphem_110"></span>**`polyphem_110`** Polyphem: “[bangs against the cave wall] HELP! I'VE BEEN BLINDED!”

    - Next → [polyphem_111](#d-polyphem_111)

    <span id="d-polyphem_15"></span>**`polyphem_15`** Polyphem: “[to the sheep] Quiet now. The visitor is looking.”

    - Next → [polyphem_16](#d-polyphem_16)

    <span id="d-polyphem_111"></span>**`polyphem_111`** [Aphem](../monsters/ll2_cyclops2.md): “[voices from outside, muffled, bored] What's wrong, Polyphem?”

    - Next → [polyphem_112](#d-polyphem_112)

    <span id="d-polyphem_16"></span>**`polyphem_16`** Polyphem: “You're in luck, little one. It's not a holiday today.”

    - Next → [polyphem_17](#d-polyphem_17)

    <span id="d-polyphem_112"></span>**`polyphem_112`** [Polyphem](../monsters/polyphem_bed.md): “NOBODY! NOBODY BLINDED ME!”

    - Next → [polyphem_113](#d-polyphem_113)

    <span id="d-polyphem_17"></span>**`polyphem_17`** Polyphem: “[grins proudly] But it will be soon.”

    - Next → [polyphem_18](#d-polyphem_18)

    <span id="d-polyphem_113"></span>**`polyphem_113`** [Dummy NPC](../monsters/none.md): “A stunned pause outside.”

    - Next → [polyphem_114](#d-polyphem_114)

    <span id="d-polyphem_18"></span>**`polyphem_18`** Polyphem: “The door is locked. You can't leave now. Don't be angry. Rules are rules.”

    - Next → [polyphem_18a](#d-polyphem_18a)

    <span id="d-polyphem_114"></span>**`polyphem_114`** [Aphem](../monsters/ll2_cyclops2.md): “... What?”

    - Next → [polyphem_115](#d-polyphem_115)

    <span id="d-polyphem_18a"></span>**`polyphem_18a`** Polyphem: “This door has no key. Keys always get lost... It only opens when I look in this mirror. Clever, clever - just like me.”

    - “So I can't just kill you to get out again.” → [polyphem_19a](#d-polyphem_19a)
    - “Are you a cyclops?” → [polyphem_19a](#d-polyphem_19a)

    <span id="d-polyphem_115"></span>**`polyphem_115`** [Polyasem](../monsters/ll2_cyclops1.md): “If nobody blinded you, why are you screaming?”

    - Next → [polyphem_116](#d-polyphem_116)

    <span id="d-polyphem_19a"></span>**`polyphem_19a`** Polyphem: “What? How you dare? Me the mightiest of all cyclops! Me Polyphem!”

    - Next → [polyphem_19b](#d-polyphem_19b)

    <span id="d-polyphem_116"></span>**`polyphem_116`** [Polyphem](../monsters/polyphem_bed.md): “BECAUSE IT HURTS!”

    - Next → [polyphem_117](#d-polyphem_117)

    <span id="d-polyphem_19b"></span>**`polyphem_19b`** Polyphem: “[beats his chest] My relatives will be coming for the next feast.”

    - Next → [polyphem_20](#d-polyphem_20)

    <span id="d-polyphem_117"></span>**`polyphem_117`** Polyphem: “[desperately] NOBODY WAS DOING IT!”

    - Next → [polyphem_118](#d-polyphem_118)

    <span id="d-polyphem_20"></span>**`polyphem_20`** Polyphem: “My hungry brothers.”

    - Next → [polyphem_21](#d-polyphem_21)

    <span id="d-polyphem_118"></span>**`polyphem_118`** Polyphem: “HE'S STANDING HERE! OR WAS STANDING! NOT ANYMORE!”

    - Next → [polyphem_119](#d-polyphem_119)

    <span id="d-polyphem_21"></span>**`polyphem_21`** Polyphem: “[leans toward the player] And I'll bring the main course.”

    - Next → [polyphem_23](#d-polyphem_23)

    <span id="d-polyphem_119"></span>**`polyphem_119`** [Aphem](../monsters/ll2_cyclops2.md): “Then cool your eye.”

    - Next → [polyphem_120](#d-polyphem_120)

    <span id="d-polyphem_23"></span>**`polyphem_23`** Polyphem: “[straightens up, smugly] You can stay until then. The sheep are nice. They don't talk much.”

    - Next → [polyphem_24](#d-polyphem_24)

    <span id="d-polyphem_120"></span>**`polyphem_120`** [Polyasem](../monsters/ll2_cyclops1.md): “And stop drinking.”

    - Next → [polyphem_121](#d-polyphem_121)

    <span id="d-polyphem_24"></span>**`polyphem_24`** Polyphem: “You should take a leaf out of their book.”

    - Next → [polyphem_25](#d-polyphem_25)

    <span id="d-polyphem_121"></span>**`polyphem_121`** [Dummy NPC](../monsters/none.md): “Laughter outside, footsteps receding.”

    - Next → [polyphem_122](#d-polyphem_122)

    <span id="d-polyphem_25"></span>**`polyphem_25`** Polyphem: “[turns to the mirror, straightens up] Me too, by the way. Nice, I mean. Very nice, in fact.”

    - Next → [polyphem_26](#d-polyphem_26)

    <span id="d-polyphem_122"></span>**`polyphem_122`** [Polyphem](../monsters/polyphem_bed.md): “COME BACK!”

    - Next → [polyphem_123](#d-polyphem_123)

    <span id="d-polyphem_26"></span>**`polyphem_26`** Polyphem: “They say I have an eye for guests.”

    - Next → [polyphem_30](#d-polyphem_30)

    <span id="d-polyphem_123"></span>**`polyphem_123`** Polyphem: “HE'S DANGEROUS!”

    - Next → [polyphem_124](#d-polyphem_124)

    <span id="d-polyphem_30"></span>**`polyphem_30`** Polyphem: “Who are you, anyway?”

    - “My name is Nobody.” → [polyphem_31](#d-polyphem_31)

    <span id="d-polyphem_124"></span>**`polyphem_124`** Polyphem: “[quieter, offended] Very dangerous indeed. But nothing against me, Polyphem!”

    - Next → [polyphem_125](#d-polyphem_125)

    <span id="d-polyphem_31"></span>**`polyphem_31`** Polyphem: “Nobody, huh? But that's not important. I just need to know what to call the dish.” — **effects:** sets stage 52 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-52)


    <span id="d-polyphem_125"></span>**`polyphem_125`** Polyphem: “Coward! Invisible coward!”

    - Next → [polyphem_127](#d-polyphem_127)

    <span id="d-polyphem_127"></span>**`polyphem_127`** Polyphem: “[sniffs] I can still smell you.”

    - Next → [polyphem_128](#d-polyphem_128)

    <span id="d-polyphem_128"></span>**`polyphem_128`** Polyphem: “Never mind. You're not getting out of here.”

    - Next → [polyphem_129](#d-polyphem_129)

    <span id="d-polyphem_129"></span>**`polyphem_129`** Polyphem: “I'll let the sheep out, then I'll find you more easily.” — **effects:** removes monsters from ll2_cyclops_cave, spawns monsters on ll2_cyclops_cave, sets stage 57 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-57), clears stage 110 of [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-110), changes map ll2_cyclops_cave, spawns monsters on mountainlake27, spawns monsters on mountainlake27, changes map mountainlake27




## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 56 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=polyphem.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=polyphem.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=polyphem.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=polyphem.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `polyphem` |
    | Spawn group | `polyphem` |
    | Loot table | – |
    | Conversation | `polyphem` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:36` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "polyphem",
     "name": "Polyphem",
     "iconID": "monsters_ld1:36",
     "monsterClass": "humanoid",
     "spawnGroup": "polyphem",
     "phraseID": "polyphem"
    }
    ```


<small>Data from v0.8.18</small>
