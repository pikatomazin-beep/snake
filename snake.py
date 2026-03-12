#Napiši snake-game v pygamu
#koda od prej ti lahko sliži za inspiracijo (npr dolzina kace s kvadratki -> to pride prav)

#za projekt naredite github repozitorij, in spremembe sproti comitatje addajte in pushajte
#na koncu morajo biti v repozitoriju vsaj 3 vecji commiti

#okviren plan

#I. Naredi ogrodje -> while zanka, canvas, eventi za exit itd


#II. Naredi kvadrat -> ta kvadrat bo v prihodnisti ratala kača, zaenkrat naj bo samo kvadrat
#	naredi logiko da ta kvadrat lahko zavija levo desno z kliki na gumne na tipkovnici
#	naredi logiko, da se nakej izpiše, ko se ta kvadrat dotakne stene
#	naredi logiko, da se ta kvadrat premika po nekem "gridu" -> hint nastavi clock.tick na nekaj malega,
#		vsak frame premakni kaco za nekaj pixlov, ta premik predstavlja sirino vsake celice


#III. Kvadrat spremeni v seznam kvadratov, ki predstavljajo kaco


#IV. Naredi logiko, da se nekaj izpiše, ce se kace zabije sama vase


#V. Naredi nek nov kvadrat ki predstavlja hrano
#	-> naredi da se vsakic ko ga kaca poje z glavo prestavi na nakljucno mesto in kaca zrasta


#od tu naprej je treba samo še štet score, kej izpiovat na ekrat, dt kk gumb za game over pa restart itd... neke olepšave




#1. dodatna naloga:
#naredi branch "izgled"
#v tem brancu naredi logiko, da ko igra tece, lahko pritisnes gumb "space" kar celotni kaci nastavi nakljucno barvo

#2. dodatna naloga:
#naredi branch "multiplayer"
#v tem branchu naredi logiko, da sta na zacetku igre 2 kaci, ena se upravlja z wasd, druga z gumbi s puscicami
#ce se aca zabije vase, v drugo kaco ali v steno, izgubi

#3. dodatna naloga
#naredi megre obeh branchov

import pygame
import random

pygame.init()
clock = pygame.time.Clock()

canvas = pygame.display.set_mode((500,500))
pygame.display.set_caption('Snakegame.com')

font = pygame.font.SysFont(None,40)

ext = False
lives = 3
score = 0

color = (180,210,250)
color1 = (240,225,250)
color2 = (255,0,0)

koordinatex = 20
koordinatey = 20

player = [(200,200)]
smer = (koordinatex,0)

jabukx = random.randrange(0,500,koordinatex)
jabuky = random.randrange(0,500,koordinatey)
food = (jabukx,jabuky)

while not ext:

    clock.tick(10)
    canvas.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ext = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                smer = (0,-koordinatey)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                smer = (0,koordinatey)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                smer = (-koordinatex,0)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                smer = (koordinatex,0)

    headx = player[0][0] + smer[0]
    heady = player[0][1] + smer[1]
    newhead = (headx,heady)

    crash = False

    if headx < 0 or headx >= 500:
        smer = (-smer[0], smer[1])
        headx = player[0][0] + smer[0]

    if heady < 0 or heady >= 500:
        smer = (smer[0], -smer[1])
        heady = player[0][1] + smer[1]

    newhead = (headx, heady)

    if newhead in player:
        crash = True

    if crash:
        lives -= 1

        if lives == 0:
            ext = True


    else:
        player.insert(0,newhead)

        if newhead == food:
            score += 1
            jabukx = random.randrange(0,500,koordinatex)
            jabuky = random.randrange(0,500,koordinatey)
            food = (jabukx,jabuky)
        else:
            player.pop()

    for part in player:
        pygame.draw.rect(canvas,color1,(part[0],part[1],koordinatex,koordinatey))

    pygame.draw.rect(canvas,color2,(food[0],food[1],koordinatex,koordinatey))

    livestext = font.render("Lives: " + str(lives),True,(0,0,0))
    canvas.blit(livestext,(10,10))

    scoretext = font.render("Score: " + str(score),True,(0,0,0))
    canvas.blit(scoretext,(350,10))

    pygame.display.update()

pygame.quit()

