# AI Football Prediction Data Collector

A Python-based football prediction data collection, processing, and organization tool designed to work with prediction information published on an external football prediction website powered by a trained machine-learning model.

The project automates the organization of football match predictions, extracts and manages prediction-related information, filters records by date, handles duplicate entries, sorts prediction datasets, and saves structured results in CSV files for further analysis, historical tracking, and statistical research.

## Overview

Football prediction platforms may use trained machine-learning models, statistical methods, historical match data, or other analytical techniques to generate predictions for upcoming matches.

**AI Football Prediction Data Collector** focuses on collecting and managing the prediction information made available by such an external platform.

Rather than training its own machine-learning model, this project provides a Python data-processing workflow that can help make externally generated football predictions easier to store, review, compare, and analyze.

The project uses Python libraries such as Pandas, Requests, Beautiful Soup, and lxml to support data processing and web-content handling.

Its modular functions handle date calculations, directory creation, CSV storage, duplicate removal, sorting, date-based filtering, and the selection and organization of primary and supporting predictions.

## Key Features

* **AI-assisted prediction data collection:** Designed for collecting prediction information generated or published by an external prediction platform.
* **Python-based data processing:** Uses Pandas to organize prediction records into structured tabular datasets.
* **Date-based organization:** Creates date-specific directories for storing collected files.
* **CSV data storage:** Saves prediction records in CSV format for future reference and analysis.
* **Incremental data saving:** Appends new prediction records to an existing CSV file when possible.
* **Duplicate removal:** Removes duplicate rows to help maintain cleaner datasets.
* **Prediction sorting:** Sorts prediction datasets by a selected column in descending order.
* **Daily prediction filtering:** Filters records using a date-related value.
* **Primary and supporting tips:** Organizes selected prediction categories, tips, and their associated percentages.
* **Prediction record management:** Stores match dates, kickoff times, leagues, home teams, away teams, prediction categories, tips, and percentage values.
* **Flexible file organization:** Keeps generated CSV files grouped into date-specific directories.
* **Reusable utility functions:** Separates common operations into functions that can be reused throughout the project.

## How the AI Integration Works

The project is designed around the following workflow:

1. An external football prediction website generates or publishes predictions using its own trained model or analytical system.
2. The Python script works with the website's available prediction information.
3. Prediction records are organized into structured data.
4. Selected predictions and associated percentages are saved to CSV files.
5. The collected records can be reviewed, compared, and used for further statistical analysis.

### Important distinction

This repository does not, based on the current implementation, train or deploy the external website's AI model. Its AI connection comes from working with predictions supplied by an external platform.

The actual prediction method, model architecture, training dataset, and accuracy of the external platform are outside the scope of this script unless separately documented and independently verified.

## Project Structure

The project can be organized as follows:

```text
AI-Football-Prediction-Data-Collector/
│
├── CSV FILES/
│   └── Date-specific folders containing collected CSV datasets
│
├── main.py
│
├── requirements.txt
│
└── README.md
```

`main.py` represents the Python script containing the functions described in this repository. If your actual script has another filename, use that filename in the project structure and usage instructions.

The `CSV FILES` directory is created relative to the Python script when the data-saving functions execute.

## Technologies Used

| Technology     | Purpose                                                         |
| -------------- | --------------------------------------------------------------- |
| Python         | Main programming language                                       |
| Pandas         | Tabular data processing, filtering, sorting, and CSV operations |
| Requests       | HTTP requests to web resources                                  |
| Beautiful Soup | Parsing and extracting information from HTML                    |
| lxml           | HTML parsing and processing                                     |
| os             | File paths and directory management                             |
| datetime       | Date calculations and date-based organization                   |
| random         | Randomization utilities                                         |
| time           | Timing and delay utilities                                      |

Some imported libraries are not used directly in the functions currently shown. Their use may depend on other parts of the project.

## Installation

### 1. Install Python

Install a Python version compatible with the dependencies used by your project.

### 2. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Football-Prediction-Data-Collector.git
```

Replace `YOUR_USERNAME` with your GitHub username.

### 3. Navigate to the project directory

```bash
cd AI-Football-Prediction-Data-Collector
```

### 4. Install the dependencies

Create a `requirements.txt` file containing the packages required by your complete script. For the code shown in this repository, the main third-party dependencies are:

```text
beautifulsoup4
lxml
pandas
requests
```

Install them using:

```bash
python -m pip install -r requirements.txt
```

The `datetime`, `os`, `random`, and `time` modules are included with Python and do not need separate installation.

## Core Functions

### 1. `main_date(day)`

Calculates a date by adding a specified number of days to the current date.

This function is useful for organizing prediction data around a target date.

Example:

```python
from datetime import date, timedelta

def main_date(day):
    last_date = date.today() + timedelta(days=day)
    return last_date
```

A value of `0` represents today, a positive value represents a future date, and a negative value represents a date in the past.

### 2. `save_daily_csv()`

Creates a directory for storing prediction files associated with the target date.

The directory structure follows this general pattern:

```text
CSV FILES/
└── YYYY-MM-DD Files/
```

The function uses the script's directory as the starting point, making the output location independent of the terminal's current working directory.

If the directory already exists, the function prints a message and returns the intended path.

### 3. `drop_date(path)`

Reads a CSV file, filters its records using the `DATE` column, and saves the filtered records back to the same file.

The function is intended to retain records matching a date-related value derived from `main_date(date_value)`.

**Note:** The current implementation extracts only the day component of the target date and checks whether the `DATE` value starts with it. This may retain unintended records if dates use inconsistent formats or if the file contains multiple months. For reliable daily filtering, compare normalized full dates instead.

### 4. `saving_files(data, path)`

Converts incoming prediction data into a Pandas DataFrame and saves it to a CSV file.

If the file already exists, the function reads the existing data, appends the new records, and writes the combined dataset back to the file.

If reading the existing file fails, it attempts to create a new CSV file.

This function supports incremental collection, allowing new prediction records to be added without intentionally replacing the entire existing dataset.

### 5. `drop_duplicate(path)`

Reads a CSV file, removes duplicate rows, resets the DataFrame index, and saves the cleaned dataset.

This is useful when repeated collection runs may produce duplicate records.

The current implementation removes rows that match across all columns. It does not identify duplicates using only the match name, date, or another selected field.

### 6. `sorting_values(path, path_to, value)`

Reads a CSV file, sorts the records by the selected column in descending order, and saves the sorted dataset to a destination path.

This can be used to organize predictions by percentage, score, or another numeric or sortable field.

Example:

```python
sorting_values(
    path="predictions.csv",
    path_to="sorted_predictions.csv",
    value="TIP PER"
)
```

The example assumes the input CSV contains a `TIP PER` column.

### 7. `daily_pred(path, path_to, **kwargs)`

Processes a prediction dataset and prepares a selected primary tip and supporting tip for storage.

The output schema contains:

* `DATE`
* `TIME`
* `LEAGUE`
* `HOME TEAM`
* `AWAY TEAM`
* `TIP CATE`
* `TIP`
* `TIP PER`
* `SUP CATE`
* `SUP TIP`
* `SUP PER`

The function accepts keyword arguments representing prediction categories and the columns containing their associated percentages.

It identifies the highest value in the first supplied percentage column. When the maximum appears more than once, it applies an additional sorting step using the second supplied percentage column.

It then collects the match details, selected prediction categories, tip values, and associated percentages, and passes the resulting record to `saving_files()`.

**Implementation note:** The function currently assumes that the input CSV is non-empty, that the required columns exist, and that at least two keyword arguments are supplied in the expected order. These assumptions should be validated if the project is expanded or used with different datasets.

## Prediction Data Format

The `daily_pred()` function expects a source dataset containing match information and prediction-related columns.

The match information includes:

| Column      | Description                    |
| ----------- | ------------------------------ |
| `DATE`      | Date associated with the match |
| `TIME`      | Match time                     |
| `LEAGUE`    | Competition or league          |
| `HOME TEAM` | Home team                      |
| `AWAY TEAM` | Away team                      |

The prediction columns depend on the external platform and the way its data is prepared.

The output also contains a primary prediction and a supporting prediction, each with a category, tip, and associated percentage.

**Important:** A prediction percentage supplied by a website should not automatically be interpreted as a calibrated probability or a verified chance of winning. Its meaning depends on the source platform's methodology.

## Typical Workflow

A general workflow for using the project's functions is:

1. Obtain prediction data from the external source using the collection logic implemented in your complete project.
2. Prepare the source data as a CSV with the required match and prediction columns.
3. Create a date-specific output directory using `save_daily_csv()`.
4. Process and save selected prediction records using `daily_pred()` and `saving_files()`.
5. Remove duplicate rows using `drop_duplicate()`.
6. Sort records using `sorting_values()` when needed.
7. Apply date-based filtering when appropriate.
8. Review the resulting CSV files for missing data, inconsistent values, and duplicate matches.
9. Use the collected records for historical comparisons and additional statistical analysis.

The functions listed above provide data-management capabilities. The exact execution order depends on how they are connected in the complete application.

## Example Usage

The following example illustrates the date-directory and CSV-saving utilities. It is a minimal example, not a complete scraper for any particular website.

```python
from datetime import date, timedelta
import os
import pandas as pd

date_value = 0

def main_date(day):
    return date.today() + timedelta(days=day)

def save_daily_csv():
    outcome_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "CSV FILES"
    )

    todays_dir = f"{main_date(date_value)} Files"
    full_path = os.path.join(outcome_dir, todays_dir)

    os.makedirs(full_path, exist_ok=True)
    return full_path

def saving_files(data, path):
    df = pd.DataFrame(data)

    if os.path.exists(path):
        existing_df = pd.read_csv(path)
        df = pd.concat([existing_df, df], ignore_index=True)

    df.to_csv(path, index=False)

output_dir = save_daily_csv()
output_file = os.path.join(output_dir, "predictions.csv")

sample_data = [
    {
        "DATE": str(main_date(0)),
        "TIME": "15:00",
        "LEAGUE": "Example League",
        "HOME TEAM": "Home Team",
        "AWAY TEAM": "Away Team",
        "TIP CATE": "1",
        "TIP": "Example Tip",
        "TIP PER": 75.0,
        "SUP CATE": "X",
        "SUP TIP": "Supporting Tip",
        "SUP PER": 65.0
    }
]

saving_files(sample_data, output_file)
```

This example demonstrates local CSV storage only. The sample teams, league, tips, and percentages are placeholders and are not real predictions.

## Data Quality and Reliability

Collected prediction data becomes more useful when it is consistent, traceable, and easy to validate.

Recommended checks include:

* Verify that match dates use a consistent format.
* Confirm that required columns exist before processing.
* Handle empty CSV files and empty DataFrames.
* Convert percentage columns to numeric values before sorting.
* Check that appended records use the same column schema.
* Identify duplicates using a clearly defined match key when appropriate.
* Preserve the original source data when performing destructive filtering.
* Record the collection timestamp when historical tracking is important.
* Handle website timeouts, HTTP errors, and changes in page structure.
* Review whether the external website permits automated access and reuse of its data.

## Limitations

The current implementation has several assumptions worth understanding:

* The external website is responsible for generating or supplying the original predictions.
* The script does not independently establish the accuracy of the external model.
* The shown functions do not include a complete website-specific extraction routine.
* Date filtering relies on a day-based string match rather than a full-date comparison.
* Broad exception handling may conceal errors unrelated to an existing directory or missing file.
* The CSV append logic does not automatically prevent duplicates.
* The prediction selection function assumes specific column names and keyword ordering.
* The source prediction percentages may not be calibrated probabilities.
* Historical records alone do not prove that a prediction strategy is profitable.

These limitations can be addressed through stronger validation, logging, error handling, data provenance, and independent performance evaluation.

## Future Improvements

Potential improvements include:

* Add a robust website-specific extraction module.
* Implement full-date filtering using normalized date values.
* Introduce structured logging and informative exception handling.
* Validate required columns before processing.
* Add configurable prediction categories and percentage fields.
* Support duplicate detection using match date, league, home team, and away team.
* Record source URLs and collection timestamps where permitted.
* Add automated tests for date filtering, CSV appending, sorting, and prediction selection.
* Generate summary reports from historical prediction records.
* Compare predictions with actual match outcomes when reliable results are available.
* Evaluate prediction performance using suitable statistical metrics and clearly defined test periods.
* Develop dashboards for exploring collected predictions and historical results.

Any future evaluation of prediction accuracy should use actual match outcomes and a clearly defined methodology, rather than relying only on the percentages published by the source website.

## Responsible Use

This project is intended for programming, data collection, data management, and statistical research.

Football predictions are uncertain. The presence of an AI model on an external website does not guarantee accurate predictions, successful bets, or positive long-term returns.

Users should independently assess prediction quality, follow applicable laws and platform terms, and avoid treating historical performance as a guarantee of future outcomes.

## Contributing

Contributions that improve data validation, maintainability, error handling, testing, and documentation are welcome.

When contributing:

1. Keep functions focused on clearly defined tasks.
2. Validate input data before processing.
3. Handle expected errors explicitly.
4. Avoid committing private credentials or sensitive information.
5. Document changes that affect CSV schemas or prediction-selection behavior.


## Author

**Ezee Kits**

GitHub: [@Ezee-Kits](https://github.com/Ezee-Kits)

---

*AI Football Prediction Data Collector — collecting, organizing, and preparing externally generated football predictions for structured analysis.*
