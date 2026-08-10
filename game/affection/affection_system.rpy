init python:
    class CharacterAffection(object):
        """
        A reusable Object-Oriented class to track affection for any character.
        
        Usage:
            default eileen_affection = CharacterAffection("Eileen", max_points=100)
            
            $ eileen_affection.add(10)
            $ eileen_affection.subtract(5)
        """
        def __init__(self, name, max_points=100):
            """
            Initializes a new CharacterAffection tracker.
            
            :param name: The name of the character (string)
            :param max_points: The maximum amount of affection the character can have
            """
            self.name = name
            self.points = 0
            self.max_points = max_points

        def add(self, amount):
            """
            Adds affection points. Caps at max_points.
            """
            self.points += amount
            if self.points > self.max_points:
                self.points = self.max_points

        def subtract(self, amount):
            """
            Subtracts affection points. Ensures points do not go below 0.
            """
            self.points -= amount
            if self.points < 0:
                self.points = 0
                
        def set_points(self, amount):
            """
            Directly sets the affection points, clamping it within 0 and max_points.
            """
            self.points = max(0, min(amount, self.max_points))
