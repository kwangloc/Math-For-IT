def main():
    points = [(4, 5), (6,4), (7,6), (8,7), (9,8), (5,10), (4,9), (5,9), (8,11), (8,5)]
    convex_hull_points = convex_hull(points)
    print("Toa do cac diem bao loi:", convex_hull_points)
    area = calculate_polygon_area(convex_hull_points)
    print("Dien tich: ", area)

def orientation(p, q, r): # hướng tạo thành của 3 điểm
    # -1 rẽ trái
    # 0 thẳng hàng
    # 1 rẽ phải
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else -1

def convex_hull(points):
    n = len(points)
    
    if n < 3:
        return points
    
    # Sắp xếp các điểm tăng dần theo tạo độ x (x bằng nhau thì xét y)
    points.sort(key=lambda p: (p[0], p[1]))
    
    # khởi tạo 2 list bao trên và bao dưới
    upper_hull = []
    lower_hull = []
    
    # bao trên
    for point in points:
        # bổ sung 2 điểm đầu
        # bổ sung điểm thứ 3, nếu 3 điểm cuối của list ko tạo thành rẽ phải thì xóa điểm giữa
        while len(upper_hull) >= 2 and orientation(upper_hull[-2], upper_hull[-1], point) != -1:
            upper_hull.pop()
        upper_hull.append(point)
    
    # bao dưới
    for point in reversed(points):
        # bổ sung 2 điểm cuối
        # bổ sung điểm thứ 3, nếu 3 điểm cuối của list ko tạo thành rẽ phải thì xóa điểm giữa
        while len(lower_hull) >= 2 and orientation(lower_hull[-2], lower_hull[-1], point) != -1:
            lower_hull.pop()
        lower_hull.append(point)
    
    # kết hợp bao trên và bao dưới
    convex_hull = upper_hull[:-1] + lower_hull[:-1]
    
    return convex_hull

def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        print("A polygon with at least three vertices is required.")
        return None

    # Applying Shoelace Formula to calculate the area
    area = 0.5 * sum((vertices[i][0] * vertices[(i + 1) % n][1] - vertices[(i + 1) % n][0] * vertices[i][1]) for i in range(n))

    return abs(area)

if __name__ == "__main__":
    main()


