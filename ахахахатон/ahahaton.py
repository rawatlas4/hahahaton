import pygame

pygame.init()

WHITE = (255, 255, 255)

win = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

images = []

background_path = "fon.jpg"#фон загружаем и до размеров окна добавляем в список
background = pygame.image.load(background_path)
background = pygame.transform.scale(background, (1280, 720))
images.append(background)



class Label():
    def __init__(self, x=10, y=10, fsize=30, color=WHITE):
        self.font = pygame.font.SysFont("verdana", fsize)  # Вибір шрифта
        self.text = ""
        self.color = color
        self.x = x
        self.y = y

    def set_text(self, text):
        self.text = text  # Задати текст

    def draw(self):
        text_surface = self.font.render(self.text, True, self.color)  # Створити поверхню з текстом
        win.blit(text_surface, (self.x, self.y))  # Вивести текст на екран

    def is_clicked(self, mouse_pos):
        text_surface = self.font.render(self.text, True, self.color)
        rect = text_surface.get_rect(topleft=(self.x, self.y))
        return rect.collidepoint(mouse_pos)




exit_label = Label(10,10,40,WHITE)
exit_label.set_text("EXIT")


exxit = False
while not exxit:
    win.blit(images[0],(0,0))
    exit_label.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Вихід з гри
            exxit = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos  # Отримуємо координати кліку
            if exit_label.is_clicked((x,y)):
                exxit = True
    # Оновлення дисплея
    pygame.display.update()
    clock.tick(40)  # FPS = 40
# Вихід з гри
pygame.quit()