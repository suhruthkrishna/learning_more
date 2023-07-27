# lambda parameter: expression
# addAll=lambda x,y,z: x+y+z
# full_name=lambda first,last:"The full name is "+first+" "+last
# check_Age=lambda x:True if x>18 else False
# print(addAll(32,64,74))
# print(full_name(first="Suhruth",last="Krishna"))
# print(check_Age(22))
def new_value(k):
    return lambda x:x*k
new_double=new_value(2)
new_triple=new_value(3)
print(new_double(12))
print(new_triple(13))


