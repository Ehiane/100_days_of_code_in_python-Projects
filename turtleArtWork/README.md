# 🐢🖼️🎨|turtleArtWorks

This project showcases the power and creativity of Turtle graphics, a Python library for creating stunning visual artwork. The code includes various features, including the ability to draw connected polygon shapes, generate random walk art, and create mesmerizing spirograph patterns. The project not only demonstrates programming skills but also highlights the importance of documentation and the ability to explore and leverage new libraries.

## Demo(s)
<p align="center">
  <img src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/96b96803-3b38-47b9-9406-70be99a57897" alt="David Hirst Flumineque replica" width="300">
  <img src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/0edb6d01-2c5e-4c4d-a8ad-099cd298ec14" alt="Polygon Demo" width="300">
  <img src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/7bfd4e7c-1cab-42c5-a645-6eb679cb15eb" alt="Random Walk Demo" width="300">
  <img src="https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/e929f951-61d2-479a-b02d-69cbe329b523" alt="Untitled Video" width="300">
</p>


## Key Features

### Replicate of  David Hirst's Flumequine artwork

> Attempted to replicate David Hirst's Flumequine artwork by creating a grid of circles and alternating row directions using Turtle graphics.

![David Hirst Flumineque replica - Made with Clipchamp](https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/96b96803-3b38-47b9-9406-70be99a57897)



### Drawing Connected Polygon Shapes

> The code includes functions to draw connected polygon shapes, ranging from a triangle to a decagon. Each shape is filled with a randomly selected color, creating visually appealing geometric patterns. This feature demonstrates proficiency in creating modular and reusable code.

![polygon demo - Made with Clipchamp](https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/0edb6d01-2c5e-4c4d-a8ad-099cd298ec14)



### Random Walk Art Generator

> The project includes a random walk art generator that creates unique and unpredictable patterns. The Turtle object moves in random directions, creating strokes of various lengths and colors. This feature showcases creativity and the ability to utilize randomness to generate artwork.

![random walk demo - Made with Clipchamp](https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/7bfd4e7c-1cab-42c5-a645-6eb679cb15eb)



### Mesmerizing Spirograph Patterns

> The code allows you to generate captivating spirograph patterns. By specifying the gap size between each circle, the Turtle object draws intricate and symmetrical designs. This feature demonstrates an understanding of mathematical concepts and the ability to translate them into visual representations.

![Untitled video - Made with Clipchamp (1)](https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/e929f951-61d2-479a-b02d-69cbe329b523)


## Dependencies

The code relies on the following libraries:
- Turtle: `pip install turtle`
- Random: Already included in Python's standard library
- Colorgram: `pip install colorgram.py`

**Note:** The Colorgram library is used to extract colors from an image and generate the color list. Make sure to install this library before running the code.



### Importance of Documentation and Library Exploration

The project emphasizes the significance of documentation and the process of exploring new libraries. By referring to the Turtle documentation and experimenting with different functions and features, the code demonstrates the ability to learn and apply new technologies. This showcases adaptability, self-directed learning, and a growth mindset.

## Usage

1. Install the necessary libraries:
   - Turtle: `should be already built in with python 3.8, if not:`
     ```python
     pip install turtle
     ```
   - Random: Already included in Python's standard library
   - Colorgram: `pip install colorgram.py`

2. Import the required modules:
   - `import turtle as t`
   - `import random as r`
   - `import colorgram`

3. Set up the Turtle graphics window and create a Turtle object:
```python
  t.colormode(255)
  t.setup()
  screen = t.Screen()
  screen_size = t.screensize(2000, 2000, 'black')
  turtle = t.Turtle()
```


4. Extract colors from an image using Colorgram:
```
  rgb_colors = []
  colors = colorgram.extract('image.jpg', 30)
  for color in colors:
  r = color.rgb.r
  g = color.rgb.g
  b = color.rgb.b
  new_color = (r, g, b)
  rgb_colors.append(new_color)
```
Replace `'image.jpg'` with the path to the desired image. This code snippet generates the `color_list` using the Colorgram library.

5. Explore the different features:
- Drawing connected polygon shapes: Call the respective shape functions (triangle, square, pentagon, etc.) with the desired parameters.
- Random walk art generator: Call the `random_walk(obj)` function with the desired Turtle object.
- Spirograph: Call the `draw_spirograph(gap_size)` function with the desired gap size between each circle.

6. Run the code and observe the captivating artwork created by Turtle graphics.

## Benefits

- Demonstrates proficiency in Python programming and familiarity with the Turtle graphics library.
- Showcases creativity and the ability to generate visually appealing artwork.
- Highlights the importance of documentation in accessing and understanding new libraries.
- Demonstrates self-directed learning and the ability to explore and apply new technologies.
- Exhibits attention to detail, modular code design, and the ability to create reusable functions.

## References

- Turtle documentation: [https://docs.python.org/3/library/turtle.html](https://docs.python.org/3/library/turtle.html)
- Random module documentation: [https://docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html)
- Colorgram library: [https://github.com/obskyr/colorgram.py](https://github.com/obskyr/colorgram.py)

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

