# 🐿️🗃️🧮 |analysingSquirrelData

[![GitHub license](https://img.shields.io/badge/License-MIT-blue.svg)](analysingSquirrelData/blob/master/LICENSE)
![Squirrel Shocked GIF - Squirrel Shocked Shock - Discover   Share GIFs](https://github.com/Ehiane/100_days_of_code_in_python-Projects/assets/79903725/b330f225-8d78-4e3b-ae0f-43ee249861a3)


## Squirrel Fur Color Analysis

This repository contains a Python script that analyzes the fur color distribution of squirrels based on data from the 2018 Central Park Squirrel Census. The script reads the squirrel data from a CSV file, performs the analysis, and creates a new dataset with the count of gray, cinnamon, and black squirrels.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Results](#results)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

The 2018 Central Park Squirrel Census provided valuable data on squirrel populations, including information about their fur colors. This Python script takes the squirrel dataset, performs an analysis to find the individual counts of gray, cinnamon, and black squirrels, and generates a new dataset with the results. The analysis is done using the Pandas library, which allows for efficient data manipulation and computation.

## Prerequisites

Make sure you have the following installed before running the script:

- Python 3.x: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Pandas library: Install using `pip install pandas`

## Installation

1. Clone this repository to your local machine:
   ```
   git clone ttps://github.com/Ehiane/100_days_of_code_in_python-Projects/tree/main/analysingSquirrelData
   ```
2. Navigate to the project directory:
   ```
   cd analysingSquirrelData
   ```
3. Install the required dependencies:
   ```
   pip install pandas
   ```

## Usage

1. Replace the existing dataset with your own squirrel data in CSV format. Ensure the data contains a column with the fur color information.

2. Modify the `FILE_NAME` and `QUERRY` variables in the Python script to match the file path and the name of the column containing fur colors.

3. Run the Python script:
```
python automate.py
```

4. The script will perform the analysis and generate a new CSV file named `personal_fur_count.csv` with the counts of gray, cinnamon, and black squirrels.

## Dataset

Ensure your dataset is formatted as follows:
```
, Fur Color , ...
0, Gray , ...
1, Cinnamon , ...
2, Black , ...
... , ... , ...
```

The fur color values should be one of "Gray", "Cinnamon", or "Black" for accurate analysis.

## Results

The script will produce a new dataset with the count of gray, cinnamon, and black squirrels. The columns will be labeled as follows:
```
, Fur Color , Count
0, Gray , ...
1, Cinnamon , ...
2, Black , ...
```

The `Count` column will represent the number of squirrels for each fur color.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This dataset was obtained from [2018 Central Park Squirrel Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw)


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
