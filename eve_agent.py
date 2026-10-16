import random, math

SIZE = 10

# Hidden EVE
eve = (random.randint(0, SIZE-1), random.randint(0, SIZE-1))
wall_e = (0, 0)

# Initial belief
belief = {(x, y): 1/(SIZE*SIZE)
          for x in range(SIZE)
          for y in range(SIZE)}

def signal(pos):
    d = math.dist(pos, eve)
    return max(0, math.exp(-d/3) + random.gauss(0, 0.05))

def normalize():
    total = sum(belief.values())
    for c in belief:
        belief[c] /= total

# Search loop
for step in range(20):

    obs = signal(wall_e)

    # Bayesian update
    for cell in belief:
        d = math.dist(wall_e, cell)
        expected = math.exp(-d/3)
        likelihood = math.exp(-(obs-expected)**2 / 0.02)
        belief[cell] *= likelihood

    normalize()

    # Most likely location
    target = max(belief, key=belief.get)

    print(f"Step {step}: WALL-E={wall_e}, Target={target}")

    # Move one step toward target
    x, y = wall_e
    tx, ty = target

    if x < tx: x += 1
    elif x > tx: x -= 1
    elif y < ty: y += 1
    elif y > ty: y -= 1

    wall_e = (x, y)

# Result
guess = max(belief, key=belief.get)

print("\nPredicted:", guess)
print("Actual   :", eve)
print("Error    :", round(math.dist(guess, eve), 2))