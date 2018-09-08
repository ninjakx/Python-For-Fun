import pygame,sys,eztext

import time,random
pygame.init()
white=(255,255,255)
black=(0,0,0)
w=800
h=600
from pygame.locals import *
gameDisplay=pygame.display.set_mode((w,h))
gameDisplay.set_alpha(None)
pygame.display.set_caption('Hangman')
clk=pygame.time.Clock()
font=pygame.font.SysFont(None,20)
txtbx = eztext.Input(maxlength=45, color=(255,0,0), prompt='Player Name: ')  

def main():
 #message(txtbx,black)
  while 1:
    #clk.tick(30)
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.KEYUP :
            if event.key==pygame.K_RETURN:
              print(txtbx.value)
              return
    bg=pygame.image.load("p.jpg")
    bg = pygame.transform.scale(bg, (800, 600)) 

    gameDisplay.fill((255,255,255))
    txtbx.update(events)
    
    txtbx.draw(gameDisplay)
    pygame.display.update()
class pane(object):
 font=pygame.font.SysFont(None,40)
 gameDisplay=pygame.display.set_mode((w,h),0,32)
 def box(self,width,height):
    self.rect=pygame.draw.rect(gameDisplay,(250,0,0), (100-10, 100-10, width+10+10, height+10), 2)
    pygame.display.update()
 def name(self):
    
    
    text='Hello, '+txtbx.value+' ,Time to play hangman!'
    
    
    text_width, text_height = self.font.size(text)
    print(text_width,text_height)
 
    screen_text=self.font.render(text,True,(255,0,0))
    self.gameDisplay.blit(screen_text,[100,100])
    pygame.display.update()
    return (text_width,text_height)

def startgame():
    
    gameDisplay.fill((255,255,255))
    
    
    text=["MY name is :","my hobby is :"]
    ans=["kriti","coding"]
    score=0
    for i in range(2):
     gameDisplay.fill((255,255,255))
     time.sleep(1)
     turnleft=3   
     print(i,text[i],ans[i])

     while(turnleft>0):
      guesses=str(input())
      gameDisplay.fill((255,255,255))
      if (guesses == ans[i]):
        
        font=pygame.font.SysFont(None,30)
        score=score+10   

        
        screen_text=font.render("correct",True,(255,0,0))
    
        gameDisplay.blit(screen_text,[100,100])
        pygame.display.update()
        break
        
      else:
        turnleft=turnleft-1
        
        font=pygame.font.SysFont(None,30)
           
        screen_text=font.render("incorrect",True,(255,0,0))
    
        gameDisplay.blit(screen_text,[100,100])
        screen_text=font.render("No. of turns left :"+str(turnleft),True,(255,0,0))
    
        gameDisplay.blit(screen_text,[300,300])
       
        pygame.display.update()
        
    time.sleep(1)
    gameDisplay.fill((255,255,255))
    screen_text=font.render("score : "+str(score),True,(255,0,0))
      
    gameDisplay.blit(screen_text,[350,350])
    pygame.display.update()
      
       
    '''time.sleep(4)
    gameDisplay.fill((255,255,255))
    screen_text=font.render("bas",True,(255,0,0))
    
    gameDisplay.blit(screen_text,[100,100])
    pygame.display.update()'''
    
    
    

if __name__ == '__main__':
 pan3=pane()
 main()
 gameDisplay.fill(white)
 width,height=pan3.name()
 pan3.box(width,height)
 startgame()
