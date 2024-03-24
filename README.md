# AlphaChanger

AlphaChanger is a Flask-based web application that allows users to convert text between Latin and Cyrillic alphabets. This can be particularly useful for users who need to transliterate text between these two alphabets.

## Features

- Convert text from Latin to Cyrillic and vice versa.
- Simple RESTful API for easy integration into other applications.
- Cross-Origin Resource Sharing (CORS) enabled for handling requests from different domains.

## Usage

To use AlphaChanger, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your_username/AlphaChanger.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Access the application in your browser at `http://localhost:5000`.

5. Use the provided API endpoint (`/translate`) to convert text programmatically. Send a POST request with JSON data containing the `context` and `pattern` fields to convert text.

## API Endpoint

### POST /translate

Convert text between Latin and Cyrillic alphabets.

#### Request

```json
{
    "context": "Text to convert",
    "pattern": "latin" or "cyrillic"
}
```
context: The text to be converted.
pattern: The desired output pattern, either "latin" or "cyrillic".
Response
```json
{
    "result": "Converted text"
}
```

###Contributing
Contributions are welcome! If you'd like to contribute to AlphaChanger, please follow these steps:

1. Fork the repository.
1. Create a new branch (git checkout -b feature/new-feature).
1. Make your changes.
1. Commit your changes (git commit -am 'Add new feature').
1. Push to the branch (git push origin feature/new-feature).
1. Create a new pull request.

Acknowledgements
* [Flask](https://flask.palletsprojects.com/en/3.0.x/api/): The web framework used for building the application.
* [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/): A Flask extension for handling Cross-Origin Resource Sharing (CORS).
