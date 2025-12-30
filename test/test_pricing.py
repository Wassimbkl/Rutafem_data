import sys
sys.path.append(".")

from src.pricing import compute_price


res = compute_price(
    "Place Saint-Michel, Paris",
    "Gare de Lyon, Paris",
    passengers=2
)

print(res)
