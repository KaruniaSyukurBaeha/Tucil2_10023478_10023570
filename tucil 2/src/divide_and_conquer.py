import numpy as np
import matplotlib.pyplot as plt

def bezier_quadratic_divide_conquer(P, num_points):
    def bezier(t, points):
        n = len(points)
        if n == 1:
            return points[0]
        else:
            Q = [(1 - t) * points[i] + t * points[i + 1] for i in range(n - 1)]
            return bezier(t, Q)

    def de_casteljau(t, points):
        n = len(points)
        if n == 1:
            return points[0]
        else:
            Q = [(1 - t) * points[i] + t * points[i + 1] for i in range(n - 1)]
            return de_casteljau(t, Q)

    curve_points = []
    plt.plot([p[0] for p in P], [p[1] for p in P], 'ro-', alpha=0.5)  # Plot garis yang menghubungkan titik kontrol

    for i in range(num_points):
        t = i / (num_points - 1)
        point = de_casteljau(t, P)
        curve_points.append(point)

        # Visualisasi proses pembentukan kurva
        plt.plot(point[0], point[1], 'go')  # Gambar titik pada kurva Bézier yang sedang diproses
        plt.title('Bezier Curve Construction (Divide and Conquer)')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        plt.pause(0.01)

    # Gambar garis yang menghubungkan titik kontrol yang sudah diproses
    plt.plot([p[0] for p in P], [p[1] for p in P], 'b-')

    return curve_points

# Contoh penggunaan:
num_control_points = 3
P = np.array([[0, 0], [1, 2], [2, 0]])  # Buat titik kontrol
num_points = 100
curve_points = bezier_quadratic_divide_conquer(P, num_points)

# Plot kurva Bézier
curve_points = np.array(curve_points)
plt.plot(curve_points[:, 0], curve_points[:, 1], label='Bezier Curve')
plt.scatter(P[:, 0], P[:, 1], color='red', label='Control Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Bezier Curve (Divide and Conquer)')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
