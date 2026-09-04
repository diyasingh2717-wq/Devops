from marks import calculate_grade

def test_grade_A():
    total, percentage, grade = calculate_grade([95, 90, 92, 93, 94])
    assert grade == 'A'

def test_grade_B():
    total, percentage, grade = calculate_grade([80, 75, 78, 77, 76])
    assert grade == 'B'

def test_fail():
    total, percentage, grade = calculate_grade([30, 35, 20, 25, 30])
    assert grade == 'F'