import pygame

def resize(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)

def find_collision_window(item, width, height):
    rect = item.location.get_rect()
    rect.x = item.x
    rect.y = item.y
    #print(rect)
    #print("left", rect.left, " right", rect.right)
    #print("bottom", rect.bottom, " top", rect.top)
    if rect.right >= width or rect.left <= 0:
        item.x_Speed *= -1
    if rect.bottom >= height or rect.top <= 0:
        item.y_Speed *= -1
        
def find_collision_windowRect(rect, width, height):
    #print(rect)
    #print("left", rect.left, " right", rect.right)
    #print("bottom", rect.bottom, " top", rect.top)
    if rect.right >= width:
        rect.x -= 2
        return True
    if rect.left <= 0:
        rect.x += 2
        return True
    if rect.bottom >= height:
        rect.y -= 2
        return True
    if rect.top <= 0:
        rect.y += 2
        return True
    

collision_tolerance = 10
def find_collision_rect(rect, item):
    rect2 = item.location.get_rect()
    rect2.x = item.x
    rect2.y = item.y

    if rect.colliderect(rect2):
        if abs(rect.top - rect2.bottom) < collision_tolerance and item.y_Speed > 0:
            item.y_Speed *= -1
        if abs(rect.bottom - rect2.top) < collision_tolerance and item.y_Speed < 0:
            item.y_Speed *= -1
        if abs(rect.right - rect2.left) < collision_tolerance and item.x_Speed < 0:
            item.y_Speed *= -1
        if abs(rect.left - rect2.right) < collision_tolerance and item.x_Speed > 0:
            item.y_Speed *= -1
    return 0