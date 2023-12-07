window.addEventListener('load', function() {
    // Cavas setup
    const mainCanvas = document.getElementById('main-canvas');
    const ctx = mainCanvas.getContext('2d');
    mainCanvas.width = 800;
    mainCanvas.height = 600;

    class InputHandler {
        constructor(game) {
            this.game = game;
            this.possibleKeys = ['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight', ' '];
            window.addEventListener('keydown', e => {
                if (this.possibleKeys.includes(e.key) && this.game.keys.indexOf(e.key) === -1) {
                    this.game.keys.push(e.key);
                }
            });
            window.addEventListener('keyup', e => {
                if (this.possibleKeys.includes(e.key)) {
                    this.game.keys.splice(this.game.keys.indexOf(e.key), 1);
                }
            });
        }
    }

    class Projectile {
        constructor(game, x, y) {
            this.game = game;
            this.x = x;
            this.y = y;
            this.width = 10;
            this.height = 10;
            this.speed = 5;
            this.markedForDeletion = false;
        }

        update(deltaTime) {
            this.x += this.speed;
            if (this.x > this.game.width) {
                this.markedForDeletion = true;
            }
        }

        draw(context) {
            context.fillStyle = 'red';
            context.fillRect(this.x, this.y, this.width, this.height);
        }
    }

    class Player {
        constructor(game) {
            this.game = game;
            this.width = 50;
            this.height = 40;
            this.x = 20;
            this.y = 100;
            this.speed = 5;
            this.speedX = 0;
            this.speedY = 0;
            this.projectiles = [];
            this.shootCooldown = 0;
            this.shootCooldownMax = 10;
        }

        update(deltaTime) {
            if (this.game.keys.includes('ArrowUp')) {
                this.speedY = this.speed * -1;
            } else if (this.game.keys.includes('ArrowDown')) {
                this.speedY = this.speed;
            } else {
                this.speedY = 0;
            }

            if (this.game.keys.includes('ArrowLeft')) {
                this.speedX = this.speed * -1;
            } else if (this.game.keys.includes('ArrowRight')) {
                this.speedX = this.speed;
            } else {
                this.speedX = 0;
            }
            
            this.x += this.speedX;
            this.y += this.speedY;

            if (this.game.keys.includes(' ') && this.shootCooldown === 0) {
                this.shoot();
                this.shootCooldown = this.shootCooldownMax;
            }
            
            if (this.shootCooldown > 0) {
                this.shootCooldown--;
            }
            
            this.projectiles.forEach(projectile => {
                projectile.update();
            });
            this.projectiles = this.projectiles.filter(projectile => !projectile.markedForDeletion);
        }

        draw(context) {
            context.fillStyle = 'blue';
            context.fillRect(this.x, this.y, this.width, this.height);
            this.projectiles.forEach(projectile => {
                projectile.draw(context);
            });
        }

        shoot() {
            const projectile = new Projectile(this.game, this.x + this.width, this.y + this.height / 2);
            this.projectiles.push(projectile);
        }
    }

    class Enemy {

    }

    class Layer {

    }

    class Background {

    }

    class UI {

    }

    class Game {
        constructor(width, height) {
            this.width = width;
            this.height = height;
            this.player = new Player(this);
            this.inputHandler = new InputHandler(this);
            this.keys = [];
        }

        update(deltaTime) {
            this.player.update();
        }

        draw(context) {
            this.player.draw(context);
        }
    }

    const game = new Game(mainCanvas.width, mainCanvas.height);
    let lastTime = 0;

    // Game loop
    function gameLoop(timeStamp) {
        const deltaTime = timeStamp - lastTime;
        lastTime = timeStamp;
        console.log(deltaTime);
        ctx.clearRect(0, 0, mainCanvas.width, mainCanvas.height);
        game.update(deltaTime);
        game.draw(ctx);

        // Call gameLoop again on the next frame
        requestAnimationFrame(gameLoop);
    }
    
    // Start the game loop
    gameLoop(0);
});
