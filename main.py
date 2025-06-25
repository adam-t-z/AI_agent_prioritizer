import os
from openai import OpenAI
from dotenv import load_dotenv

# load the .env file
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# Step 1: Read tasks from file
def read_tasks(file_name="tasks.txt"):
    with open(file_name, "r") as file:
        tasks = [line.strip() for line in file if line.strip()]
    return tasks

tasks = read_tasks()

# Step 2: Build the prompt
task_list_text = "\n".join(f"- {task}" for task in tasks)

prompt = f"""
You are a smart task priotizer. I give you a list of tasks and you sort them in order of importance to four categories 'Urgent and Improtant', 'Urgent Not Important', 'Not Urgent But Important', 'Not Urgent Nor Important'.

These are the tasks:
{task_list_text}

Return them in this format:

Urgent and improtant:
    - task 1
    - task 2
    - ...
Urgent not important:
...
"""

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)


# Step 3: Send to DeepSeek

# “I tell the client to create a chat completion with a certain model, giving it a conversation history made of messages with roles and contents.”
# “C-C-C” = client.chat.completions.create
response = client.chat.completions.create(
    model="deepseek/deepseek-chat-v3-0324:free",
    messages=[
        {"role": "user", "content": prompt}
    ]
)


output_text = response.choices[0].message.content

# 💾 Step 4: Save the response to a file
with open("prioritized_tasks.txt", "w", encoding="utf-8") as file:
    file.write(output_text)

print("\n✅ Prioritized tasks saved to prioritized_tasks.txt")