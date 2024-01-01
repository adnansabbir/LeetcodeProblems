
    function findContentChildren(g: number[], s: number[]): number {
        g.sort((a, b) => a - b);
        s.sort((a, b) => a - b);

        let contentChildCount = 0;
        let pointerG = 0;
        let pointerS = 0;
        // Iterate using two pointers
        while (pointerG < g.length && pointerS < s.length) {
            // If the current cookie satisfies the current child's greed
            if (s[pointerS] >= g[pointerG]) {
                contentChildCount++;
                pointerG++;
            }
            pointerS++;
        }
        return contentChildCount;
    }

