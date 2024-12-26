class Machine:
    def __init__(self, productivity: int, cost: float, avg_part_price: float):
        self.productivity = productivity
        self.cost = cost
        self.avg_part_price = avg_part_price

    def breakeven_parts(self) -> float:
        return self.cost / self.avg_part_price

    def payback_time(self, fixed_price: float) -> float:
        return self.cost / (self.productivity * fixed_price)


class MillingMachine(Machine):
    def __init__(self, productivity: int, cost: float, avg_part_price: float, milling_speed: float):
        """
        :param milling_speed: Скорость фрезеровки (мм/сек).
        """
        super().__init__(productivity, cost, avg_part_price)
        self.milling_speed = milling_speed


class CNC(Machine):
    def __init__(self, productivity: int, cost: float, avg_part_price: float, precision: float):
        """
        :param precision: Точность станка (в микронах).
        """
        super().__init__(productivity, cost, avg_part_price)
        self.precision = precision



if __name__ == "__main__":
    machine = Machine(productivity=100, cost=50000, avg_part_price=50)
    print(f"Количество деталей для окупаемости станка: {machine.breakeven_parts():.2f}")

    milling_machine = MillingMachine(productivity=120, cost=70000, avg_part_price=60, milling_speed=5.0)
    print(f"Время окупаемости фрезерного станка: {milling_machine.payback_time(70):.2f} часов")

    cnc = CNC(productivity=150, cost=100000, avg_part_price=80, precision=0.01)
    print(f"Время окупаемости станка с ЧПУ: {cnc.payback_time(90):.2f} часов")
