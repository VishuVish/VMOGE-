import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the angles for the TP mode (φ = constant , θ = varies)
phi = np.linspace(0, 2* np.pi, 100)  # Polar angle 
H = 1  # Arbitrary magnetic field magnitude

# Calculate the magnetic field components
Hx_LT = H* np.cos(phi) # No x- component in TP Mode
Hy_LT = H* np.sin(phi) # No y-component in LP Mode
Hz_LT = np.zeros_like(phi) # No z-component in LT mode

# Create the 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the LT Mode field orbit
ax.plot(Hx_LT, Hy_LT, Hz_LT, label='LT Mode (x-y plane)', color='blue', linewidth=2)

# Add labels and title
ax.set_xlabel('Hx')
ax.set_ylabel('Hy')
ax.set_zlabel('Hz')
ax.set_title('LT Mode: Field Orbit in the {x,y}-Plane')

# Add a legend
ax.legend()

# Set equal aspect ratio for better visualization
ax.set_box_aspect([1, 1, 1])

# Show the plot
plt.show()