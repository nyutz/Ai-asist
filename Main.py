from systems import retry_generation

print("🧠 AI Assistant Started")
print("Ketik 'exit' untuk keluar\n")

while True:

    user_input = input("You: ")

    # keluar
    if user_input.lower() == "exit":
        print("👋 Goodbye")
        break

    # generate dengan retry system
    result = retry_generation(user_input)

    print("\nAssistant:\n")
    print(result)
    print("\n" + "="*50 + "\n")
