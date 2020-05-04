def int_to_bit(num):
    arr = []
    for i in range(16):
        arr.append(num >> i & 1)
    arr.reverse()
    return arr


def get_manchester_code(list_of_bits):
    new_list = []
    for i in list_of_bits:
        if i:
            new_list.append(1)
            new_list.append(0)
        else:
            new_list.append(0)
            new_list.append(1)
    return new_list


def is_message_broken(list_with_manchester_code):
    state = True
    for i in range(0, int(len(list_with_manchester_code)), 2):
        if list_with_manchester_code[i] != list_with_manchester_code[i + 1]:
            state = False
        else:
            return True
    return state


def get_original_message(list_with_manchester_code):
    message = []
    for i in range(0, int(len(list_with_manchester_code)), 2):
        message.append(list_with_manchester_code[i])
    return message


number = 732
list_of_bit = int_to_bit(number)
print("number == " + str(number))
print("message before operations == " + str(list_of_bit))
print("manchester code == " + str(get_manchester_code(list_of_bit)))
print("message after decoding == " + str(get_original_message(get_manchester_code(list_of_bit))))
print("is message broken == " + str(is_message_broken(get_manchester_code(list_of_bit))))
