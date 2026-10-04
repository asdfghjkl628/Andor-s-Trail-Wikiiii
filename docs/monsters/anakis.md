# ![](../assets/icons/monsters/monsters_ld1_84.png){ .sprite } Anakis

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

- [brimhaven7](../maps/brimhaven7.md)
- [brimhaven_anakis_house](../maps/brimhaven_anakis_house.md)

## Quests

- [A quick glance](../quests/quick_glance.md): stages 10, 15, 20, 40, 50, 60, 70, 75, 90

??? quote "Dialogue (17 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-anakis_start"></span>**`anakis_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 10 of [A quick glance](../quests/quick_glance.md#stage-10))* → [anakis_help_find_sister](#d-anakis_help_find_sister)
    - branch 2 *(if NOT reached stage 20 of [A quick glance](../quests/quick_glance.md#stage-20); NOT reached stage 50 of [A quick glance](../quests/quick_glance.md#stage-50))* → [anakis_meet_2nd_time](#d-anakis_meet_2nd_time)
    - branch 3 *(if NOT reached stage 50 of [A quick glance](../quests/quick_glance.md#stage-50))* → [anakis_did_you_find_my_sister](#d-anakis_did_you_find_my_sister)
    - branch 4 *(if NOT reached stage 60 of [A quick glance](../quests/quick_glance.md#stage-60); NOT reached stage 70 of [A quick glance](../quests/quick_glance.md#stage-70))* → [anakis_can_you_take_revenge](#d-anakis_can_you_take_revenge)
    - branch 5 *(if NOT reached stage 90 of [A quick glance](../quests/quick_glance.md#stage-90); latest stage of [A quick glance](../quests/quick_glance.md#stage-85) is 85)* → [anakis_thank_healing_sister](#d-anakis_thank_healing_sister)
    - branch 6 *(if NOT reached stage 90 of [A quick glance](../quests/quick_glance.md#stage-90))* → [anakis_did_you_take_revenge](#d-anakis_did_you_take_revenge)
    - branch 7 *(if reached stage 85 of [A quick glance](../quests/quick_glance.md#stage-85))* → [anakis_at_home_thanks](#d-anakis_at_home_thanks)
    - branch 8 *(if reached stage 30 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-30); NOT reached stage 85 of [A quick glance](../quests/quick_glance.md#stage-85))* → [anakis_at_home_angry](#d-anakis_at_home_angry)
    - branch 9 → [anakis_at_home_morning](#d-anakis_at_home_morning)

    <span id="d-anakis_help_find_sister"></span>**`anakis_help_find_sister`** Anakis: “Hello my name is Anakis. I hope you can you help me. Yesterday my sister Juttarka left the city to go up to this hill. She did not come home and now I am searching for her. I fear she went into that cave.” — **effects:** sets stage 10 of [A quick glance](../quests/quick_glance.md#stage-10)

    - “I found a statue that looks almost like a real woman. [Describe the statue to Anakis]” *(if reached stage 10 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-10))* → [anakis_thank_finding_sister](#d-anakis_thank_finding_sister)
    - “Yes, I will search for your sister.” *(if NOT reached stage 10 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-10))* → [anakis_agreed_find_sister](#d-anakis_agreed_find_sister)
    - “No, that's none of my business.” → [anakis_deny_help](#d-anakis_deny_help)

    <span id="d-anakis_meet_2nd_time"></span>**`anakis_meet_2nd_time`** Anakis: “Hello again. Can you please help me to find my sister Juttarka?”

    - “I found a statue looking almost like a real woman. [Describe the statue to Anakis]” *(if reached stage 10 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-10))* → [anakis_thank_finding_sister](#d-anakis_thank_finding_sister)
    - “Yes, I will search for your sister.” → [anakis_agreed_find_sister](#d-anakis_agreed_find_sister)
    - “No, that's none of my business.” → [anakis_deny_help](#d-anakis_deny_help)

    <span id="d-anakis_did_you_find_my_sister"></span>**`anakis_did_you_find_my_sister`** Anakis: “Did you find my sister?”

    - “No, not yet.” → *conversation ends*
    - “I only found a stone statue that looks almost like a real woman. [Describe the statue to Anakis]” *(if reached stage 10 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-10))* → [anakis_thank_finding_sister](#d-anakis_thank_finding_sister)

    <span id="d-anakis_can_you_take_revenge"></span>**`anakis_can_you_take_revenge`** Anakis: “Can you find the Basilisk and kill it? And maybe there is a way to help my sister. But take care that the same fate that happened to my sister does not befall you.” — **effects:** sets stage 60 of [A quick glance](../quests/quick_glance.md#stage-60)

    - “I already found the Basilisk and killed it.” *(if killed 1× [Ancient basilisk](../monsters/old_basilisk.md))* → [anakis_thank_taking_revenge](#d-anakis_thank_taking_revenge)
    - “I will take revenge, but first tell me how I might help your sister.” *(if NOT killed 1× [Ancient basilisk](../monsters/old_basilisk.md))* → [anakis_talk_to_priest](#d-anakis_talk_to_priest)
    - “I can't imagine how to help your sister but I will take revenge for her and find a way to kill that Basilisk.” *(if NOT killed 1× [Ancient basilisk](../monsters/old_basilisk.md))* → [anakis_agreed_take_revenge](#d-anakis_agreed_take_revenge)
    - “No, that's too dangerous for me.” → *conversation ends*

    <span id="d-anakis_thank_healing_sister"></span>**`anakis_thank_healing_sister`** Anakis: “Thank you so much for rescuing my sister Juttarka. She just came out of the cave and told me what you did for her. I will now go home, too.” — **effects:** sets stage 90 of [A quick glance](../quests/quick_glance.md#stage-90), spawns monsters on brimhaven_anakis_house, removes monsters from brimhaven7

    - Next → *NPC leaves*

    <span id="d-anakis_did_you_take_revenge"></span>**`anakis_did_you_take_revenge`** Anakis: “Did you kill the Basilisk?”

    - “I found the Basilisk and killed it, but I decided to take the blood for myself.” *(if killed 1× [Ancient basilisk](../monsters/old_basilisk.md); reached stage 30 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-30))* → [anakis_sad_blood_not_use_for_sister](#d-anakis_sad_blood_not_use_for_sister)
    - “I found the Basilisk and killed it.” *(if NOT reached stage 75 of [A quick glance](../quests/quick_glance.md#stage-75); killed 1× [Ancient basilisk](../monsters/old_basilisk.md))* → [anakis_thank_taking_revenge](#d-anakis_thank_taking_revenge)
    - “I found no way to help your sister, but I took revenge and killed the Basilisk.” *(if reached stage 75 of [A quick glance](../quests/quick_glance.md#stage-75); killed 1× [Ancient basilisk](../monsters/old_basilisk.md); NOT reached stage 30 of [quick_glance_hidden_found_statue (hidden flag)](../quests/quick_glance_hidden_found_statue.md#stage-30))* → [anakis_thank_taking_revenge](#d-anakis_thank_taking_revenge)
    - “No, not yet.” → *conversation ends*
    - “I will take revenge, but let me first think if it is possible to help your sister.” → [anakis_talk_to_priest](#d-anakis_talk_to_priest)

    <span id="d-anakis_at_home_thanks"></span>**`anakis_at_home_thanks`** Anakis: “Thank you so much for helping my sister Juttarka. We are all very happy.”


    <span id="d-anakis_at_home_angry"></span>**`anakis_at_home_angry`** Anakis: “Go away. I don't want to talk to people like you.”


    <span id="d-anakis_at_home_morning"></span>**`anakis_at_home_morning`** Anakis: “Thank you for trying to help my sister. I am so sad.”


    <span id="d-anakis_thank_finding_sister"></span>**`anakis_thank_finding_sister`** Anakis: “Oh no, that's her! Thank you for helping me to find out what happened to her. I think it was the Basilisk who did that to her.” — **effects:** sets stage 50 of [A quick glance](../quests/quick_glance.md#stage-50), sets stage 40 of [A quick glance](../quests/quick_glance.md#stage-40)

    - Next → [anakis_can_you_take_revenge](#d-anakis_can_you_take_revenge)

    <span id="d-anakis_agreed_find_sister"></span>**`anakis_agreed_find_sister`** Anakis: “Thank you. My sister has long hair and is wearing a long skirt. Please take care. Fangwurm the priest in western Brimhaven told us about a Basilisk in the cave that will turn you to stone when you go near him and your eyes meet its eyes.” — **effects:** sets stage 20 of [A quick glance](../quests/quick_glance.md#stage-20)


    <span id="d-anakis_deny_help"></span>**`anakis_deny_help`** Anakis: “Oh, thats's sad.” — **effects:** sets stage 15 of [A quick glance](../quests/quick_glance.md#stage-15)


    <span id="d-anakis_thank_taking_revenge"></span>**`anakis_thank_taking_revenge`** Anakis: “Thank you for taking revenge for Juttarka. I will go now and mourn for my sister.” — **effects:** sets stage 90 of [A quick glance](../quests/quick_glance.md#stage-90), spawns monsters on brimhaven_anakis_house, removes monsters from brimhaven7

    - Next → *NPC leaves*

    <span id="d-anakis_talk_to_priest"></span>**`anakis_talk_to_priest`** Anakis: “I have no idea how to help her. But maybe Fangwurm the priest in western Brimhaven has some information.” — **effects:** sets stage 70 of [A quick glance](../quests/quick_glance.md#stage-70), sets stage 75 of [A quick glance](../quests/quick_glance.md#stage-75)


    <span id="d-anakis_agreed_take_revenge"></span>**`anakis_agreed_take_revenge`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 70 of [A quick glance](../quests/quick_glance.md#stage-70)


    <span id="d-anakis_sad_blood_not_use_for_sister"></span>**`anakis_sad_blood_not_use_for_sister`** Anakis: “Oh no. Why did you not even try to help her? Now i will go and mourn for my sister.” — **effects:** sets stage 90 of [A quick glance](../quests/quick_glance.md#stage-90), spawns monsters on brimhaven_anakis_house, removes monsters from brimhaven7

    - Next → *NPC leaves*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=anakis.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=anakis.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=anakis.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=anakis.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `anakis` · Data from v0.8.18</small>
