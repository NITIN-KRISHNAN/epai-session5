from session5 import squared_power_list, temp_converter, speed_converter, polygon_area, time_it
import pytest
import math
import os
import re
import inspect
import session5


MANDATORY_FUNCTIONS = [
    'squared_power_list',
    'time_it',
    'temp_converter',
    'speed_converter',
    'polygon_area',
    ]


def test_squared_power_list_validate_input_type():
    with pytest.raises(ValueError):
        squared_power_list(-0.5, start=0,end=4.9)
    with pytest.raises(ValueError):
        squared_power_list("number", start=0,end=4.9)
    with pytest.raises(ValueError):
        squared_power_list(2, start=0, end=('a','b'))

def test_squared_power_list_validate_start_lessthan_end():
    with pytest.raises(ValueError):
        squared_power_list(-0.5, start=0,end=-4)

def test_squared_power_list():
    res = squared_power_list(2, start=0,end=5)
    assert res == [1.0, 2.0, 4.0, 8.0, 16.0,32.0], "fail test_squared_power_list"

def test_temp_converter_validate_input_type():
    with pytest.raises(ValueError):
        temp_converter("4", temp_given_in = 7)

def test_temp_converter_validate_input_temp_unit():
    with pytest.raises(ValueError):
        temp_converter(0, temp_given_in = 'k')

def test_temp_converter_validate_input_below_abs_zero():
    with pytest.raises(ValueError):
        temp_converter(-275, temp_given_in = 'c')
    with pytest.raises(ValueError):
        temp_converter(-500, temp_given_in = 'f')

def test_temp_converter():
    res = math.isclose(temp_converter(0, temp_given_in = 'c'), 32.0, abs_tol = 0.1)
    assert res, "fail test_temp_converter"
    
    res = math.isclose(temp_converter(0, temp_given_in = 'f'), -17.77, abs_tol = 0.1)
    assert res, "fail test_temp_converter"
    
    res = math.isclose(temp_converter(100, temp_given_in = 'c'), 212.0, abs_tol = 0.1)
    assert res, "fail test_temp_converter"
    
    res = math.isclose(temp_converter(100, temp_given_in = 'f'), 37.7, abs_tol = 0.1)
    assert res, "fail test_temp_converter"

def test_speed_converter_validate_input_type():
    with pytest.raises(ValueError):
        speed_converter("-2", 'km', 'r')

def test_speed_converter_validate_input_distance_unit():
    with pytest.raises(ValueError):
        speed_converter(-2, 'q', 'r')

def test_speed_converter_validate_input_time_unit():
    with pytest.raises(ValueError):
        speed_converter(-2, 'km', 'r')

def test_speed_converter_validate_input_below_abs_zero():
    with pytest.raises(ValueError):
        speed_converter(-2, 'km', 'r')

def test_speed_converter_validate_to_m_s():
    res = math.isclose(speed_converter(100, 'm', 's'), 27.77, abs_tol = 0.1)
    assert res, "fail test_speed_converter_validate_to_m_s"

    res = math.isclose(speed_converter(48, 'm', 's'), 13.33, abs_tol = 0.1)
    assert res, "fail test_speed_converter_validate_to_m_s"

def test_speed_converter_validate_to_ft_s():
    res = math.isclose(speed_converter(100, 'ft', 's'), 91.13, abs_tol = 0.1)
    assert res, "fail test_speed_converter_validate_to_ft_s"

    res = math.isclose(speed_converter(48, 'ft', 's'), 43.74, abs_tol = 0.1)
    assert res, "fail test_speed_converter_validate_to_ft_s"

def test_speed_converter_validate_to_yrd_s():
    res = math.isclose(speed_converter(100, 'yrd', 's'), 30.37, abs_tol = 0.1)
    assert res, "fail test_speed_converter_validate_to_yrd_s"

    res = math.isclose(speed_converter(48, 'yrd', 's'), 14.58, abs_tol = 0.1)
    assert res, "fail test_speed_converter_validate_to_yrd_s"

def test_speed_converter_validate_to_km_hr():
    res = math.isclose(speed_converter(100, 'km', 'hr'), 100, abs_tol = 0.1)
    assert res, "fail test_speed_converter_validate_to_km_hr"

    res = math.isclose(speed_converter(48, 'km', 'hr'), 48, abs_tol = 0.1)
    assert res, "fail test_speed_converter_validate_to_km_hr"

def test_speed_converter_validate_to_km_s():
    res = math.isclose(speed_converter(100, 'km', 's'), 0.027, abs_tol = 0.1)
    assert res, "fail test_speed_converter_validate_to_m_s"

    res = math.isclose(speed_converter(48, 'km', 's'), 0.013, abs_tol = 0.1)
    assert res, "fail test_speed_converter_validate_to_m_s"

# def test_speed_converter_validate_to_m_s():
#     res = math.isclose(speed_converter(100, 'm', 's'), 27.77, abs_tol = 0.1)
#     assert res, "fail test_speed_converter_validate_to_m_s"

#     res = math.isclose(temp_converter(48, 'm', 's'), 13.33, abs_tol = 0.1)
#     assert res, "fail test_speed_converter_validate_to_m_s"

# def test_speed_converter_validate_to_m_s():
#     res = math.isclose(speed_converter(100, 'm', 's'), 27.77, abs_tol = 0.1)
#     assert res, "fail test_speed_converter_validate_to_m_s"

#     res = math.isclose(temp_converter(48, 'm', 's'), 13.33, abs_tol = 0.1)
#     assert res, "fail test_speed_converter_validate_to_m_s"

# def test_speed_converter_validate_to_m_s():
#     res = math.isclose(speed_converter(100, 'm', 's'), 27.77, abs_tol = 0.1)
#     assert res, "fail test_speed_converter_validate_to_m_s"

#     res = math.isclose(temp_converter(48, 'm', 's'), 13.33, abs_tol = 0.1)
#     assert res, "fail test_speed_converter_validate_to_m_s"

# def test_speed_converter_validate_to_m_s():
#     res = math.isclose(speed_converter(100, 'm', 's'), 27.77, abs_tol = 0.1)
#     assert res, "fail test_speed_converter_validate_to_m_s"

#     res = math.isclose(temp_converter(48, 'm', 's'), 13.33, abs_tol = 0.1)
#     assert res, "fail test_speed_converter_validate_to_m_s"

def test_polygon_area_validate_input_type():
    with pytest.raises(ValueError):
        polygon_area("-2", (8,'i'))

def test_polygon_area_validate_positive_length():
    with pytest.raises(ValueError):
        polygon_area(-2, 4)

def test_polygon_area_validate_sides_range():
    with pytest.raises(ValueError):
        polygon_area(2, 0)
    with pytest.raises(ValueError):
        polygon_area(2, 15)

def test_polygon_area():
    res = math.isclose(polygon_area(2, 6), 10.39, abs_tol = 0.1)
    assert res, "fail test_polygon_area"

    res = math.isclose(polygon_area(2, 5), 6.88, abs_tol = 0.1)
    assert res, "fail test_polygon_area"

    res = math.isclose(polygon_area(2, 4), 4, abs_tol = 0.1)
    assert res, "fail test_polygon_area"

    res = math.isclose(polygon_area(2, 3), 1.73, abs_tol = 0.1)
    assert res, "fail test_polygon_area"

    assert res, "fail test_polygon_area"

def test_time_it_print():
   assert  time_it(print, 1, 2, 3, sep = '-', end = ' ***\n', repetitions = 5) > 0
   
def test_time_it_squared_power_list():
   assert  time_it(squared_power_list, 2, start=0, end=5, repetitions=5) > 0

def test_time_it_polygon_area():
   assert  time_it(polygon_area, 15, sides = 3, repetitions=10) > 0

def test_time_it_temp_converter():
   assert  time_it(temp_converter, 100, temp_given_in = 'f', repetitions=100) > 0
   
def test_time_it_speed_converter():
   assert  time_it(speed_converter, 100, dist='km', time='m', repetitions=200) > 0
   
def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 350, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in MANDATORY_FUNCTIONS:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"    

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 
        
def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
        

def test_mandatory_fuctions_availability():
    MANDATORY_FUNCTIONS_AVAILABILITY = True
    f = open("session5.py", "r")
    content = f.read()
    f.close()
    for c in MANDATORY_FUNCTIONS:
        if c not in content:
            MANDATORY_FUNCTIONS_AVAILABILITY = False
            pass
    assert MANDATORY_FUNCTIONS_AVAILABILITY == True, "You have not implemented all the functions"