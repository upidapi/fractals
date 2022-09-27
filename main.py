import pygame as pg


def serpinski_points(p1, p2, p3):
    """
      p3
    p1  p2

        p3
      r2  r1
    p1  r3  p2

          p3
        p1  p2
      p3      p3
    p1  p2  p1  p2
    """

    half_x = (p3[0] - p1[0]) / 2
    half_y = (p3[1] - p1[1]) / 2

    r1 = (p1[0] + half_x * 3, p1[1] - half_y)
    r2 = (p1[0] + half_x * 1, p1[1] - half_y)
    r3 = (p1[0] + half_x * 2, p1[1])

    return r1, r2, r3


def call_serpinski(p1, p2, p3):
    sub_triangle = serpinski_points(p1, p2, p3)
    sub =


pg.init()

while True:
    pass
