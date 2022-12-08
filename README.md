# LINE-ChatGPT-Python
This project is a chatbot that uses the LINE messaging API to interact with users. It listens for Post Requests from /callback and when a user sends a text message to the bot, it uses the revChatGPT library to generate a response, which is then sent to the user using the LINE messaging API.
It also uses the Flask library to create a web application and the ngrok library to create a tunnel so that the LINE messaging platform can communicate with the chatbot. When the code is run, it will start the Flask app and ngrok and output a URL that can be used to access the app. If the ngrok tunnel is restarted, the URL will be automatically updated.
To use this chatbot, you will need to get your own LINE channel access token and channel secret from the LINE Developers site and replace the placeholder values in the code. If you want to use the openai.Completion API, you will also need to provide your own openai API key and replace the placeholder value in the code. Once you've done that, you can run the code and use the output URL to access the chatbot.
## Requirements
- Python 3
- Flask
- LINE messaging API libraries
- revChatGPT library
- ngrok (optional)
## Usage
1. Get your own LINE channel access token and channel secret from the LINE Developers site and replace the placeholders in the script with them.
2. If you want to use the openai.Completion API, register for an account on the openai website and get an API key, then replace the placeholder in the script with it.
3. Install the required packages, including ngrok if you want to use it.
4. Run the script, which will start the Flask app and print a URL.
5. Use a web browser to access the printed URL and interact with the chatbot via the LINE messaging platform.
## Notes
- If you use ngrok, the printed URL will automatically be updated if the ngrok tunnel is restarted.
- If you want to modify the way the chatbot responds, you can modify the parameters of the revChatGPT package.
- If you want to use the openai.Completion API to generate responses, uncomment the openai.Completion.create() function in the script.