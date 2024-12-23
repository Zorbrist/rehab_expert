# inference_eng.py

class InferenceEngine:
    def __init__(self, rules, facts):
        self.rules = rules
        self.facts = facts

    def infer(self):
        recommendations = []
        for rule in self.rules:
            # Check if all conditions in the rule are met
            if all(condition in self.facts for condition in rule["if"]):
                recommendations.append(rule["then"])
        return recommendations
