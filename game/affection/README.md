# Affection System Documentation

This folder contains a reusable, Object-Oriented system for tracking character affection points in your Ren'Py game. 

## Files in this system

- `affection_system.rpy`: Contains the `CharacterAffection` Python class, which manages the math for affection points (adding, subtracting, and capping).
- `affection_screens.rpy`: Contains the `relationship_indicator` screen, which is a dynamic UI element that takes a `CharacterAffection` object and displays its current status.
- `script_for_test.txt`: A ready-to-use copypasta script. Just copy its contents into your `script.rpy` to immediately test and see how the affection system works in-game.

---

## How to use it

### 1. Define a Character and their Affection Tracker

In your `script.rpy` (or any other initialization script), you need to define your character and their affection tracker using the `default` keyword so that the points are saved and loaded correctly.

```renpy
define e = Character("Eileen")
define b = Character("Bob")

# Initialize trackers
default eileen_affection = CharacterAffection("Eileen")

# You can also set a custom max_points limit (the default is 100)
default bob_affection = CharacterAffection("Bob", max_points=50)
```

### 2. Showing the UI

Whenever you want the player to see the affection bar (e.g. during a conversation), you can show it using `show screen` and pass the character's tracker to it.

```renpy
label start:
    show screen relationship_indicator(eileen_affection)
    e "Hello! My affection bar is now visible."
```

If you want to hide it later:
```renpy
    hide screen relationship_indicator
```

### 3. Modifying Affection Points

Instead of directly changing the variable (like `$ eileen_affection.points += 10`), you should use the built-in methods. These methods automatically prevent the points from dropping below 0 or exceeding the max limit.

```renpy
    # Add points
    $ eileen_affection.add(10)
    
    # Subtract points
    $ eileen_affection.subtract(5)
    
    # Set points directly
    $ eileen_affection.set_points(50)
```

### Example Dialogue Flow

```renpy
label bob_route:
    show screen relationship_indicator(bob_affection)
    
    b "Did you bring the pizza?"
    
    menu:
        "Yes, I did!":
            $ bob_affection.add(20)
            b "You're the best!"
            
        "I forgot...":
            $ bob_affection.subtract(10)
            b "Man, I'm so hungry..."
            
    hide screen relationship_indicator
    return
```
