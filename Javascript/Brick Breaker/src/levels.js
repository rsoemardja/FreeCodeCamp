import Brick from "/src/brick";

export function buildLevel(game, level) {
    let bricks = [];

    level.forEach((row, rowIndex) => {
        row.forEach((brick, brickIndex => {
            if (brick === 1) {
                let position = {
                    x: 80 * brickindex,
                    y: 75 + 24 * rowIndex
                };
                bricks.push(new Brick(game, position));
            }
        });
    });
return bricks;
}