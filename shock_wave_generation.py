import numpy as np
from PIL import Image


def shock_wave_propagation(
        image_depth: int = 3, circle_radius: int = 100, wave_distortion: float = 1.05
) -> Image.Image:

    assert 1 <= wave_distortion <= 1.2, "distortion is not in range"
    assert 1 <= image_depth <= 8, "depth is not in range"
    assert 80 <= circle_radius <= 120, "circle radius is not in range"

    inner_color = np.array([256, 70, 40], dtype=int)
    rgba = Image.new('RGBA', (256, 256), (0, 0, 0, 0))
    for x in range(rgba.width):
        for y in range(rgba.height):
            # Find the distance to the center
            distance_to_center = np.sqrt((x - rgba.width // 2) ** 2 + (y - rgba.height // 2) ** 2)

            if distance_to_center <= circle_radius:
                # Make distanceToCenter on a scale from 0 to 1
                distance_to_center = distance_to_center / circle_radius

                # calculate pixel saturation
                saturation = inner_color * (np.exp(image_depth * distance_to_center) - 1) / (np.exp(image_depth) - 1)
                rgba.putpixel((x, y), tuple(np.append(inner_color, saturation.mean(dtype=int))))

            elif circle_radius <= distance_to_center <= wave_distortion * circle_radius:
                rgba.putpixel((x, y), tuple(np.append(inner_color, inner_color.mean(dtype=int))))
    return rgba


if __name__ == '__main__':
    depth = 3
    circle_size = 100
    distortion = 1.05

    shock_wave_propagation(depth, circle_size, distortion)
