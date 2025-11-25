import pygame, sys
pygame.init()

# Setup
screen = pygame.display.set_mode((400, 300))
font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()

PIN = "1234"
balance = 1000
input_text = ""
state = "pin"  # pin, menu, withdraw

def draw(texts):
    screen.fill((30, 30, 30))
    for i, t in enumerate(texts):
        screen.blit(font.render(t, True, (255,255,255)), (20, 30 + i*40))
    pygame.display.flip()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif e.key == pygame.K_RETURN:
                if state == "pin":
                    if input_text == PIN:
                        state = "menu"
                    input_text = ""
                elif state == "withdraw":
                    if input_text.isdigit():
                        amt = int(input_text)
                        if amt > balance:
                            amt = balance
                        balance -= amt
                    input_text = ""
                    state = "menu"
            elif state == "menu" and balance > 0 and e.key == pygame.K_w:
                state = "withdraw"
            else:
                input_text += e.unicode

    # Draw screen based on state
    if state == "pin":
        draw(["Enter PIN:", input_text])
    elif state == "menu":
        if balance > 0:
            draw([f"Balance: ${balance}", "Press W to Withdraw"])
        else:
            draw(["Balance: $0", "No balance left!"])
    elif state == "withdraw":
        draw([f"Enter amount to withdraw (max ${balance}):", input_text])

    clock.tick(30)

