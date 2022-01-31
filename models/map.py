class MapInit(object):
    def __init__(self):
        # Координаты центра карты на старте. Задал координаты университета
        self.lat, self.lon = -33.856951, 151.215137
        # self.lon = 50.813492
        self.zoom = 16  # Масштаб карты на старте. Изменяется от 1 до 19
        self.type = "map"  # Другие значения "sat", "sat,skl"

    # Преобразование координат в параметр ll, требуется без пробелов, через запятую и без скобок
    def ll(self):
        return f"{str(self.lon)},{str(self.lat)}"
