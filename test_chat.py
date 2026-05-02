from classifier import analyze_message
from chat import generate_response

message = "My account was hacked!"

category, priority = analyze_message(message)
response = generate_response(message, category, priority)

print(f"Category: {category}")
print(f"Priority: {priority}")
print(f"Response: {response}")