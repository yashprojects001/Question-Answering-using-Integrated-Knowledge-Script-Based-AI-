# Program 3: Integrated Knowledge-Based Question Answering

# Structured text facts
text_facts = {
    "person": "Mary",
    "activity": "shopping",
    "location": "market",
    "object_bought": "red coat"
}

# World knowledge (script)
world_knowledge = {
    "shopping": {
        "location": "market",
        "not_at_home": True
    }
}

def answer_question(question):
    question = question.lower()

    # Q1: What did Mary buy?
    if "what did mary buy" in question:
        return text_facts["object_bought"]

    # Q2: Where was Mary?
    if "where was mary" in question:
        return text_facts["location"]

    # Q3: Why couldn't mary's brother reach her?
    if "why couldn't mary's brother reach her" in question:
        if world_knowledge["shopping"]["not_at_home"]:
            return "Because she wasn't home."

    return "No answer found."

# Example Run
print("Integrated Knowledge System Loaded.")
user_question = input("Enter your question: ")
print("Answer:", answer_question(user_question))
