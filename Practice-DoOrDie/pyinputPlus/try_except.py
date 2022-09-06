while True:
    print('Enter Your Age')
    age = input()
    
    try:
        age=int(age)
    except:
        print('Enter Numeric digits')
        continue
    if age <1:
        print('please enter a positive Number') 
        continue

    break



print(f'You Age is {age}.')