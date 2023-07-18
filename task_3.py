import datetime

start = datetime.datetime.now()
time_start = start.microsecond/1000

# Задача 1

number = int(input("Введите целое положительное число :"))
def factorial_number(number:int):
    factorial = 1
    for n in range(1, number+1):
        factorial = factorial * n
    print(f'Факториал числа "{number}"= {factorial}')
    return factorial
factorial_number (number)

# Задача 2

string = 'absddsabllk'
sub_string = 'ab'
sub_string_len = len(sub_string)
insertion = 0
for i in range(len(string)):
    if string[i:i+sub_string_len] == sub_string:
        insertion += 1
print(f"Подстрока входит в строку {insertion} раза")

# Задача 3

nums_1 = [1, 3]    #  Общее колличество чисел в массивах нечетное.
nums_2 = [2]

# nums_1 = [1, 2]    #  Общее колличество чисел в массивах четное.
# nums_2 = [3, 4]

def findMedianSortedArrays( nums_1, nums_2):
    merged_array = nums_1 + nums_2
    merged_array_sort = sorted(merged_array)
    len_nums = len(merged_array_sort)
    remains = len_nums % 2
    middle_element = int((len_nums - remains) / 2)
    if remains == 1:
        median = merged_array_sort[middle_element]
        print(f"Медиана массивов =  {median}")
    else:
        array_element_1 = merged_array_sort[middle_element-1]
        array_element_2 = merged_array_sort[middle_element]
        median = (array_element_1+array_element_2)/2
        print(f"Медиана массивов =  {median}")
    return median

findMedianSortedArrays(nums_1, nums_2)

end = datetime.datetime.now()
time_end = end.microsecond/1000
print(f"Время в миллисекундаx {time_end-time_start}")



