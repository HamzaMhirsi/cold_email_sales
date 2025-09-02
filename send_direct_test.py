#!/usr/bin/env python3
"""
Direct test email sender with better error handling
"""

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from email_template import get_email_template

# Load environment variables
load_dotenv()

def send_test_emails():
    """Send test emails with improved error handling"""
    
    # Get credentials from environment
    email_host = os.getenv('EMAIL_HOST', 'smtp.zoho.com')  # Default to correct Zoho SMTP
    email_port = int(os.getenv('EMAIL_PORT', 587))
    email_user = os.getenv('EMAIL_USER')
    email_password = os.getenv('EMAIL_PASSWORD')
    from_email = os.getenv('EMAIL_FROM_EMAIL', email_user)
    
    # Fix common SMTP hostname issues
    if email_host == 'smtp.zoho.ma':
        email_host = 'smtp.zoho.com'
        print(f"🔧 Fixed SMTP hostname: {email_host}")
    
    # Fix potential double slash issue in password
    if email_password and '//' in email_password:
        email_password = email_password.replace('//', '/')
        print(f"🔧 Fixed double slash in password")
    
    # Clean up any potential encoding issues
    email_password = email_password.strip() if email_password else None
    
    if not email_user or not email_password:
        print("❌ Email credentials not found in .env file")
        print("Please add EMAIL_USER and EMAIL_PASSWORD to your .env file")
        return False
    
    # Test recipients
    test_recipients = [
        ("hamza.mhirsi6@gmail.com", "Hamza"),
        ("issamhaidaoui@gmail.com", "Issam")
    ]
    
    booking_link = os.getenv('BOOKING_LINK', 'https://calendly.com/hamza-wraki')
    
    print(f"📧 SMTP Server: {email_host}:{email_port}")
    print(f"🔐 Auth user: {email_user}")
    print(f"📨 From email: {from_email}")
    print(f"🔗 Booking link: {booking_link}")
    print(f"🔑 Using password: {email_password[:4]}...{email_password[-4:] if len(email_password) > 8 else '***'}")
    print("🔄 Attempting to send test emails...\n")
    
    for email, name in test_recipients:
        try:
            # Generate email content
            # Get booking link from environment
            booking_link = os.getenv('BOOKING_LINK', 'https://calendly.com/hamza-wraki')
            
            subject, html_body, text_body = get_email_template(
                first_name=name,
                company_name="Test Company",
                job_title="Test Position",
                booking_link=booking_link
            )
            
            # Create message
            msg = MIMEMultipart('alternative')
            msg['From'] = f"Hamza Mhirsi <{from_email}>"
            msg['To'] = email
            msg['Subject'] = subject
            
            # Add both versions
            text_part = MIMEText(text_body, 'plain')
            html_part = MIMEText(html_body, 'html')
            msg.attach(text_part)
            msg.attach(html_part)
            
            # Send via SMTP
            with smtplib.SMTP(email_host, email_port) as server:
                server.starttls()
                print(f"🔐 Attempting login with: {email_user}")
                server.login(email_user, email_password)
                server.send_message(msg)
            
            print(f"✅ Successfully sent to {name} ({email})")
            
        except smtplib.SMTPAuthenticationError as e:
            print(f"❌ Authentication failed for {email}: {e}")
            print("   For Zoho Mail, you may need to:")
            print("   1. Generate an App Password in Zoho account settings")
            print("   2. Use the App Password instead of your regular password")
            print("   3. Enable IMAP/SMTP access in your Zoho settings")
        except smtplib.SMTPException as e:
            print(f"❌ SMTP error for {email}: {e}")
        except Exception as e:
            print(f"❌ Failed to send to {email}: {e}")
    
    return True

if __name__ == "__main__":
    send_test_emails()
