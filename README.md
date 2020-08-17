# epai-session5

## Functions

- ### squared_power_list

  This function returns a sequence of powers of given range (from start to end) to the power of the mentioned number.

  Range start has to be less than the range end and start and end shpuld be integers. The power of number can be integer or float. 

- ### temp_converter

  This functions converts a given temperature from Celcius to Fanrenheit scale and vice a versa. The temperature should not be below absolute temperature. Temperature is accepted only in Celcius to Fanrenheit scale.

- ### speed_converter

  This functions converts the speed given in km/hr to a the desired distance unit and time unit.

  The supported distance units are km, m, ft, yrd.

  The supported time units are ms, s, m, hr, day.

  The input speed can not be negative. 

- ### polygon_area

  This function computed the area of a regular polygon of give number of sides and given side length.

  This function supports computation of area upto hexagon.

  3 < = number of sides < = 6

  The lenght of the side cannot be negative.

- ### time_it

  This function is used to calculate time taken to execute the above functions for a given nimber of interations and for the given set of arguments.

## Test Cases

- test_squared_power_list_validate_input_type

  Validates the input type of squared_power_list function

- test_squared_power_list_validate_start_lessthan_end

  Validates that the start of the range is less than the end of the range

- test_squared_power_list

  Tests squared_power_list returns correct list for input power = 2 , start = 0 , end = 5.  

- test_temp_converter_validate_input_type

  Validates the input type of temp_converter function

- test_temp_converter_validate_input_temp_unit

  Validates if the unit of temprature is supported

- test_temp_converter_validate_input_below_abs_zero

  checks if the temperature is not below absoute zero

- test_temp_converter

  checks if the conversions is correct for some input values

- test_speed_converter_validate_input_type

- test_speed_converter_validate_input_distance_unit

- test_speed_converter_validate_input_time_unit

- test_speed_converter_validate_input_below_abs_zero

- test_speed_converter_validate_to_m_s

- test_speed_converter_validate_to_ft_s

- test_speed_converter_validate_to_yrd_s

- test_speed_converter_validate_to_km_hr

- test_speed_converter_validate_to_km_s

- test_polygon_area_validate_input_type

- test_polygon_area_validate_positive_length

- test_polygon_area_validate_sides_range

- test_polygon_area

- test_time_it_print

- test_time_it_squared_power_list

- test_time_it_polygon_area

- test_time_it_temp_converter

- test_time_it_speed_converter

- test_readme_exists

- test_readme_contents

- test_readme_proper_description

- test_readme_file_for_formatting

- test_function_name_had_cap_letter

- test_mandatory_fuctions_availability

## Test Report

All the above mentioned test cases have passed