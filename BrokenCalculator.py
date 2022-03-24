def brokenCalc(self, startValue: int, target: int) -> int:
        steps = 0
        while target > startValue:
            steps += 1 + target % 2
            target += target % 2
            target //= 2
        return steps + (startValue - target)