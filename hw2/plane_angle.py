import math

class Point:
    def __init__(self, x, y, z):
        # your code here        
        """Инициализация точки с координатами x, y, z"""
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __sub__(self, other):
        # your code here        
        """Вычитание точек для создания вектора"""
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other):
        # your code here        
        """Скалярное произведение двух векторов"""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        # your code here        
        """Векторное произведение двух векторов"""
        return Point(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def absolute(self):
        """Вычисление длины вектора"""
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

def plane_angle(a, b, c, d):
    # your code here
    """
        Вычисление угла между плоскостями ABC и BCD.
        Возвращает угол в градусах.
        """
    # Создаем векторы AB, BC, CD
    ab = b - a
    bc = c - b
    cd = d - c

    # Вычисляем нормали к плоскостям через векторное произведение
    x = ab.cross(bc)  # Нормаль к первой плоскости
    y = bc.cross(cd)  # Нормаль ко второй плоскости

    # Вычисляем косинус угла между нормалями
    cos_phi = x.dot(y) / (x.absolute() * y.absolute())

    # Преобразуем радианы в градусы
    phi = math.degrees(math.acos(cos_phi))

    return phi

if __name__ == '__main__':
    # your code here
    a = Point(0, 0, 0)
    b = Point(1, 0, 0)
    c = Point(1, 1, 0)
    d = Point(1, 1, 1)

    angle = plane_angle(a, b, c, d)
    print(f"Угол между плоскостями: {angle:.2f} градусов")