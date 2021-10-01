"""
        if 'url:value' in pattern_value:
            value = pattern_value.split("'")[-2]
            temp_path = PATH + '/url.txt'
            if check_list(temp_path,value):
                update_list(temp_path,value)
        elif 'ipv4-addr:value' in pattern_value:
            value = pattern_value.split("'")[-2]
            temp_path = PATH + '/ipv4_addr.txt'
            if check_list(temp_path,value):
                update_list(temp_path,value)
        elif 'ipv6-addr:value' in pattern_value:
            value = pattern_value.split("'")[-2]
            temp_path = PATH + '/ipv6_addr.txt'
            if check_list(temp_path,value):
                update_list(temp_path,value)
        elif 'domain:value' in pattern_value:
            value = pattern_value.split("'")[-2]
            temp_path = PATH + '/domain.txt'
            if check_list(temp_path,value):
                update_list(temp_path,value)
        elif 'E-mail:value' in pattern_value:
            value = pattern_value.split("'")[-2]
            temp_path = PATH + '/email.txt'
            if check_list(temp_path,value):
                update_list(temp_path,value)
        elif 'MD5:value' in pattern_value:
            value = pattern_value.split("'")[-2]
            temp_path = PATH + '/md5.txt'
            if check_list(temp_path,value):
                update_list(temp_path,value)
        elif 'SHA1:value' in pattern_value:
            value = pattern_value.split("'")[-2]
            temp_path = PATH + '/sha1.txt'
            if check_list(temp_path,value):
                update_list(temp_path,value)
        
        else:
            pattern_status = False
        """