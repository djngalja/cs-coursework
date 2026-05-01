![n8n](https://img.shields.io/badge/n8n-EA4B71?style=for-the-badge&logo=n8n&logoColor=white) 
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![LeetCode](https://img.shields.io/badge/LeetCode-000000?style=for-the-badge&logo=LeetCode&logoColor=#d16c06)

# n8n Mini projects

A small collection of AI-powered Telegram bots built with n8n.

## Projects

### 1. [AI Tutor Bot](Telegram_AI_tutor_bot)
A bot that creates personalized learning plans, delivers content via Telegram and tracks user progress. Features multi-agent AI coordination and real-time search results.

### 2. Book Digest Bot
A bot that fetches new book releases from an RSS feed and sends summaries to subscribers of your Telegram channel every evening.

#### Setup
- Import `Book_digest_bot.json` into your n8n workflow
- Replace placeholders:
    - RSS feed URL
    - Telegram channel ID
    - Telegram API credential
    - OpenAI credential

### 3. LeetCode Daily Bot
This bot delivers AI-formatted content of a daily LeetCode challenge to your Telegram channel.

#### Setup
- Import `LeetCode_daily_Telegram_bot.json` into your n8n workflow
- Replace placeholders:
    - Telegram channel ID
    - Telegram API credential
    - OpenAI credential

#### Acknowledgments
This project utilizes the [LeetCode API / LeetCode Sorted](https://github.com/noworneverev/leetcode-api).