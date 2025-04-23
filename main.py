class BusinessIdea:
    def __init__(self, title, tools, roi, steps):
        self.title = title
        self.tools = tools
        self.roi = roi
        self.steps = steps

    def display(self):
        # Fancy printout or return structured data
        pass

class IdeaGenerator:
    def __init__(self):
        self.ideas = []  # Load from file or create internally

    def generate_idea(self) -> BusinessIdea:
        # Randomly (or logically) create and return a new idea
        pass

class User:
    def __init__(self, name):
        self.name = name
        self.saved_ideas = []

    def save_idea(self, idea: BusinessIdea):
        self.saved_ideas.append(idea)
