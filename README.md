# telegram-send-file

A simple command-line tool to send files and messages via Telegram, and receive messages from Telegram bots.

## Features

- **Send files** to Telegram users via command line
- **Send text messages** from stdin to Telegram users
- **Receive messages** from Telegram bots with optional wait mode
- Simple configuration using Python dictionaries
- Lightweight with minimal dependencies

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/raymondclowe/telegram-send-file.git
cd telegram-send-file
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your bot token and users (see Configuration section below)

## Configuration

### 1. Set up your Telegram Bot Token

Create a `secrets.py` file based on the example:

```bash
cp secrets-example.py secrets.py
```

Edit `secrets.py` and add your Telegram bot token:

```python
TG_TOKEN = "your:bot:api:token"
```

**How to get a bot token:**
1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the API token provided by BotFather

### 2. Set up User IDs

Create a `users.py` file based on the example:

```bash
cp users-example.py users.py
```

Edit `users.py` and add your users with their chat IDs:

```python
users = {'joe': '1234', 'bob': '4321', 'sue': 'abcd'}
```

**How to get a user's chat ID:**
1. Search for [@getidsbot](https://t.me/getidsbot) in Telegram
2. Start a conversation with the bot
3. The bot will reply with your chat ID
4. Add the username and chat ID to the `users` dictionary

## Usage

### Sending Files

Send a file to a specific user:

```bash
python tgsnd.py username filename.txt
```

Example:
```bash
python tgsnd.py joe report.pdf
python tgsnd.py bob document.docx
```

### Sending Text from stdin

Send text input directly to a user:

```bash
echo "Hello World" | python tgsnd.py username
```

Or pipe command output:
```bash
ls -la | python tgsnd.py joe
cat logfile.txt | python tgsnd.py bob
```

### Receiving Messages

Receive messages from your Telegram bot:

```bash
python tgrcv.py
```

**Wait mode** - Keep the connection open and wait for new messages (up to 60 seconds):

```bash
python tgrcv.py username --wait
# or
python tgrcv.py username -w
```

## Example Workflows

### Monitoring Script Output

```bash
# Send log files
python tgsnd.py admin /var/log/system.log

# Monitor script execution
./backup_script.sh 2>&1 | python tgsnd.py admin
```

### Automated Notifications

```bash
# Send completion notification
python your_script.py && echo "Script completed successfully!" | python tgsnd.py admin
```

### Receiving Commands

```bash
# Poll for messages
while true; do
    python tgrcv.py admin --wait
    sleep 5
done
```

## Error Handling

The tools provide informative error messages:

- **Unknown user**: The username is not in the `users.py` dictionary
- **File not found**: The specified file doesn't exist
- **File not sent**: Error sending the file (check bot token and permissions)
- **No message**: No messages available in the queue

## Security Notes

⚠️ **Important**: Never commit `secrets.py` or `users.py` to version control! These files are already included in `.gitignore`.

## License

This project is open source. Please check with the repository owner for specific license terms.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.
