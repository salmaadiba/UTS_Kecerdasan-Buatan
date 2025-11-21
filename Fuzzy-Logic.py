def triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b <= x < c:
        return (c - x) / (c - b)
    else:
        return 0


def fuzzy_tip(food, service):
    # Membership Food
    food_bad = triangular(food, 0, 0, 5)
    food_good = triangular(food, 5, 10, 10)

    # Membership Service
    service_poor = triangular(service, 0, 0, 5)
    service_excellent = triangular(service, 5, 10, 10)

    # Rule firing strength
    rule_low = max(service_poor, food_bad)
    rule_high = min(service_excellent, food_good)

    # Representative (tip) values:
    tip_low = 5     # center of Low (0,0,10)
    tip_high = 15   # center of High (10,20,20)

    # Weighted average
    numerator = rule_low * tip_low + rule_high * tip_high
    denominator = rule_low + rule_high

    if denominator == 0:
        return 0

    return numerator / denominator


# -------------------------------------------------
# Main Program
# -------------------------------------------------
food = float(input("Masukkan Food Quality (0-10): "))
service = float(input("Masukkan Service Quality (0-10): "))

tip = fuzzy_tip(food, service)
print(f"\nTip yang disarankan: {tip:.2f}%")
