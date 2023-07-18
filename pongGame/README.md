# Pin-Pong Game

This is a simple implementation of the classic game "Ping-Pong" using Python and Turtle graphics.

## Game Components

The game consists of the following components:

- Create screen
- Create and move paddles
- Create ball
- Make the ball move
- Detect collision with walls and bounce
- Detect collision with paddles
- Detect when a paddle misses the ball
- Keep score

## Installation

1. Clone the repository or download the source code.
2. Make sure you have Python installed on your system.
3. Install the required dependencies using the following command:

```shell
pip install turtle
```
## Usage
Run the main.py file to start the game. The game will be displayed on a new window.

* Player 1 controls the left paddle using the "W" and "S" keys.
* Player 2 controls the right paddle using the up and down arrow keys.

The objective of the game is to hit the ball with the paddles and prevent it from crossing your side. Each time the ball passes a paddle and goes into the opponent's side, a point is awarded to the opponent. The player with the highest score wins the game.
## Code Structure
The game code is divided into several files:

* main.py: Contains the main game loop and initializes the game components.
* paddle.py: Defines the Paddle class responsible for the paddle's behavior and movements.
* ball.py: Defines the Ball class responsible for the ball's behavior and movements.
* scoreboard.py: Defines the ScoreBoard class responsible for displaying and updating the scores.
## Customization
You can customize the game by modifying the following variables:

* LEFT_PADDLE_START_POSITION: Initial position of the left paddle.
* RIGHT_PADDLE_START_POSITION: Initial position of the right paddle.
* ON, OFF: Constants representing the game state (on/off).
* screen.setup(width, height): Set the width and height of the game window.
* screen.bgcolor("color"): Set the background color of the game window.
* screen.title("title"): Set the title of the game window.

Feel free to explore and modify the code to add new features or make improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Credits
Special thanks to [Angla Yu](https://twitter.com/yu_angela) for bringing about the idea for this project through her [`100 days of code`](https://www.udemy.com/course/100-days-of-code/) course on Udemy


## Contact
*  🔗: [my website](http://www.ehiane.info/) 
*  📧: ehis.oigiagbe@gmail.com
<p align="left">
    <a href="http://www.ehiane.info/" target="_blank"><img align="center" src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/55af3614-5f7d-4774-be46-e26a1d98f97d" alt="My Website" height="30" width="30" /></a>
    <a href="https://www.linkedin.com/in/ehiane-oigiagbe/" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="LinkedIn" height="30" width="40" /></a>
    <a href="https://github.com/Ehiane" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="GitHub" height="30" width="40" /></a>
    <a href="mailto:ehis.oigiagbe@gmail.com" target="_blank"><img align="center" src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/5018798f-b468-4411-897a-085da028be38" alt="Gmail" height="30" width="40" /></a>
</p>

