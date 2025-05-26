import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class MobiusStrip:
    def __init__(self, R, w, n):
        self.R = R   # Radius of the strip
        self.w = w   # Width of the strip
        self.n = n   # Number of points to discretize the strip
        self.u = np.linspace(0, 2 * np.pi, n)  # Parameter u varies from 0 to 2π
        self.v = np.linspace(-w / 2, w / 2, n)  # Parameter v varies from -w/2 to w/2
        self.x, self.y, self.z = self.compute_mesh() 

    def compute_mesh(self):
        """Compute the 3D mesh/grid of (x, y, z) points on the surface."""
        u, v = np.meshgrid(self.u, self.v)
        # Parametric equations for the Mobius strip
        
        x = (self.R + v * np.cos(u / 2)) * np.cos(u) # x(u,v)=(R+v⋅cos⁡(u2))⋅cos⁡(u)
        y = (self.R + v * np.cos(u / 2)) * np.sin(u) # y(u,v)=(R+v⋅cos⁡(u2))⋅sin⁡(u)
        z = v * np.sin(u / 2) # z(u,v)=v⋅sin⁡(u2)
        return x, y, z

    def surface_area(self):
        """Calculate the surface area of the Mobius strip."""
        # Using the formula for surface area of a parametric surface 
        # A = ∫∫ ||(∂r/∂u) × (∂r/∂v)|| dudv 
        # where r(u, v) = (x(u, v), y(u, v), z(u, v))
        
        # Compute parameter differentials (du and dv)
        du = self.u[1] - self.u[0]
        dv = self.v[1] - self.v[0]

        # Compute the partial derivatives
        dx_du, dx_dv = np.gradient(self.x, du, dv)
        dy_du, dy_dv = np.gradient(self.y, du, dv)
        dz_du, dz_dv = np.gradient(self.z, du, dv)

        # Cross product of tangent vectors
        # (∂r/∂u) = (dx_du, dy_du, dz_du)
        # (∂r/∂v) = (dx_dv, dy_dv, dz_dv)
        # Compute the cross product of ∂r/∂u and ∂r/∂v at each (u,v) 
        cross_x = dy_du * dz_dv - dz_du * dy_dv
        cross_y = dz_du * dx_dv - dx_du * dz_dv
        cross_z = dx_du * dy_dv - dy_du * dx_dv

        # Magnitude of the cross product gives the area element
        # ||(∂r/∂u) × (∂r/∂v)||
        dA = np.sqrt(cross_x**2 + cross_y**2 + cross_z**2)

        # The surface area is approximated by summing the area elements
        return np.sum(dA) * du * dv


    def edge_length(self):
        """Calculate the length of the Mobius strip's edge."""

        # Extract the two edges of the Mobius strip from the coordinate arrays:
        # The first row (index 0) and the last row (index -1) of x, y, z represent the two edges
        edge = np.array([
            [self.x[0, :], self.y[0, :], self.z[0, :]],
            [self.x[-1, :], self.y[-1, :], self.z[-1, :]]
        ])
        total_length = 0

        # Iterate over both edges to calculate their lengths
        for edge_points in edge:
            x, y, z = edge_points

            # Compute the differences between consecutive points along the edge
            dx = np.diff(x)
            dy = np.diff(y)
            dz = np.diff(z)

            # Calculate the Euclidean distance between consecutive points
            # ds = sqrt(dx^2 + dy^2 + dz^2)
            ds = np.sqrt(dx**2 + dy**2 + dz**2)

            # Sum the distances to get the total length of the edge
            total_length += np.sum(ds)


        return total_length # Return combined length of both edges


    def plot(self):
        """Visualize the Mobius strip."""
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.x, self.y, self.z, color='cyan', edgecolor='k', alpha=0.7)
        ax.set_title('Mobius Strip')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
        plt.show()

# Example usage
if __name__ == "__main__":
    R = float(input("Enter the radius of the Mobius strip (R): "))
    w = float(input("Enter the width of the Mobius strip (w): "))
    n = int(input("Enter the number of points (n): "))
    mobius = MobiusStrip(R, w, n)
    
    print(f"Surface Area: {mobius.surface_area()}")
    print(f"Edge Length: {mobius.edge_length()}")
    
    mobius.plot()