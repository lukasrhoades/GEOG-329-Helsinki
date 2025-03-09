# Exercise 6 - Data analysis with Pandas II

In this week's exercise we will continue developing our skills using Pandas to analyze climate data.

After making your changes to the notebook, you will need to upload it to GitHub.

If you are uncertain about **the style of your code**, take a look at the **[PEP 8 - Style guide for Python code](https://www.python.org/dev/peps/pep-0008/)**.

- **Exercise 6 is due by the start of the next lesson (9:15 am, 16 October 2019)**.
- Don't forget to check out the [hints for this week's exercise](https://geo-python.github.io/2019/lessons/L6/exercise-6.html) if you're having trouble.
- Scores on this exercise are out of **20 points (Problems 1-3)**. Problem 4 is optional.

## Before you start

### Clone the Exercise 6 repository

Make sure you cloned your own repository (repository name contains your GitHub username). After solving the problems, remember to commit your changes and push them to GitHub. Remember also to answer all written questions in the exercise, in addition to the programming tasks.

### Input data

For problems 1-3 in this exercise we will be using climate data from the Helsinki-Vantaa airport station.
For these problems, we have daily observations obtained from the [NOAA Global Historical Climatology Network](https://www.ncdc.noaa.gov/cdo-web/search?datasetid=GHCND).
The file was downloaded using the "Custom GHCN-Daily Text" output format, including following attributes:

| Attribute                | Description                      |
|--------------------------|----------------------------------|
| `STATION`                | Unique ID of the weather station |
| `ELEVATION`              | Elevation of the station         |
| `LATITUDE` , `LONGITUDE` | Coordinates of the station       |
| `DATE`                   | Date of the measurement          |
| `PRCP`                   | Precipitation                    |
| `TAVG`                   | Average temperature              |
| `TMAX`                   | Maximum temperature              |
| `TMIN`                   | Minimum temperature              |

The file for this problem is exactly as available from the NOAA website. You can take a [look of the data](data/1091402.txt).

**Note**: once again that temperatures in this dataset are given in degrees Fahrenheit.

Additional information about the data format can be found in the [hints for Exercise 6](https://geo-python.github.io/site/lessons/L6/exercise-6.html).

## Problems

**Note**: Problems 1-3 are all in one notebook.

- [Problems 1-3: Analysing Helsinki climate data](Exercise-6-problems-1-3.ipynb)
- [Problem 4: Analysing Sodankyla climate data (optional)](Exercise-6-problem-4.ipynb)
- [Exercise 6 summary](Exercise-6-summary.ipynb)