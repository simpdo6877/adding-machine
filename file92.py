
while True:
    try:
        first_number=int(input('what is the first number you want to add?'))
        second_number=int(input('waht is the second numberyou want to add?'))
        sum = first_number+second_number
        print('the sum of the two numbers is',sum)
        break
    except:
        print('Your silly. That is not and integer...')