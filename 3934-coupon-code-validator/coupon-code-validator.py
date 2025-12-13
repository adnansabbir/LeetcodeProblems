class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        e, g, p, r = [], [], [], []

        for i in range(len(isActive)):
            if not isActive[i]:
                continue

            bl = businessLine[i]
            if bl not in ("electronics", "grocery", "pharmacy", "restaurant"):
                continue

            if not code[i]:
                continue

            if not all(ch.isalnum() or ch == '_' for ch in code[i]):
                continue

            if bl.startswith("e"): e.append(code[i])
            if bl.startswith("g"): g.append(code[i])
            if bl.startswith("p"): p.append(code[i])
            if bl.startswith("r"): r.append(code[i])

        return sorted(e) + sorted(g) + sorted(p) + sorted(r)