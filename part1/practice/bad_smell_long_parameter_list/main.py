# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, x: int, y: int, field, speed=1):
        self.y = y
        self.x = x
        self.speed = speed
        self.field = field  # класс поля, на котором персонаж находится.

    def move(self, state, direction):
        speed = self._get_speed(state)

        match direction:
            case 'UP':
                self.field.set_unit(x=self.x, y=self.y + speed, unit=self)
            case 'Down':
                self.field.set_unit(x=self.x, y=self.y - speed, unit=self)
            case 'LEFT':
                self.field.set_unit(x=self.x - speed, y=self.y, unit=self)
            case 'RIGHT':
                self.field.set_unit(x=self.x + speed, y=self.y, unit=self)

    def _get_speed(self, state):
        if state == 'FLY':
            self.speed *= 1.2
        elif state == 'CRAWL':
            self.speed *= 0.5
        else:
            raise ValueError('Рожденный ползать летать не должен!')
