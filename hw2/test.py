import math
import pytest
import subprocess
from fact import fact_rec, fact_it
from show_employee import show_employee
from sum_and_sub import sum_and_sub
from process_list import process_list, process_list_comprehension, process_list_gen
from my_sum import my_sum
from email_validation import fun
from fibonacci import fibonacci, cube
from hw2.average_scores import compute_average_scores
from phone_number import normalize_phone
from hw2.circle_square_mk import circle_square_mk

INTERPRETER = 'python'

def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()

test_data = {
    'fact': [
        (5, 120),
        (1, 1),
        (10, 3628800)
    ],
    'not_fact': [
        (-1, "Error!"),
        (1000000000, "Error!"),
        ("string", "Error!"),
        (3.5, "Error!")
    ],
    'employee': [
        ("Gazimagomedova Aisha", 100000, "Gazimagomedova Aisha: 100000 ₽"),
        ("Sanaya Ilya", 50000, "Sanaya Ilya: 50000 ₽"),
        ("Ivanov Ivan", 75000, "Ivanov Ivan: 75000 ₽")
    ],
    'not_employee': [
        ("", 100 , "Error!"),
        ("Aisha", -1000, "Error!"),
        ("Ilya", "100000", "Error!")
    ],
    'sum_and_sub':[
        (5, 3, (8, 2)),
        (-2, 4, (2, -6)),
        (0, 0, (0, 0)),
        (3.5, 6.3, (9.8, -2.8))
    ],
    'not_sum_and_sub':[
        ("5", 3, "Error!"),
        (5, "3", "Error!")
    ],
    'process_list':[
        ([1, 2, 3, 4], [1, 4, 27, 16]),
        ([2, 4, 6, 8], [4, 16, 36, 64]),
        ([1, 3, 5, 7], [1, 27, 125, 343])
    ],
    'my_sum':[
        ([1, 2, 3], 6),
        ([1.5, 2.5], 4.0),
        ([-1, -2, -3], -6),
        ([1], 1),
        ([0, 0, 0], 0)
    ],
    'not_my_sum':[
        (["1", 2], "Error!"),
        ([1, "2", 3], "Error!")
    ],
    'email':[
    ("lara@mospolytech.ru", True),
    ("brian-23@mospolytech.ru", True),
    ("britts_54@mospolytech.ru", True),
    ("lara.mospolytech.ru", False),
    ("@mospolytech.ru", False),
    ("lara@.ru", False),
    ("lara@mospolytech", False),
    ("lara@mospolytech.ru.", False)
    ],
    'fibonacci': [
        (5, [0, 1, 1, 2, 3]),
        (6, [0, 1, 1, 2, 3, 5])
    ],
    'cubes': [
        (5, [0, 1, 1, 8, 27]),
        (6, [0, 1, 1, 8, 27, 125])
    ],
    'valid_scores': [
        (
            [(89, 90, 78, 93, 80),
             (90, 91, 85, 88, 86),
             (91, 92, 83, 89, 90.5)],
            (90.0, 91.0, 82.0, 90.0, 85.5)
        )
    ],
    'invalid_scores': [
        (
            [(101, 90, 78),
             (90, 91, 85)],
            ValueError
        ),
        (
            [(-1, 90, 78),
             (90, 91, 85)],
            ValueError
        )
    ],
    'normalize': [
        ("81234567890", "71234567890"),
        ("89991234567", "79991234567"),
        ("7-234-567-89", "723456789"),
        ("07123456789", "7123456789"),
    ],
    'valid_cases': [
        (1.0, 1000000),
        (2.0, 10000),
        (5.0, 1000)
    ],
    'invalid_cases': [
        (-1.0, 1000000),
        (0.0, 1000000),
        (1.0, 0),
        (1.0, -1000000)
    ],
}

@pytest.mark.parametrize("input_data, expected", test_data['fact'])
def test_fact_it(input_data, expected):
    assert fact_it(input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['not_fact'])
def test_fact_it_invalid(input_data, expected):
    with pytest.raises((ValueError, TypeError)) as exc_info:
        fact_it(input_data)
    assert str(exc_info.value) == expected

@pytest.mark.parametrize("input_data, expected", test_data['fact'])
def test_fact_rec(input_data, expected):
    assert fact_rec(input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['not_fact'])
def test_fact_rec_invalid(input_data, expected):
    with pytest.raises((ValueError, TypeError)) as exc_info:
        fact_rec(input_data)
    assert str(exc_info.value) == expected

@pytest.mark.parametrize("name, salary, expected", test_data['employee'])
def test_show_employee_valid(name, salary, expected):
    assert show_employee(name, salary) == expected

@pytest.mark.parametrize("name, salary, expected", test_data['not_employee'])
def test_show_employee_invalid(name, salary, expected):
    with pytest.raises((ValueError, TypeError)) as exc_info:
        show_employee(name, salary)
    assert str(exc_info.value) == expected

@pytest.mark.parametrize("a, b, expected", test_data['sum_and_sub'])
def test_sum_and_sub_valid(a, b, expected):
    assert sum_and_sub(a, b) == expected

@pytest.mark.parametrize("a, b, expected", test_data['not_sum_and_sub'])
def test_sum_and_sub_invalid(a, b, expected):
    with pytest.raises(TypeError) as exc_info:
        sum_and_sub(a, b)
    assert str(exc_info.value) == expected

@pytest.mark.parametrize("input_data, expected", test_data['process_list'])
def test_process_list_valid(input_data, expected):
    assert process_list(input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['process_list'])
def test_process_list_comprehension_valid(input_data, expected):
    assert process_list_comprehension(input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['process_list'])
def test_process_list_gen_valid(input_data, expected):
    assert list(process_list_gen(input_data)) == expected

@pytest.mark.parametrize("args, expected", test_data['my_sum'])
def test_my_sum_valid(args, expected):
    assert my_sum(*args) == expected

@pytest.mark.parametrize("args, expected", test_data['not_my_sum'])
def test_my_sum_invalid(args, expected):
    with pytest.raises(TypeError) as exc_info:
        my_sum(*args)
    assert str(exc_info.value) == expected

@pytest.mark.parametrize("email, expected", test_data['email'])
def test_email_validation(email, expected):
    assert fun(email) == expected

@pytest.mark.parametrize("n, expected", test_data['fibonacci'])
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected

@pytest.mark.parametrize("x, expected", [(0, 0), (1, 1), (2, 8), (3, 27), (5, 125)])
def test_cube(x, expected):
    assert cube(x) == expected

@pytest.mark.parametrize("scores, expected", test_data['valid_scores'])
def test_compute_average_scores_valid(scores, expected):
    result = compute_average_scores(scores)
    assert result == expected

@pytest.mark.parametrize("scores, expected_error", test_data['invalid_scores'])
def test_compute_average_scores_invalid(scores, expected_error):
    with pytest.raises(expected_error):
        compute_average_scores(scores)

@pytest.mark.parametrize("input_data, expected", test_data['normalize'])
def test_normalize_phone(input_data, expected):
    assert normalize_phone(input_data) == expected

@pytest.mark.parametrize("r, n", test_data['valid_cases'])
def test_circle_square_mk_valid(r, n):
    result = circle_square_mk(r, n)
    theoretical = math.pi * r * r
    error = abs(result - theoretical)
    print(f"r={r}, n={n}:")
    print(f"  Результат метода Монте-Карло: {result:.6f}")
    print(f"  Теоретическое значение: {theoretical:.6f}")
    print(f"  Абсолютная погрешность: {error:.6f}")
    print(f"  Относительная погрешность: {error/theoretical*100:.6f}%")

@pytest.mark.parametrize("r, n", test_data['invalid_cases'])
def test_circle_square_mk_invalid(r, n):
    with pytest.raises(ValueError) as exc_info:
        circle_square_mk(r, n)
    assert str(exc_info.value) == "Error!"