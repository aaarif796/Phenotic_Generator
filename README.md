# Phonetic Generator

Phonetic Generator is a Python Django project designed to provide phonetic translations for text input in various languages, including Urdu, Hindi, Nepali, and Telugu. It aims to assist language learners, educators, and researchers in understanding and pronouncing words accurately across different linguistic contexts.

## Project Overview

### Objective
The main objective of the Phonetic Generator project is to create a versatile tool that can translate text into phonetic representations in multiple languages, facilitating pronunciation learning and linguistic research.

### Functionality
Using various language processing libraries and translation APIs, the project generates phonetic transcriptions for input text in languages such as Urdu, Hindi, Nepali, and Telugu, enabling users to understand and pronounce words accurately across different linguistic contexts.

## Project Highlights

- **Language Support:** The project supports multiple languages, enhancing its utility for learners and researchers interested in linguistics and phonetics.
  
- **Integration:** Leveraging Google Translate API and other language processing libraries like `eng_to_ipa`, the project seamlessly integrates with external resources to provide accurate and reliable phonetic translations.
  
- **Ease of Use:** With a user-friendly interface, the Phonetic Generator simplifies the process of obtaining phonetic representations for text, making it accessible to a wide range of users, including language learners, educators, and researchers.
  
- **Scalability:** Built using Django, the project is designed for scalability, allowing for future enhancements such as additional language support and improved phonetic transcription accuracy.
  
- **Community Contribution:** The project is open-source under the MIT License, inviting contributions from developers worldwide to enhance its functionality and language coverage, fostering collaborative development in the field of linguistic tools and resources.

### Installation

1. **Navigate to the project directory:**

    ```bash
    cd Phonetic_Generator
    ```

2. **Create a virtual environment (recommended):**

    ```bash
    python -m venv env
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```bash
        .\env\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source env/bin/activate
        ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Usage

Run the Django development server:

```bash
python manage.py runserver
