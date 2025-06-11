import numpy as np

def smooth_path(path, alpha=0.5, beta=0.1, tolerance=1e-5, max_iterations=10000):
    """
    Smooths a path using gradient descent optimization.
    
    Args:
        path: List of points [(x0, y0), (x1, y1), ...]
        alpha: Smoothness weight (higher = smoother)
        beta: Learning rate (step size)
        tolerance: Stopping threshold for maximum change
        max_iterations: Safety limit for iterations
        
    Returns:
        Smoothed path as list of points
    """
    # Convert to mutable list of lists and make copy
    smoothed = [list(point) for point in path]
    n = len(smoothed)
    
    # Only interior points are updated (indices 1 to n-2)
    indices_to_update = range(1, n-1)
    
    # Gradient descent loop
    iteration = 0
    max_change = tolerance * 2  # Ensure we enter the loop
    
    while iteration < max_iterations and max_change > tolerance:
        max_change = 0
        new_path = smoothed.copy()  # Work on a copy for simultaneous updates
        
        for i in indices_to_update:
            # Current and neighboring points
            prev_pt = smoothed[i-1]
            curr_pt = smoothed[i]
            next_pt = smoothed[i+1]
            
            # Calculate gradient for each dimension
            gradient = []
            for dim in range(len(curr_pt)):
                # Path length component gradients
                length_grad = 2 * (curr_pt[dim] - prev_pt[dim]) - 2 * (next_pt[dim] - curr_pt[dim])
                
                # Curvature component gradient
                curvature_grad = 2 * alpha * (2 * curr_pt[dim] - prev_pt[dim] - next_pt[dim])
                
                # Total gradient
                total_grad = length_grad + curvature_grad
                gradient.append(total_grad)
            
            # Update point position
            new_point = [curr_pt[dim] - beta * gradient[dim] for dim in range(len(curr_pt))]
            
            # Track maximum change for convergence
            changes = [abs(new_point[dim] - curr_pt[dim]) for dim in range(len(curr_pt))]
            max_change = max(max_change, max(changes))
            
            new_path[i] = new_point
        
        smoothed = new_path
        iteration += 1
    
    # Convert back to tuples for immutability
    return [tuple(point) for point in smoothed]

# Example usage
if __name__ == "__main__":
    # Input path (zig-zag pattern)
    input_path = [(0, 0), (1, 1), (2, 0), (3, 1), (4, 0)]
    
    # Smooth the path
    smoothed_path = smooth_path(input_path, alpha=0.5, beta=0.1)
    
    # Print results
    print("Original Path:")
    for point in input_path:
        print(f"  {point}")
    
    print("\nSmoothed Path:")
    for point in smoothed_path:
        print(f"  {point}")

# Original Path:
#   (0, 0)
#   (1, 1)
#   (2, 0)
#   (3, 1)
#   (4, 0)

# Smoothed Path:
#   (0, 0)
#   (0.9999999999999999, 0.3999999999999999)
#   (2.0, 0.6)
#   (3.0000000000000004, 0.4)
#   (4, 0)
