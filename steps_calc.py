#!/usr/bin/env python

"""steps.py: Calculate the stepped ramp levels used by Anduril.
Usage: steps.py floor ceiling num_steps
For example:
    > ./steps.py 1 150 3
    1: 1
    2: 75
    3: 150
"""

def main(args):
    floor, ceil, steps = [int(x) for x in args[:3]]
    for i in range(steps):
        guess = floor + (i * (float(ceil-floor)/(steps-1)))
        this = nearest_level(guess, floor, ceil, steps)
        # print(f'{i+1}: {this}')
        print(f'{i+1}: {round(this)}')


def nearest_level(target, floor, ceil, steps):
    """Copied/adapted from anduril.c"""
    # bounds check
    mode_min = floor
    mode_max = ceil

    if target < mode_min: return mode_min
    if target > mode_max: return mode_max

    ramp_range = ceil - floor
    ramp_discrete_step_size = ramp_range / (steps-1)
    this_level = floor

    for i in range(steps):
        this_level = floor + (i * ramp_range / (steps-1))
        diff = abs(target - this_level)
        if diff <= (ramp_discrete_step_size / 2):
            return this_level

    return this_level


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
