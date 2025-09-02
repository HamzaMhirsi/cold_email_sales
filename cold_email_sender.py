#!/usr/bin/env python3
"""
Cold Email Automation Script for Wraki Sales Outreach
"""

import csv
import smtplib
import time
import logging
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from dotenv import load_dotenv
from email_template import get_email_template, get_follow_up_template

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('email_campaign.log'),
        logging.StreamHandler()
    ]
)

class ColdEmailSender:
    def __init__(self):
        self.email_host = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
        self.email_port = int(os.getenv('EMAIL_PORT', 587))
        self.email_user = os.getenv('EMAIL_USER')
        self.email_password = os.getenv('EMAIL_PASSWORD')
        self.from_name = os.getenv('EMAIL_FROM_NAME', 'Hamza Mhirsi')
        self.from_email = os.getenv('EMAIL_FROM_EMAIL')
        self.wraki_website = os.getenv('WRAKI_WEBSITE', 'https://wraki.ma')
        self.booking_link = os.getenv('BOOKING_LINK', 'https://calendly.com/your-booking-link')
        self.delay_between_emails = int(os.getenv('DELAY_BETWEEN_EMAILS', 5))
        self.max_emails_per_day = int(os.getenv('MAX_EMAILS_PER_DAY', 50))
        
        # Validate required environment variables
        if not all([self.email_user, self.email_password, self.from_email]):
            raise ValueError("Missing required email credentials in environment variables")
    
    def connect_to_smtp(self):
        """Establish SMTP connection"""
        try:
            server = smtplib.SMTP(self.email_host, self.email_port)
            server.starttls()
            server.login(self.email_user, self.email_password)
            logging.info("Successfully connected to SMTP server")
            return server
        except Exception as e:
            logging.error(f"Failed to connect to SMTP server: {e}")
            raise
    
    def extract_email_from_row(self, row):
        """Extract the first valid email from the row"""
        email_columns = [
            'Find Work Email', 'Find Work Email (2)', 'Find Work Email (3)', 
            'Find Work Email (4)', 'Find Work Email (5)', 'Find Email',
            'Find Work Email (6)', 'Find work email', 'Find Work Email (7)', 'Work Email'
        ]
        
        for col in email_columns:
            if col in row and row[col]:
                email = row[col].strip()
                # Check if it's a valid email (contains @ and doesn't contain error messages)
                if '@' in email and not any(error in email.lower() for error in ['no email', 'not found', '❌']):
                    # Clean up email if it has checkmark
                    if '✅' in email:
                        email = email.replace('✅', '').strip()
                    return email
        return None
    
    def send_email(self, server, to_email, subject, html_body, text_body, contact_name, test_mode=False):
        """Send individual email or simulate in test mode"""
        try:
            if test_mode:
                logging.info(f"[TEST MODE] Would send email to {contact_name} ({to_email})")
                logging.info(f"[TEST MODE] Subject: {subject}")
                return True
            
            msg = MIMEMultipart('alternative')
            msg['From'] = f"{self.from_name} <{self.from_email}>"
            msg['To'] = to_email
            msg['Subject'] = subject
            
            # Add both plain text and HTML versions
            text_part = MIMEText(text_body, 'plain')
            html_part = MIMEText(html_body, 'html')
            
            msg.attach(text_part)
            msg.attach(html_part)
            
            server.send_message(msg)
            logging.info(f"Email sent successfully to {contact_name} ({to_email})")
            return True
            
        except Exception as e:
            logging.error(f"Failed to send email to {contact_name} ({to_email}): {e}")
            return False
    
    def load_contacts(self, csv_file_path):
        """Load contacts from CSV file"""
        contacts = []
        try:
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    email = self.extract_email_from_row(row)
                    if email:
                        contact = {
                            'first_name': row.get('First Name', '').strip(),
                            'last_name': row.get('Last Name', '').strip(),
                            'full_name': row.get('Full Name', '').strip(),
                            'company_name': row.get('Company Name', '').strip(),
                            'job_title': row.get('Job Title', '').strip(),
                            'location': row.get('Location', '').strip(),
                            'linkedin': row.get('LinkedIn Profile', '').strip(),
                            'email': email
                        }
                        contacts.append(contact)
            
            logging.info(f"Loaded {len(contacts)} contacts with valid emails")
            return contacts
            
        except Exception as e:
            logging.error(f"Failed to load contacts from {csv_file_path}: {e}")
            raise
    
    def send_campaign(self, csv_file_path, start_index=0, max_emails=None, test_mode=False):
        """Send cold email campaign"""
        if max_emails is None:
            max_emails = self.max_emails_per_day
        
        contacts = self.load_contacts(csv_file_path)
        
        if start_index >= len(contacts):
            logging.warning(f"Start index {start_index} is beyond the number of contacts ({len(contacts)})")
            return
        
        # Limit contacts to send to
        end_index = min(start_index + max_emails, len(contacts))
        contacts_to_email = contacts[start_index:end_index]
        
        mode_text = "[TEST MODE] " if test_mode else ""
        logging.info(f"{mode_text}Starting email campaign: sending to {len(contacts_to_email)} contacts (index {start_index} to {end_index-1})")
        
        server = None
        if not test_mode:
            server = self.connect_to_smtp()
        
        sent_count = 0
        failed_count = 0
        
        try:
            for i, contact in enumerate(contacts_to_email, start=start_index):
                first_name = contact['first_name'] or contact['full_name'].split()[0] if contact['full_name'] else 'there'
                
                subject, html_body, text_body = get_email_template(
                    first_name=first_name,
                    company_name=contact['company_name'],
                    job_title=contact['job_title'],
                    booking_link=self.booking_link
                )
                
                success = self.send_email(
                    server=server,
                    to_email=contact['email'],
                    subject=subject,
                    html_body=html_body,
                    text_body=text_body,
                    contact_name=contact['full_name'] or f"{contact['first_name']} {contact['last_name']}",
                    test_mode=test_mode
                )
                
                if success:
                    sent_count += 1
                else:
                    failed_count += 1
                
                # Add delay between emails to avoid being flagged as spam
                if i < end_index - 1:  # Don't delay after the last email
                    delay_time = 1 if test_mode else self.delay_between_emails
                    logging.info(f"Waiting {delay_time} seconds before next email...")
                    time.sleep(delay_time)
        
        finally:
            if server:
                server.quit()
            logging.info(f"{mode_text}Campaign completed. Sent: {sent_count}, Failed: {failed_count}")
            logging.info(f"Next batch should start from index: {end_index}")
    
    def preview_emails(self, csv_file_path, count=5):
        """Preview email templates for the first few contacts"""
        contacts = self.load_contacts(csv_file_path)
        
        print(f"\n=== EMAIL PREVIEW (First {min(count, len(contacts))} contacts) ===\n")
        
        for i, contact in enumerate(contacts[:count]):
            first_name = contact['first_name'] or contact['full_name'].split()[0] if contact['full_name'] else 'there'
            
            subject, html_body, text_body = get_email_template(
                first_name=first_name,
                company_name=contact['company_name'],
                job_title=contact['job_title'],
                booking_link=self.booking_link
            )
            
            print(f"--- Contact {i+1}: {contact['full_name']} ({contact['email']}) ---")
            print(f"Subject: {subject}")
            print(f"Text Body:\n{text_body}")
            print("\n" + "="*80 + "\n")

def main():
    """Main function to run the email campaign"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Cold Email Campaign for Wraki')
    parser.add_argument('--csv', required=True, help='Path to the CSV file with contacts')
    parser.add_argument('--preview', action='store_true', help='Preview emails without sending')
    parser.add_argument('--test', action='store_true', help='Test mode - simulate sending without actually sending emails')
    parser.add_argument('--start', type=int, default=0, help='Start index for contacts (default: 0)')
    parser.add_argument('--max', type=int, help='Maximum number of emails to send (default: from env)')
    parser.add_argument('--preview-count', type=int, default=5, help='Number of emails to preview (default: 5)')
    
    args = parser.parse_args()
    
    try:
        sender = ColdEmailSender()
        
        if args.preview:
            sender.preview_emails(args.csv, args.preview_count)
        elif args.test:
            sender.send_campaign(args.csv, args.start, args.max, test_mode=True)
        else:
            sender.send_campaign(args.csv, args.start, args.max)
            
    except Exception as e:
        logging.error(f"Campaign failed: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
