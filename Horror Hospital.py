#map modeled after Brookhaven Hospital Map(1F) from Silent Hill 2

import sys




def title_screen():
 input("\nWelcome to Hospital Horrors! Press enter to continue.")
 input("\nmove left: a\nmove right:d\nmove up:w\nmove down:s\npick up object:p\nopen doors:i")
 input("\nLet's begin!")
 wake_up()


def wake_up():
    input("\nYou wake up in your hospital bed to the sound of a blood curdling scream down the hallway. There is darkness all around you.")
    input("\nThe dead silence that follows makes your heart beat quicker.")
    input("\nYou don't know how you ended up in this dark hospital all alone. All you know is that you need to escape!")
    input("\nYou get up from the bed, still not being able to see a thing.")
    input("\nPress 'w,a,s,d' to explore room and 'p' to pick up objects.")
    explore=""
    while explore!=("a","s","d","w","g","h","p"):
        explore=input("\nPress w-forward,a-left,s-turn around,d-right to explore the room. Press i to open doors.\n")
        if explore=="s":
            print("\nYou look at the bed. Although it looks comfy, now is probably not the best time for a nap.")
        if explore=="a":
            flash=input("\nYou see a black cylinder-like object on the grimy hospital floor.\nPress p to pick it up?")
            if flash=="p":
                print("\nYou pick up the object and discover that it is a flash light. You turn it on.")
                flash_light()
            else:
                print("\nYou chose to not pick up the object.")
        if explore=="d":
            print("\nYou see a blank wall in front of you.")
        if explore=="w":
            print("\nYou see the vague outlines of a door in front of you. Although you want to get out as soon as you can,\nit's probably better "
                  "not to stumble blindly down a dark hallway where something threatening might be lurking.")


def flash_light():
    input("\nThe flash light illuminates the tiny hospital room.")
    light_explore=""
    while light_explore!=("a","s","d","w","g","h","p"):
        light_explore=input("\nPress w-forward,a-left,s-turn around,d-right to explore the room. Press i to open doors.\n")
        if light_explore=="s":
            print("\nYou look at the bed. There is a thin layer of dirt on the white sheets.")
        elif light_explore=="a":
            input("\nSomeone has written a threatening message in blood on the wall:'Don't bother, it's too late.'")
        elif light_explore=="d":
            hole=input("\nYou see tacky wallpaper with bouquets of roses printed all over it. There is a small hole in the wall.\nWould you like to look through it? Press i to look.")
            if hole=="i":
                input("\nYou look through the hole.")
                input("\nAt first, you see nothing, but then you see what looks like a large, unraveled spiderweb strewn all around the room from floor to ceiling.")
                input("\nLarge cotton cocoons hang from the ceiling.")
                input("\nLong spindly legs jut out from something sitting in the corner of the room.")
                input("\nYou can't see what it is from the tiny hole.")
            else:
                print("\nYou decide not to look through the hole. Who knows what horrible thing you'd see?")
        elif light_explore=="w":
            exit=input("\nWould you like to exit into the hallway? Press w again to confirm.")
            if exit=="w":
                input("\nYou open the door, stepping out into the dark corridor.")
                explore_hallway()
            else:
                print("\nYou decide to stay in the room for a bit. Probably safer in here anyways.")


def explore_hallway():
    input("\nYou turn and face the long, dark hallway.")
    input("\nYou listen for any noise, and hear a heart-stopping crunching sound to your left.")
    corridor_explore = ""
    while corridor_explore != ("a", "s", "d", "w", "g", "h", "p"):
        corridor_explore=input("\nPress w-forward,a-left,s-turn around,d-right to explore hallway. Press i to open doors.\n")
        if corridor_explore=="w":
            input("\nYou walk down the hallway. Stopping to examine your surroundings, you notice a door to your right that says 'C3' on it.")
            input("\nYou can still hear something chewing on flesh behind you. It doesn't seem to have noticed you yet.")
            hallway_second_block()
        if corridor_explore=="a":
            input("\nYou look to your left and see what looks like a giant blob-shaped monster with human arms for legs chewing on some unfortunate victim in a hospital gown.")
            first_game_over=input("\nWould you like to get a closer look? Press a again to go left.")
            if first_game_over=="a":
                input("\nA twisted fascination draws you closer to the creature.")
                input("\nYou see four tendril like appendages sticking out from the creature's body, each with its own human-like mouth tearing into the victim's flesh.")
                input("\nYou hear a loud crunch under your foot. Looking down, you see the now broken syringe on the ground.")
                input("\nThe creature stops eating, turning toward you with it's four mouths.")
                input("\nThe monster lets out an ear-piercing scream as it rushes at you.")
                input("\nThe last thing you hear is the creature's scream as it tears your flesh from your bones.")
                you_died_blob_monster_one()
            else:
                input("\nYou decide it's best not to get any closer. The monster seems preoccupied with its meal. As long as you are quiet, it will not notice you.")
                input("\nYou face the never-ending darkness of the hallway ahead again.")

        if corridor_explore=="d":
            input("\nYou look at the door to the room you just came out of, the label 'C4' printed on a tiny plaque.")
            go_back=input("\nDo you want to go back inside? Press i for yes and any other key for no.")
            if go_back=="i":
                input("\nYou step inside the small hospital room again, closing the door behind you.")
                flash_light()
            else:
                print("\nYou decide to not go back into the room. You face the long hallway again.")
                continue
        if corridor_explore == "s":
            input("\nYou turn around and notice a door labeled 'Outdoor Pool Area.' To your right, there is a blob-like monster with human arms for legs feasting on a corpse.")
            down_the_hallway_one()


def down_the_hallway_one():
    corridor_explore = ""
    open_again = ""
    open_once_more=""
    while corridor_explore != ("a", "s", "d", "w", "g", "h", "p"):
        corridor_explore=input("\nPress w-forward,a-left,s-turn around,d-right to explore hallway. Press i to open doors.\n")
        if corridor_explore == "w":
            input("\nThere is a door in front of you labeled 'Outdoor Pool Area.'")
            down_the_hallway_one()
        if corridor_explore=="s":
            explore_hallway()
        if corridor_explore=="d":
            input("\nYou look to your right and see what looks like a giant blob-shaped monster with human arms for legs chewing on some unfortunate victim in a hospital gown.")
            first_game_over = input("\nWould you like to get a closer look? Press d again to go right.")
            if first_game_over == "d":
                input("\nA twisted fascination draws you closer to the creature.")
                input("\nYou see four tendril like appendages sticking out from the creature's body, each with its own human-like mouth tearing into the victim's flesh.")
                input("\nYou hear a loud crunch under your foot. Looking down, you see the now broken syringe on the ground.")
                input("\nThe creature stops eating, turning toward you with it's four mouths.")
                input("\nThe monster lets out an ear-piercing scream as it rushes at you.")
                input("\nThe last thing you hear is the creature's scream as it tears your flesh from your bones.")
                you_died_blob_monster_one()
            else:
                input("\nYou decide it's best not to get any closer. The monster seems preoccupied with its meal. As long as you are quiet, it will not notice you.")
                input("\nYou face the door leading to the pool area again.")
                continue
        if corridor_explore=="a":
            input("\nYou look at the door to the room you just came out of, the label 'C4' printed on a tiny plaque.")
            go_back_two = input("\nDo you want to go back inside? Press i for yes and any other key for no.")
            if go_back_two == "i":
                input("\nYou step inside the small hospital room again, closing the door behind you.")
                flash_light()
            else:
                print("\nYou decide not go back into the room. You face the 'outdoor pool area' door again.")
                continue

        if corridor_explore=="i":
          input("\nYou try opening the door but it is locked. The door makes a loud creaking sound as you try to open it.")
          input("\nThe creature doesn't seem to notice, but it's probably best not to push your luck by trying to open it again.")
        while open_again != ("a", "s", "d", "w", "g", "h", "p"):
          open_again = input("\nPress i to keep trying to open the door and any other key to quit.\n")
          if open_again == "i":
            open_again = input("\nYou try to open the door again. A much louder creak echoes in the hallway. The creature stops eating, listening for any noise.")
            open_once_more = input("\nPress i to keep trying to open the door and any other key to quit.\n")
          if open_once_more=="i":
                input("\nYou try one more time to open the door despite already knowing that it's locked.")
                input("\nThe four-mouthed creature screams as it hears you, rushing at you.")
                input("\nThe last thing you hear is its horrid scream as it rips out your entrails.")
                you_died_blob_monster_one()
          else:
            input("\nYou decide to not open the door.")
            down_the_hallway_one()


def hallway_second_block():
    corridor_explore=""
    while corridor_explore != ("a", "s", "d", "w", "g", "h", "p"):
        corridor_explore=input("\nPress w-forward,a-left,s-turn around,d-right to explore hallway. Press i to open doors.\n")
        if corridor_explore=="a":
            input("\nYou shine your flashlight against the dirty,blood-stained wall to your left.")
            input("\nThere is a message on the wall written in blood: ")
            input("\n'You can't escape from its web. Don't go in there.'")
            continue
        if corridor_explore=="d":
            input("\nThe door knob on the door to your right is sticky to the touch.")
            input("\nYou feel something sticky underneath your feet.")
            input("\nYou shine your flashlight down and notice a sticky substance coming out from this room.")
            spider_game_over=input("\nWould you like to enter this room? Press i for yes and any other key for no.")
            if spider_game_over=="i":
                input("\nYou enter the room, accidentally dropping your flashlight as you walk right into a thick string of web.")
                input("\nYou kneel to pick it up, only to find that your knees are now stuck to the floor.")
                input("\nYou struggle in vain until you hear something stir behind you.")
                input("\nYou turn around and see an eight-legged creature.")
                input("\nIts entire body is made up of human faces, each one contorted in a unique expression of pain.")
                input("\nThe creature pushes the door shut, killing your last hope of freedom.")
                input("\nOnly darkness now.")
                you_died_spider_monster_one()
            else:
                input("\nYou decide not to go into the room. Seems like a pretty bad idea.")
                continue
        if corridor_explore=="s":
            walk_back=input("\nWould you like to turn back around and walk towards the 'Outdoor Pool Area' door? Press s again to confirm.")
            if walk_back=="s":
                input("\nYou turn around and walk back towards the 'Outdoor Pool Area' door. The blob monster is still chewing happily on its meal to your right.")
                down_the_hallway_one()
            else:
                input("\nYou decide to keep facing forward.")
                continue
        if corridor_explore=="w":
            hallway_third_block_one()


def hallway_third_block_one():
    input("\nYou walk further down the hallway until you find yourself accidentally stepping on broken glass.")
    input("\nYou stop hearing the blob monster's loud chewing. It's only a matter of seconds before it turns the corner and sees you.")
    corridor_explore = ""
    while corridor_explore != ("a", "s", "d", "w", "g", "h", "p"):
     corridor_explore = input("\nPress w-forward,a-left,s-turn around,d-right to explore hallway. Press i to open doors.\n")
     if corridor_explore=="w":
         input("\nNot even looking back, you run as fast as you can until you see two doors, one to your left and one to your right.")
         hallway_fourth_block_one()
     if corridor_explore=="d":
            input("\nThere is a door to your right labeled 'C2.'")
            input("\nYou need a number code to open it.")
     if corridor_explore=="a":
         input("\nThere is a blank wall to your left. Nothing important.")
     if corridor_explore=="s":
         hallway_third_block_backwards_one()


def hallway_third_block_backwards_one():
         input("\nYou turn around and see a monster now looking at you with it's two big, antennae eyes.")
         input("\nWith blood still dripping from its four mouths, the creature screams as it runs at you.")
         input("\nDo you want to press s to turn back around and run for your life or do you want to stay where you are?")
         corridor_explore=""
         while corridor_explore != ("a", "s", "d", "w", "g", "h", "p"):
          corridor_explore = input("\nPress w-forward,a-left,s-turn around,d-right to explore hallway. Press i to open doors.\n")
          if corridor_explore=="s":
                input("\nYou turn around and run as fast as you can until you see two doors, one to your left and one to your right.")
                hallway_fourth_block_one()
          if corridor_explore=="a":
                input("\nYou look at the door labeled 'C2.'")
                input("\nIt requires a number code to open.")
                input("\nThe monster continues to stumble towards you.")
                input("\nYou could try opening it with 'i' using brute force, but that's probably not a great idea.")
                open_again=input("\nPress w-forward,a-left,s-turn around,d-right to explore hallway. Press i to open doors.\n")
                if open_again=="i":
                    input("\nYou try opening the door with all of your strength, but it doesn't budge.")
                    input("\nYou don't have much time to feel sad about this though, as the monster uses its brute force to knock you down and tear your flesh.")
                    you_died_blob_monster_two()
                else:
                    input("\nYou decide to not try and open the door.")
                    continue
          if corridor_explore=="w":
              input("\nInstead of running, you think that maybe charging at the monster is the most logical choice.")
              input("\nDespite having no weapons or anyway to defend yourself, maybe you can beat it through will power alone!")
              are_you_kidding=input("\nWould you like to charge at the monster? Press 'w' to confirm and any other key for no.")
              if are_you_kidding=="w":
                     input("\nYou run heroically towards the terrible screaming monstrosity.")
                     input("\nDespite being a strong candidate for the Darwin award, no one can say you didn't die an honorable, gruesome death.")
                     you_died_blob_monster_two()
              else:
                     input("\nYou realize that this would basically be suicide, and decide to turn around and run anyway from this monster.")
                     input("\nYou run as fast as you can until you see two doors, one to your left and one to your right.")
                     hallway_fourth_block_one()
          if corridor_explore=="d":
                input("\nInstead of running, you decide to examine the blank wall to your right.")
                input("\nThe monster is getting closer.")
                see_again=""
                while see_again!=("a","s","d","w"):
                    see_again = input("\nPress w-forward,a-left,s-turn around,d-right to explore hallway. Press i to open doors.\n")
                    if see_again=="d":
                      see_again=input("\nIt looks terribly dirty, someone should clean it.")
                      input("\nProbably won't be you though considering that the monster has just caught up to you.")
                      input("\nThe last thing you see is your blood spattered all over the wall.")
                      you_died_blob_monster_two()
                    else:
                     input("You decide to stop looking at the wall. Probably for the best considering the blood-thirsty monster in front of you.")
                     hallway_third_block_backwards_one()



def hallway_fourth_block_one():
    corridor_explore=""
    input("\nYou feel yourself sweat as you look back and forth between each door.")
    while corridor_explore != ("a", "s", "d", "w", "g", "h", "p"):
        corridor_explore = input("\nPress w-forward,a-left,s-turn around,d-right to explore hallway. Press i to open doors.\n")
        if corridor_explore=="w":
            input("\nThere seems to be a makeshift barricade up ahead made up mostly of chairs and over turn hospital beds.")
            input("\nAre you sure that you want to run to this dead end?")
            dead_end=input("\nPress w to run to the end of the hallway and any other key for no.")
            if dead_end=="w":
                input("\nYou run to the end of the hallway.")
                input("\nDespite looking hastily thrown together, the barricade is too strong for you to move.")
                input("\nYou see your blood splatter all over the barricade as the monster catches up to you, screaming with two of its mouths while feasting on your flesh with the other two.")
                you_died_blob_monster_three()
            else:
                input("\nYou decide not to run towards the barricade.")
                continue
        if corridor_explore == "a":
            input("\nThere is a door to your left.")
            save_yourself=input("\nWould you like to press i to open it?")
            if save_yourself=="i":
              input("\nTo your relief, it opens!")
              input("\nYou rush inside, slamming the door behind you.")
              input("\nThe monster continues to scream in the hallway as you shine your flashlight on the dark room.")
              examination_room()
            else:
                input("\nYou decide not to open the door.")
                continue
        if corridor_explore=="s":
            input("\nThe monster is almost right behind you. Are you sure you want to turn around?")
            turn_around=input("\nPress s to turn around and any other key for no.")
            if turn_around=="s":
                input("\nYou decide to turn around.")
                input("\nThe monster raises four of its twelve human arm legs, pushing you down to the ground.")
                input("\nIts four mouths rip you to pieces as the world goes dark.")
                you_died_blob_monster_three()
            else:
                input("\nYou decide not to turn around. Probably a smart move.")
                continue
        if corridor_explore=="d":
            input("\nThere is a door to your right.")
            does_not_open=input("\nWould you like to press i to open it?")
            if does_not_open=="i":
              input("\nUnfortunately, the door does not budge.")
              input("\nDo you want to try and open the door again?")
              still_locked = input("\nPress i for yes and any other key for no.")
              if still_locked == "i":
                    input("\nYou try opening the locked door again but it is still locked.")
                    input("\nThe monster's ear-piercing scream is the last thing you hear as it tears at your flesh.")
                    you_died_blob_monster_three()
              else:
                    input("\nYou decide to not try and open the door again. What would be the point?")
                    continue
            else:
                input("\nYou decide to not try and open the door.")
                continue





def examination_room():
    input("\nThe room seems to have been stripped bare, except for one hospital bed in front of you.")
    input("\nBlack mold is growing out of every corner.")
    input("\nYou shine your flashlight all around the tiny room.")
    input("\nAlthough you don't see anything, you swear you hear something breathing to your right.")
    input("\nThe blob monster outside has stopped screaming, though you can still hear its monstrous footsteps stomping back and forth in the hallway.")
    exam_explore=""
    while exam_explore != ("a", "s", "d", "w", "g", "h", "p"):
        exam_explore = input("\nPress w-forward,a-left,s-turn around,d-right to explore examination room. Press i to open doors.\n")
        if exam_explore=="s":
            input("\nYou can still hear the footsteps of the blob monster pacing right outside the door.")
            get_killed=input("\nWould you like to go outside anyways? Press i to go out into the hallway and any other key not to.")
            if get_killed=="i":
                input("\nYou go out into the hallway.")
                input("\nAfter just five minutes, the horrendous creature is enjoying the easiest meal it has ever had to catch.")
                you_died_blob_monster_four()
            else:
                input("\nYou decide not to head into the hallway. Why risk getting eaten?")
                input("\nYou face the hospital room again.")
                continue
        if exam_explore=="a":
            input("\nYou look to the left of the room.")
            input("\nThere is a message written on the wall:")
            input("\n'It wants to add you to its collection.'")
        if exam_explore=="d":
            input("\nYou look to the right of the room.")
            input("\nThe blank wall before you seems normal at first.")
            input("\nBut as you continue to look at it, the wall seems to be pulsing, each pulse perfectly timed with the mysterious sound of breathing reverberating in the room.")
        if exam_explore=="w":
            input("\nThere is a hospital bed right in front of you with a particularly bad odor.")
            remove_sheets=input("\nPress p to move aside the sheets and any other key not to.")
            if remove_sheets=="p":
                input("\nYou toss aside the sheets and see a large puddle of water in the center of the bed.")
                input("\nIn the middle of the water, there is a sheet of paper on top of what looks like a pile of tar.")
                pick_up=input("\nWould you like to pick up the sheet of paper? Press p for yes and any other key for no.")
                if pick_up=="p":
                    input("\nYou try to tug the piece of paper off of the tar-covered hill.")
                    input("\nIt doesn't give. The breathing in the right corner grows more labored and loud.")
                    once_more=input("\nOne more pull might do the trick. Press p to try again and any other key to give up.")
                    if once_more=="p":
                        input("\nWith one more gentle tug, you are able to pull the sheet of paper free.")
                        input("\nYou hear a sharp inhale reverberate around the room as the ground shakes under your feet.")
                        input("\nA dark ooze drips out of the top right corner of the room.")
                        input("\nThen, what looks like a pale hand protrudes from the slime.")
                        input("\nMore arms join it, until there is a giant cluster of hands coming out of the corner of the room.")
                        input("\nThey all reach out for you with their elongated arms.")
                        slime_monster()
                    else:
                        input("\nYou decide not to try again. You put the sheet back on the bed, hoping to mitigate the odor.")
                        continue

                else:
                    input("\nYou decide not to pick up the piece of paper. You put the sheet back on the bed to mitigate the odor.")
                    continue
            else:
                input("\nYou decide not to tug at the foul smelling sheets. Something probably died under there.")
                continue


def slime_monster():
    input("\nThe hands continue to move towards you, some grabbing at the air, some the ceiling, and others at the floor.")
    input("\nIt's only a matter of time before they grab you.")
    slime_explore = ""
    while slime_explore != ("a", "s", "d", "w", "g", "h", "i","p"):
        slime_explore = input("\nPress w-forward,a-left,s-turn around,d-right to explore examination room. Press i to open doors.\n")
        if slime_explore == "s":
            input("\nYou turn around and see the door leading out to the hallway.")
            input("\nIt might be safer out there than it is in here.")
            escape_slime=input("\nWould you like to escape from this room? Press i to open the door and any other key to stay in the room.")
            if escape_slime=="i":
                input("\nYou push open the door, slamming it behind you as you step out into the dark hallway.")
                hallway_fourth_block_two()
            else:
                input("\nYou decide to stay in the room for some reason.")
                input("\nThe monster grabs your ankles, dragging you to its disgusting, slime-filled corner.")
                input("\nYour desperate, outstretched hands are the last part of you to disappear into the black goo.")
                you_died_slime_monster()
        if slime_explore=="a":
            input("\nYou look to your left and see a message written on the wall: ")
            input("\nIt wants to add you to its collection.")
            input("\nNow knowing what 'it' is, maybe it's best if you try to get out of this room.")
            input("\nYou remember that there is a door behind you.")
            okay_fine=input("\nWould you like to keep staring at the wall though? Press a for yes and any other key for no.")
            if okay_fine=="a":
                input("\nYou continue to stare at the wall.")
                input("\nThe monster grabs your ankles, dragging you to its disgusting, slime-filled corner.")
                input("\nYour desperate, outstretched hands are the last part of you to disappear into the black goo.")
                you_died_slime_monster()
            else:
                input("\nYou decide to stop staring at the wall.")
                continue
        if slime_explore=="d":
            input("\nYou shine your flashlight to your right.")
            input("\nA large grey, human-like eye stares back at you, its black pupil shrinking under your flashlight's harsh light.")
            input("\nThe creature sharply inhales as the hands continue to feel around every inch of the room.")
            input("\nYou remember that there is a door behind you.")
            why_though=input("\nWould you like to keep staring at the weird eye in front of you instead of escaping? Press d for yes and any other key for no.")
            if why_though=="d":
                input("\nThe monster lets out a long exhale as you feel the hands grip your ankles.")
                input("\nYour desperate, outstretched hands are the last part of you to disappear into the black goo.")
                you_died_slime_monster()
            else:
                input("\nYou decide to stop staring at the giant eye.")
                continue
        if slime_explore=="w":
            input("\nThe monster's hands continue to emerge from the corner of the room.")
            input("\nAre you sure that you want to walk towards the monster?")
            kill_yourself=input("\nPress w to end it all and any other key to keep going.")
            if kill_yourself=="w":
                input("\nYou walk towards the monster, figuring what's the point?")
                input("\nOpening the door right behind you is just too much effort.")
                input("\nThe monster grabs your ankles, dragging you to its disgusting, slime-filled corner.")
                input("\nYour desperate, outstretched hands are the last part of you to disappear into the black goo.")
                you_died_slime_monster()
            else:
                input("\nYou decide to keep braving this nightmare.")
                input("\nGood for you!")
                input("\nEscaping shouldn't be too hard. After all, there is an unlocked door right behind you.")
                continue



def hallway_fourth_block_two():
    input("\nYou face the barricade, made up of hospital beds and wheel chairs, at the end of the hallway.")
    input("\nYou hear a loud scratching sound behind you.")
    explore=""
    while explore != ("a", "s", "d", "w", "g", "h", "i","p"):
        explore = input("\nPress w-forward,a-left,s-turn around,d-right to explore hallway. Press i to open doors.\n")
        if explore == "s":
            input("\nYou turn around and see the blob monster scratching at a door towards the end of the hallway.")
            input("\nIt seems completely preoccupied with whatever is behind that door.")
            input("\nWould you like to walk further down the hallway?")
            keep_going=input("\nPress s again for yes and any other key for no.")
            if keep_going=="s":
                input("\nYou walk further down the hallway.")
                hallway_third_block_backwards_two()
            else:
                input("\nYou decide to stay where you are, facing the barricade again.")
                continue
        if explore=="w":
            input("\nThe barricade in front of you is insurmountable.")
            input("\nYou hear the faint sound of pain-filled moaning mixed with choked laughter coming from the other side.")
            input("\nAlthough there seems to be nothing there, you feel this new creature's presence.")
            input("\nIt's probably for the best that you'll never know what horrid thing is making that sound.")
        if explore=="a":
            input("\nYou look at the door to the examination room.")
            input("\nBlack tar oozes out the bottom of the door.")
            meh=input("\nWould you like to go back into the room with the tar monster? Press i for yes and any other key for no.")
            if meh=="i":
                input("\nYou open the door.")
                input("\nBefore you can even take one step inside, the monster grabs you, shutting the door behind you.")
                you_died_slime_monster_two()
            else:
                input("\nYou decide not to open the door with the terrifying monster you just escaped from behind it.")
                continue
        if explore=="d":
            input("\nYou look to your right and see a door.")
            input("\nThere is a small message written on the door.")
            input("\n'Some guy died in here. It should have been you.'")
            it_wont_open=input("\nDo you want to try and open it? Press i for yes and any other key for no.")
            if it_wont_open=="i":
                input("\nYou try opening the door.")
                input("\nIt doesn't budge.")
            else:
                input("\nYou decide to not open the door.")


def hallway_third_block_backwards_two():
    input("\nYou accidentally step on the same glass as before, but the monster doesn't seem to notice.")
    input("\nWhatever is behind that door has its complete attention as it scrapes at the door with five of its human-like hands.")
    explore_third=""
    while explore_third != ("a", "s", "d", "w", "g", "h", "i","p"):
        explore_third = input("\nPress w-forward,a-left,s-turn around,d-right to explore hallway. Press i to open doors.\n")
        if explore_third=="s":
            input("\nWould you like to turn back around and walk back towards the barricade?")
            walk_back=input("\nPress s again for yes and any other key for no.")
            if walk_back=="s":
                input("\nYou decide to turn around and walk back.")
                hallway_fourth_block_two()
            else:
                input("\nYou decide to not head back towards the barricade.")
                continue
        if explore_third=="w":
            input("\nThe blob monster is blocking off the rest of the hallway.")
            input("\nYou could try to slip past it, but then it would probably notice you.")
            input("\nWould you like to try and sneak past the blob monster?")
            keep_going=input("\nPress w again for yes and any other key for no.")
            if keep_going=="w":
                input("\nYou try to side-step past the monster.")
                input("\nYou accidentally brush by one of its twelve arms.")
                input("\nThe monster turns to face you with its four, tendril-like mouths.")
                input("\nThe last thing you hear is its horrible, high-pitched scream.")
                you_died_blob_monster_five()
            else:
                input("\nYou decide to not slip past the monster.")
                continue
        if explore_third=="a":
            input("\nYou notice a door to your left with the label 'C2' on it.")
            input("\nIt requires a number code to open.")
            input("\nRemembering the piece of paper you got from the other room, you take it out of your pocket.")
            input("\nThere is a number code written on it that may open this door.")
            input("\nThe blob monster lets out a frustrated groan as it continues to scratch at the door.")
            key_door=input("\nWould you like to open the door? Press i for yes and any other key for no.")
            if key_door=="i":
                input("\nYou punch the code into the key pad.")
                input("\nThe door unlocks with a loud beep that makes your heart stop.")
                input("\nThe blob monster stops pawing at the door, raising two of its tendril mouths in the air.")
                input("\nLuckily, you manage to open the door and slip into the next room right as it opens one of its mouth to scream.")
                c2_room()
            else:
                input("\nYou decide to not open the door.")
                continue
        if explore_third=="d":
            input("\nThere is a blank wall to your left.")
            input("\nLooking down, you also notice a black marker on the floor.")
            input("\nMaybe you should write your own creepy message to be read by the next unlucky sap to end up here.")
            own_message=input("\nPlease enter your own creepy message or press q not to: ")
            if own_message=="q":
                input("\nYou decide to not write a message.")
                continue
            else:
                input("\nThe next time someone is forced to wander these cursed hospice halls, they may turn and shine their flash light on your chilling message: "+own_message+" How blood-curdling!")
                continue

def c2_room():
    input("\nYou shine your flashlight on a single wooden table in the center of the room.")
    explore_c2 = ""
    while explore_c2 != ("a", "s", "d", "w", "g", "h", "i", "p"):
     explore_c2 = input("\nPress w-forward,a-left,s-turn around,d-right to explore room C2. Press i to open doors.\n")
     if explore_c2=="s":
        input("\nYou face the door you just came in through.")
        input("\nWould you like to go back out into the hallway?")
        go_back=input("\nPress i to go back out and any other key to stay in the room.")
        if go_back=="i":
            input("\nYou go back out into the hallway.")
            hallway_third_block_backwards_two()
        else:
            input("\nYou decide to stay in the room.")
            continue
     if explore_c2=="w":
         input("\nYou look down at the table and see a single metal key.")
         input("\nThere is a tag attached to it that reads 'key to outdoor pool area.'")
         input("\nWould you like to pick up the key?")
         get_key=input("\nPress p to pick up the key and any other key not to.")
         if get_key=="p":
            input("\nYou pick up the key.")
            writing_on_wall_c2_room()
         else:
            input("\nYou decide not to pick up the key.")
            continue
     if explore_c2=="a":
        input("\nYou look to your left and see nothing but a turned over wheel chair and a bottle of spilled pills.")
     if explore_c2=="d":
        input("\nYou look to your right and see what looks like a body bag on the floor.")
        input("\nIt writhes and twists on the floor like a worm.")
        input("\nYou hear what sounds like a man groaning inside but there is something off about it, inhuman.")
        input("\nWould you like to open the body bag?")
        open_bag=input("\nPress i for yes and any other key for no.")
        if open_bag=="i":
            input("\nYou unzip the black body bag.")
            input("\nA mixture of of what smells like moldy cheese and sour milk hits your nostrils as some mysterious, slimy substance spills out of the bag.")
            input("\nIt spills over your hands, and before you know it, both of them have melted into a pile of liquid on the ground.")
            input("\nThe substance has a mind of its own as it travels up your arms.")
            input("\nYou scream in agony until the foul substance covers your head, dissolving your mind into an opaque liquid.")
            you_died_body_bag_monster()
        else:
            input("\nYou decide to not open the weird, groaning bag.")


def writing_on_wall_c2_room():
    input("\nYour flashlight dies as you pocket the key.")
    input("\nYou can't see a thing as you try flicking the flashlight's switch on and off.")
    input("\nIn the dark, you can hear strange groaning to your right and the vague outline of something trying to prop itself up.")
    input("\nA sudden inhuman, high-pitched scream sounds from down the hall, followed by the sound of a slamming door.")
    input("\nThe thing to your right is now standing upright and hopping towards you.")
    input("\nIt's clumsy movements would be funny if not for its pain-filled groan which seems to grow louder the closer it gets.")
    escape_c2=""
    while escape_c2 != ("a", "s", "d", "w", "g", "h", "i", "p"):
     escape_c2 = input("\nPress w-forward,a-left,s-turn around,d-right to explore room C2. Press i to open doors.\n")
     if escape_c2=="s":
         input("\nWould you like to exit from room C2?")
         leave_room=input("\nPress i to go back into the hallway and any other key to stay in the room.")
         if leave_room=="i":
            input("\nYou leave the room, slamming the door behind you.")
            hallway_block_three_three()
         else:
            input("\nYou decide not to leave the room.")
     if escape_c2=="w":
         input("\nAre you sure that you want to walk further into the room away from the only other door? You aren't alone in here.")
         why_not=input("\nPress w again to walk to the other end of the room or any other key to stay where you are.")
         if why_not=="w":
             input("\nYou walk to the end of the room.")
             input("\nThere is nothing past the wooden table but a blank wall.")
             input("\nBefore you can think of turning back around, you feel a horrifying slimy substance drip down your shoulder as the strange, body bag monster stands right behind you.")
             input("\nThe substance seems to liquefy everything it touches, a revelation you come to shortly before your entire head melts into a puddle.")
             you_died_body_bag_monster_two()
         else:
             input("\nYou decide to stay where you are.")
             continue
     if escape_c2=="a":
         input("\nYou look to your left and see a wheelchair and a bottle of spilled pills.")
         input("\nYou can feel the strange bag-like monster getting closer and closer to you.")
         input("\nWould you like to walk over to the wheelchair on your left?")
         input("\nRemember, you're not alone in here.")
         keep_looking=input("\nPress a again to walk to your left and any other key to stay where you are.")
         if keep_looking=="a":
             input("\nYou walk over to the wheelchair.")
             input("\nIt seems pretty ordinary, nothing unusual about it.")
             input("\nAs you think more about how average this wheelchair is, you hear a loud groan right behind you.")
             input("\nYou turn around and see the body-bag-like creature towering over you.")
             input("\nIt release a foul-smelling, substance that turns even your bones to liquid.")
             input("\nPainful as it is, at least it's a quick way to go.")
             you_died_body_bag_monster_two()
         else:
             input("\nYou decide to stay where you are near the door.")
     if escape_c2=="d":
        input("\nYou look to your right and see the body bag monster hopping towards you.")
        input("\nPathetic as it looks, there's no telling what it might do to you if it catches up to you.")
        input("\nYour flashlight feels cold and heavy in your hands, each flick of its switch reminding you how pointless it is to keep holding onto it.")
        input("\nWould you like to throw your useless flashlight at the body bag monster?")
        curiosity_kills=input("\nPress i to throw your flashlight at the monster and any other key not to.")
        if curiosity_kills=="i":
            input("\nFed up with all of these stupid monsters, you throw your flashlight at it, hitting it with a satisfying squish.")
            input("\nThe monster groans one more time, before releasing a strange liquid which starts to spread all over the room.")
            input("\nYou watch the substance dissolve your flashlight into a pile of liquid.")
            get_out=input("\nWould you like to escape from room C2 before the mysterious substance touches you? Press i to escape through the door and any other key to stay where you are.")
            if get_out=="i":
                input("\nYou open the door and escape into the hallway, not even looking back once.")
                hallway_block_three_three()
            else:
                input("\nYou decide to stay where you are, paralyzed with fear.")
                input("\nThe liquid drenches through your shoes, dissolving them and your feet into a puddle.")
                input("\nWithin seconds, there is nothing left of you but a pile of fluid on the floor.")
                you_died_body_bag_monster_two()
        else:
            input("\nYou decide not to throw your flashlight at the monster. Who knows what might happen?")


def hallway_block_three_three():
    input("\nYou face the blockade at the end of the hallway.")
    input("\nSuddenly, the door to the examination room bursts open in front of you.")
    input("\nThousands of hands, all intertwined and woven together, emerge from the room.")
    input("\nThey grab at the walls, the ceiling, the floor, pulling themselves down the hallway towards you.")
    escape_hallway = ""
    while escape_hallway != ("a", "s", "d", "w", "g", "h", "i", "p"):
        escape_hallway = input("\nPress s to run for your life!!...or press w to stay where you are.\n")
        if escape_hallway=="s":
           hallway_block_two_three_backwards()
        elif escape_hallway=="w":
            input("\nYou stay where you are, watching the strange creature get closer and closer.")
            input("\nIt grabs your arms and pulls you down the hallway at a frightening speed.")
            input("\nYou make one last vain attempt to hold onto the examination room's door frame before being dragged inside, the door slamming behind you.")
            you_died_hallway_monster()
        else:
            continue


def hallway_block_two_three_backwards():
    input("\nYou run as fast as you can, not wanting to look at the hideous thing chasing you.")
    input("\nAs you run, you notice that the blob-shaped monster is no longer in the hallway.")
    input("\nYou stop to catch a glimpse of the door it was clawing at, and notice one of the creature's disembodied arms is jamming the door, keeping it from closing.")
    input("\nYou see what look like strings of silk from a spiderweb on the other side of the door.")
    input("\nWould you like to try and hide from the monster in this room, or do you want to keep running down the hallway?")
    keep_going=""
    while keep_going != ("w","i"):
        keep_going = input("\nPress i to enter the room or w to keep going.\n")
        if keep_going=="w":
          hallway_block_one_three_backwards()
        if keep_going=="i":
          input("\nYou kick the monster's arm aside and shut the door behind you.")
          input("\nThe room is pitch black.")
          input("\nYou step further into the room, until you find yourself stuck in place.")
          input("\nYou panic as one of your arms gets stuck in a thick strand of web.")
          input("\nLooking up, you now see the blob monster from the hallway wrapped up in some kind of strange, white cocoon.")
          input("\nTwo of its arms stick out, hanging limp.")
          input("\nA strange, eight-legged creature moves towards you as you continue to struggle.")
          input("\nThe spider-like creature's body is covered with human faces, each one twisted in a unique expression of agony.")
          input("\nThey all seem to look at you, as the spider begins to wrap you in its webbing.")
          you_died_hallway_monster_spider()
        else:
          input("\nYou can't decide on whether to hide or run.")
          input("\nThe many armed monster grabs your ankles, dragging you down the hallway.")
          input("\nYou scream as the door to the examination room slams shut.")
          you_died_hallway_monster_two()


def hallway_block_one_three_backwards():
    input("\nYou run to the end of the hallway.")
    input("\nYou see a door labeled 'Outdoor Pool Area.'")
    input("\nYou take out the key and unlock the door.")
    input("\nThe monster is getting closer and closer, grabbing at the air, trying to find you.")
    almost_there = ""
    while almost_there != ("s", "i",):
        almost_there = input("\nPress i to open the door or s to stay where you are.")
        if almost_there=="i":
            input("\nYou open the door, shutting it behind you right before the monster is able to grab you.")
            input("\nYou manage to lock the door before the monster can open it again.")
            pool_corridor()
        if almost_there=="s":
            input("\nYou turn around to face the monster.")
            input("\nIt grabs your legs, pulling you down the hallway and back to the examination room.")
            input("\nYou try to grab at anything to save yourself but its too late.")
            input("\nThe monster has you now.")
            you_died_hallway_monster_three()

def pool_corridor():
    input("\nYou run down the corridor as the monster bangs at the closed door.")
    input("\nIt's only a matter of time before it busts through.")
    input("\nTo your right you catch a glimpse of a giant web down a short hallway.")
    input("\nIt is filled with spider-looking creatures, with eight legs, human skin, and various human faces on them, all of them with agonized expressions.")
    input("\nYou keep running until you see a door to your left with light coming in through a small window.")
    input("\nThe door at the end of the hallway opens as the monster pushes its way through.")
    input("\nWould you like to exit through this door or keep running to the end of the hallway?")
    almost_there=""
    while almost_there != ("a", "s", "d", "w", "g", "h", "i", "p"):
        almost_there = input("\nPress i to go through the door or w to keep running down the hall.")
        if almost_there=="i":
          pool_function()
        if almost_there=="w":
          input("\nYou panic and decide to keep running down the hallway.")
          input("\nAnother blob monster with four-tentacle mouths waits for you at the end of the corridor.")
          input("\nIt manages to charge at you and end your life before the monster behind you can grab you.")
          you_died_blob_monster_pool_corridor()

def pool_function():
    input("\nCold, fresh air breezes past your face as you step through the door.")
    input("\nOnce you close it, all of the monstrous creatures seem to disappear like a bad dream.")
    input("\nA thick fog covers everything, making it impossible to see past the fence surrounding the pool.")
    input("\nThere is an empty pool in front of you.")
    input("\nLooking down, you see a large black hole at the bottom of the pool.")
    input("\nIt seems to go on forever.")
    input("\nThe fence surrounds the entire pool area.")
    input("\nHowever, there is a small gap in the part of the fence to your left.")
    input("\nWould you like to go through the gap in the fence into the unknown?")
    finally_done=""
    while finally_done != ("a", "s", "d", "w", "g", "h", "i", "p"):
        finally_done=input("\nPress i to go through the fence and any other key not to.")
        if finally_done=="i":
          input("\nYou slide through the gap in the fence.")
          input("\nNone of the immediate surrounding buildings look familiar to you.")
          input("\nIn the distance, you swear you hear someone screaming, but its too far away to tell.")
          input("\nFighting the urge to turn back, you walk into the fog, braving whatever horrors await you.")
          you_win()
        else:
         input("\nYou decide to stay by the pool for a bit, needing a break from facing yet more awful nightmarish monstrosities.")


def you_win():
    input("\nThank you for playing my game!")
    input("\nThis plot was heavily inspired by Silent Hill 2, with the basic layout of the map having been modeled from the 1st floor of Brookhaven Hospital from said game.")
    input("\nThis was my first big coding project using Python.")
    input("\nThank you so much for taking the time to play through it!")
    input("\nA smiley face for you: \n:)")
    input("\nGoodbye!")
    sys.exit()

















def you_died_blob_monster_one():
    keep_playing=""
    while keep_playing!="Y" or "N":
        keep_playing = input("\nYou have just been killed by a monstrous blob. Would you like to keep playing? Y or N?")
        if keep_playing=="Y":
            print("\nYay!:)")
            explore_hallway()
        elif keep_playing=="N":
            input("\nThanks for playing!")
            sys.exit()
        else:
            continue

def you_died_blob_monster_two():
    keep_playing=""
    while keep_playing!="Y" or "N":
        keep_playing = input("\nYou have just been killed by a monstrous blob. Would you like to keep playing? Y or N?")
        if keep_playing=="Y":
            print("\nYay!:)")
            hallway_third_block_one()
        elif keep_playing=="N":
            input("\nThanks for playing!")
            sys.exit()
        else:
            continue

def you_died_blob_monster_three():
    keep_playing = ""
    while keep_playing != "Y" or "N":
        keep_playing = input("\nYou have just been killed by a monstrous blob. Would you like to keep playing? Y or N?")
        if keep_playing == "Y":
            print("\nYay!:)")
            hallway_fourth_block_one()
        elif keep_playing == "N":
            input("\nThanks for playing!")
            sys.exit()
        else:
            continue

def you_died_blob_monster_four():
    keep_playing = ""
    while keep_playing != "Y" or "N":
        keep_playing = input("\nYou have just been killed by a monstrous blob. Would you like to keep playing? Y or N?")
        if keep_playing == "Y":
            print("\nYay!:)")
            examination_room()
        elif keep_playing == "N":
            input("\nThanks for playing!")
            sys.exit()
        else:
            continue

def you_died_blob_monster_five():
    keep_playing = ""
    while keep_playing != "Y" or "N":
        keep_playing = input("\nYou have just been killed by a monstrous blob. Would you like to keep playing? Y or N?")
        if keep_playing == "Y":
            print("\nYay!:)")
            hallway_third_block_backwards_two()
        elif keep_playing == "N":
            input("\nThanks for playing!")
            sys.exit()
        else:
            continue


def you_died_spider_monster_one():
    keep_playing=""
    while keep_playing!="Y" or "N":
        keep_playing = input("\nYou have just been killed by a spider monster. Would you like to keep playing? Y or N?")
        if keep_playing=="Y":
            print("\nYay!:)")
            input("\nYou walk down the hallway. Stopping to examine your surroundings, you notice a door to your right that says 'C3' on it.")
            input("\nThe blob-monster can still be heard chewing on flesh behind you. It doesn't seem to have noticed you yet.")
            hallway_second_block()
        elif keep_playing=="N":
            input("\nThanks for playing!")
            sys.exit()
        else:
            continue

def you_died_slime_monster():
    keep_playing = ""
    while keep_playing != "Y" or "N":
      keep_playing = input("\nYou have just been killed by a slime monster. Would you like to keep playing? Y or N?")
      if keep_playing == "Y":
         print("\nYay!:)")
         slime_monster()
      elif keep_playing == "N":
             input("\nThanks for playing!")
             sys.exit()
      else:
            continue

def you_died_slime_monster_two():
    keep_playing = ""
    while keep_playing != "Y" or "N":
     keep_playing = input("\nYou have just been killed by a slime monster. Would you like to keep playing? Y or N?")
     if keep_playing == "Y":
         print("\nYay!:)")
         hallway_fourth_block_two()
     elif keep_playing == "N":
         input("\nThanks for playing!")
         sys.exit()
     else:
         continue

def you_died_body_bag_monster():
    keep_playing = ""
    while keep_playing != "Y" or "N":
     keep_playing = input("\nYou have just been killed by a body bag monster. Would you like to keep playing? Y or N?")
     if keep_playing == "Y":
         print("\nYay!:)")
         c2_room()
     elif keep_playing == "N":
         input("\nThanks for playing!")
         sys.exit()
     else:
         continue

def you_died_body_bag_monster_two():
    keep_playing = ""
    while keep_playing != "Y" or "N":
     keep_playing = input("\nYou have just been killed by a body bag monster. Would you like to keep playing? Y or N?")
     if keep_playing == "Y":
         print("\nYay!:)")
         writing_on_wall_c2_room()
     elif keep_playing == "N":
         input("\nThanks for playing!")
         sys.exit()
     else:
         continue

def you_died_hallway_monster():
    keep_playing = ""
    while keep_playing != "Y" or "N":
     keep_playing = input("\nYou have just been killed by a monster with many hands. Would you like to keep playing? Y or N?")
     if keep_playing == "Y":
        print("\nYay!:)")
        hallway_block_three_three()
     elif keep_playing == "N":
        input("\nThanks for playing!")
        sys.exit()
     else:
         continue

def you_died_hallway_monster_spider():
    keep_playing = ""
    while keep_playing != "Y" or "N":
     keep_playing = input("\nYou have just been killed by a monster spider. Would you like to keep playing? Y or N?")
     if keep_playing == "Y":
        print("\nYay!:)")
        hallway_block_two_three_backwards()
     elif keep_playing == "N":
        input("\nThanks for playing!")
        sys.exit()
     else:
         continue


def you_died_hallway_monster_two():
    keep_playing = ""
    while keep_playing != "Y" or "N":
     keep_playing = input("\nYou have just been killed by a monster with many hands. Would you like to keep playing? Y or N?")
     if keep_playing == "Y":
        print("\nYay!:)")
        hallway_block_two_three_backwards()
     elif keep_playing == "N":
        input("\nThanks for playing!")
        sys.exit()
     else:
         continue

def you_died_hallway_monster_three():
    keep_playing = ""
    while keep_playing != "Y" or "N":
     keep_playing = input("\nYou have just been killed by a monster with many hands. Would you like to keep playing? Y or N?")
     if keep_playing == "Y":
        print("\nYay!:)")
        hallway_block_one_three_backwards()
     elif keep_playing == "N":
        input("\nThanks for playing!")
        sys.exit()
     else:
         continue

def you_died_blob_monster_pool_corridor():
    keep_playing = ""
    while keep_playing != "Y" or "N":
        keep_playing = input("\nYou have just been killed by a blob monster. Would you like to keep playing? Y or N?")
        if keep_playing == "Y":
            print("\nYay!:)")
            pool_corridor()
        elif keep_playing == "N":
            input("\nThanks for playing!")
            sys.exit()
        else:
         continue





title_screen()
#wake_up()
#flash_light()
#hallway_one()
#explore_hallway()
#down_the_hallway_one()
#hallway_second_block()
#hallway_third_block_one()
#hallway_third_block_backwards_one()
#hallway_fourth_block_one()
#examination_room()
#slime_monster()
#hallway_fourth_block_two()
#c2_room()
#writing_on_wall_c2_room()
#hallway_block_two_three_backwards()
#pool_corridor()

