# Smooth shock wave effect

## For running the application were used:
* __PyCharm 2020.3.2 (Professional Edition) Build #PY-203.6682.179, built on December 30, 2020__
* __Runtime version: 11.0.9.1+11-b1145.63 amd64__
* __VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.__
* __Windows 10 10.0__

## For compiling source code following libraries were used:
* __pygame==2.0.1__ 
* __pip==21.0.1__ 
* __numpy==1.21.2__
* __pillow==8.3.2__

## How-to-use:
* __pip install -r requirements__
* __Ctrl+Shift+F10__

## Image loading:
* Drop image to project folder and specify it's name as shown below: \
`filename = "Background_image.jpg"` \
`Image = pygame.image.load(filename)`


## Shock wave params:

* __wave_propagation_velocity__ by default is `5`, in range `0 <= wave_propagation_velocity <= 30`
* __wave_distortion__ by default is `1.05`, in range `1 <= wave_distortion <= 1.2`
* __image_depth__ by default is `3`, in range `1 <= image_depth <= 8`
* __circle_radius__ by default is `5`, in range `80 <= circle_radius <= 120`
