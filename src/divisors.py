def count_divisible_numbers(from_number: int, to_number: int, divisor: int):
    while(from_number != to_number):
        if (from_number % divisor == 0): 
            print(from_number)
        from_number+=1

count_divisible_numbers(2, 10, 2)
