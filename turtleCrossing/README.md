# 🐢🛣️🚗|Turtle Cross Game

Turtle Cross is a simple arcade game implemented in Python using the Turtle graphics library. The objective of the game is to control the turtle and make it cross the road while avoiding the moving cars. The game gets progressively harder with each level, as the cars move faster.

## Demo
<div align="center">
    <img src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/74f86ec7-7ca4-4c0e-a99f-9294a345f014" alt="turtle_crossing - Made with Clipchamp">
</div>



## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Gameplay](#gameplay)
- [Controls](#controls)
- [Classes](#classes)
- [Credits](#credits)

## Installation

1. Clone the repository or download the source files.
2. Ensure you have Python (>= 3.6) installed on your system.
3. Install the required dependencies by running the following command:
```
pip install turtle

```

## Usage

Run the game by executing `main.py` in your Python environment.

```
python main.py

```

## Gameplay

In Turtle Cross, you control the turtle character, represented by a green turtle shape, using the arrow keys. Your objective is to move the turtle up the screen and cross the road without colliding with any of the moving cars. As the game progresses, the cars move faster, making it more challenging to cross safely.

If the turtle collides with any car, the game ends, and a "GAME OVER" message is displayed on the screen. However, if the turtle successfully crosses the road and reaches the finish line, you will advance to the next level, and the cars will move even faster.

The game continues until the turtle collides with a car or until the player decides to close the window.

## Controls

- Use the **Up arrow key** to move the turtle upward.

## Classes

### `main.py`

- **Globals**:
    - `ON`, `OFF`: Boolean constants used for game state.
    - `screen`: The Turtle graphics screen instance.
    
- **Instantiated Classes**:
    - `my_player`: An instance of the `Player` class, representing the turtle character.
    - `first_car`: An instance of the `CarManager` class, representing the first car on the road.
    - `score_board`: An instance of the `Scoreboard` class, displaying the player's current level.

- **Key-Bindings**:
    - `Up`: Binds the "Up" arrow key to the `move_up` function of the `Player` class.

- **Game Loop**:
    - The main game loop (`Game_Engine`) controls the flow of the game and checks for collisions and level completion.

### `car_manager.py`

- **Constants**:
    - `COLORS`: A list of colors used for the cars.
    - `STARTING_MOVE_DISTANCE`: The initial speed at which the cars move.
    - `MOVE_INCREMENT`: The amount the car speed increases with each level.

- **Class**:
    - `CarManager`: Handles the random generation and movement of cars.

### `player.py`

- **Constants**:
    - `STARTING_POSITION`: The initial position of the turtle.
    - `MOVE_DISTANCE`: The distance the turtle moves upward with each step.
    - `FINISH_LINE_Y`: The y-coordinate of the finish line.

- **Class**:
    - `Player`: Represents the turtle character and handles its movement.

### `score_board.py`

- **Constants**:
    - `FONT`: The font used for the scoreboard text.

- **Class**:
    - `Scoreboard`: Manages the game's score text and incrementing the levels.

## Credits

Special thanks to [Angla Yu](https://twitter.com/yu_angela) for bringing about the idea for this project through her [`100 days of code`](https://www.udemy.com/course/100-days-of-code/) course on Udemy

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Contact
*  🔗: [my website](http://www.ehiane.info/) 
*  📧: ehis.oigiagbe@gmail.com
<p align="left">
    <a href="http://www.ehiane.info/" target="_blank"><img align="center" src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/55af3614-5f7d-4774-be46-e26a1d98f97d" alt="My Website" height="30" width="30" /></a>
    <a href="https://www.linkedin.com/in/ehiane-oigiagbe/" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="LinkedIn" height="30" width="40" /></a>
    <a href="https://github.com/Ehiane" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="GitHub" height="30" width="40" /></a>
    <a href="mailto:ehis.oigiagbe@gmail.com" target="_blank"><img align="center" src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/5018798f-b468-4411-897a-085da028be38" alt="Gmail" height="30" width="40" /></a>
</p>

