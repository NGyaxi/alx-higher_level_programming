#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            division_result = dividend / divisor
        except (ZeroDivisionError, TypeError):
            if isinstance(dividend, (int, float)) and isinstance(divisor, (int, float)):
                division_result = 0
            elif not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
                print("wrong type")
                division_result = 0
            else:
                print("division by 0")
                division_result = 0
        except IndexError:
            print("out of range")
            division_result = 0
        finally:
            result.append(division_result)
    return result
