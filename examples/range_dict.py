before = {"i1": 10, "i2": 15, "i3": 10, "i5": 1}
after = {"i1": 14, "i2": 14, "i4": 5, "i5": 50}


class RangeDict(dict):
    def __missing__(self, key):
        items = (items for items in self.items() if isinstance(items[0], tuple))
        for (lower, upper), value in items:
            if lower <= key < upper:
                return value
        raise KeyError(f"Cannot find {key} in ranges")

flags = RangeDict(
    {
        (0, .1): "",
        (.1, .5): "*",
        (.5, float("inf")): "**",
    }
)


delt = "\N{greek capital letter delta}"
print(f"{' ' * 5}{'before':>8} {'after':>8} {f'|{delt}|':>8} {f'% {delt}':>10}")
for k in sorted(set(before) & set(after)):
    bef, aft = before[k], after[k]
    abs_diff, pct_diff = abs(aft - bef), abs(aft - bef) / bef
    print(
        f"{k:<4} {bef:>8.0f} {aft:>8.0f} {abs_diff:>8.2f} {pct_diff*100:>9.2f}"
        f"% {flags[pct_diff]}"
    )
