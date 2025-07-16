import pandas as pd

# --- Step 1: Data Loading and Initial Inspection ---
try:
    df = pd.read_csv('legal_dictionary.csv')
    print("Data loaded successfully.")
except FileNotFoundError:
    print("Error: 'legal_dictionary.csv' file not found. Please ensure the file is in the same directory.")
    exit() # Exit program if file is not found

# --- Step 2: Data Cleaning: Stripping Whitespace from Text Columns ---
string_columns = df.select_dtypes(include='object').columns
for col in string_columns:
    df[col] = df[col].str.strip()
print("Unnecessary whitespaces removed from text columns.")

# --- Step 3: Data Preprocessing: Expanding Split Terms ---
# This step expands terms separated by '/' into individual rows
expanded_rows = []
for index, row in df.iterrows():
    italian_terms_list = [term.strip() for term in row['Term_Italian'].split('/')]
    english_terms_list = [term.strip() for term in row['Term_English'].split('/')]

    # For simplicity and to retain original Definition/Legal_Field, we primarily expand based on Italian terms.
    # If English terms also contain slashes and need to be independently searchable with their original context,
    # a more complex expansion logic would be required (e.g., creating all combinations or
    # creating separate rows for each English term as well).
    # For this project's scope, expanding based on the Italian term and keeping the original English info is sufficient.
    for iterm in italian_terms_list:
        new_row = row.copy()
        new_row['Term_Italian'] = iterm
        expanded_rows.append(new_row)

df_expanded = pd.DataFrame(expanded_rows)
print(f"Original row count: {len(df)}")
print(f"Expanded row count after splitting terms: {len(df_expanded)}")
print("Terms separated by '/' have been expanded.")


# --- Step 4: Defining the Advanced Dictionary Search Function ---
def search_dictionary(query_term, dataframe, exact_match=True):
    """
    Searches the dictionary for the given term in Italian or English.
    Performs an exact match if exact_match=True, otherwise performs a partial match.
    Search is case-insensitive.
    """
    query_term = str(query_term).strip().lower()

    if exact_match:
        # Use '==' for exact matching
        results = dataframe[
            (dataframe['Term_Italian'].str.lower() == query_term) |
            (dataframe['Term_English'].str.lower() == query_term)
        ]
    else:
        # Use '.str.contains()' for partial matching
        results = dataframe[
            dataframe['Term_Italian'].str.lower().str.contains(query_term, na=False) |
            dataframe['Term_English'].str.lower().str.contains(query_term, na=False)
        ]

    if not results.empty:
        print(f"Results found for '{query_term}':")
        # Display unique results to avoid redundancy from expanded terms
        unique_results = results.drop_duplicates(subset=['Term_Italian', 'Term_English', 'Definition_English', 'Legal_Field'])

        for index, row in unique_results.iterrows():
            print("--------------------------------------------------")
            print(f"Italian Term: {row['Term_Italian']}")
            print(f"English Term: {row['Term_English']}")
            print(f"Definition (English): {row['Definition_English']}")
            print(f"Legal Field: {row['Legal_Field']}")
            print("--------------------------------------------------")
    else:
        print(f"The term '{query_term}' was not found in the dictionary. Please try another term.")

# --- Step 5: Interactive User Interface (Main Program Flow) ---
print("\nWelcome to the Legal Terms Dictionary! ")
print("Enter the term you want to search for, or type 'exit' to quit.")
print("For an exact match, enter the term directly.")
print("For a partial match, add ' * ' (space and asterisk) after the term.")

while True:
    user_input_term = input("\nEnter the term you want to search: ").strip()

    if user_input_term.lower() == 'exit':
        print("Closing the dictionary. Goodbye! ")
        break
    
    if user_input_term.endswith('*'):
        search_term = user_input_term[:-1].strip() # Remove the trailing '*' and any whitespace
        is_exact_match = False
        print(f"Performing partial search for '{search_term}'...")
    else:
        search_term = user_input_term
        is_exact_match = True
        print(f"Searching for an exact match for '{search_term}'...")

    search_dictionary(search_term, df_expanded, exact_match=is_exact_match)
