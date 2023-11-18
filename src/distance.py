def get_distance(acceleration: float, time: float) -> float:
        a = acceleration
        t = time
        return ((a * (t**2))/2)

print(get_distance(4,2))