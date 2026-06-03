from datetime import datetime


def show_help():
    print("\nAvailable Commands:")
    print("hello  - Greeting")
    print("name   - Bot name")
    print("time   - Current time")
    print("date   - Today's date")
    print("add    - Addition")
    print("sub    - Subtraction")
    print("mul    - Multiplication")
    print("div    - Division")
    print("help   - Show commands")
    print("bye    - Exit chatbot\n")


def calculator(operation):
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == "add":
            print(f"Bot: Result = {num1 + num2}")

        elif operation == "sub":
            print(f"Bot: Result = {num1 - num2}")

        elif operation == "mul":
            print(f"Bot: Result = {num1 * num2}")

        elif operation == "div":
            if num2 == 0:
                print("Bot: Cannot divide by zero!")
            else:
                print(f"Bot: Result = {num1 / num2}")

    except ValueError:
        print("Bot: Please enter valid numbers.")


print("=" * 40)
print(" Welcome to CodeAlpha Chatbot ")
print("=" * 40)
print("Type 'help' to see available commands.\n")

while True:

    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! How can I help you?")

    elif user == "name":
        print("Bot: I am CodeAlpha Chatbot.")

    elif user == "time":
        current_time = datetime.now().strftime("%I:%M:%S %p")
        print("Bot: Current Time =", current_time)

    elif user == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's Date =", current_date)

    elif user in ["add", "sub", "mul", "div"]:
        calculator(user)

    elif user == "help":
        show_help()

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that command.")