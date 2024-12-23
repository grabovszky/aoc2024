from solutions.day23.part1 import solve_part1
from solutions.day23.part2 import solve_part2


TEST_INPUT = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""


def test_part1():
    assert solve_part1(TEST_INPUT.strip()) == 7


def test_part2():
    assert solve_part2(TEST_INPUT.strip()) == "co,de,ka,ta"
