📩 Spam Message Detector
A simple web app built using Streamlit, Scikit-learn, and Pandas that classifies messages as Spam or Not Spam using a Naive Bayes classifier trained on SMS data.

🚀 Features
Loads and cleans SMS spam dataset.
Trains a Multinomial Naive Bayes model using CountVectorizer.
Provides a web interface where users can input a message and instantly check whether it's spam.
Caches data loading and model training for performance optimization.

📁 Dataset
This app uses the SMS Spam Collection Dataset available in spam.csv. The dataset contains labeled SMS messages:
ham: not spam
spam: spam
The file must contain columns named v1 (label) and v2 (message).

🧠 Model
Vectorization: CountVectorizer converts text messages into numerical features.
Model: MultinomialNB is used for classification due to its effectiveness in text classification tasks.

🖼️ App Interface
Enter your message in the text area.
Click "Check Message".
Get an instant prediction: Spam or Not Spam.

📄 License
This project is open-source and available under the MIT License.