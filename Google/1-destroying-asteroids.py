from typing import List

# Sort the asteroids in ascending order
# Iterate through the asteroids
# If the asteroid is greater than the mass, planet is destroyed else the planet gains mass
# Return True if the planet survives in the end

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for i in asteroids:
            if i > mass:
                return False
            mass += i
        return True