# ![](../assets/icons/monsters/monsters_cyclops_0.png){ .sprite } Gamjee

| Stat | Value |
|---|---|
| Class | giant |
| HP | 417 |
| Max AP | 10 |
| Attack cost | 6 |
| Move cost | 10 |
| Damage | 10 to 13 |
| Attack chance | 70 |
| Block chance | 101 |
| Damage resistance | 13 |
| Critical skill | 15 |
| Critical multiplier | 2.0 |

## On hit

- **On target:** Concussion (magnitude 1, 2 rounds, 5% chance)

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gamjee's rope](../items/gamjee_rope.md) | 100% | 1 |
| [Cragbreaker](../items/cragbreaker.md) | 100% | 1 |
| [Godwin's ring](../items/godwin_ring.md) | 100% | 1 |

## Found on

- [gamjee_well_4_1](../maps/gamjee_well_4_1.md)

## Quests

- [Echoes of enchantment](../quests/echoes_of_enchantment.md): stages 8, 12, 13
- [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md): stages 3, 4, 5, 6

??? quote "Dialogue (23 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-gamjee_selector"></span>**`gamjee_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 5 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-5))* → *fight starts*
    - Next *(if NOT reached stage 5 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-5); NOT reached stage 13 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-13); NOT reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8))* → [gamjee_villagers_unknown_1](#d-gamjee_villagers_unknown_1)
    - Next *(if reached stage 13 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-13))* → [gamjee_no_business](#d-gamjee_no_business)
    - Next *(if reached stage 5 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-5))* → [gamjee_villagers_known_1](#d-gamjee_villagers_known_1)
    - Next *(if NOT reached stage 5 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-5); reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8))* → [gamjee_player_left_after_agreeing_to_help](#d-gamjee_player_left_after_agreeing_to_help)

    <span id="d-gamjee_villagers_unknown_1"></span>**`gamjee_villagers_unknown_1`** Gamjee: “Human, why you come here? Gamjee no hurt you if you leave now.”

    - “I'm just exploring. Who are you, and why are you here?” → [gamjee_villagers_unknown_2](#d-gamjee_villagers_unknown_2)

    <span id="d-gamjee_no_business"></span>**`gamjee_no_business`** Gamjee: “Why you still here? Leave now.”


    <span id="d-gamjee_villagers_known_1"></span>**`gamjee_villagers_known_1`** Gamjee: “Human, why you come here? Gamjee no hurt you if you leave now.”

    - “I've found the people you captured. You need to let them go.” *(if NOT reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8))* → [gamjee_villagers_known_2](#d-gamjee_villagers_known_2)
    - “I want to help you and the villagers.” *(if reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8))* → [gamjee_compromise_1](#d-gamjee_compromise_1)

    <span id="d-gamjee_player_left_after_agreeing_to_help"></span>**`gamjee_player_left_after_agreeing_to_help`** Gamjee: “Human, why you leave? Rude.”

    - “I want to help you and the villagers.” → [gamjee_compromise_1](#d-gamjee_compromise_1)

    <span id="d-gamjee_villagers_unknown_2"></span>**`gamjee_villagers_unknown_2`** Gamjee: “Gamjee guard well. Humans come, take Gamjee's well, build village. They no ask. They just take. Gamjee scared. Need protect well. You help Gamjee?”

    - “You're afraid they'll come back and take more?” → [gamjee_villagers_unknown_peace](#d-gamjee_villagers_unknown_peace)
    - “I thought I heard somes voices earlier. Have you hurt anybody recently?” → [gamjee_villagers_unknown_3](#d-gamjee_villagers_unknown_3)

    <span id="d-gamjee_villagers_known_2"></span>**`gamjee_villagers_known_2`** Gamjee: “Captured? No, no! Gamjee protect them! Humans take Gamjee's well, build village. They no ask. They just take. Gamjee keep them safe here. You see, they not hurt.”

    - “Keeping them in a pit isn't protecting them. It's imprisoning them.” → [gamjee_villagers_known_3](#d-gamjee_villagers_known_3)

    <span id="d-gamjee_compromise_1"></span>**`gamjee_compromise_1`** Gamjee: “You help Gamjee? Humans no hurt?”

    - “I'll do what I can. Let's talk to the villagers.” *(if NOT reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8))* → [gamjee_compromise_2](#d-gamjee_compromise_2)
    - “I'll do what I can. Let's talk to the villagers.” *(if NOT reached stage 6 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-6); reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8))* → [gamjee_compromise_2a](#d-gamjee_compromise_2a)
    - “I'll do what I can. Let's talk to the villagers.” *(if reached stage 6 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-6))* → [gamjee_compromise_2](#d-gamjee_compromise_2)

    <span id="d-gamjee_villagers_unknown_peace"></span>**`gamjee_villagers_unknown_peace`** Gamjee: “Yes! Humans take all if no stop. Gamjee alone. If you help, tell humans Gamjee no bad. Maybe they listen. Maybe they share well, no fight. You help, no need for hurt.”

    - “I understand. I'll help you find a peaceful solution.” → [gamjee_compromise_1](#d-gamjee_compromise_1)

    <span id="d-gamjee_villagers_unknown_3"></span>**`gamjee_villagers_unknown_3`** Gamjee: “Me alone.”

    - “Really? I'm not so sure about that, but I'll see about that.” → *conversation ends*
    - “I don't believe you! Prove it.” → [gamjee_villagers_unknown_attack](#d-gamjee_villagers_unknown_attack)

    <span id="d-gamjee_villagers_known_3"></span>**`gamjee_villagers_known_3`** Gamjee: “No! Listen! Humans come, take Gamjee's well, leave Gamjee with nothing. Gamjee scared. If Gamjee let them go, they come back, take well again. They no understand, well is life for Gamjee. Please, you help. Tell humans Gamjee no bad. Maybe…”

    - “I see. You acted out of fear and desperation. I'll help you find a peaceful solution.” → [gamjee_compromise_1](#d-gamjee_compromise_1)
    - “It's time to make me righteous!” → [gamjee_villagers_known_fight](#d-gamjee_villagers_known_fight)

    <span id="d-gamjee_compromise_2"></span>**`gamjee_compromise_2`** Gamjee: “Let Gamjee call human with magic water.” — **effects:** removes monsters from gamjee_well_jail_cells, spawns monsters on gamjee_well_4_1, sets stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8)

    - “OK. Now that I have you two together, let's talk about how you guys can reach a compromise and share the well water.” → [gamjee_compromise_4](#d-gamjee_compromise_4)

    <span id="d-gamjee_compromise_2a"></span>**`gamjee_compromise_2a`** Gamjee: “OK.”

    - “Let's talk about how you guys can reach a compromise and share the well water.” → [gamjee_compromise_4](#d-gamjee_compromise_4)

    <span id="d-gamjee_villagers_unknown_attack"></span>**`gamjee_villagers_unknown_attack`** Gamjee: “No! Gamjee protect! If humans come back, they take all. Gamjee alone, scared.” — **effects:** sets stage 3 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-3), sets stage 5 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-5)

    - “I don't believe you! I can't take that risk. This ends now” → *fight starts*

    <span id="d-gamjee_villagers_known_fight"></span>**`gamjee_villagers_known_fight`** Gamjee: “No! Gamjee protect! If humans come back, they take all. Gamjee alone, scared.” — **effects:** sets stage 4 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-4), sets stage 5 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-5)

    - “This ends now for you!” → *fight starts*

    <span id="d-gamjee_compromise_4"></span>**`gamjee_compromise_4`** [Percival](../monsters/troll_hollow_percival.md): “Why should we trust him? He's been keeping us captive!”

    - “Gamjee is afraid you'll take the well. He wants to protect it.” → [gamjee_compromise_5](#d-gamjee_compromise_5)

    <span id="d-gamjee_compromise_5"></span>**`gamjee_compromise_5`** [Percival](../monsters/troll_hollow_percival.md): “And what about us? We need water too.”

    - Next → [gamjee_compromise_6](#d-gamjee_compromise_6)

    <span id="d-gamjee_compromise_6"></span>**`gamjee_compromise_6`** [Gamjee](../monsters/gamjee_hidden.md): “Gamjee not want hurt. Humans need water. Gamjee need too.”

    - “Is there a way you can share the well? Maybe take turns using it?” → [gamjee_compromise_7](#d-gamjee_compromise_7)

    <span id="d-gamjee_compromise_7"></span>**`gamjee_compromise_7`** [Percival](../monsters/troll_hollow_percival.md): “We can agree to that. As long as Gamjee doesn't threaten us anymore.”

    - Next → [gamjee_compromise_8](#d-gamjee_compromise_8)

    <span id="d-gamjee_compromise_8"></span>**`gamjee_compromise_8`** [Gamjee](../monsters/gamjee_hidden.md): “Gamjee promise. No hurt. Protect well. Humans share. No fight.”

    - “Alright. Let's make this work.” *(if NOT reached stage 12 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-12))* → [gamjee_compromise_9](#d-gamjee_compromise_9)
    - “So our business here is done?” *(if reached stage 12 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-12))* → [gamjee_compromise_10_no_ac](#d-gamjee_compromise_10_no_ac)

    <span id="d-gamjee_compromise_9"></span>**`gamjee_compromise_9`** Gamjee: “You human, go back village now.” — **effects:** removes monsters from gamjee_well_4_1, sets stage 6 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-6), sets stage 12 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-12), spawns monsters on wexlow_village

    - “So our business here is done?” *(if NOT reached stage 2 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-2))* → [gamjee_compromise_10_no_ac](#d-gamjee_compromise_10_no_ac)
    - “So our business here is done?” *(if reached stage 2 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-2))* → [gamjee_compromise_10_oc](#d-gamjee_compromise_10_oc)

    <span id="d-gamjee_compromise_10_no_ac"></span>**`gamjee_compromise_10_no_ac`** Gamjee: “Not same. Take rope, use to free others from pit.” — **effects:** gives 1× [Gamjee's rope](../items/gamjee_rope.md), sets stage 13 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-13)


    <span id="d-gamjee_compromise_10_oc"></span>**`gamjee_compromise_10_oc`** Gamjee: “take shiny thing back.” — **effects:** gives 1× [Oegyth crystal](../items/oegyth.md)

    - Next → [gamjee_compromise_10_no_ac](#d-gamjee_compromise_10_no_ac)



## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 23 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gamjee.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gamjee.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gamjee.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gamjee.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `gamjee` · Data from v0.8.18</small>
