import timeimport mathdef time_it(fn, *args, repetitions = 1, **kwargs):    start_time = time.time()    print('time_it', fn, args, kwargs)    for i in range(repetitions):        fn(*args, **kwargs)        end_time = time.time()    time_taken = end_time - start_time    return time_takendef squared_power_list(*args, **kwargs ):#start=0, end = 5, repetitions = 5):    print('squared_power_list',"args", args)    print('squared_power_list',"kwargs",  kwargs)    squared_power_list = list()    num = args[0]    start = kwargs.get("start")    end = kwargs.get("end")    for i in range(start, end + 1):        squared_power_list.append(math.pow(num, i))        print(i, math.pow(num, i))    return squared_power_listdef temp_converter(*args, **kwargs):    temp = args[0]    temp_given_in = kwargs.get("temp_given_in")    if (temp_given_in == 'f'):        converted_temp = (temp - 32) * 5 / 9    else:        converted_temp = (temp * 9 / 8) + 32    return converted_temp#dist can be km/m/ft/yrd, time can be ms/s/m/hr/day, speed given by user is in kmphdef speed_converter(*args, **kwargs):    speed = args[0]    dist = kwargs.get('dist')    time = kwargs.get('time')        dist_conv_dict = {'km':1, 'm':1000, 'ft':3280.84, 'yrd':1093.61}    dist_conversion = dist_conv_dict.get(dist)    time_conv_dict = {'ms':3600000, 's':3600, 'm':60, 'hr':1, 'day':0.0417}    time_conversion = time_conv_dict.get(time)    converted_speed = speed * dist_conversion / time_conversion    return converted_speed