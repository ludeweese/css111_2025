#Milestone Activity week 05
#Lucilene DeWeese

"""Compute water pressure and losses for a city water system.

This module contains functions to calculate:
1. Height of water column in an elevated tank.
2. Pressure gain due to gravity on the water column.
3. Pressure loss due to friction in pipes.
"""

# Constants
WATER_DENSITY = 998.2          # Density of water in kilograms per cubic meter (kg/m^3)
EARTH_ACCELERATION = 9.80665   # Acceleration due to Earth's gravity in meters per second squared (m/s^2)


def water_column_height(tower_height, tank_height):
    """
    Calculate the height of the water column in meters.

    Formula:
        h = t + (3/4) * w
    where:
        h = height of the water column (m)
        t = height of the tower (m)
        w = height of the walls of the tank on top of the tower (m)

    This formula accounts for the tank's wall height contributing
    partially (3/4) to the total water column height.
    """
    h = tower_height + (3 * tank_height / 4)
    return h


def pressure_gain_from_water_height(height):
    """
    Calculate the pressure gain (kPa) caused by the water column's height.

    Formula:
        P = (ρ * g * h) / 1000
    where:
        P = pressure in kilopascals (kPa)
        ρ = density of water (998.2 kg/m^3)
        g = acceleration due to gravity (9.80665 m/s^2)
        h = height of water column (m)

    The division by 1000 converts from Pascals (Pa) to kilopascals (kPa).
    """
    pressure = (WATER_DENSITY * EARTH_ACCELERATION * height) / 1000
    return pressure


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    Calculate the pressure loss (kPa) due to friction in a pipe.

    Formula:
        P = - (f * L * ρ * v^2) / (2000 * d)
    where:
        P = pressure loss in kilopascals (kPa)
        f = friction factor of the pipe (unitless)
        L = length of the pipe (m)
        ρ = density of water (998.2 kg/m^3)
        v = velocity of water in the pipe (m/s)
        d = diameter of the pipe (m)

    The negative sign indicates that this is a pressure loss (reduction).
    The division by 2000 accounts for unit conversion to kilopascals.
    """
    pressure_loss = (-friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2) / (2000 * pipe_diameter)
    return pressure_loss
