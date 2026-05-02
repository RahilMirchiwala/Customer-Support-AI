def classify_message(message: str) -> str:
  message = message.lower()

  billing_words = ["charged","payment",'money',"invoice","bill","refund","subscription","price"]
  technical_words = ["not working","login","error","bug","slow","password","crash","broken","hacked","scammed"]

  for word in billing_words:
    if word in message:
      return "Billing"
  
  for word in technical_words:
    if word in message:
      return "Technical"
    
  return "General"

def detect_priority(message: str) -> str:
  message = message.lower()

  high_words = ["urgent", "immediately","hurry","fast","no time","not working","can't login","data lost","asap","critical","hacked","scammed","suspended","failed"]
  medium_words = ["slow", "sometimes","refund","not sure","issue","problem"]

  for word in high_words:
    if word in message:
      return "High"
    
  for word in medium_words:
    if word in message:
      return "Medium"
    
  return "Low"

def analyze_message(message: str):
    category = classify_message(message)
    priority = detect_priority(message)
    return category, priority
