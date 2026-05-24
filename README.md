# IPL Data Analyzer

A beginner-friendly Python project built using **Pandas** to analyze IPL match data from **2008–2017**.

This project allows users to explore IPL statistics such as:

* Team with most wins
* Most wins in a season
* IPL season winners
* Match details between two teams

---

## Features

### 1. Most Wins Overall

Displays the team with the highest number of wins in IPL history.

### 2. Most Wins in a Season

Finds which team won the most matches in a specific IPL season.

### 3. Season Winner

Shows the IPL champion for a selected season.

### 4. Match Winner Details

Displays:

* Match winner
* Winning margin
* Toss winner
* Toss decision
* Player of the match
* Match venue

between two selected teams in a selected season.

---

## Technologies Used

* Python
* Pandas
* CSV Dataset

---

## Dataset

Dataset used:

* `matches.csv`

Contains IPL match data from 2008–2017.

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ipl-data-analyzer.git
```

### 2. Move into Project Folder

```bash
cd ipl-data-analyzer
```

### 3. Install Pandas

```bash
pip install pandas
```

### 4. Run the Program

```bash
python main.py
```

---

## Sample Menu

```text
---------IPL DATA (2008 - 2017)---------

1) Most wins so far
2) Most wins in a season
3) Season Winner
4) Match winner
```

---

## Sample Output

```text
Winner of the First Match is Mumbai Indians
Won by 5 Wickets
Toss winner = Rajasthan Royals and they decided to bat first
Player of the match = Sachin Tendulkar
Match venue = Wankhede Stadium
```

---

## Concepts Practiced

This project helped practice:

* Data cleaning with Pandas
* Filtering data
* Conditional statements
* Functions
* User input handling
* Series and DataFrame operations
* `value_counts()`
* `idxmax()`
* Handling missing values

---

## Future Improvements

Possible future upgrades:

* Add matplotlib visualizations
* Create a GUI using Tkinter
* Convert into a web app using Flask
* Add player statistics analysis
* Support latest IPL seasons

---

## Author

Made by Ashwak Kattubadi
