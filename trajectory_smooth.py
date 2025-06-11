def smooth_path(path, window_size):
    n = len(path)
    half_w = window_size // 2
    smoothed = []

    for i in range(n):
        # Determine window boundaries
        start = max(0, i - half_w)
        end = min(n, i + half_w + 1)

        # Extract points in the window
        window_points = path[start:end]

        # Compute average x and y
        avg_x = sum(p[0] for p in window_points) / len(window_points)
        avg_y = sum(p[1] for p in window_points) / len(window_points)

        smoothed.append((avg_x, avg_y))

    return smoothed

# Example usage
if __name__ == "__main__":
    path = [(0,0), (1,2), (2,4), (3,6), (4,8)]
    window_size = 3
    smoothed_path = smooth_path(path, window_size)
    print(smoothed_path)


path = [(0,0), (1,2), (2,4), (3,6), (4,8)]
window_size = 3

# smoothed_path = smooth_path(path, window_size)
# print(smoothed_path)
# # Expected output (approximately):
# # [(0.5, 1.0), (1.0, 2.0), (2.0, 4.0), (3.0, 6.0), (3.5, 7.0)]
