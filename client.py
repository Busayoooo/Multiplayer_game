import pygame

# Set up window dimensions and game window
width = 700
height = 600
win = pygame.display.set_mode((width, height))  # Create a window
pygame.display.set_caption("Hi")

# Initialize Client Number (you can modify this if needed)
ClientNumber = 0

# Define player class
class player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3  # Player speed

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()  # Get the state of all keys

        # Move left
        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        # Move right
        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        # Move up
        if keys[pygame.K_UP]:
            self.y -= self.vel

        # Move down
        if keys[pygame.K_DOWN]:
            self.y += self.vel

        # Update the player's rect position
        self.rect = (self.x, self.y, self.width, self.height)

# Function to redraw the window and update game state
def redrawWindow(win, player):
    win.fill((255, 255, 255))  # Fill the window with white
    player.draw(win)  # Draw the player
    pygame.display.update()  # Update the display

# Main loop that keeps the game running
def main():
    run = True
    p = player(50, 50, 50, 50, (0, 0, 255))  # Create a player object
    clock = pygame.time.Clock()  # Create a clock object to control FPS

    while run:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the player closes the window
                run = False
                pygame.quit()  # Quit pygame

        p.move()  # Move the player
        redrawWindow(win, p)  # Redraw the window
        clock.tick(60)  # Set the frame rate to 60 FPS

# Run the game
main()
