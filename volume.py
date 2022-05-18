#!/usr/bin/env python3

# Created by Devin Jhu
# Created on May 2022
# The volume calculator

import math


def volume(radius, height):
    # this function calculates volume

    # process & output
    volume_number = (radius * radius) * height * math.pi

    print("the volume of your cylinder is {0:.1f} cm²".format(volume_number))


def main():
    # this function get base and height then calls the function
    height_string = input("Enter height (cm): ")
    radius_string = input("Enter base (cm): ")
    try:
        radius = int(radius_string)
        height = int(height_string)
        volume(radius, height)

    except Exception:
        print("not a number")
    print("\nDone.")


if __name__ == "__main__":
    main()
