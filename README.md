# XC - Text Clipboard Manager
XC is a command-line interface (CUI) application written in Python that allows users to efficiently manage and reuse frequently used text snippets by storing them in a database. This can be particularly useful for storing email addresses, profile URLs, or any other text that users find themselves copying and pasting often.


## Features

* **Copy to Clipboard:** Easily copy text for quick pasting.
* **Save with Titles:** Organize text with personalized titles.
* **List Saved Items:** View a clear list of saved text items.
* **Delete Unnecessary Items:** Effortlessly remove unwanted entries.

## Usage
### Save Text
```bash
xc <title> <text>

# Example:
xc email myemail@gmail.com
xc gh-profile https://github.com/zahidquraishi41
```
### Copy to Clipboard
```bash
xc <title>

# Example:
xc gh-profile
```

### List Saved Items
```bash
xc --list
# or
xc -l
```
### Delete Saved Item
```bash
xc -d <title>
# or
xc --delete <title>
```

## Getting Started
```bash
# Clone the repository:
git clone https://github.com/zahidquraishi41/xc.git

# Install dependencies:
pip install -r requirements.txt

# Run the app:
python xc.py
```

### Add XC to your .bashrc for easy access:
```bash
# Replace ~/path/to/xc/main.py with the actual path to your main.py file.
echo 'alias xc="python ~/path/to/xc/main.py"' >> ~/.bashrc
source ~/.bashrc
```
## Contributing
Contributions are welcome! Feel free to open issues and submit pull requests.
