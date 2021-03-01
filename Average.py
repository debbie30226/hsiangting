def is_float(a):
    try:
        float(a)
    except ValueError:
        try:
            complex(s)
        except ValueError:
            return False
    return True
                
    
def average(data):
    a = input()
    x = 0
    while is_float(a):
        a = input()
        x = x + a
    else:
        False

    
    for i in data :
        ans += x
        return ans/len(x)
    
print(average(x))