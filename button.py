import pygame

from settings import Settings

class Button():

    def __init__(self, client, msg):
        """Initialize button attributes."""
        self.screen = client.screen
        self.settings = Settings()

        # Set the dimentions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (255, 234, 0) # yellow background for text aka button
        self.text_color = (217, 33, 33) # red text
        self.font = pygame.font.SysFont( None, 48) # Font and text size

        # Bild the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.settings.SCREEN_WIDTH//2
        self.rect.centery = self.settings.SCREEN_HEIGHT//2

        # Identify if the button is visible
        self.play_button_hide = False

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center the text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color) # Render msg as an image
        self.msg_image_rect = self.msg_image.get_rect() # Get rect to center msg within the button
        self.msg_image_rect.center = self.rect.center # Center msg inside of the button
            
    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect) # Draw a button
        self.screen.blit(self.msg_image, self.msg_image_rect) # Draw text inside of button