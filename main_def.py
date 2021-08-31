def button_pressed_def(ev3):
    pressed = []
    while len(pressed) != 1:
        pressed = ev3.buttons.pressed()
    button = pressed[0]

    # Now wait for the button to be released.
    while any(ev3.buttons.pressed()):
        pass

    # Return which button was pressed.
    return button

def menu_display_def():
    if menu_interface_selecionador == 1:
        ev3.screen.load_image('./IMG_MENU/display_menu.png')

    if menu_interface_selecionador == 2:
        ev3.screen.load_image('./IMG_MENU/display_calibração.png')
    
    if menu_interface_selecionador == 3:
        ev3.screen.load_image('./IMG_MENU/display_problemas.png')

    if menu_interface_selecionador == 4:
        ev3.screen.load_image('./IMG_MENU/display_portview.png')

def menu_seleção_def():
    if button_pressed == Button.DOWN:
        menu_interface_selecionador += 2
        if menu_interface_selecionador == 5:
            menu_interface_selecionador = 1
        if menu_interface_selecionador == 6:
            menu_interface_selecionador = 2

    if button_pressed == Button.UP:
        menu_interface_selecionador -= 2
        if menu_interface_selecionador == 0:
            menu_interface_selecionador = 4
        if menu_interface_selecionador < 0:
            menu_interface_selecionador = 3

    if button_pressed == Button.RIGHT:
        menu_interface_selecionador += 1
        if menu_interface_selecionador == 5:
            menu_interface_selecionador = 1
    
    if button_pressed == Button.LEFT:
        menu_interface_selecionador -= 1
        if menu_interface_selecionador == 0:
            menu_interface_selecionador = 4
    
    if button_pressed == Button.CENTER:
        menu_função_def()

def menu_função_def():
    if menu_interface_selecionador == 1:
        ev3.screen.load_image('./IMG_TESTE/display_problemas_teste.png')

    if menu_interface_selecionador == 2:
        ev3.screen.load_image('./IMG_TESTE/display_problemas_teste.png')

    if menu_interface_selecionador == 3:
        ev3.screen.load_image('./IMG_TESTE/display_problemas_teste.png')

    if menu_interface_selecionador == 4:
        ev3.screen.load_image('./IMG_TESTE/display_problemas_teste.png')