# main.py

from knowledge_base import get_knowledge_base
from rules import RuleBase
from inference_eng import InferenceEngine

def main():
    print("Welcome to the Rehab Expert System!")
    print("Describe your symptoms, separated by commas (e.g., 'knee pain, swelling'):")
    
    # Get user input
    user_input = input("Enter your symptoms: ").strip().lower()
    user_facts = [symptom.strip() for symptom in user_input.split(",")]

    # Load knowledge base
    rules = get_knowledge_base()
    rule_base = RuleBase(rules)

    # Initialize the inference engine
    inference_engine = InferenceEngine(rule_base.get_rules())

    # Infer recommendations based on user input
    recommendations = inference_engine.infer(user_facts)

    # Display results
    if recommendations:
        print("\nBased on your symptoms, here are the recommendations:")
        for rec in recommendations:
            print(f"- {rec}")
    else:
        print("\nNo recommendations found for the given symptoms. Please consult a specialist.")

if __name__ == "__main__":
    main()

