import numpy as np

"""
CODE-GEO V3.2: Latency Field Dynamics (phi)
-------------------------------------------
Visualizes the scalar field trajectory phi(z).
Logic: The field tracks the holographic refresh rate, 
freezing at low redshift to trigger 'Cosmic Overclocking'.
"""

def simulate_field_trajectory():
    # --- PHYSICAL PARAMETERS ---
    Z_STAR = 0.67       # Dark Energy Pivot
    PHI_STAR = 1.0      # Normalized field amplitude
    Z_WALL = 0.245      # BBN Wall Thaw-point
    NW = 14.0           # Wall Steepness

    # Redshift range: Local (0) to Early Matter Domination (10)
    z_range = [0.0, 0.1, 0.245, 0.67, 1.5, 5.0, 10.0]

    print("\n" + "="*85)
    print(f"{'LATENCY FIELD DYNAMICS (PHI): CODE-GEO V3.2':^85}")
    print("="*85)
    print(f"{'Redshift (z)':<15} | {'Field Value phi(z)':<20} | {'W(z) Thaw':<15} | {'State'}")
    print("-" * 85)

    for z in z_range:
        # 1. Claude-Frey Trajectory: phi(z) = phi_star * arctan((1+z)/(1+z_star))
        phi_z = PHI_STAR * np.arctan((1 + z) / (1 + Z_STAR))
        
        # 2. Wall Suppression (W) determines if the field is active
        # W -> 1 means field is 'thawed' (Local)
        # W -> 0 means field is 'frozen' (Global)
        w_z = 1.0 / (1.0 + ((1 + z)/(1 + Z_WALL))**NW)
        
        if z < 0.245:
            state = "THAWED (LOCAL)"
        elif z < 0.67:
            state = "TRANSITION"
        else:
            state = "FROZEN (GLOBAL)"

        print(f"{z:<15.3f} | {phi_z:<20.4f} | {w_z:<15.2e} | {state}")

    print("-" * 85)
    print(f"[*] PIVOT: z_star = {Z_STAR} (Dark Energy dominance)")
    print(f"[*] SCALE: Field saturates at pi/2 * phi_star at high redshift.")
    print("="*85 + "\n")

if __name__ == "__main__":
    simulate_field_trajectory()
