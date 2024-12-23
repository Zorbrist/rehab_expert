# inference_eng.py

class InferenceEngine:
    def __init__(self, rules):
        self.rules = rules

    def infer(self, user_facts):
        recommendations = []
        for rule in self.rules:
            # Check if all conditions in the rule are met
            if all(condition in user_facts for condition in rule["if"]):
                recommendations.append(rule["then"])
        return recommendations
