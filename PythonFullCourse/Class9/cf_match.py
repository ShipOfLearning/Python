# Match-Case Statement Demo
day = input("Enter a day number (1-7): ")
match day:
    case "1":
        print("Monday")
    case "2":
        print("Tuesday")
    case "3":
        print("Wednesday")
    case "4":
        print("Thursday")
    case "5":
        print("Friday")
    case "6":
        print("Saturday")
    case "7":
        print("Sunday")
    case _:
        print("Invalid day number")

# # demo of infinite loop with match-case to print day names
# index = 0
# while index < 3:
#     day = input("Enter a day number (1-7): ")
#     match day:
#         case "1":
#             print("Monday")
#         case "2":
#             print("Tuesday")
#         case "3":
#             print("Wednesday")
#         case "4":
#             print("Thursday")
#         case "5":
#             print("Friday")
#         case "6":
#             print("Saturday")
#         case "7":
#             print("Sunday")
#         case _:
#             print("Invalid day number")