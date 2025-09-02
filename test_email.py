#!/usr/bin/env python3
"""
Test script to send emails to specific test addresses
"""

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from email_template import get_email_template

# Load environment variables
load_dotenv()

def send_test_email(to_email, first_name="Test User"):
    """Send a test email to specified address"""
    
    # Email configuration
    email_host = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
    email_port = int(os.getenv('EMAIL_PORT', 587))
    email_user = os.getenv('EMAIL_USER')
    email_password = os.getenv('EMAIL_PASSWORD')
    from_name = os.getenv('EMAIL_FROM_NAME', 'Hamza Mhirsi')
    from_email = os.getenv('EMAIL_FROM_EMAIL')
    booking_link = os.getenv('BOOKING_LINK', 'https://calendly.com/your-booking-link')
    
    # Generate email content
    subject, html_body, text_body = get_email_template(
        first_name=first_name,
        company_name="Test Company",
        job_title="Test Position",
        booking_link=booking_link
    )
    
    try:
        # Connect to SMTP server
        server = smtplib.SMTP(email_host, email_port)
        server.starttls()
        server.login(email_user, email_password)
        
        # Create message
        msg = MIMEMultipart('alternative')
        msg['From'] = f"{from_name} <{from_email}>"
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Add both plain text and HTML versions
        text_part = MIMEText(text_body, 'plain')
        html_part = MIMEText(html_body, 'html')
        
        msg.attach(text_part)
        msg.attach(html_part)
        
        # Send email
        server.send_message(msg)
        server.quit()
        
        print(f"✅ Test email sent successfully to {to_email}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to send test email to {to_email}: {e}")
        return False

def main():
    """Send test emails to specified addresses"""
    test_emails = [
        ("hamza.mhirsi6@gmail.com", "Hamza"),
        ("issamhaidaoui@gmail.com", "Issam")
    ]
    
    print("🧪 Sending test emails with new HTML template...\n")
    
    for email, name in test_emails:
        send_test_email(email, name)
        print()
    
    print("Test completed!")

if __name__ == "__main__":
    main()
