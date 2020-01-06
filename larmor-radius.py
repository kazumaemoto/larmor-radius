#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
def main():

  # Get mass
  mass = get_mass()

  # Get temperature
  temperature = get_temperature()

  # Get thermal velocity
  thermal_velocity = get_thermal_velocity(temperature, mass)

  # Get magnetic field
  magnetic_field = get_magnetic_field()

  # Get larmor radius
  larmor_radius = get_larmor_radius(mass, thermal_velocity, magnetic_field)

  # Print
  print('Larmor radius (m): %f' % larmor_radius)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Get larmor radius
#------------------------------------------------------------------------------
def get_larmor_radius(mass, thermal_velocity, magnetic_field):

  # Import
  from scipy.constants import e

  # Get larmor radius
  larmor_radius = mass * thermal_velocity / (e * magnetic_field)

  # Return
  return larmor_radius
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Get magnetic field
#------------------------------------------------------------------------------
def get_magnetic_field():

  while True:
    # Input
    magnetic_field = input('Magnetic field (T): ')

    # Convert
    magnetic_field = float(magnetic_field)

    # Check magnetic_field
    if (magnetic_field > 0.0):
      # Break
      break
    else:
      print('Invalid.')

  # Return
  return magnetic_field
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Get mass
#------------------------------------------------------------------------------
def get_mass():

  # Import
  from scipy.constants import Avogadro, electron_mass

  # Set atomic weight
  atomic_weight = {'e': 0.0, 'Ar': 39.792, 'Kr': 83.798, 'Xe': 131.293}

  while True:
    # Input
    particle = input('Particle: ')

    # Check particle
    if particle in atomic_weight.keys():
      # Break
      break
    else:
      print('Invalid.')

  # Branch for particle
  if (particle == 'e'):
    # Set mass
    mass = electron_mass
  else:
    # Set mass
    mass = atomic_weight[particle] / Avogadro * 1.0e-3

  # Return
  return mass
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Get temperature
#------------------------------------------------------------------------------
def get_temperature():

  while True:
    # Input
    temperature = input('Temperature (eV): ')

    # Convert
    temperature = float(temperature)

    # Check temperature
    if (temperature > 0.0):
      # Break
      break
    else:
      print('Invalid.')

  # Return
  return temperature
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Get thermal velocity
#------------------------------------------------------------------------------
def get_thermal_velocity(temperature, mass):

  # Import
  from numpy import sqrt
  from scipy.constants import e, pi

  # Get thermal velocity
  thermal_velocity = sqrt(8.0 * e * temperature / (pi * mass))

  # Return
  return thermal_velocity
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Call main
#------------------------------------------------------------------------------
if __name__ == '__main__':
  main()
#------------------------------------------------------------------------------
