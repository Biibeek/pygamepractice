import pygame
from sys import exit


def score_display():
    current_time=int(pygame.time.get_ticks()/1000)-start_time
    score_surface=test_font.render(f"{current_time}",False,(64,64,64))
    score_rect=score_surface.get_rect(center=(400,50))
    screen.blit(score_surface,score_rect)
    return current_time

def display_end_screen(final_score, high_score):
    screen.fill((94, 129, 162))
    final_score_surface = test_font.render(f"Your Score: {final_score}", False, (255, 255, 255))
    final_score_rect = final_score_surface.get_rect(center=(400, 200))
    screen.blit(final_score_surface, final_score_rect)

    high_score_surface = test_font.render(f"High Score: {high_score}", False, (255, 255, 255))
    high_score_rect = high_score_surface.get_rect(center=(400, 100))
    screen.blit(high_score_surface, high_score_rect)

    restart_surface = test_font.render("Press SPACE to start again", False, (255, 255, 255))
    restart_rect = restart_surface.get_rect(center=(400, 300))
    screen.blit(restart_surface, restart_rect)

pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption("mypygameee")
test_font=pygame.font.Font('font/Pixeltype.ttf',50)


clock=pygame.time.Clock()


sky_surface=pygame.image.load('graphics/Sky.png').convert()
grd_surface=pygame.image.load('graphics/ground.png').convert()
# score_surface=test_font.render('Welcome',False,(0,255,0))
# score_rect=score_surface.get_rect(center=(400,50))
game_active=True
start_time=0
final_score=0
high_score=0

snail_surface=pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect=snail_surface.get_rect(bottomright=(600,300))

player_surf=pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect=player_surf.get_rect(midbottom=(80,300))
player_gravity=0
snail_x_pos=600
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:   
            pygame.quit()
            exit()
        if game_active:
            if event.type==pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >=300:
                    player_gravity =-20
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and player_rect.bottom >=300:
                    player_gravity =-20
        else:
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                game_active=True
                snail_rect.left=800
                start_time=int(pygame.time.get_ticks()/1000)
        
    if game_active:
        screen.blit(sky_surface,(0,0))
        # pygame.draw.rect(screen,'red',score_rect)
        # pygame.draw.rect(screen,'red',score_rect,10)
        screen.blit(grd_surface,(0,300))
        # screen.blit(score_surface,score_rect)

        snail_rect.x -=4
        if snail_rect.right <=0: snail_rect.left=800
        screen.blit(snail_surface,snail_rect)
        player_gravity +=1
        player_rect.y +=player_gravity
        if player_rect.bottom >=300:
            player_rect.bottom=300
        screen.blit(player_surf,(player_rect))
        final_score=score_display()
        # keys=pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]

        #if player_rect.colliderect(snail_rect):
        #   print("collided!!!")
        if snail_rect.colliderect(player_rect):
            game_active=False

            if final_score >high_score:
                high_score=final_score
    else:
        display_end_screen(final_score, high_score)

    clock.tick(60)
    
    pygame.display.update()
