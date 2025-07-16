# Legal Terminology Dictionary

## Project Overview

This project presents an interactive Python-based dictionary designed to provide quick and accurate access to legal terminology. Developed as part of the "Coding for Lawyers" course at the University of Bologna (Spring Semester 2024/25), its primary goal is to address the inherent complexity and multi-layered nature of legal language. The dictionary aims to minimize ambiguities and enhance the productivity of legal professionals, including lawyers, law students, translators, and researchers, by streamlining the process of understanding and using precise legal terms.

## Features

* **Bilingual Support:** Provides definitions for Italian legal terms in English.
* **Flexible Search Options:** Supports both exact and partial (wildcard) matching for search queries.
* **User-Friendly Command-Line Interface:** Easy to navigate for users with varying technical proficiencies.
* **Comprehensive Data:** Based on a `legal_dictionary.csv` file, containing a wide range of legal terms, definitions, and associated legal fields.

## Project Structure

The repository contains the following key files:

* `odev.py`: The main Python script that implements the dictionary's functionality, including data loading, cleaning, preprocessing, and the interactive search interface.
* `legal_dictionary.csv`: The dataset containing the legal terms, their English equivalents, definitions, and legal fields.
* `README.md`: This document, providing an overview and instructions for the project.

## How to Use (Installation & Usage)

To run the Legal Terminology Dictionary on your local machine, follow these steps:

1.  **Clone the Repository (Optional, if you haven't already):**
    If you haven't cloned it yet, you can download the project files by clicking "Code" and then "Download ZIP" on the GitHub page, or by using Git:
    ```bash
    git clone [https://github.com/fyate/legal-terms-dictionary.git](https://github.com/fyate/legal-terms-dictionary.git)
    cd legal-terms-dictionary
    ```
2.  **Ensure Python is Installed:** Make sure you have Python (version 3.x recommended) installed on your system. You can download it from [python.org]
3.  **Install Dependencies:** The project requires the `pandas` library. Install it using pip:
    ```bash
    pip install pandas
    ```
4.  **Run the Dictionary:** Execute the main Python script from your terminal:
    ```bash
    python odev.py
    ```
    The program will then prompt you to enter terms to search for. Type `exit` to quit.

## Contributing

Currently, this project is maintained by fyate. For any inquiries or suggestions, please open an issue in the repository.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). This means anyone can use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, with attribution.
