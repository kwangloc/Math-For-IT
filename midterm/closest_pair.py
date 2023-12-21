import math

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

# Hàm tính khoảng cách giữa 2 điểm
def distance2Points(p1, p2):
	return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

# Ap dung phuong phap Brute Force de tim cap diem gan nhau nhat cua 2 khoang 
def bruteForce(P, n):
	min = float('inf')
	for i in range(n):
		for j in range(i+1, n):
			if distance2Points(P[i], P[j]) < min:
				min = distance2Points(P[i], P[j])
	return min

def min(x, y):
	return x if x < y else y

# Hàm tìm cặp điểm gần nhất trong vùng lân cận cách đường thẳng giữa một khoảng d

def stripClosest(strip, size, d):
	min = d 
	# Tìm cặp điểm có hiệu giữa tọa độ y bé hơn d
	for i in range(size):
		for j in range(i+1, size):
			if (strip[j].y - strip[i].y) < min:
				if distance2Points(strip[i],strip[j]) < min:
					min = distance2Points(strip[i], strip[j])

	return min


# Px chứa các điểm được sắp xếp theo tọa độ x giảm dần 
# Py chứa các điểm được sắp xếp theo tọa độ y giảm dần 
def closestUtil(Px, Py, n):
	# Nếu có ít hơn 3 điểm thì dùng luôn brute force
	if n <= 3:
		return bruteForce(Px, n)

	# Tìm điểm ở giữa (để chia đôi thành 2 nửa)
	mid = n // 2
	midPoint = Px[mid]

	Pyl = [None] * mid # khởi tạo list chứa các điểm ở khoảng trái (sắp xếp giảm dần theo tọa độ y)
	Pyr = [None] * (n-mid) # khởi tạo list chứa các điểm ở khoảng phải (sắp xếp giảm dần theo tọa độ y)
	li = ri = 0 # chỉ số để quản lý khoảng trái và khoảng phải
	
	# chạy vòng lặp để thêm các phần tử vào 2 list tương ứng với 2 khoảng
	for i in range(n):
		if ((Py[i].x < midPoint.x or (Py[i].x == midPoint.x and Py[i].y < midPoint.y)) and li<mid): 
			Pyl[li] = Py[i]
			li += 1
		else:
			Pyr[ri] = Py[i]
			ri += 1

	dl = closestUtil(Px, Pyl, mid) # cặp điểm gần nhất trong nửa trái
	dr = closestUtil(Px[mid:], Pyr, n-mid) # cặp điểm gần nhất trong nửa phải

	d = min(dl, dr)

	# khởi tạo mảng chứa các điểm nằm trong vùng lân cận đường chia đôi, cách ko quá d
	strip = [None] * n
	j = 0
	for i in range(n):
		if abs(Py[i].x - midPoint.x) < d:
			strip[j] = Py[i]
			j += 1

    # trả về cặp điểm min giữa: điểm gần nhất trong khoảng strip và d
	return stripClosest(strip, j, d)

def closest(P, n):
	Px = P # các điểm được sắp xếp giảm dần theo tọa độ x
	Py = P # các điểm được sắp xếp giảm dần theo tọa độ y
	Px.sort(key=lambda x:x.x)
	Py.sort(key=lambda x:x.y)

	return closestUtil(Px, Py, n)

def main():
	# P = [Point(2, 3), Point(12, 30), Point(40, 50), Point(5, 1), Point(12, 10), Point(3, 4)]
	P = [Point(1, 1), Point(2, 3), Point(4, 4), Point(7, 7), Point(12, 10), Point(20, 4)]
	n = len(P)
	print("The smallest distance is", closest(P, n))
	
if __name__ == '__main__':
	main()
