# LLM_projects
Initial setups for the project.
1. **Open Command Prompt**

Press Win + R, type `cmd`, and press Enter  

Run `python --version` to find out which python you're on.  
Ideally you'd be using a version of Python 3.11, so we're completely in sync.  
I believe Python 3.12 works also, but (as of Feb 2025) Python 3.13 does **not** yet work as several Data Science dependencies are not yet ready for Python 3.13.  
If you need to install Python or install another version, you can download it here:  
https://www.python.org/downloads/

2. Navigate to the "project root directory" by entering something like `cd C:\Users\YourUsername\Documents\Projects\llm_engineering` using the actual path to your llm_engineering project root directory. Do a `dir` and check you can see subdirectories for each week of the course.  

Then, create a new virtual environment with this command:  
`python -m venv llms`

3. Activate the virtual environment with  
`llms\Scripts\activate`
You should see (llms) in your command prompt, which is your sign that things are going well.

4. Run `python -m pip install --upgrade pip` followed by `pip install -r requirements.txt`  
This may take a few minutes to install.  
If you see an error like this:

> Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": [https://visualstudio.microsoft.com/visual-cpp-build-tools/](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

Then please follow the link and install Microsoft C++ Build Tools. A student also mentioned that [these instructions](https://github.com/bycloudai/InstallVSBuildToolsWindows) might be helpful for people on Windows 11.   

In the very unlikely event that this step doesn't go well, you should try the bullet-proof (but slower) version:  
`pip install --retries 5 --timeout 15 --no-cache-dir --force-reinstall -r requirements.txt`

6. **Start Jupyter Lab:**

From within the `llm_engineering` folder, type: `jupyter lab`  
...and Jupyter Lab should open up, ready for you to get started. Open the `week1` folder and double click on `day1.ipynb`. Success! Now close down jupyter lab and move on to Part 3.

If there are any problems, contact me!

### Part 3 - OpenAI key (OPTIONAL but recommended)

Particularly during weeks 1 and 2 of the course, you'll be writing code to call the APIs of Frontier models (models at the forefront of AI).

For week 1, you'll only need OpenAI, and you can add the others if you wish later on.

1. Create an OpenAI account if you don't have one by visiting:  
https://platform.openai.com/

2. OpenAI asks for a minimum credit to use the API. For me in the US, it's \$5. The API calls will spend against this \$5. On this course, we'll only use a small portion of this. I do recommend you make the investment as you'll be able to put it to excellent use. But if you'd prefer not to pay for the API, I give you an alternative in the course using Ollama.

You can add your credit balance to OpenAI at Settings > Billing:  
https://platform.openai.com/settings/organization/billing/overview

I recommend you disable the automatic recharge!

3. Create your API key

The webpage where you set up your OpenAI key is at https://platform.openai.com/api-keys - press the green 'Create new secret key' button and press 'Create secret key'. Keep a record of the API key somewhere private; you won't be able to retrieve it from the OpenAI screens in the future. It should start `sk-proj-`.

In week 2 we will also set up keys for Anthropic and Google, which you can do here when we get there.  
- Claude API at https://console.anthropic.com/ from Anthropic
- Gemini API at https://ai.google.dev/gemini-api from Google

Later in the course you'll be using the fabulous HuggingFace platform; an account is available for free at https://huggingface.co - you can create an API token from the Avatar menu >> Settings >> Access Tokens.

And in Week 6/7 you'll be using the terrific Weights & Biases at https://wandb.ai to watch over your training batches. Accounts are also free, and you can set up a token in a similar way.

### PART 4 - .env file

When you have these keys, please create a new file called `.env` in your project root directory. The filename needs to be exactly the four characters ".env" rather than "my-keys.env" or ".env.txt". Here's how to do it:

1. Open the Notepad (Windows + R to open the Run box, enter `notepad`)

2. In the Notepad, type this, replacing xxxx with your API key (starting `sk-proj-`).

```
OPENAI_API_KEY=xxxx
```

If you have other keys, you can add them too, or come back to this in future weeks:  
```
GOOGLE_API_KEY=xxxx
ANTHROPIC_API_KEY=xxxx
DEEPSEEK_API_KEY=xxxx
HF_TOKEN=xxxx
```

Double check there are no spaces before or after the `=` sign, and no spaces at the end of the key.

3. Go to File > Save As. In the "Save as type" dropdown, select All Files. In the "File name" field, type exactly **.env** as the filename. Choose to save this in the project root directory (the folder called `llm_engineering`) and click Save.

4. Navigate to the folder where you saved the file in Explorer and ensure it was saved as ".env" not ".env.txt" - if necessary rename it to ".env" -  you might need to ensure that "Show file extensions" is set to "On" so that you see the file extensions. Message or email me if that doesn't make sense!

This file won't appear in Jupyter Lab because jupyter hides files starting with a dot. This file is listed in the `.gitignore` file, so it won't get checked in and your keys stay safe.

### Part 5 - Showtime!!

- Open **Anaconda Prompt** (search for it in the Start menu) if you used Anaconda, otherwise open a Powershell if you used the alternative approach in Part 2B
  
- Navigate to the "project root directory" by entering something like `cd C:\Users\YourUsername\Documents\Projects\llm_engineering` using the actual path to your llm_engineering project root directory. Do a `dir` and check you can see subdirectories for each week of the course.

- Activate your environment with `conda activate llms` if you used Anaconda or `llms\Scripts\activate` if you used the alternative approach in Part 2B

- You should see (llms) in your prompt which is your sign that all is well. And now, type: `jupyter lab` and Jupyter Lab should open up, ready for you to get started. Open the `week1` folder and double click on `day1.ipynb`. 

And you're off to the races!

Note that any time you start jupyter lab in the future, you'll need to follow these Part 5 instructions to start it from within the `llm_engineering` directory with the `llms` environment activated.

For those new to Jupyter Lab / Jupyter Notebook, it's a delightful Data Science environment where you can simply hit shift+return in any cell to run it; start at the top and work your way down! There's a notebook in the week1 folder with a [Guide to Jupyter Lab](week1/Guide%20to%20Jupyter.ipynb), and an [Intermediate Python](week1/Intermediate%20Python.ipynb) tutorial, if that would be helpful. When we move to Google Colab in Week 3, you'll experience the same interface for Python runtimes in the cloud. 

If you have any problems, I've included a notebook in week1 called [troubleshooting.ipynb](week1/troubleshooting.ipynb) to figure it out.

Please do message me or email me at ed@edwarddonner.com if this doesn't work or if I can help with anything. I can't wait to hear how you get on.
