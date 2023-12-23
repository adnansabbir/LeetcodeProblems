function isPathCrossing(path: string): boolean {
    
        const visitedPositions: Set<string> = new Set();
        const position = [0,0]
        visitedPositions.add(`${position[0]},${position[1]}`);

        for (const direction of path) {
            switch (direction) {
                case 'N':
                    position[1]++;
                    break;
                case 'S':
                    position[1]--;
                    break;
                case 'E':
                    position[0]++;
                    break;
                case 'W':
                    position[0]--;
                    break;
            }

            const currentPosition: string = `${position[0]},${position[1]}`;
            if (visitedPositions.has(currentPosition)) {
                return true;
            }
            visitedPositions.add(currentPosition);
        }

        return false;
};