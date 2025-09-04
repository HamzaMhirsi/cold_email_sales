#!/usr/bin/env python3
"""
Test script to send multi-language email samples
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
    """Send test emails in all 3 languages"""
    
    # Email configuration
    email_host = os.getenv('EMAIL_HOST', 'smtp.zoho.eu')
    email_port = int(os.getenv('EMAIL_PORT', 587))
    email_user = os.getenv('EMAIL_USER')
    email_password = os.getenv('EMAIL_PASSWORD')
    from_name = os.getenv('EMAIL_FROM_NAME', 'Hamza Mhirsi')
    from_email = os.getenv('EMAIL_FROM_EMAIL')
    booking_link = os.getenv('BOOKING_LINK', 'https://calendly.com/hamza-mhirsi6/1995')
    
    # Test recipient
    test_email = "hamza.mhirsi6@gmail.com"
    
    # Test data for each language
    test_cases = [
        {
            'language': 'english',
            'first_name': 'Hamza',
            'company_name': 'Test Company USA',
            'job_title': 'CEO',
            'subject_prefix': '[ENGLISH TEST]'
        },
        {
            'language': 'arabic', 
            'first_name': 'حمزة',
            'company_name': 'شركة الاختبار السعودية',
            'job_title': 'مدير عام',
            'subject_prefix': '[ARABIC TEST]'
        },
        {
            'language': 'french',
            'first_name': 'Hamza',
            'company_name': 'Entreprise Test France',
            'job_title': 'Directeur Général',
            'subject_prefix': '[FRENCH TEST]'
        }
    ]
    
    # Connect to SMTP
    try:
        server = smtplib.SMTP(email_host, email_port)
        server.starttls()
        server.login(email_user, email_password)
        print(f"✅ Connected to SMTP server: {email_host}")
        
        # Send test email for each language
        for test_case in test_cases:
            print(f"\n📧 Sending {test_case['language'].upper()} test email...")
            
            # Generate email template
            subject, html_body, text_body = get_email_template(
                first_name=test_case['first_name'],
                company_name=test_case['company_name'],
                job_title=test_case['job_title'],
                booking_link=booking_link,
                language=test_case['language']
            )
            
            # Add test prefix to subject
            subject = f"{test_case['subject_prefix']} {subject}"
            
            # Create email message
            msg = MIMEMultipart('alternative')
            msg['From'] = f"{from_name} <{from_email}>"
            msg['To'] = test_email
            msg['Subject'] = subject
            
            # Add both plain text and HTML versions
            text_part = MIMEText(text_body, 'plain', 'utf-8')
            html_part = MIMEText(html_body, 'html', 'utf-8')
            
            msg.attach(text_part)
            msg.attach(html_part)
            
            # Send email
            server.send_message(msg)
            print(f"✅ {test_case['language'].upper()} email sent successfully!")
            print(f"   Subject: {subject}")
        
        server.quit()
        print(f"\n🎉 All test emails sent to {test_email}")
        
    except Exception as e:
        print(f"❌ Error sending emails: {e}")
        return False
    
    return True

if __name__ == "__main__":
    send_test_emails()
