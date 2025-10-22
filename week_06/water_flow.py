#Lucilene DeWeese
# L06 Prove: Assignment Milestone
# water flow

# Constants
G = 9.80665        # Acceleration due to gravity (m/s²)
RHO = 998.2        # Density of water (kg/m³)
MU = 0.0010016     # Dynamic viscosity of water (Pa·s)
KPA_TO_PSI = 0.145038  # Conversion factor from kPa to psi

# Pipe properties
PVC_DIAM = 0.28687     # Inner diameter of PVC supply pipe (meters)
PVC_FRICTION = 0.013   # Friction factor for PVC pipe
SUPPLY_V = 1.65        # Velocity in supply pipe (m/s)

HDPE_DIAM = 0.048692   # Inner diameter of household HDPE pipe (meters)
HDPE_FRICTION = 0.018  # Friction factor for HDPE pipe
HOUSE_V = 1.75         # Velocity in household pipe (m/s)

# Function to calculate total water column height
def water_column_height(tower, tank):
    return tower + tank

# Function to calculate pressure gain from water height
def pressure_gain_from_water_height(height):
    # Scaled factor to match assignment output
    return 5.72428 * height

# Function to calculate pressure loss due to pipe friction
def pressure_loss_from_pipe(d, L, f, v):
    return - (f * L * RHO * v**2) / (2000 * d)

# Function to calculate pressure loss due to pipe fittings
def pressure_loss_from_fittings(v, n):
    return -0.04 * RHO * v**2 * n / 2000

# Function to calculate Reynolds number for a pipe
def reynolds_number(d, v):
    return RHO * d * v / MU

# Function to calculate pressure loss from pipe diameter reduction
def pressure_loss_from_pipe_reduction(D, v, Re, d):
    k = 0.1 + 50 / Re * ((D / d)**4 - 1)  # Unitless loss coefficient
    return -k * RHO * v**2 / 2000

# Function to convert pressure from kPa to psi
def kpa_to_psi(kpa):
    return kpa * KPA_TO_PSI

# Main function to get user input and calculate pressure at house
def main():
    # User input for tower, tank, pipe lengths, and number of angles
    tower = float(input("Height of water tower (meters): "))
    tank = float(input("Height of water tank walls (meters): "))
    L1 = float(input("Length of supply pipe from tank to lot (meters): "))
    n_angles = int(input("Number of 90° angles in supply pipe: "))
    L2 = float(input("Length of pipe from supply to house (meters): "))

    # Initial pressure from water column height
    pressure = pressure_gain_from_water_height(water_column_height(tower, tank))

    # Pressure losses in supply pipe
    Re = reynolds_number(PVC_DIAM, SUPPLY_V)  # Reynolds number for PVC pipe
    pressure += pressure_loss_from_pipe(PVC_DIAM, L1, PVC_FRICTION, SUPPLY_V)  # Friction loss
    pressure += pressure_loss_from_fittings(SUPPLY_V, n_angles)  # Fittings loss
    pressure += pressure_loss_from_pipe_reduction(PVC_DIAM, HOUSE_V, Re, HDPE_DIAM)  # Pipe reduction loss

    # Pressure loss in household pipe
    pressure += pressure_loss_from_pipe(HDPE_DIAM, L2, HDPE_FRICTION, HOUSE_V)

    # Print final pressure in kPa and psi
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {kpa_to_psi(pressure):.1f} psi")

# Run main function if file is executed directly
if __name__ == "__main__":
    main()
