# 🧠 Simple AI Task Prioritizer

This is a simple AI-powered agent that reads tasks from a `tasks.txt` file, prioritizes them using DeepSeek's API, and outputs the results to `prioritized_tasks.txt`.

---

## 📁 Project Structure

```
your-project-folder/
├── main.py                 # Main script that runs the agent
├── tasks.txt               # Input file containing a list of tasks
├── prioritized_tasks.txt   # Output file with prioritized tasks
├── .env.example            # Example environment file with API key placeholder
├── .gitignore              # Git ignore rules
├── requirements.txt        # Required Libs
```

---

## 🚀 How It Works

1. **Input**: Add your tasks to `tasks.txt`, one per line.
2. **Processing**: `main.py` uses DeepSeek's API to prioritize the tasks.
3. **Output**: A sorted list is written to `prioritized_tasks.txt`.

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. (Optional) Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, install required libraries manually (e.g., `python-dotenv`, `openai`, etc.).

### 4. Set up your API key

1. Copy the example environment file:

```bash
copy .env.example .env
```

2. Open `.env` and replace the placeholder:

```
OPENROUTER_API_KEY=your_actual_api_key_here
```

---

## 🧪 Run the Project

Make sure `tasks.txt` has tasks listed line by line, then run:

```bash
python main.py
```

The AI will generate a prioritized list in `prioritized_tasks.txt`.

---

## 🔐 Security

- `.env` and `venv/` are included in `.gitignore` to prevent committing secrets or virtual environments.
- Only share `.env.example`, which contains no sensitive information.

---

## 📃 License

This project is open-source and available under the MIT License.
