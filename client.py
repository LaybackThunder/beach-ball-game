import pygame, sys

from settings import Settings
from ball import Ball

class Client():
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init() # Instantiate pygame modules
        self.settings = Settings() # Instance Settings

        # Pygame screen
        self.screen = pygame.display.set_mode(
            (self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        pygame.display.set_caption('Beach Ball') # Add string to top of game's window

        # Instanciate objects
        self.ball = Ball(self)

        # Colors and background color
        self.LIGHT_GRAY = (230, 230, 230)
        self.BACKGROUND_COLOR = (self.LIGHT_GRAY)

        # Clock
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._check_ball_update()
            self._update_screen()  
            self.clock.tick(self.FPS)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            self._check_buttondown_events(event)

    def _update_screen(self):
        """Update images on teh screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop 
        self.screen.fill(self.settings.BACKGROUND_COLOR)
        self.ball.blitme()

        # Make most recently drawn screen visible; like animation
        pygame.display.flip()

    def _check_buttondown_events(self, event):
        """Checks all button down events."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            self._check_click_ball(mouse_pos)

    def _check_click_ball(self, mouse_pos):
        """Change ball direction when clicked."""
        if self.ball.rect.collidepoint(mouse_pos):
            # change ball x and y directions
            self.ball.change_ball_x_direction()
            self.ball.change_ball_y_direction()

    def _check_wall_collition(self):
        """Ball bounces if it hits the walls or floor or ceiling."""
        # Walls
        if self.ball.rect.left <= 0 or self.ball.rect.right >= self.settings.SCREEN_WIDTH:
            self.ball.change_ball_x_direction()
        # Floor and ceiling
        if self.ball.rect.top <= 0 or self.ball.rect.bottom >= self.settings.SCREEN_HEIGHT:
            self.ball.change_ball_y_direction()

    def _check_ball_update(self):
        """Check for ball update and its collitions."""
        self.ball.update()
        self._check_wall_collition()

if __name__ == '__main__':
    # Make game instance and run the game.
    client = Client()
    client.run_game()