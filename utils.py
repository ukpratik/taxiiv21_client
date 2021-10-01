import os
from datetime import datetime, timedelta
from linesout import *
from load_config import *


# This algorithm is is used to parse the object and add the required values to our local list
def parse_object(object):
    pattern_status = True
    if object['type'] == 'indicator':
        pattern_value = object['pattern']

        debug_L1_print("Pattern value type : " + str(type(pattern_value)))
        debug_L1_print(pattern_value)

        pattern_type_value = pattern_value.split(":")[0][1:]
        indicator_value = pattern_value.split("'")[-2]

        # debug_L1_print(pattern_type_value,indicator_value)

        if pattern_type_value in pattern_value:
            temp_path = PATH + 'indicators/' + str(pattern_type_value) + '.txt'

            debug_L1_print(temp_path)

            if check_list(temp_path,indicator_value):
                update_list(temp_path,indicator_value)

        if pattern_status == False:
            debug_L2_print("Handle different pattern status here.")
    else:
        debug_L2_print("Handle different Object type here , Object Type : " + object['type'])
        object_type = object['type']
        try:
            pattern_value = object['pattern']
        except:
            debug_L2_print("Can't find pattern field in the object ; ")
            return

        debug_L1_print("Pattern value type : " + str(type(pattern_value)))
        debug_L1_print(pattern_value)

        pattern_type_value = pattern_value.split(":")[0][1:]
        indicator_value = pattern_value.split("'")[-2]

        debug_L1_print(pattern_type_value,indicator_value)

        if pattern_type_value in pattern_value:
            pattern_type_value = pattern_type_value.replace('.','_').replace("'",'')
            temp_path = PATH + object_type + '/' + str(pattern_type_value) + '.txt'

            debug_L1_print(temp_path)

            if check_list(temp_path,indicator_value):
                update_list(temp_path,indicator_value)

        if pattern_status == False:
            debug_L2_print("Handle different pattern status here.")


# This function is used to check and avoid repeated values in our local list.
def check_list(path,value):
    if not os.path.exists(path):
        try:
            with open(path, 'w') as fp:
                pass   
        except FileNotFoundError:
            dir_name = path.split('/')[-2]
            try:
                os.mkdir(PATH + dir_name)
            except:
                pass
            with open(path, 'w') as fp:
                pass
    else:
        with open(path, 'r') as f:
            data = f.read().split('\n')
            if value in data:
                return False
            else:
                return True
        return True


# This function is used to update our local list for ruleengine 
def update_list(path,value):
    with open(path,'a') as f:
        f.write(value)
        f.write('\n')


def get_added_after():
    filename = 'added_after.txt'
    res = ''
    # mins = 60  # 1 hour
    # seconds = 60 * mins
    # time_to_cut = timedelta(seconds=seconds)

    if not os.path.exists(filename):
        with open(filename, 'w') as fp:
            pass   
        return None
    else:
        with open(filename, 'r') as f:
            res = f.read()
        # with open(filename, 'w') as f:
        #     f.write(str(curr_time - time_to_cut))
        return res


def get_list(path,value=None):
    if not os.path.exists(path):
        try:
            with open(path, 'w') as fp:
                pass   
        except FileNotFoundError:
            dir_name = path.split('/')[-2]
            os.mkdir(PATH + dir_name)
            with open(path, 'w') as fp:
                pass
    else:
        with open(path, 'r') as f:
            data = f.read().split('\n')
            return data


def store_data(object):
    path = 'all_objects/all_objects.json'
    if not os.path.exists(path):
        try:
            with open(path, 'w') as fp:
                pass   
        except FileNotFoundError:
            dir_name = 'all_objects'
            try:
                os.mkdir(dir_name)
            except:
                pass
            with open(path, 'w') as fp:
                pass
    with open(path, 'a') as f:
            f.write(json.dumps(object,indent=4))
            f.write('\n')

def update_added_after():
    filename = 'added_after.txt'
    curr_time = datetime.now()
    # mins = 60  # 1 hour
    # seconds = 60 * mins
    # time_to_cut = timedelta(seconds=seconds)
    days = 1
    time_to_cut = timedelta(days=days)
    with open(filename, 'w') as f:
        f.write(str(curr_time - time_to_cut))

# 1  DONE
# make history added after file.
# from datetime import datetime, timedelta
# curr_datetime = datetime.now()
# time_to_cut = 60*60 (60 seconds * 60 mintues)
# write(str(curr_datetime - time_to_cut))
# 

# 2 
# dont read the file every time for checking,
# (a) if got the value in the returned objects, 
# (b) load once and 
# (c) check from there 
# (d) at the end overwrite all those to respective files

# 3  DONE
# while updating our list(database) replace the '.', "'", with '_' and '' respt.

# 4  DONE
# for feedback and improving and experimenting, store & append all the objects in a json file,

# 5 NOT NECESSARY , EVERY THING WILLL BE ADDED TO DEFAULT ONE, ELSE THE LIBRARY WILL BE UPDATED
# Explore all the API Roots not only default one

# 6  DONE
# check value of 'more' for 'true', if true, explore(poll) again with filter value next