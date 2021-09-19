import pygame
from shock_wave_generation import shock_wave_propagation
import numpy as np
import argparse
import os

"""

Variable params

"""
wave_propagation_velocity = 5
depth = 3
circle_size = 100
distortion = 1.05

"""

Stable params

"""

FPS = 60
display_width = 640
display_height = 480
wave_width, wave_height = 256, 256
clock = pygame.time.Clock()
pygame.display.set_caption('SRK project')


class Scale(pygame.sprite.Sprite):

    assert 1 <= wave_propagation_velocity <= 30, 'wave_propagation_velocity is not in range'

    def __init__(self, xy_pos, image):
        super().__init__()
        self.original_image = image
        self.image = image
        self.image = pygame.transform.scale(self.original_image, (wave_width, wave_height))
        self.rect = self.image.get_rect(center=xy_pos)
        self.mode = 1
        self.grow = 0

    def update(self):
        if self.grow > 1000:
            self.rect = self.image.get_rect(
                center=(
                    np.random.randint(int(display_width/6),
                                      int(display_width/1.2)),
                    np.random.randint(int(display_height/6),
                                      int(display_height/1.2))
                )
            )
            self.grow = 0
        if self.grow >= 1:
            pass
        else:
            self.mode = 1
        self.grow += wave_propagation_velocity * self.mode
        orig_x, orig_y = self.original_image.get_size()
        size_x = orig_x + round(self.grow)
        size_y = orig_y + round(self.grow)
        self.image = pygame.transform.smoothscale(self.original_image, (size_x, size_y))
        self.rect = self.image.get_rect(center=self.rect.center)


class NotScale(pygame.sprite.Sprite):

    def __init__(self, center, image):

        assert filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')), "file is not an image"

        super().__init__()
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect(center=center)

    def update(self):
        self.rect = self.image.get_rect(center=self.rect.center)


def random_blast_point():

    x_pos = np.random.randint(0, display_width + 1)
    y_pos = np.random.randint(0, display_height + 1)
    return x_pos, y_pos


def get_parser():
    parser = argparse.ArgumentParser(description='Smooth shockwave propagation',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-im', '--bg_image', required=True, type=str,
                        help='path to filename background image')
    parser.add_argument('-wpv', '--wave_propagation_velocity is in range 0 <= wave_propagation_velocity <= 30', default=5, type=int,
                        help='wave ')
    parser.add_argument('-wd', '--wave_distortion', default=1.05, type=float,
                        help='wave_distortionis in range 1 <= wave_distortion <= 1.2')
    parser.add_argument('-id', '--image_depth', default=3, type=int,
                        help='image_depth is in range 1 <= image_depth <= 8')
    parser.add_argument('-cr', '--circle_radius', default=100, tye=int,
                        help='circle_radius is in range 80 <= circle_radius <= 120')
    return parser


pygame.init()


if __name__ == "__main__":

    """
    
    Input image loading
    
    """
    args = get_parser().parse_known_args()[0]
    filename = args.bg_image  # or specify path to your background image (ex. filename = "Background_image.jpg")
    assert os.path.exists(filename)
    Image = pygame.image.load(filename)

    Image = pygame.transform.scale(Image, (display_width, display_height))

    wave = shock_wave_propagation(depth, circle_size, distortion)
    wave = pygame.image.fromstring(wave.tobytes(), wave.size, wave.mode)
    wave = pygame.transform.scale(wave, (wave_width, wave_height))

    window = pygame.display.set_mode((display_width, display_height))

    sprite = NotScale(window.get_rect().center, Image)
    halo = Scale(random_blast_point(), wave)

    group = pygame.sprite.Group(sprite, halo)

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        group.update()
        group.draw(window)
        pygame.display.flip()

    pygame.quit()
    exit()
