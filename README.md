# Wraki Cold Email Sales Automation

Professional cold email automation system for Wraki sales outreach to supply chain and logistics professionals.

## Features

- **Automated Email Campaigns**: Send personalized cold emails to contacts from CSV files
- **Professional Templates**: Pre-built email templates optimized for supply chain professionals
- **Email Validation**: Automatically extracts and validates email addresses from multiple columns
- **Rate Limiting**: Built-in delays and daily limits to avoid spam detection
- **Comprehensive Logging**: Detailed logs of all email activities
- **Preview Mode**: Test your templates before sending
- **Batch Processing**: Send emails in batches with configurable start points

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment**:
   - Copy `.env.example` to `.env`
   - Fill in your email credentials and settings:
     ```
     EMAIL_HOST=smtp.gmail.com
     EMAIL_PORT=587
     EMAIL_USER=your_email@gmail.com
     EMAIL_PASSWORD=your_app_password
     EMAIL_FROM_NAME=Your Name
     EMAIL_FROM_EMAIL=your_email@gmail.com
     WRAKI_WEBSITE=https://wraki.ma
     BOOKING_LINK=https://calendly.com/your-booking-link
     DELAY_BETWEEN_EMAILS=5
     MAX_EMAILS_PER_DAY=50
     ```

3. **Gmail Setup** (if using Gmail):
   - Enable 2-factor authentication
   - Generate an App Password (not your regular password)
   - Use the App Password in the `EMAIL_PASSWORD` field

## Usage

### Preview Emails (Recommended First Step)
```bash
python cold_email_sender.py --csv "Contact/Find-people-Table-(2)-Default-view-export-1755811832779.csv" --preview
```

### Send Email Campaign
```bash
# Send first 50 emails (default)
python cold_email_sender.py --csv "Contact/Find-people-Table-(2)-Default-view-export-1755811832779.csv"

# Send specific number of emails
python cold_email_sender.py --csv "Contact/Find-people-Table-(2)-Default-view-export-1755811832779.csv" --max 25

# Start from a specific contact (useful for continuing campaigns)
python cold_email_sender.py --csv "Contact/Find-people-Table-(2)-Default-view-export-1755811832779.csv" --start 50 --max 25
```

### Command Line Options
- `--csv`: Path to your CSV file with contacts (required)
- `--preview`: Preview emails without sending them
- `--start`: Start index for contacts (default: 0)
- `--max`: Maximum number of emails to send
- `--preview-count`: Number of emails to preview (default: 5)

## Email Template

The system uses a professional template that:
- Personalizes with recipient's name, company, and job title
- Highlights Wraki's value proposition for supply chain optimization
- Includes a clear call-to-action for booking a call
- Maintains a professional, consultative tone

## CSV Format

The script expects a CSV with these columns:
- `First Name`, `Last Name`, `Full Name`
- `Company Name`, `Job Title`, `Location`
- `LinkedIn Profile`
- Email columns: `Find Work Email`, `Work Email`, etc. (multiple columns supported)

## Logging

All activities are logged to:
- Console output (real-time)
- `email_campaign.log` file (persistent)

## Best Practices

1. **Start Small**: Always preview emails first and test with a small batch
2. **Respect Limits**: Don't exceed 50-100 emails per day to avoid spam detection
3. **Monitor Results**: Check logs regularly for delivery issues
4. **Personalize**: The template automatically personalizes, but review for accuracy
5. **Follow Up**: Use the follow-up template for non-responders after 1-2 weeks

## Security Notes

- Never commit your `.env` file to version control
- Use App Passwords, not regular passwords for Gmail
- Keep your email credentials secure
- Monitor your email account for any suspicious activity

## Troubleshooting

- **Authentication Error**: Check your email credentials and App Password
- **Connection Error**: Verify SMTP settings and internet connection
- **Rate Limiting**: Increase delay between emails if getting blocked
- **Missing Emails**: Check the CSV format and email column names
This is a cold email reach repo that can be used for sales
