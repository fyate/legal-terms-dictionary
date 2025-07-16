# Legal Terms Dictionary

This repository contains a Python-based interactive legal terms dictionary. It allows users to search for legal terms in Italian and view their English equivalents, definitions, and the relevant legal field. The dictionary can perform both exact and partial matches for terms.

## Features

* **Interactive Search:** Command-line interface for easy term lookup.
* **Dual Language Support:** Provides Italian-to-English translations and definitions.
* **Flexible Search:** Supports exact matches and partial searches (using `*`).
* **Structured Data:** Uses a CSV file (`legal_dictionary.csv`) to store legal terms.
* **Error Handling:** Basic error handling for missing dictionary file.

## Files in this Repository

* `main.py`: The main Python script that implements the dictionary's functionality. It handles data loading, cleaning, preprocessing, and the interactive search interface.
* `legal_dictionary.csv`: The CSV file containing the legal terms, their English equivalents, definitions, and legal fields. This file serves as the database for the dictionary.

## How to Run the Application

To run this legal terms dictionary on your local machine, follow these steps:

1.  **Prerequisites:**
    * Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/).
    * `pandas` library. If you don't have it, install it using pip:
        ```bash
        pip install pandas
        ```

2.  **Run the Script:**
    Navigate to the `legal-terms-dictionary` directory in your terminal or command prompt and execute the Python script:
    ```bash
    python main.py
    ```

## How to Use the Dictionary

Once the application is running, you will see a welcome message and prompts to enter terms:

* **Exact Match:** Enter the full Italian term you are looking for (e.g., `Legge`).
* **Partial Match:** Enter the beginning of the term followed by an asterisk and a space (e.g., `Violenza *`).
* **Exit:** Type `exit` to close the application.


## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/fyate/legal-terms-dictionary/blob/main/LICENSE) file for details.
