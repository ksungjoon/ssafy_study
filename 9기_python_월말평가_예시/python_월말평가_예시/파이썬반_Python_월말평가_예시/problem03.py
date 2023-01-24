def is_user_data_valid(user_data):
    result = 0
    if bool(user_data['id']) == True and bool(user_data['password']) == True:
        result += 1
    return bool(result)
    pass




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': '',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data1)) 
    # False 

    user_data2 = {
        'id': 'jungssafy',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data2)) 
    # True