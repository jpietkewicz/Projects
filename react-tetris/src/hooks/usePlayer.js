import { useState, useCallback } from 'react';

import { TETROMINOS, randomTetromino } from '../tetrominos';
import { STAGE_WIDTH, checkCollision } from '../gameHelpers';

export const usePlayer = () => {
    const [player, setPlayer] = useState({
        pos: { x: 0, y: 0 },
        tetromino: TETROMINOS[0].shape,
        collided: false,
    });

    function rotate(matrix, dir) {
        const rotatedTetromino = matrix.map((_, index) => 
            matrix.map(col => col[index]),
        );

        if (dir > 0) {
            return rotatedTetromino.map(row => row.reverse());
        }
        return rotatedTetromino.reverse();
    }

    function playerRotate(stage, dir) {
        const playerClone = JSON.parse(JSON.stringify(player));
        playerClone.tetromino = rotate(playerClone.tetromino, dir);

        const pos = playerClone.pos.x;
        let offset = 1;
        while(checkCollision(playerClone, stage, { x: 0, y: 0 })) {
            playerClone.pos.x += offset;
            offset = -(offset + (offset > 0 ? 1 : -1));
            if (offset > playerClone.tetromino[0].length) {
                rotate(playerClone.tetromino, -dir);
                playerClone.pos.x = pos;
                return;
            }
        }
        setPlayer(playerClone);
    }

    const updatePlayerPos = ({ x, y, collided }) => {
        setPlayer(prev => ({
            ...prev,
            pos: { x: (prev.pos.x += x), y: (prev.pos.y += y) },
            collided,
        }));
    };

    const resetPlayer = useCallback(() => {
        setPlayer({
            pos: { x: STAGE_WIDTH / 2 - 2, y: 0 },
            tetromino: randomTetromino().shape,
            collided: false,
        });
    }, []);

    return [player, updatePlayerPos, resetPlayer, playerRotate];
};