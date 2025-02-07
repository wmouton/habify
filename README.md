![Habify Banner](/images/habify-banner.png)

# Habify 🏆  
A lightweight Python script that fetches your pending tasks from **Habitica** and sends desktop notifications using `notify-send`. 🚀  

## Features  
- 📋 Fetches your **dailies** and **todos** from Habitica  
- 🔔 Sends notifications for pending tasks  
- 🔒 Uses `.env` for storing API credentials securely  

## 📌 Requirements  
- Python 3.6+  
- A Habitica account  
- `notify-send` (available on most Linux distributions)  
- `env` and `venv` for virtual environments  

---

## 🚀 Installation  

### 1. Clone the repository  
```sh
git clone https://github.com/wmouton/habify.git
cd habify
```

### 2. Set up a virtual environment  
Inside the project directory, run:  
```sh
python -m venv env
```
Activate the virtual environment:  
```sh
source env/bin/activate  # For Linux/macOS
env\Scripts\activate     # For Windows (PowerShell)
```

### 3. Install dependencies  
```sh
pip install -r requirements.txt
```

### 4. Set up Habitica API credentials  
Create a `.env` file in the project directory and add your Habitica credentials:  
```
HABITICA_USER_ID=your_user_id_here
HABITICA_API_TOKEN=your_api_token_here
```

You can find your Habitica **User ID** and **API Token** under [Settings → API](https://habitica.com/user/settings/api).  

## ▶️ Usage  
Run the script to check for pending tasks and receive notifications:  
```sh
python habify.py
```

## 🛠 Configuration  

### Customize Task Types  
By default, the script fetches **dailies** and **todos**. If you want to modify this behavior, update the `get_pending_tasks()` function in `habify.py`.  

## 🤝 Contributing  
Contributions are welcome! To contribute:  
1. Fork the repo  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Commit your changes (`git commit -m "Add new feature"`)  
4. Push to your branch (`git push origin feature-branch`)  
5. Open a pull request  

## 📜 License  
Habify is licensed under the **GPL-3.0 License**. See [LICENSE](LICENSE) for details.  

## ⭐ Support  
If you find Habify useful, consider giving it a ⭐ on GitHub! 🚀  

Let me know if you want any other additions! 🚀
