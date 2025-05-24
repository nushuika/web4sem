import subprocess
import pytest

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
    'python_if_else': [
        ('1', 'Weird'),
        ('4', 'Not Weird'),
        ('8', 'Weird'),
        ('24', 'Not Weird'),
        ('101', 'Error!')
    ],
    'arithmetic_operators': [
        (['1', '2'], ['3', '-1', '2']),
        (['10000000000', '1'], ['10000000001', '9999999999', '10000000000']),
        (['10', '-5'], ['Error!']),
        (['0', '2'], ['Error!']),
    ],
    'division': [
        (['10', '2'], ['5', '5.0']),
        (['15', '3'], ['5', '5.0']),
        (['10', '0'], ['Error!']),
        (['17', '5'], ['3', '3.4']),
        (['1000000000', '2'], ['500000000', '500000000.0']),
    ],
    'loops': [
        (['1'], ['0']),
        (['2'], ['0','1']),
        (['20'], ['0','1','4','9','16','25','36','49','64','81','100','121','144','169','196','225','256','289','324','361']),
        (['0'], ['Error!']),
        (['21'], ['Error!']),
    ],
    'print_function': [
        (['1'], ['1']),
        (['2'], ['12']),
        (['20'], ['1234567891011121314151617181920']),
        (['0'], ['Error!']),
        (['21'], ['Error!']),
        (['-5'], ['Error!']),
    ],
    'second_score': [
        (['3', '1 2 3'], ['2']),
        (['4', '1 2 3 4'], ['3']),
        (['10', '1 2 3 4 5 6 7 8 9 10'], ['9']),
        (['4', '1 1 2 2'], ['1']),
        (['3', '1 2'], ['Error!']),
        (['2', '1 2 3'], ['Error!']),
        (['2', '1 1'], ['Error!']),
    ],
    'nested_list': [
        (['3', 'Alice Bob Charlie', '87.5 89.2 87.5'], ['Bob']),
        (['5', 'Alice Bob Charlie David Eve', '87.5 89.2 87.5 90.0 88.5'], ['Eve']),
        (['1', 'Alice', '87.5'], ['Error!']),
    ],
    'lists': [
        (['2', 'insert 0 5','print'], ['[5]']),
        (['2', 'append 10', 'print'], ['[10]']),
        (['4' , 'insert 0 5', 'append 10', 'remove 5', 'print'], ['[10]']),
    ],
    'swap_case': [
        (['Hello World'],['hELLO wORLD']),
        (['a'*1000],['A'*1000]),
        (['a'*1001],['Error!']),
    ],
    'split_and_join': [
        (['Hello World'], ['Hello-World']),
        (['Hello    World'], ['Hello-World']),
    ],
    'anagram': [
        (['listen', 'silent'], ['YES']),
        (['hello', 'world'], ['NO']),
    ],
    'metro': [
        (['1', '2 5', '3'],['1']),
        (['3', '1 5', '2 4', '3 7', '3'],['3']),
        (['2', '1 2', '4 5', '3'],['0']),
        (['1', '1 5', '1'],['1']),
    ],
    'minion_game': [
        (['BANANA'],['Stuart 12']),
        (['AAAA'],['Kevin 10']),
        (['B'],['Stuart 1']),
        (['A'],['Kevin 1']),
    ],
    'is_leap': [
        (['2000'],['True']),
        (['1900'],['False']),
        (['1899'],['Error!']),
        (['100001'],['Error!']),
    ],
    'happiness': [
        (['3 2','1 2 3','1 2','3 4'],['1']),
        (['3 1','1 1 1','1','2'],['3']),
        (['3','1 2 3','',''],['']),
    ],
    'pirate_ship': [
        (['50 3','Gold 10 60','Silver 20 100','Copper 30 120'],['Gold 10 60.00','Silver 20 100.00','Copper 20.00 80.00']),
    ],
    'matrix_mult': [
        (['2','1 2','3 4','5 6','7 8'],['19 22','43 50']),
        (['2','0 0','0 0','1 1','1 1'],['0 0','0 0']),
        (['2','-1 2','3 -4','5 -6','-7 8'],['-19 22','43 -50']),
    ],
}

def test_hello_world():
    assert run_script('hello.py') == "Hello, World!"

@pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])
def test_python_if_else(input_data, expected):
    assert run_script('python_if_else.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['division'])
def test_division(input_data, expected):
    assert run_script('division.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['loops'])
def test_loops(input_data, expected):
    assert run_script('loops.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['print_function'])
def test_print_function(input_data, expected):
    assert run_script('print_function.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['second_score'])
def test_second_score(input_data, expected):
    assert run_script('second_score.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['nested_list'])
def test_nested_list(input_data, expected):
    assert run_script('nested_list.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['lists'])
def test_lists(input_data, expected):
    assert run_script('lists.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['swap_case'])
def test_swap_case(input_data, expected):
    assert run_script('swap_case.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['split_and_join'])
def test_split_and_join(input_data, expected):
    assert run_script('split_and_join.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['anagram'])
def test_anagram(input_data, expected):
    assert run_script('anagram.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['metro'])
def test_metro(input_data, expected):
    assert run_script('metro.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['minion_game'])
def test_minion_game(input_data, expected):
    assert run_script('minion_game.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['is_leap'])
def test_is_leap(input_data, expected):
    assert run_script('is_leap.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['happiness'])
def test_happiness(input_data, expected):
    assert run_script('happiness.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['pirate_ship'])
def test_pirate_ship(input_data, expected):
    assert run_script('pirate_ship.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['matrix_mult'])
def test_matrix_mult(input_data, expected):
    assert run_script('matrix_mult.py', input_data).split('\n') == expected
