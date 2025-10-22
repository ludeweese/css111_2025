# Lucilene DeWeese
# L06 Prove: Assignment Milestone
#test water flow

# Import pytest for testing and all functions from water_flow.py to be tested
import pytest
from water_flow import (
    water_column_height,
    pressure_gain_from_water_height,
    pressure_loss_from_pipe,
    pressure_loss_from_fittings,
    reynolds_number,
    pressure_loss_from_pipe_reduction,
    kpa_to_psi
)
# Test water_column_height function
# Verify correct sum of tower and tank heights
def test_water_column_height():
    assert water_column_height(36.6, 9.1) == 45.7
    assert water_column_height(0, 0) == 0
    assert water_column_height(10, 5) == 15
    assert water_column_height(1.5, 0.5) == 2.0

# Test pressure_gain_from_water_height function
# Verify pressure gain from water height (using scaled factor)
def test_pressure_gain_from_water_height():
    assert pytest.approx(pressure_gain_from_water_height(45.7), 0.1) == 261.7
    assert pressure_gain_from_water_height(0) == 0
    assert pytest.approx(pressure_gain_from_water_height(10), 0.01) == 57.24

# Test pressure_loss_from_pipe function
# Verify pressure loss from friction in a pipe
def test_pressure_loss_from_pipe():
    assert pytest.approx(pressure_loss_from_pipe(0.28687, 1524.0, 0.013, 1.65), 0.001) == -93.842
    assert pressure_loss_from_pipe(0.048692, 15.2, 0.018, 1.75) < 0
    assert pressure_loss_from_pipe(0.2, 0, 0.015, 1.0) == 0

# Test pressure_loss_from_fittings function
# Verify pressure loss due to pipe fittings
def test_pressure_loss_from_fittings():
    assert pytest.approx(pressure_loss_from_fittings(0, 3), 0.001) == 0.0
    assert pytest.approx(pressure_loss_from_fittings(1.65, 0), 0.001) == 0.0
    assert pytest.approx(pressure_loss_from_fittings(1.65, 2), 0.001) == -0.1087
    assert pytest.approx(pressure_loss_from_fittings(1.75, 2), 0.001) == -0.12228
    assert pytest.approx(pressure_loss_from_fittings(1.75, 5), 0.001) == -0.306

# Test reynolds_number function
# Verify Reynolds number calculation for different diameters and velocities
def test_reynolds_number():
    assert pytest.approx(reynolds_number(0.048692, 0), 1) == 0
    assert pytest.approx(reynolds_number(0.048692, 1.65), 1) == 80069
    assert pytest.approx(reynolds_number(0.048692, 1.75), 1) == 84922
    assert pytest.approx(reynolds_number(0.28687, 1.65), 1) == 471729
    assert pytest.approx(reynolds_number(0.28687, 1.75), 1) == 500318

# Test pressure_loss_from_pipe_reduction function
# Verify pressure loss due to pipe diameter reduction
def test_pressure_loss_from_pipe_reduction():
    assert pytest.approx(pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692), 0.001) == 0.0
    assert pytest.approx(pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692), 0.001) == -0.309
    assert pytest.approx(pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692), 0.001) == -0.33673

# Test kpa_to_psi conversion function
# Verify conversion from kilopascals to psi
def test_kpa_to_psi():
    assert pytest.approx(kpa_to_psi(0), 0.001) == 0
    assert pytest.approx(kpa_to_psi(100), 0.001) == 14.5038
    assert pytest.approx(kpa_to_psi(158.7), 0.001) == 23.03
    assert pytest.approx(kpa_to_psi(344.738), 0.001) == 50.0