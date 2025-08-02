import json
import random

# Sample feeling inputs and their associated genres
samples = [
    ("I'm feeling really low today.", ["Comedy", "Family"]),
    ("I need something thrilling and exciting.", ["Action", "Thriller"]),
    ("Feeling sad and heartbroken.", ["Romance", "Drama"]),
    ("I’m in the mood for something romantic.", ["Romance"]),
    ("Bored and want to watch something wild.", ["Action", "Sci-Fi"]),
    ("Feeling inspired and positive!", ["Drama", "Biography"]),
    ("Feeling nostalgic.", ["Drama", "Family"]),
    ("Feeling stressed out.", ["Comedy", "Fantasy"]),
    ("I want to laugh!", ["Comedy"]),
    ("Feeling lonely and quiet.", ["Romance", "Drama"]),
    ("I’m curious and want something mind-bending.", ["Sci-Fi", "Mystery"]),
    ("Feeling like solving puzzles.", ["Mystery", "Thriller"]),
    ("Need something to pump me up!", ["Action", "Adventure"]),
    ("Feeling gloomy.", ["Comedy", "Romance"]),
    ("Want something beautiful and deep.", ["Drama", "Romance"]),
    ("Feeling like I want to escape reality.", ["Fantasy", "Adventure"]),
    ("Feeling creative.", ["Animation", "Fantasy"]),
    ("Feeling like I want to cry.", ["Drama", "Romance"]),
    ("I'm in the mood for something magical.", ["Fantasy", "Family"]),
    ("Feeling excited and energetic!", ["Action", "Comedy"]),
    ("I'm having a lazy Sunday.", ["Family", "Animation"]),
    ("I want something romantic but funny.", ["Romance", "Comedy"]),
    ("Feeling curious and philosophical.", ["Sci-Fi", "Drama"]),
    ("Feeling hopeful and uplifted.", ["Biography", "Drama"]),
    ("Need something relaxing and light.", ["Comedy", "Romance"]),
    ("Want to laugh out loud!", ["Comedy"]),
    ("Feeling angry.", ["Action", "Thriller"]),
    ("Feeling shy and awkward.", ["Romance", "Comedy"]),
    ("Feeling like an adventure.", ["Adventure", "Fantasy"]),
    ("Feeling lost.", ["Drama", "Mystery"]),
]

# Save as JSON
with open("training_data.json", "w", encoding="utf-8") as f:
    json.dump([{"feeling": f, "genres": g} for f, g in samples], f, indent=2, ensure_ascii=False)

print("✅ Dummy dataset saved as training_data.json")
