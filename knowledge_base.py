# knowledge_base.py

def get_knowledge_base():
    # Define some sample rules
    rules = [
        {"if": ["knee pain", "swelling"], "then": "recommend physiotherapy for the knee"},
        {"if": ["back pain", "difficulty bending"], "then": "recommend core strengthening exercises"},
        {"if": ["shoulder pain", "limited motion"], "then": "recommend shoulder mobility exercises"},
        {"if": ["neck pain", "stiffness"], "then": "recommend neck stretching exercises"},
    ]
    return rules
