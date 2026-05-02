# test karo directly
from classifier import classify_message,detect_priority,analyze_message

# print(classify_message("I was charged twice"))
# print(classify_message("App is not working"))
# print(classify_message("Hello, I need help"))

# print(classify_message("I got the bills mixed up with my error logs")) #limitation

# fix :- It uses substring matching which can cause false positives. The fix would be whole-word matching using regex or upgrading to an LLM-based classifier.

print(analyze_message("My payment is not working, I need help urgently"))

