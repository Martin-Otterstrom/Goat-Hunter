import time
import pygame
from pygame import mixer
import random
import sys
import os

# Animation speed logic - 12:25 -> https://youtu.be/MYaxPa_eZS0 <-
# Making Score counter + generating text - 2:57 -> https://youtu.be/E4Ih9mpn5tk <-
# Pretty essential: Score + slash collition.

# How to add more enemies = if 1 in 10: Spawn super goat, if 1 in 100: spawn goat rain. if score > 10 if 1 in 3:
# Spawn goat, wait (between a and b seconds) spawn another. If score gets better goats get stronger and at a certain
# Point they get 2 lives and 3 and then like unkillable?

# Things to ad: Settings with adjustable stuff, highscores, better sounds, unlocking music an skins if better highscore
# Powerupps, other animals, multiple goats, goat meteor rain, goats get progressive stronger and faster
# survival points (with sound if reach milestone), survivalpointgain is multiplied when goats become unkillable?
# Hovering text! Other weapons?, superoptional: 2 players? Different modes, easy, medium, hard, Impossible!
# A bit improved graphics mabye, supperoptional: add cropping to different screen sizes in settings?
# In settings. Mabye add timer?
# Mabye make nighttime, optional and hard but ulltracool!: Make a "Camera follow" on the player.
# If "Camera follow" is possible: make different biomes and some small shops?
# If I REALLY want to make it an ulltra full game I could make seperate lvls in a storymode + tutorial

# If i make all these I can also list game on steam and charge it for 1$? Push the wishlist in videos!

goat_quoutes = [
    '\"Ideas are easy. It\'s the execution of ideas that really separates the sheep from the goats.\"- Sue Grafton',
    '\"Goats are really cute, especially little ones. But they do smell a little bit.\" - Jacob Tremblay ',
    '\"Books are no different from goats! They enjoy an afternoon out on the lawn.\" - Kate Bernheimer ',
    'We saw goats foraging but couldn\'t work out what they could possibly be eating.\" - Fiona Bruce',
    '\"Every man can tell how many goats or sheep he possesses, but not how many friends.\"-Marcus Tullius',
    '\"It is written that there shall be a separation, and the sheep shall be separated from the goats.\"',
    '\"I\'m terrified of goats.\" - Annalise Basso',
    '\"Goats are the cable talk show panelists of the animal world, ready at a moment\'s notice to interject\"',
    "\"I think that the reason why 'Goats' is called 'Goats' is because you can't give direction to goats.\"",
    '\"In my neighborhood, there are stray goats everywhere, and, someone owns it >:(\".',
    '\"A close family member once offered his opinion that I exhibit the phone manners of a goat\"',
    '\"And I like pygmy goats, because they\'re just lovely, and ducks.\" - Richard Hammond',
    '\"I hate pigs. I hate goats.\" - Blake Shelton',
]

caption_list = [
    "\"Best game ever\" - literally everyone",
    "Goats do be goatin\'",
    "What's your 1 min highscore?",
    "The hard way is the easy way, the easy way is the hard way",
    "What's beyond the edge of expanding space?",
    "never give up",
    "you died lolol",
    "^-^",
    "What a time to be alive!",
    "xaxaxaxaxaxaxa",
    "compete with a friend - who gets the highest score within x time?",
    "forgot keybinds? a,d,space,arrowkeys"
]


class GameState():
    def __init__(self):
        self.state = 'intro'

    def End(self):
        global endIndex, end, dead, random_number
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'intro'

        # Drawing
        screen.fill((0, 0, 0))
        # Resetting endIndex
        if endIndex >= 6:
            endIndex = 0
        # Displaying animation
        screen.blit(end[int(endIndex)], (0, 0))
        endIndex += 0.1

        # Displaying text

        text_score = Game_font.render("score: " + str(int(score)), False, dark_turquoise)
        screen.blit(text_score, (650, 760))

        text_time = Game_font.render("Time: " + str(int(time)) + " sec", False, dark_cyan)
        screen.blit(text_time, (488, 760))

        text_5 = menu_font.render(f"{message_3}", False, yellow)
        screen.blit(text_5, (330, 100))

        text_6 = even_smaller_menu_font.render(f"{message_4}", False, white)
        screen.blit(text_6, (760, 250))

        pygame.display.flip()

    def intro(self):
        global menu_stepIndex, dead, Main_menu, score, time, goat_quoutes
        dead = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'main_game'
        # Resetting score and time
        score = 0
        time = 0
        # Drawing - display meny screen with sprite animation

        # Resetting menu_stepIndex

        if menu_stepIndex >= 13:  # Making stepIndex larger and floordividing example in yt vid
            menu_stepIndex = 0

        # Displaying menu
        screen.blit(Main_menu[int(menu_stepIndex)], (0, 0))
        menu_stepIndex += 0.15
        # Displaying text
        text_1 = menu_font.render(f"{message_1}", False, black)
        text_2 = smaller_menu_font.render(f"{message_2}", False, yellow)
        text_6 = even_smaller_menu_font.render(f"{message_4}", False, white)

        screen.blit(text_6, (805, 500))
        screen.blit(text_1, (100, 300))
        screen.blit(text_2, (582, 440))

        # Goat fonts
        goatquote = goat_quoutes[random_number]
        text_goatquote = Game_font.render(goatquote, False, lime)
        screen.blit(text_goatquote, (20, 760))
        # 1.Create a font (and font size) 2. Write text on a new surface 3. Put the text surface on the main surface
        pygame.display.flip()

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            ''' if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'End' '''

        # input
        userInput = pygame.key.get_pressed()

        # Movement
        player.move_hero(userInput)
        player.jump_motion(userInput)

        # Enemy
        if len(enemies) == 0:
            random_nr = random.randint(0, 1)
            if random_nr == 1:
                enemy = Enemy(1150, 590, goat_running_L)
                enemies.append(enemy)
            if random_nr == 0:
                enemy = Enemy(-150, 590, goat_running_R)
                enemies.append(enemy)
        for enemy in enemies:
            enemy.move()
            if enemy.off_screen():
                enemies.remove(enemy)

        # Drawing
        screen.blit(bg, (0, 0))
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

        # Displaying text
        text_3 = Game_font.render(f"{RS_cooldown_message}", False, red)
        text_4 = Game_font.render(f"{RS_cooldown_message_2}", False, kinda_lime_but_also_green)
        text_5 = Game_font.render(f"{LS_cooldown_message}", False, red)
        text_6 = Game_font.render(f"{LS_cooldown_message_2}", False, kinda_lime_but_also_green)
        text_7 = Game_font.render("score: " + str(int(score)), False, pink)
        text_8 = Game_font.render("Time: " + str(int(time)) + " sec", False, white)

        screen.blit(text_7, (650, 760))
        screen.blit(text_8, (488, 760))

        if RCooldown:
            screen.blit(text_3, (1050, 760))
        else:
            screen.blit(text_4, (1050, 760))
        if Lcooldown:
            screen.blit(text_5, (20, 760))
        else:
            screen.blit(text_6, (20, 760))

        pygame.display.flip()

    def state_manager(self):
        global dead, player, vel_x, vel_y
        if self.state == 'intro':
            self.intro()
        if self.state == 'main_game':
            self.main_game()

        if dead:
            self.state = 'End'
            player = Hero(600, 590)  # Resetting player pos after death
            vel_x = 7
            vel_y = 7
        if self.state == 'End':
            self.End()


# General setup
pygame.init()
clock = pygame.time.Clock()
game_state = GameState()
# Sound
# background music
mixer.init()
mixer.music.load('song_alternative.ogg')
mixer.music.play(-1)

# die and score sound located in enemy class, function: hit


# Game Screen
screen_width = 1250  # 1550
screen_height = 800  # 800
screen = pygame.display.set_mode((screen_width, screen_height))
# Caption
random_caption = random.randint(0, 11)
pygame.display.set_caption(str(caption_list[random_caption]))
# Background
bg_file = pygame.image.load('BG_R.png')
bg = pygame.transform.scale(bg_file, (screen_width, screen_height))

# Sprite image Lists:

# Main menu
Main_menu = [None] * 14
for picIndex in range(1, 14):
    Main_menu[picIndex - 1] = pygame.image.load(
        os.path.join("main_meny", "Mainmeny_" + str(picIndex) + ".png"))
    picIndex += 1
# Dying screen / End screen
end = [None] * 7
for picIndex in range(1, 7):
    end[picIndex - 1] = pygame.transform.scale(pygame.image.load(
        os.path.join("end", "end__" + str(picIndex) + ".png")), (1250, 800))
    picIndex += 1

# Hero (Player)
hero_right = [None] * 9
for picIndex in range(1, 9):
    hero_right[picIndex - 1] = pygame.transform.scale(pygame.image.load(
        os.path.join("Walking_right", "Knight_walking_right_animation_" + str(picIndex) + ".png")), (150, 150))
    picIndex += 1

hero_left = [None] * 9
for picIndex in range(1, 9):
    hero_left[picIndex - 1] = pygame.transform.scale(pygame.image.load(
        os.path.join("walking_left", "Knight_walking_left_animation__" + str(picIndex) + ".png")), (150, 150))
    picIndex += 1

hero_stationary = [None] * 3
for picIndex in range(1, 3):
    hero_stationary[picIndex - 1] = pygame.transform.scale(pygame.image.load(
        os.path.join("Idleing", "tile_" + str(picIndex) + ".png")), (150, 150))
    picIndex += 1

hero_R_slash = [None] * 7
for picIndex in range(1, 7):
    hero_R_slash[picIndex - 1] = pygame.transform.scale(pygame.image.load(
        os.path.join("Slash_animation_R", "Knight_slashing_animation_" + str(picIndex) + ".png")), (150, 150))
    picIndex += 1

hero_L_slash = [None] * 7
for picIndex in range(1, 7):
    hero_L_slash[picIndex - 1] = pygame.transform.scale(pygame.image.load(
        os.path.join("Slash_animation_L", "Knight_slashing_left_animation_" + str(picIndex) + ".png")), (150, 150))
    picIndex += 1

# Goat
goat_standing_R = [None] * 3
for picIndex in range(1, 3):
    goat_standing_R[picIndex - 1] = pygame.transform.scale(pygame.image.load(
        os.path.join("goat_standing_R", "R_Stand_" + str(picIndex) + ".png")), (150, 150))
    picIndex += 1

goat_standing_L = [None] * 3
for picIndex in range(1, 3):
    goat_standing_L[picIndex - 1] = pygame.transform.scale(pygame.image.load(
        os.path.join("goat_standing_L", "L_Stand_" + str(picIndex) + ".png")), (150, 150))
    picIndex += 1

goat_running_R = [None] * 9
for picIndex in range(1, 9):
    goat_running_R[picIndex - 1] = pygame.transform.scale(pygame.image.load(
        os.path.join("goat_running_R", "R_Run_" + str(picIndex) + ".png")), (150, 150))
    picIndex += 1

goat_running_L = [None] * 9
for picIndex in range(1, 9):
    goat_running_L[picIndex - 1] = pygame.transform.scale(pygame.image.load(
        os.path.join("goat_running_L", "L_Run_" + str(picIndex) + ".png")), (150, 150))
    picIndex += 1


class Hero:
    def __init__(self, x, y):
        # Walking
        self.lives = 3
        self.x = x
        self.y = y
        self.vel_x = 14 / 25
        self.stationary = False
        self.face_right = True
        self.face_left = False
        self.stepIndex = 0
        self.stationary_stepIndex = 0
        # Slashing
        self.R_slash = False
        self.L_slash = False
        self.RSIndex = 0  # Short for Right_slash_Index
        self.LSIndex = 0  # Short for Left_slash_Index
        # Cool down
        self.Reset = 0
        self.LReset = 0
        # self.RS_image = hero_R_slash[self.RSIndex]
        self.Rcool_down_count = 0
        self.Lcool_down_count = 0
        # Hitboxes
        self.hitbox = (self.x, self.y, 64, 64)
        self.R_slash_hitbox = (self.x, self.y, 64, 64)
        self.L_slash_hitbox = (self.x, self.y, 64, 64)

    def move_hero(self, userInput):

        if userInput[pygame.K_RIGHT] and self.x <= screen_width - 75:
            self.x += self.vel_x * dt
            self.face_right = True
            self.face_left = False
            self.stationary = False
            self.L_slash = False
            self.R_slash = False

        elif userInput[pygame.K_LEFT] and self.x >= 0:
            self.x -= self.vel_x * dt
            self.face_right = False
            self.face_left = True
            self.stationary = False
            self.L_slash = False
            self.R_slash = False

        elif userInput[pygame.K_d] and self.Reset == 0 and self.x <= screen_width - 75:
            self.L_slash = False
            self.R_slash = True
            """print('R_slash = ' + str(self.R_slash))"""
            self.x += 5 / 30 * dt
            self.face_right = False
            self.face_left = False
            self.stationary = False

        elif userInput[pygame.K_a] and self.LReset == 0 and self.x >= 0:
            self.x -= 5 / 30 * dt
            self.L_slash = True
            """print('L_slash = ' + str(self.L_slash))"""
            self.R_slash = False
            self.face_right = False
            self.face_left = False
            self.stationary = False

        elif userInput[pygame.K_d] and self.Reset >= 1:
            self.L_slash = False
            self.R_slash = False
            self.face_right = False
            self.face_left = False
            self.stationary = True

        elif userInput[pygame.K_a] and self.LReset >= 1:
            self.L_slash = False
            self.R_slash = False
            self.face_right = False
            self.face_left = False
            self.stationary = True

        else:
            self.stepIndex = 0
            self.stationary = True
            self.face_right = False
            self.face_left = False
            self.L_slash = False
            self.R_slash = False

    def jump_motion(self, userInput):
        global jump, vel_y, dead
        if dead:  # Trying to solve wierd spawning bug (game think hero is in a jump and floats down) bug usually starts
            jump = False  # when jumping and dying at the same time but happens random on some rare occasions?
        if jump is False and userInput[pygame.K_SPACE]:
            jump = True
        if jump is True:
            self.y -= vel_y * 8  # Multiplying by a constant makes the jump higher. ex: *4
            vel_y -= 1
            if vel_y < -7:
                jump = False
                vel_y = 7

    def draw(self, screen):
        global RCooldown, Lcooldown
        # Hitboxes
        self.hitbox = (self.x, self.y + 45, 75, 105)
        self.L_slash_hitbox = (self.x - 14, self.y + 45, 75, 105)
        self.R_slash_hitbox = (self.x + 80, self.y + 45, 75, 105)
        # Showing hitboxes
        """pygame.draw.rect(screen, yellow, self.hitbox, 2)
        pygame.draw.rect(screen, blue, self.R_slash_hitbox, 2)
        pygame.draw.rect(screen, pink, self.L_slash_hitbox, 2)"""

        if self.stepIndex >= 8:
            self.stepIndex = 0
        if self.stationary_stepIndex >= 2:
            self.stationary_stepIndex = 0
        if self.RSIndex >= 6:
            self.RSIndex = 0
            self.Reset += 1
            RCooldown = True
        self.Rcool_down_count += 1
        if self.Rcool_down_count >= 40:
            self.Reset = 0
            RCooldown = False
        if self.LSIndex >= 6:
            self.LSIndex = 0
            self.LReset += 1
            Lcooldown = True
        self.Lcool_down_count += 1
        if self.Lcool_down_count >= 40:
            self.LReset = 0
            Lcooldown = False
        if self.face_left:
            screen.blit(hero_left[int(self.stepIndex)], (self.x, self.y))
            self.stepIndex += 0.1  # Increased value of added stepIndex = faster animation speed.
        if self.stationary:
            screen.blit(hero_stationary[int(self.stationary_stepIndex)], (self.x, self.y))
            self.stationary_stepIndex += 0.1
        if self.face_right:
            screen.blit(hero_left[int(self.stepIndex)], (self.x, self.y))
            self.stepIndex += 0.1

        if self.R_slash and self.Reset == 0:
            self.Rcool_down_count = 0
            screen.blit(hero_R_slash[int(self.RSIndex)], (self.x, self.y))
            self.RSIndex += 0.3
        if self.L_slash and self.LReset == 0:
            self.Lcool_down_count = 0
            screen.blit(hero_L_slash[int(self.LSIndex)], (self.x, self.y))
            self.LSIndex += 0.3

class Enemy:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.stepIndex = 0
        # Health
        self.hitbox = (self.x, self.y, 64, 64)

    def step(self):
        if self.stepIndex >= 8:
            self.stepIndex = 0

    def draw(self, screen):
        # Hitboxes

        if self.direction == goat_running_L:
            self.hitbox = (self.x, self.y + 50, 120, 95)
        if self.direction == goat_running_R:
            self.hitbox = (self.x + 20, self.y + 50, 120, 95)
        # Displaying hitbox
        """pygame.draw.rect(screen, red, self.hitbox, 2)"""

        self.step()
        if self.direction == goat_running_L:
            screen.blit(goat_running_L[int(self.stepIndex)], (self.x, self.y))
        if self.direction == goat_running_R:
            screen.blit(goat_running_R[int(self.stepIndex)], (self.x, self.y))
        self.stepIndex += 0.18

    def move(self):
        self.hit()
        if self.direction == goat_running_L:
            self.x -= 4 * dt / 25
        if self.direction == goat_running_R:
            self.x += 4 * dt / 25

    def hit(self):
        global dead, score, time
        self.player_hitboxrect = pygame.Rect(player.hitbox)
        self.enemy_hitboxrect = pygame.Rect(self.hitbox)
        self.Rslashhitboxrect = pygame.Rect(player.R_slash_hitbox)
        self.Lslashhitboxrect = pygame.Rect(player.L_slash_hitbox)
        self.die_sound = mixer.Sound('die.mp3')
        self.score_sound = mixer.Sound('score.wav')

        if not dead:
            score += dt / 25 / 5
            time += dt / 1000
            if self.player_hitboxrect.colliderect(self.enemy_hitboxrect):
                dead = True
                self.die_sound.play()
                for enemy in enemies:
                    enemies.remove(enemy)
            for enemy in enemies:
                if self.Rslashhitboxrect.colliderect(self.enemy_hitboxrect):
                    if player.R_slash:
                        enemies.remove(enemy)
                        self.score_sound.play()
                        score += 20 * dt / 25

                if self.Lslashhitboxrect.colliderect(self.enemy_hitboxrect):
                    if player.L_slash:
                        enemies.remove(enemy)
                        self.score_sound.play()
                        score += 20 * dt / 25

    def off_screen(self):
        return not (self.x >= -200 and self.x <= screen_width + 150)


# Instance of Hero-Class
player = Hero(600, 590)

# Instance of Enemy-class
enemies = []

# Colors
black = (0, 0, 0)
yellow = (255, 255, 0)
lime = (0, 255, 0)
red = (255, 0, 0)
green = (0, 128, 0)
pink = (255, 102, 204)
white = (255, 255, 255)
blue = (0, 0, 255)
orange = (255, 165, 0)
dark_turquoise = (0, 206, 209)
dark_cyan = (0, 139, 139)
tomato = (255, 99, 71)

kinda_lime_but_also_green = (50, 205, 50)
# Text variables
menu_font = pygame.font.Font('dpcomic.ttf', 200)
smaller_menu_font = pygame.font.Font('dpcomic.ttf', 75)
even_smaller_menu_font = pygame.font.Font('dpcomic.ttf', 30)
Game_font = pygame.font.Font('dpcomic.ttf', 30)
message_1 = "Goat Hunter"
message_2 = "A game by 5bil"
message_3 = "you died"
message_4 = "Click to continue"
message_5 = "Click to continue"
message_time = "Time: "
# display text str(10 - cooldowncounter)
RS_cooldown_message = "R Cooldown"
LS_cooldown_message = "L Cooldown"
RS_cooldown_message_2 = "No R Cooldown"
LS_cooldown_message_2 = "No L Cooldown"

# slashing


# Variables
time = 0
score = 0
random_number = random.randint(0, 11)
dead = False
RCooldown = False
Lcooldown = False
stepIndex = 0
menu_stepIndex = 0
endIndex = 0
# radius = 15  # circle radius mabye never use?
vel_x = 7  # speed, other known as 'velocity'
vel_y = 7
jump = False
# move_left = False Not used (yet)
# move_right = False
# Idling = True
# idle_Index = 0

# Update Screen - game loop
while True:
    game_state.state_manager()
    dt = clock.tick(60)
    """print(clock.get_fps())"""
    """print(str(dt))"""
