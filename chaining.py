# chaining.py

def forward_chaining(rules, facts):
    new_facts = facts.copy()
    recommendations = []

    while True:
        added_new_fact = False
        for rule in rules:
            if all(condition in new_facts for condition in rule["if"]) and rule["then"] not in new_facts:
                new_facts.append(rule["then"])
                recommendations.append(rule["then"])
                added_new_fact = True

        if not added_new_fact:
            break

    return recommendations

