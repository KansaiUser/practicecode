def will_collide(vehicle_path, obstacle_path):
    max_len = max(len(vehicle_path), len(obstacle_path))
    
    # Extend the shorter path by repeating its last position
    if len(vehicle_path) < max_len:
        vehicle_path += [vehicle_path[-1]] * (max_len - len(vehicle_path))
    if len(obstacle_path) < max_len:
        obstacle_path += [obstacle_path[-1]] * (max_len - len(obstacle_path))
    
    # Compare positions at each time step
    for t in range(max_len):
        if vehicle_path[t] == obstacle_path[t]:
            return True  # Collision detected
    return False


# Test case 1
v1 = [(0,0), (1,0), (2,0), (3,0)]
o1 = [(0,2), (1,2), (2,0), (3,0)]
print(will_collide(v1, o1))  # True (collision at t=2 and t=3)

# Test case 2
v2 = [(0,0), (1,0), (2,0)]
o2 = [(0,1), (1,1), (2,1)]
print(will_collide(v2, o2))  # False
