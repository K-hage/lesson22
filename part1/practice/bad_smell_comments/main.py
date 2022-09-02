# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных,
# чтобы было понятно, за что эти переменные отвечают
# и что происходит и без комментариев


class Unit:
    def move_to_field(self, field, x: int, y: int, direction, is_fly, is_crawl, speed=1):

        if is_fly and is_crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
        elif is_crawl:
            speed *= 0.5

            if direction == 'UP':
                new_y = y + speed
                new_x = x
            elif direction == 'DOWN':
                new_y = y - speed
                new_x = x
            elif direction == 'LEFT':
                new_y = y
                new_x = x - speed
            elif direction == 'RIGHT':
                new_y = y
                new_x = x + speed

            field.set_unit(x=new_x, y=new_y, unit=self)
