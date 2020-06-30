class Road:
    def __init__(self, _length, _width, _gage):
# gage - толщина
        Road._length = _length
        Road._width = _width
        Road._gage = _gage

    def calc(self):
        result = Road._length * Road._width * Road._gage * 25
        return result

road = Road(5000, 20, 5)

print(road.calc()/1000)