function numberOfWeakCharacters(properties) {
    properties = properties.sort(function (a, b) { return a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]; });
    var size = properties.length - 1;
    var attacks = {};
    for (var i = 0; i <= size; i++) {
        var prop = properties[i];
        if (!attacks[prop[0]]) {
            attacks[prop[0]] = [i, -1];
            if (i != 0) {
                attacks[properties[i - 1][0]][1] = i;
            }
        }
    }
    // console.log(properties)
    // console.log(attacks)
    var largestFromLast = new Array(properties.length);
    for (var i = size; i >= 0; i--) {
        if (i == size) {
            largestFromLast[i] = properties[i][1];
        }
        else {
            largestFromLast[i] = Math.max(largestFromLast[i + 1], properties[i][1]);
        }
    }
    var hasLargerDefence = function (start, value) {
        var end = size;
        while (start <= end) {
            var mid = Math.floor((start + end) / 2);
            if (largestFromLast[mid] > value)
                return true;
            else if (largestFromLast[mid] <= value) {
                end = mid - 1;
            }
            else {
                start = mid + 1;
            }
        }
        return false;
    };
    var weakCaharacters = 0;
    for (var _i = 0, properties_1 = properties; _i < properties_1.length; _i++) {
        var prop = properties_1[_i];
        var largerAttackIndex = attacks[prop[0]][1];
        if (largerAttackIndex === -1)
            continue;
        if (hasLargerDefence(largerAttackIndex, prop[1])) {
            weakCaharacters++;
        }
    }
    return weakCaharacters;
}
;
