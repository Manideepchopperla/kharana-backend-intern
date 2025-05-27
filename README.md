# Python script that models a Mobius strip using parametric equations and computes key geometric properties

## Code Structure Overview
The code is organized as a class-based representation of a Möbius strip, encapsulated within a MobiusStrip class. The key components include:

### 1. Initialization (__init__):

  Takes in three parameters: R (radius), w (width), and n (resolution).
  
  Defines parameter grids u and v using np.linspace, and computes the 3D mesh (x, y, z) using the Möbius parametric equations.
  
  ### 2. compute_mesh():
  
  Computes the coordinates of the Möbius strip surface based on the parametric equations:
  
  ```

  ​x(u,v)=(R+v⋅cos⁡(u2))⋅cos⁡(u)
  
  y(u,v)=(R+v⋅cos⁡(u2))⋅sin⁡(u)
  
  z(u,v)=v⋅sin⁡(u2)
  
  Where: u ∈ [0 , 2π] and v ∈ [−w/2 , w/2]

  ```

 
### 3. surface_area():

Approximates the surface area using the double integral over the parameter space:
  ```

  A = ∫∫ ||(∂r/∂u) × (∂r/∂v)|| du dv 

  ```
This is done numerically using np.gradient to estimate partial derivatives and then computing the magnitude of their cross product at each point.

### 4. edge_length():

Approximates the combined length of the two boundary curves of the strip (top and bottom edges).

Uses Euclidean distance between consecutive points along each edge.
```

ds = sqrt(dx^2 + dy^2 + dz^2)

```

### 5. plot():

Visualizes the Möbius strip using matplotlib's 3D plotting capabilities.

### 6. Main Block:

Handles user input for parameters and prints the calculated surface area and edge length, then displays the plot.

## Surface Area Approximation
The Mobius strip's surface is represented as a parametric surface over two variables (u, v). The surface area is computed by:

Numerically approximating partial derivatives using np.gradient for ***∂x/∂u, ∂x/∂v, ∂y/∂u, ∂y/∂v, ∂z/∂u, ∂z/∂v***.

Computing the cross product of the tangent vectors 
```

cross_x = dy_du * dz_dv - dz_du * dy_dv

cross_y = dz_du * dx_dv - dx_du * dz_dv

cross_z = dx_du * dy_dv - dy_du * dx_dv

```

Calculating the norm of the cross product, giving the infinitesimal area element 

```

dA = np.sqrt(cross_x**2 + cross_y**2 + cross_z**2)

```

Summing over all grid elements of dA and multiply with du and dv to get the total surface area.

```

np.sum(dA) * du * dv

```

## Example :

  ### Input : 
  ```
  
  Radius(R) = 2

  Width(w) = 1

  Resoution(n) = 200
  
  ```

  ### Output : 

  ```

  Surface Area : 12.72 (apporx)

  Edge Length : 25.33 (apporx)

  ```
  ### Plot : 
![Screenshot 2025-05-26 224431](https://github.com/user-attachments/assets/1cbc7896-c5ba-4c99-bd14-601bdff9b44c)




## Contact

For any inquiries, please reach out to:

- **Name:** Manideep Chopperla
- **Email:** [manideepchopperla1808@gmail.com](mailto:manideepchopperla1808@gmail.com)
- **GitHub:** [Manideepchopperla](https://github.com/Manideepchopperla)

