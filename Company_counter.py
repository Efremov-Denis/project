effect = int(input("Enter your effect")) # выручка
charges = int(input("Enter your charges")) # издержки
profit = effect - charges
if profit > 0:
    print("your company is successful")
    print(f"profitability is: {profit / effect * 100:.4f}")
    workers = int(input("How many employees work in your company?"))
    print(f"one worker profit is: {profit / workers:.4f}")
if profit < 0:
    print("your company isn't successful")
if profit == 0:
    print("your company isn't successful")