# SlackBot
## Dependencies
- Requires `slack_sdk` and `slack_bolt` packages.
- Requires `venv`.
- Requires `python-dotenv` package for loading env variables from `.env` file.
- Requires `Slack_APP_TOKEN` and `SLACK_BOT_TOKEN` in the `.env` file.

## Features
- Captures `@mentions` in the slack chat.
- Sends reply in the channel mentioned.
- Sends alerts in the `alerts` channel.
