# ![](../assets/icons/monsters/monsters_tometik2_58.png){ .sprite } Local artist

| Stat | Value |
|---|---|
| Class | ? |
| HP | 0 |
| Max AP | 10 |
| Attack cost | 10 |
| Move cost | 10 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Found on

- [stoutford_artist](../maps/stoutford_artist.md)

## Quests

- [Unusual experiences and achievements](../quests/achievements.md): stages 150
- [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md): stages 58

??? quote "Dialogue (12 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-stoutford_artist_selector"></span>**`stoutford_artist_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 150 of [Unusual experiences and achievements](../quests/achievements.md#stage-150); NOT reached stage 58 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-58))* → [stoutford_artist_not_welcome](#d-stoutford_artist_not_welcome)
    - Next → [stoutford_artist_welcome_10](#d-stoutford_artist_welcome_10)

    <span id="d-stoutford_artist_not_welcome"></span>**`stoutford_artist_not_welcome`** Local artist: “Leave! You are not welcome here.” — **effects:** moves you to [stoutford_sw](../maps/stoutford_sw.md)


    <span id="d-stoutford_artist_welcome_10"></span>**`stoutford_artist_welcome_10`** Local artist: “Oh, a visitor? Welcome! Come, come. Sit down.”

    - “No, thanks, I have to go.” → *conversation ends*
    - “Who are you?” → [stoutford_artist_welcome_15](#d-stoutford_artist_welcome_15)
    - “Why are you up here alone?” → [stoutford_artist_welcome_16](#d-stoutford_artist_welcome_16)

    <span id="d-stoutford_artist_welcome_15"></span>**`stoutford_artist_welcome_15`** Local artist: “Just a man with a brush and a view. I spend my days painting what others overlook.”

    - “Oh, but what about...” *(if NOT reached stage 150 of [Unusual experiences and achievements](../quests/achievements.md#stage-150); reached stage 57 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-57))* → [stoutford_artist_player_killed_rubycrest_10](#d-stoutford_artist_player_killed_rubycrest_10)
    - “Well, I'm just an explorer with a weapon.” → *conversation ends*

    <span id="d-stoutford_artist_welcome_16"></span>**`stoutford_artist_welcome_16`** Local artist: “Peace and perspective. Down there, it's noise and trade. Up here, I see everything more clearly.”

    - “Are you from...” *(if NOT reached stage 150 of [Unusual experiences and achievements](../quests/achievements.md#stage-150); reached stage 57 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-57))* → [stoutford_artist_player_killed_rubycrest_10](#d-stoutford_artist_player_killed_rubycrest_10)
    - “I understand that.” → *conversation ends*

    <span id="d-stoutford_artist_player_killed_rubycrest_10"></span>**`stoutford_artist_player_killed_rubycrest_10`** Local artist: “...wait a second. Hold that thought. [while leaning in...] Please come closer. [He sniffs your hands]”

    - Next → [stoutford_artist_palyer_killed_rubycrest_20](#d-stoutford_artist_palyer_killed_rubycrest_20)

    <span id="d-stoutford_artist_palyer_killed_rubycrest_20"></span>**`stoutford_artist_palyer_killed_rubycrest_20`** Local artist: “You killed my friend!”

    - “Well, he probably deserived it. Whoever this person is.” → [stoutford_artist_palyer_killed_rubycrest_30](#d-stoutford_artist_palyer_killed_rubycrest_30)
    - “Me? Nah. Not me. [Lie] I've never killed anybody.” → [stoutford_artist_palyer_killed_rubycrest_30](#d-stoutford_artist_palyer_killed_rubycrest_30)

    <span id="d-stoutford_artist_palyer_killed_rubycrest_30"></span>**`stoutford_artist_palyer_killed_rubycrest_30`** Local artist: “Yes, yes you most certainly killed him. His scent is all over your hands.”

    - “His scent?” → [stoutford_artist_palyer_killed_rubycrest_40](#d-stoutford_artist_palyer_killed_rubycrest_40)

    <span id="d-stoutford_artist_palyer_killed_rubycrest_40"></span>**`stoutford_artist_palyer_killed_rubycrest_40`** Local artist: “You killed my best friend! You killed the only thing I have to talk to up here on these hills.”

    - “Who did I kill? You are the only person up here that I've encountered.” → [stoutford_artist_palyer_killed_rubycrest_50](#d-stoutford_artist_palyer_killed_rubycrest_50)

    <span id="d-stoutford_artist_palyer_killed_rubycrest_50"></span>**`stoutford_artist_palyer_killed_rubycrest_50`** Local artist: “You killed the unique and exotic bird that calls these hills "home". My best friend! So I am now asking you to leave. [pointing his finger towards the door.]” — **effects:** sets stage 150 of [Unusual experiences and achievements](../quests/achievements.md#stage-150)

    - “Oh, but I can stay.” *(if carry 1× [Gem of warmth](../items/gem_fire.md))* → [stoutford_artist_palyer_killed_rubycrest_gow](#d-stoutford_artist_palyer_killed_rubycrest_gow)
    - “I will stay. You are not the boss of me.” *(if NOT carry 1× [Gem of warmth](../items/gem_fire.md))* → [stoutford_artist_palyer_killed_rubycrest_60](#d-stoutford_artist_palyer_killed_rubycrest_60)

    <span id="d-stoutford_artist_palyer_killed_rubycrest_gow"></span>**`stoutford_artist_palyer_killed_rubycrest_gow`** Local artist: “There's sorrow in you...maybe even regret. Perhaps you're not the monster I feared. Very well. You may stay, but only because I sense "warmth" in your heart and we won't speak of the bird again.” — **effects:** sets stage 58 of [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md#stage-58)


    <span id="d-stoutford_artist_palyer_killed_rubycrest_60"></span>**`stoutford_artist_palyer_killed_rubycrest_60`** Local artist: “You are to leave now. [pointing his finger towards the door.]” — **effects:** moves you to [stoutford_sw](../maps/stoutford_sw.md)




## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_artist.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_artist.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_artist.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_artist.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `stoutford_artist` · Data from v0.8.18</small>
