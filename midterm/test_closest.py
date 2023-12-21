import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def brute_force_closest_pair(points): # o(n^2): dùng cho dataset nhỏ
    min_distance = float('inf')
    closest_pair = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])

    return closest_pair, min_distance

def closest_pair_divide_and_conquer(points):
    n = len(points)

    # Nếu có ít hơn 3 điểm
    if n <= 3:
        return brute_force_closest_pair(points)

    # Sắp xếp các điểm theo x-coordinate
    sorted_points = sorted(points, key=lambda x: x[0])

    # Chia thành 2 nửa
    mid = n // 2
    left_half = sorted_points[:mid]
    right_half = sorted_points[mid:]

    # Đệ quy tìm ra cặp điểm gần nhất của 2 nửa
    left_pair, left_distance = closest_pair_divide_and_conquer(left_half)
    right_pair, right_distance = closest_pair_divide_and_conquer(right_half)

    # tìm min(min_left, min_right)
    min_distance = min(left_distance, right_distance)

    # Merge the two halves and find pairs with points in different halves
    # điểm ở giữa theo tọa độ x
    mid_x = sorted_points[mid][0]

    # strip chứa các điểm lân cận trong khoảng cách min_distance tính từ đường chia đôi 
    strip = []

    for point in sorted_points:
        if abs(point[0] - mid_x) < min_distance:
            strip.append(point)

    # kiểm tra xem strip có chứa cặp điểm nào có khoảng cách bé hơn min_distance hay không
    strip_pair, strip_distance = closest_pair_in_strip(strip, min_distance)

    # return cặp điểm gần nhau nhất
    if strip_distance < min_distance:
        return strip_pair, strip_distance
    elif left_distance < right_distance:
        return left_pair, left_distance
    else:
        return right_pair, right_distance

def closest_pair_in_strip(strip, min_distance):
    strip_length = len(strip)
    min_strip_distance = min_distance
    closest_strip_pair = None

    # sắp xếp strip theo tọa độ y
    strip.sort(key=lambda x: x[1])

    # Lặp qua mỗi điểm trong strip và so sánh với các điểm tiếp theo (tối đa 7 điểm)
    for i in range(strip_length):
        j = i + 1
        while j < strip_length and strip[j][1] - strip[i][1] < min_distance:
            distance = euclidean_distance(strip[i], strip[j])
            if distance < min_strip_distance:
                min_strip_distance = distance
                closest_strip_pair = (strip[i], strip[j])
            j += 1

    return closest_strip_pair, min_strip_distance

points = [(4, 5), (6, 4), (8, 5), (9, 8), (8, 11), (5, 10), (4, 9)]
closest_pair, distance = closest_pair_divide_and_conquer(points)
print("Closest pair:", closest_pair)
print("Distance:", distance)
