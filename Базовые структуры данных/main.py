# все операции над данными провожу на отдельных строках, за исключением логических и арифметических, для увеличения читаемости
# 1st programm
print(9**0.5*5)
# 2nd programm
print(9.99>9.98 and 1000!=1000.1)
# 3rd programm
first_expr=2*2+2
second_expr=2*(2+2)
third_expr= first_expr == second_expr
print(first_expr, second_expr, third_expr)
# 4th programm
input_data = '123.456'
# Ваш вариант решения
output=float(input_data) # int() type convert error, input_data after convert has type float, but not int
print(int(output*10%10)) # int() for get digit before dot
# Мой вариант решения
dot_index=input_data.find(".") # at start we get index of dot in string
print(int(input_data[dot_index+1])) # here we use index of dot for targeting to digit we are interested in