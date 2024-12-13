![Chatbot Screenshot](https://github.com/IT21313370/rule_based_chatbot/blob/master/static/Screenshot%202024-12-13%20105107.png)

```markdown
# Flask Chatbot

A simple chatbot application built using Flask, Python, and natural language processing (NLP). The chatbot provides predefined responses based on user inputs and can be extended with more sophisticated features as needed.

## Features

- **Basic NLP**: Uses predefined responses to common queries like greetings, farewells, and simple questions.
- **Flask Backend**: A lightweight Python web framework for building the API that handles the chatbot interaction.
- **HTML Frontend**: Simple web interface for users to chat with the bot.
- **Customizable**: Easily extendable to add more sophisticated conversation flows and integrate with other services.

## Tech Stack

- **Python**: The core language for building the chatbot.
- **Flask**: A lightweight web framework used to create the server-side application.
- **NLTK**: Natural Language Toolkit, used for basic text processing (can be expanded for more complex NLP tasks).
- **MongoDB/Firebase**: (optional) Use either MongoDB or Firebase for storing user interactions or other data.

## Installation

### Prerequisites

- Python 3.12.7
- pip (Python package manager)

### Steps to Run the Project

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/IT21313370/rule_based_chatbot.git
   cd chatbot-flask
   ```

2. Set up a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:

   ```bash
   python app.py
   ```

   The app will start on `http://127.0.0.1:5000/` by default.

5. Open your web browser and navigate to `http://127.0.0.1:5000/` to interact with the chatbot.

## How It Works

1. **User Input**: The user types a message in the input field on the frontend.
2. **Flask Backend**: The frontend sends a POST request with the user's message to the Flask server.
3. **Response Generation**: The backend processes the message, checks for predefined responses, and sends back an appropriate response.
4. **Display Response**: The response is displayed on the frontend in the chatbox.

## Predefined Responses

The chatbot currently has predefined responses for the following user inputs:

- **hi**: "Hello! How can I assist you today?"
- **hello**: "Hi there! How can I help?"
- **bye**: "Goodbye! Have a nice day!"
- **how are you**: "I'm just a bot, but I'm doing well. Thanks for asking!"
- **what is your name**: "I am your assistant bot."

These responses can be easily extended by modifying the `predefined_responses` dictionary in the `app.py` file.

## To Do

- Add more advanced NLP features for natural conversation.
- Integrate external APIs to provide more dynamic responses (e.g., weather, news, etc.).
- Store user interactions in MongoDB or Firebase for future enhancements.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to open an issue or reach out to [your contact info].
```

### Explanation of Sections:

- **Title**: Provides the project name at the top.
- **Features**: Highlights the main functionality of your chatbot.
- **Tech Stack**: Lists the technologies used in the project.
- **Installation**: Provides step-by-step instructions for setting up the project on a local machine.
- **How It Works**: Describes the general flow of how the chatbot operates, from user input to response.
- **Predefined Responses**: Describes some of the simple responses the chatbot can give.
- **To Do**: Gives an idea of how the project can be extended or improved in the future.
- **Contributing**: Explains how others can contribute to the project if they want to.
- **License**: States the licensing terms for the project (MIT License in this case).
- **Contact**: A place for users to reach out or ask questions.

### Steps to Upload README to GitHub:
1. **Create the README File**: Create a file named `README.md` in the root of your project directory and paste the above content.
2. **Push to GitHub**: If you haven't already, commit the README to GitHub:
   ```bash
   git add README.md
   git commit -m "Added README"
   git push
   ```
