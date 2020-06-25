import pygame

pygame.init()

width = 1000
height = 600
offset_x = (width/5-128)/2
offset_y = (height/4-128)/2




i2 = pygame.image.load("img/h2.png")
i3 = pygame.image.load("img/globe.png")
i4 = pygame.image.load("img/cinema.png")
i5 = pygame.image.load("img/basketball.png")
i6 = pygame.image.load("img/science.png")
i7 = pygame.image.load("img/quiz.png")
i8 = pygame.image.load("img/cross.png")

history_true = True
geography_true = True
cinema_true = True
sport_true = True
science_true = True
trivia_true = True

running = True

while running:
    win = pygame.display.set_mode((width, height))
    win.fill((119,136,153))
    if history_true:
        win.blit(i2, (int(width/5 + offset_x), int(height/4 + offset_y)))
    else:
        win.blit(i2, (int(width / 5 + offset_x), int(height / 4 + offset_y)))
        win.blit(i8, (int(width/5 + offset_x), int(height/4 + offset_y)))

    if geography_true:
        win.blit(i3, (int(width/5*2 + offset_x), int(height/4 + offset_y)))
    else:
        win.blit(i3, (int(width/5*2 + offset_x), int(height/4 + offset_y)))
        win.blit(i8, (int(width / 5 * 2 + offset_x), int(height / 4 + offset_y)))

    if cinema_true:
        win.blit(i4, (int(width/5*3 + offset_x), int(height/4 + offset_y)))
    else:
        win.blit(i4, (int(width / 5 * 3 + offset_x), int(height / 4 + offset_y)))
        win.blit(i8, (int(width / 5 * 3 + offset_x), int(height / 4 + offset_y)))

    if sport_true:
        win.blit(i5, (int(width/5 + offset_x), int(height/2 + offset_y)))
    else:
        win.blit(i5, (int(width / 5 + offset_x), int(height / 2 + offset_y)))
        win.blit(i8, (int(width / 5 + offset_x), int(height / 2 + offset_y)))

    if science_true:
        win.blit(i6, (int(width/5*2 + offset_x), int(height/2 + offset_y)))
    else:
        win.blit(i6, (int(width / 5 * 2 + offset_x), int(height / 2 + offset_y)))
        win.blit(i8, (int(width / 5 * 2 + offset_x), int(height / 2 + offset_y)))

    if trivia_true:
        win.blit(i7, (int(width/5*3 + offset_x), int(height/2 + offset_y)))
    else:
        win.blit(i7, (int(width/5*3 + offset_x), int(height/2 + offset_y)))
        win.blit(i8, (int(width/5*3 + offset_x), int(height/2 + offset_y)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()
            if pos_x < width/5 + offset_x + 128 and pos_x > width/5 + offset_x and pos_y > height/4 + offset_y and pos_y < height/4 + offset_y + 128 and history_true:
                running2 = True
                while running2:
                    win2 = pygame.display.set_mode((600, 600))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running2 = False

                history_true = False

            if pos_x < width/5*2 + offset_x + 128 and pos_x > width/5*2 + offset_x and pos_y > height/4 + offset_y and pos_y < height/4 + offset_y + 128 and geography_true:
                print("geografija")
                geography_true = False

            if pos_x < width/5*3 + offset_x + 128 and pos_x > width/5*3 + offset_x and pos_y > height/4 + offset_y and pos_y < height/4 + offset_y + 128 and cinema_true:
                print("film")
                cinema_true = False

            if pos_x < width/5 + offset_x + 128 and pos_x > width/5 + offset_x and pos_y > height/2 + offset_y and pos_y < height/2 + offset_y + 128 and sport_true:
                print("sport")
                sport_true = False

            if pos_x < width/5*2 + offset_x + 128 and pos_x > width/5*2 + offset_x and pos_y > height/2 + offset_y and pos_y < height/2 + offset_y + 128 and science_true:
                print("nauka")
                science_true = False

            if pos_x < width/5*3 + offset_x + 128 and pos_x > width/5*3 + offset_x and pos_y > height/2 + offset_y and pos_y < height/2 + offset_y + 128 and trivia_true:
                print("trivia")
                trivia_true = False

    pygame.display.update()
