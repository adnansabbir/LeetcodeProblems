function computeArea(ax1: number, ay1: number, ax2: number, ay2: number, bx1: number, by1: number, bx2: number, by2: number): number {
    const rectangle1Area = (ax2 - ax1) * (ay2 - ay1)
    const rectangle2Area = (bx2 - bx1) * (by2 - by1)

    const overlapX = Math.max(0, Math.min(ax2, bx2) - Math.max(ax1, bx1))
    const overlapY = Math.max(0, Math.min(ay2, by2) - Math.max(ay1, by1))

    return rectangle1Area + rectangle2Area - (overlapX * overlapY)
};