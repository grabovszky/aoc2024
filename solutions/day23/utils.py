from itertools import combinations


def parse_input(content):
    """Parse network connections into adjacency lists for faster access."""
    # Use dict for O(1) neighbor lookups
    neighbors = {}

    for line in content.strip().split("\n"):
        a, b = line.split("-")
        neighbors.setdefault(a, set()).add(b)
        neighbors.setdefault(b, set()).add(a)

    return neighbors


def find_triplets(neighbors):
    """Find all 3-computer cliques efficiently."""
    triplets = set()
    computers = list(neighbors.keys())

    # For each computer, look at pairs of its neighbors
    for comp in computers:
        # Get all pairs of neighbors
        for n1, n2 in combinations(neighbors[comp], 2):
            # Check if neighbors are connected
            if n2 in neighbors[n1]:
                # Ensure consistent ordering for deduplication
                triplet = tuple(sorted([comp, n1, n2]))
                triplets.add(triplet)

    return triplets


def find_max_clique(neighbors):
    """Find largest clique using Bron-Kerbosch with pivoting."""

    def bron_kerbosch(r, p, x):
        nonlocal max_clique
        if not p and not x:
            if len(r) > len(max_clique):
                max_clique = r.copy()
            return

        pivot = max((len(neighbors[v] & p) for v in (p | x)), default=0)
        for v in list(p):
            if len(neighbors[v] & p) == pivot:
                new_r = r | {v}
                new_p = p & neighbors[v]
                new_x = x & neighbors[v]
                bron_kerbosch(new_r, new_p, new_x)
                p.remove(v)
                x.add(v)

    max_clique = set()
    p = set(neighbors.keys())
    bron_kerbosch(set(), p, set())
    return max_clique


def has_t_computer(computers):
    """Check if any computer starts with 't'."""
    return any(c.startswith("t") for c in computers)
