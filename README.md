# Global-News-Digest

Global News Digest


🚀 OverviewGlobal News Digest is an innovative web application that leverages the power of Google's Gemini AI to provide a personalized and dynamic news browsing experience. Users can generate news articles on demand based on specific topics or even their current mood, and get instant, concise summaries of any article.This project serves as a demonstration of integrating large language models (LLMs) into a client-side web application for real-time content generation and intelligent summarization.


✨ FeaturesAI-Powered News Generation: Generate fresh, short news articles on virtually any topic by simply typing a query. The articles include a title, a brief summary, and a category.Mood-Based News Selection: Choose from a selection of moods (e.g., "Excited," "Curious," "Relaxed") to automatically generate news topics that align with your emotional state, offering a unique way to discover content.Instant Article Summaries: Get the key takeaways from any generated article with a single click. A dedicated "Summarize Article



✨" button uses AI to provide a very concise, one-sentence summary in a pop-up modal.Aesthetic and Responsive Interface: Built with Tailwind CSS, the application features a clean, modern, and fully responsive design, ensuring a great user experience across various devices.Standalone Python Demo: Includes a separate Python script (generate_news_demo.py) demonstrating how to interact with the Gemini API for news generation in a backend environment.


🛠️ Technologies UsedFrontend:HTML5CSS3 (with Tailwind CSS via CDN for rapid styling)JavaScript (Vanilla JS for all logic and API interactions)AI Integration:Google Gemini API (gemini-2.0-flash model) for news generation and summarization.Development Server:VSCode Live Server (for local development)Python Demo:Python 3google-generativeai library



⚙️ How to Run LocallyFollow these steps to set up and run the Global News Digest application on your local machine.PrerequisitesWeb Browser: A modern web browser (Google Chrome, Mozilla Firefox, Microsoft Edge, etc.).Text Editor: Visual Studio Code (VSCode) is highly recommended for its Live Server extension.VSCode Live Server Extension: Install this extension in VSCode for easy local hosting.Python 3: Required only if you want to run the generate_news_demo.py script.Google Gemini API Key: You'll need an API key to interact with the Gemini model. Get one for free from Google AI Studio.Step-by-Step SetupClone or Download the Project:Create a new folder on your computer (e.g., global-news-app).Copy the index.html content into a file named index.html inside this folder.Copy the generate_news_demo.py content into a file named generate_news_demo.py inside the same folder.Configure API Keys:For index.html (Web Application):The GEMINI_API_KEY in index.html is set as an empty string (const GEMINI_API_KEY = "";). When running in a Canvas environment, this key is automatically injected. If you are running this outside the Canvas environment (e.g., directly via VSCode Live Server for local development), you would typically paste your Gemini API key directly here:const GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"; // Replace with your actual key


Security Warning: Exposing API keys directly in client-side code is NOT recommended for production applications. For a production environment, you should use a backend server to proxy your API calls, keeping your API key secure on the server-side. This setup is for demonstration and local testing purposes only.For generate_news_demo.py (Python Demo Script):It's best practice to load your API key from an environment variable.Set Environment Variable:Linux/macOS: export GEMINI_API_KEY='YOUR_API_KEY_HERE'Windows (Command Prompt): set GEMINI_API_KEY=YOUR_API_KEY_HEREWindows (PowerShell): $env:GEMINI_API_KEY='YOUR_API_KEY_HERE'(Replace YOUR_API_KEY_HERE with your actual Gemini API key).Alternatively (Less Secure for Production): You can directly paste your key into the generate_news_demo.py file:API_KEY = "YOUR_API_KEY_HERE" # Replace with your actual key





Install Python Dependencies (for Python Demo Script only):Open your terminal or command prompt.Navigate to your project folder: cd path/to/your/global-news-appInstall the Google Generative AI library:pip install google-generativeai
Running the Web Application (index.html)Open in VSCode: Open the global-news-app folder in Visual Studio Code (File > Open Folder...).Launch with Live Server: In the VSCode Explorer (left sidebar), right-click on index.html and select "Open with Live Server."Your default web browser will automatically open the application at a local address (e.g., http://127.0.0.1:5500/index.html).Running the Python Demo Script (generate_news_demo.py)Open Terminal: Open your terminal or command prompt.Navigate to Project Folder: cd path/to/your/global-news-appExecute the Script:python generate_news_demo.py
The script will prompt you to enter a news topic, generate articles, and print them to the console




.📂 Project Structureglobal-news-app/
├── index.html                # Main web application file (HTML, CSS, JavaScript)
└── generate_news_demo.py     # Standalone Python script for Gemini API demo




index.html: Contains the entire frontend of the application, including the HTML structure, inline CSS for custom styles (complementing Tailwind CSS), and all JavaScript logic for UI interaction, Gemini API calls, and dynamic content rendering.generate_news_demo.py: A simple Python script that demonstrates how to make calls to the Gemini API using the google-generativeai library. It's independent of the web application's runtime.



💡 Future Enhancements (Ideas)Real News Integration: Integrate with a real news API (e.g., NewsAPI, GNews API) to fetch actual headlines and then use Gemini for summarization or rephrasing.User Accounts & Preferences: Allow users to save their favorite moods, topics, or articles.More Advanced Summarization: Offer different summary lengths (e.g., bullet points, short paragraph, detailed).Content Filtering: Add options to filter news by category, date, or sentiment.Image Generation for Articles: Use an image generation API (like Imagen) to create unique images for each generated news article.Backend for API Key Security: Implement a simple Node.js/Python/Flask backend to proxy Gemini API calls, securing the API key.PWA (Progressive Web App) Features: Make the app installable and usable offline.




📄 LicenseThis project is open-source and available under the MIT License.





📧 ContactIf you have any questions, suggestions, or feedback, feel free to reach out!
