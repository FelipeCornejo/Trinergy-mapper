import sys, pygame
from TrinergyMapperPMGD import main


pygame.init()

class Cursor(pygame.Rect):
   def __init__(self):
      #un cuadrado
      pygame.Rect.__init__(self,0,0,1,1)
   def update(self):
      #las posiciones del mouse en base al cuadrado
      self.left,self.top = pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):
   def __init__(self, boton, botonpress, x, y):
      #definimos como sera el boton sin presionar
      self.boton1 = boton
      
      #definimos como sera el boton presionado
      self.boton1press = botonpress
      self.boton2 = boton
      self.boton2press = botonpress
      self.boton = self.boton1
      self.boton = self.boton2
      #entrega las coordenas de un rectangulo
      self.rect = self.boton.get_rect()
      self.rect.left,self.rect.top = (x,y)
      
   def update(self,pantalla,cursor):
      if cursor.colliderect(self.rect):
         self.boton = self.boton1press
         self.boton = self.boton2press
      else:
         self.boton = self.boton1
         self.boton = self.boton2

      pantalla.blit(self.boton,self.rect)


size = width, height = 1024, 600
pygame.display.set_caption("Trinergy Mapper PMGD")

##imagenes##
imagen_inicio = pygame.image.load("Logos/features/bgui.jpg")
logo = pygame.image.load("Logos/features/logo.png")
botonUtility = pygame.image.load ("Logos/features/boton1.png")
botonUtility = pygame.transform.scale(botonUtility,(193,74))
botonUtilityPress = pygame.image.load("Logos/features/boton1press.png")
botonUtilityPress = pygame.transform.scale(botonUtilityPress,(193,74))
botonExit = pygame.image.load ("Logos/features/boton2.png")
botonExit = pygame.transform.scale(botonExit,(193,74))
botonExitPress = pygame.image.load ("Logos/features/boton2press.png")
botonExitPress = pygame.transform.scale(botonExitPress,(193,74))
rectan= pygame.image.load("Logos/features/rectantra.png")
eslogan = pygame.image.load("Logos/features/eslogan.png")
eslogan = pygame.transform.scale(eslogan,(200,25))
atencion = pygame.image.load("Logos/features/atencion.png")

reloj = pygame.time.Clock()
cursor = Cursor()

def inicio():
   boton1 = Boton(botonUtility,botonUtilityPress,220,425)
   boton2 = Boton(botonExit,botonExitPress,611,425)
   
   inicio = True
   while inicio:
      for eventos in pygame.event.get():
         #si dentro de la pantalla se detecta un click
         if eventos.type==pygame.MOUSEBUTTONDOWN:
            #si el cursor obtenido por la clase cursor , choca con el boton y se clickea
            if cursor.colliderect(boton1.rect):
               #salimos de la pantalla de inicio
               inicio = False
               break
            if cursor.colliderect(boton2.rect):
               #salimos de la pantalla de inicio
               pygame.quit()
               quit()
         #en caso de que se aprete la X de la pantalla para que se cierre el programa
         if eventos.type == pygame.QUIT:
            pygame.quit()
            quit()
      #definimos la imagen que se mostrara
      imagen_inicio = pygame.image.load("Logos/features/bgui.jpg")
      logo = pygame.image.load("Logos/features/logo.png")
      eslogan = pygame.image.load("Logos/features/eslogan.png")
      eslogan = pygame.transform.scale(eslogan,(500,63))
      #cargamos la imagen sobre la pantalla
      screen.blit(imagen_inicio,(0,0))
      screen.blit(logo,(313, 100))
      screen.blit(eslogan,(262, 220))
      #actualizamos nuestro cursor
      cursor.update()
      #actualizamos el boton
      boton1.update(screen,cursor)
      boton2.update(screen,cursor)
      #actualizamos la pantalla
      pygame.display.update()
      #el reloj es para el control de fotogramas por segundos
      reloj.tick(30)

def confirmacion(ejecutar):
   #creamos el boton que sera el de "comenzar"
   boton1 = Boton(botonUtility,botonUtilityPress,611,340)
   boton2 = Boton(botonExit,botonExitPress,611,425)
   
   inicio = True
   while inicio:
      for eventos in pygame.event.get():
         #si dentro de la pantalla se detecta un click
         if eventos.type==pygame.MOUSEBUTTONDOWN:
            #si el cursor obtenido por la clase cursor , choca con el boton y se clickea
            if cursor.colliderect(boton1.rect):
               #salimos de la pantalla de inicio
               ejecutar = True
               inicio = False
               return ejecutar
               break
            if cursor.colliderect(boton2.rect):
               pygame.quit()
               quit()
         #en caso de que se aprete la X de la pantalla para que se cierre el prgrama, esta funcion esta en gran parte del codigo
         if eventos.type == pygame.QUIT:
            pygame.quit()
            quit()
      #definimos la imagen que se mostrara
      imagen_inicio = pygame.image.load("Logos/features/bgui.jpg")
      logo = pygame.image.load("Logos/features/logo.png")
      eslogan = pygame.image.load("Logos/features/eslogan.png")
      eslogan = pygame.transform.scale(eslogan,(500,63))
      atencion = pygame.image.load("Logos/features/atencion.png")
      atencion = pygame.transform.scale(atencion,(242,242))
      #cargamos la imagen sobre la pantalla
      screen.blit(imagen_inicio,(0,0))
      screen.blit(logo,(313, 100))
      screen.blit(eslogan,(262, 220))
      screen.blit(atencion,(100, 300))
      #actualizamos nuestro cursor
      cursor.update()
      #actualizamos el boton
      boton1.update(screen,cursor)
      boton2.update(screen,cursor)
      #actualizamos la pantalla
      pygame.display.update()
      #el reloj es para el control de fotogramas por segundos
      reloj.tick(30)

def ejecucion(start):   
   inicio = False
   while not(inicio):
      for eventos in pygame.event.get():
         #en caso de que se aprete la X de la pantalla para que se cierre el programa, esta funcion esta en gran parte del codigo
         if eventos.type == pygame.QUIT:
            pygame.quit()
            quit()
      main()
      pygame.quit()
      quit()
      


screen = pygame.display.set_mode(size)
ejecutar = False
start = True
while start:
   inicio()
   ejecutar = confirmacion(ejecutar)
   if ejecutar:
      #carga = Carga()
      start = ejecucion(start)
