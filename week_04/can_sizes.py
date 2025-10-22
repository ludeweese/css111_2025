#Team Activity

import math

def main():
    """
    Computes and prints the storage efficiency for 12 steel can sizes.
    """
    # Table of can sizes: (Name, Radius (cm), Height (cm))
    CAN_SIZES = [
        ("#1 Picnic", 6.83, 10.16),
        ("#1 Tall", 7.78, 11.91),
        ("#2", 8.73, 11.59),
        ("#2.5", 10.32, 11.91),
        ("#3 Cylinder", 10.79, 17.78),
        ("#5", 13.02, 14.29),
        ("#6Z", 5.40, 8.89),
        ("#8Z short", 6.83, 7.62),
        ("#10", 15.72, 17.78),
        ("#211", 6.83, 12.38),
        ("#300", 7.62, 11.27),
        ("#303", 8.10, 11.11)
    ]

    # Print table header
    print(f"{'Can Size':<11} {'Storage Efficiency':>18}")
    print("-" * 34)
    
    # Track the best efficiency
    best_efficiency = -1
    best_can_name = ""

    for name, radius, height in CAN_SIZES:
        # Calculate volume and surface area
        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        
        # Calculate storage efficiency
        storage_efficiency = volume / surface_area
        
        # Check for the best efficiency
        if storage_efficiency > best_efficiency:
            best_efficiency = storage_efficiency
            best_can_name = name
        
        # Print the result formatted to two decimals
        print(f"{name:<11} {storage_efficiency:>18.2f}")

    print("\n" + "-" * 34)
    print(f"The can size with the highest storage efficiency is: {best_can_name} ({best_efficiency:.2f})")

def compute_volume(radius, height):
    """
    Computes the volume of a cylinder.
    Volume = pi * radius^2 * height
    """
    return math.pi * radius**2 * height

def compute_surface_area(radius, height):
    """
    Computes the surface area of a cylinder (two ends and the side).
    Surface Area = 2 * pi * radius * (radius + height)
    """
    return 2 * math.pi * radius * (radius + height)

# Start the program
if __name__ == "__main__":
    main()
