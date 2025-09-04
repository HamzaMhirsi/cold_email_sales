#!/usr/bin/env python3
"""
Campaign tracking system for managing email outreach progress
"""

import csv
import os
from datetime import datetime, timedelta
import logging

class CampaignTracker:
    def __init__(self, tracking_file="campaign_tracking.csv"):
        self.tracking_file = tracking_file
        self.fieldnames = [
            'contact_id', 'first_name', 'last_name', 'full_name', 'company_name', 
            'job_title', 'location', 'email', 'language', 'phone', 'linkedin_profile',
            'initial_email_sent', 'initial_email_date', 'initial_email_subject',
            'follow_up_1_sent', 'follow_up_1_date', 'follow_up_2_sent', 'follow_up_2_date',
            'follow_up_3_sent', 'follow_up_3_date', 'email_opened', 'email_clicked',
            'replied', 'reply_date', 'reply_content', 'meeting_scheduled', 'meeting_date',
            'lead_status', 'lead_score', 'notes', 'last_contact_date', 'next_follow_up_date',
            'campaign_batch', 'email_template_version', 'unsubscribed', 'bounce_status',
            'created_date', 'updated_date'
        ]
        self._ensure_tracking_file_exists()
    
    def _ensure_tracking_file_exists(self):
        """Create tracking file with headers if it doesn't exist"""
        if not os.path.exists(self.tracking_file):
            with open(self.tracking_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()
    
    def generate_contact_id(self, email):
        """Generate unique contact ID from email"""
        return f"WRK_{email.split('@')[0]}_{hash(email) % 10000:04d}"
    
    def log_initial_email(self, contact, subject, language, campaign_batch="BATCH_001"):
        """Log initial email sent to contact"""
        contact_id = self.generate_contact_id(contact['email'])
        now = datetime.now().isoformat()
        
        # Check if contact already exists
        existing_contact = self.get_contact_by_email(contact['email'])
        
        if existing_contact:
            # Update existing contact
            self.update_contact(contact['email'], {
                'initial_email_sent': True,
                'initial_email_date': now,
                'initial_email_subject': subject,
                'last_contact_date': now,
                'next_follow_up_date': (datetime.now() + timedelta(days=3)).isoformat(),
                'updated_date': now
            })
            logging.info(f"Updated existing contact: {contact['email']}")
        else:
            # Create new contact record
            new_record = {
                'contact_id': contact_id,
                'first_name': contact.get('first_name', ''),
                'last_name': contact.get('last_name', ''),
                'full_name': contact.get('full_name', ''),
                'company_name': contact.get('company_name', ''),
                'job_title': contact.get('job_title', ''),
                'location': contact.get('location', ''),
                'email': contact['email'],
                'language': language,
                'phone': contact.get('phone', ''),
                'linkedin_profile': contact.get('linkedin', ''),
                'initial_email_sent': True,
                'initial_email_date': now,
                'initial_email_subject': subject,
                'follow_up_1_sent': False,
                'follow_up_2_sent': False,
                'follow_up_3_sent': False,
                'email_opened': False,
                'email_clicked': False,
                'replied': False,
                'meeting_scheduled': False,
                'lead_status': 'COLD',
                'lead_score': 0,
                'notes': '',
                'last_contact_date': now,
                'next_follow_up_date': (datetime.now() + timedelta(days=3)).isoformat(),
                'campaign_batch': campaign_batch,
                'email_template_version': '1.0',
                'unsubscribed': False,
                'bounce_status': '',
                'created_date': now,
                'updated_date': now
            }
            
            # Append to CSV
            with open(self.tracking_file, 'a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writerow(new_record)
            
            logging.info(f"Added new contact to tracking: {contact['email']}")
    
    def get_contact_by_email(self, email):
        """Get contact record by email"""
        try:
            with open(self.tracking_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['email'] == email:
                        return row
        except FileNotFoundError:
            return None
        return None
    
    def update_contact(self, email, updates):
        """Update contact record"""
        contacts = []
        updated = False
        
        # Read all contacts
        with open(self.tracking_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['email'] == email:
                    row.update(updates)
                    row['updated_date'] = datetime.now().isoformat()
                    updated = True
                contacts.append(row)
        
        if updated:
            # Write back all contacts
            with open(self.tracking_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()
                writer.writerows(contacts)
    
    def get_contacts_for_follow_up(self, follow_up_number=1):
        """Get contacts ready for follow-up"""
        contacts_for_follow_up = []
        now = datetime.now()
        
        try:
            with open(self.tracking_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Check if contact is ready for follow-up
                    if (row['initial_email_sent'] == 'True' and 
                        row[f'follow_up_{follow_up_number}_sent'] == 'False' and
                        row['replied'] == 'False' and
                        row['unsubscribed'] == 'False'):
                        
                        # Check if follow-up date has passed
                        if row['next_follow_up_date']:
                            next_follow_up = datetime.fromisoformat(row['next_follow_up_date'])
                            if now >= next_follow_up:
                                contacts_for_follow_up.append(row)
        except FileNotFoundError:
            pass
        
        return contacts_for_follow_up
    
    def log_follow_up(self, email, follow_up_number, subject):
        """Log follow-up email sent"""
        now = datetime.now().isoformat()
        next_follow_up_days = {1: 5, 2: 7, 3: 14}  # Days until next follow-up
        
        updates = {
            f'follow_up_{follow_up_number}_sent': True,
            f'follow_up_{follow_up_number}_date': now,
            'last_contact_date': now,
            'lead_status': 'WARM' if follow_up_number >= 2 else 'COLD'
        }
        
        # Set next follow-up date if not the last follow-up
        if follow_up_number < 3:
            next_date = datetime.now() + timedelta(days=next_follow_up_days[follow_up_number])
            updates['next_follow_up_date'] = next_date.isoformat()
        
        self.update_contact(email, updates)
    
    def log_reply(self, email, reply_content=""):
        """Log when contact replies"""
        updates = {
            'replied': True,
            'reply_date': datetime.now().isoformat(),
            'reply_content': reply_content,
            'lead_status': 'HOT',
            'lead_score': 80
        }
        self.update_contact(email, updates)
    
    def log_meeting_scheduled(self, email, meeting_date):
        """Log when meeting is scheduled"""
        updates = {
            'meeting_scheduled': True,
            'meeting_date': meeting_date,
            'lead_status': 'QUALIFIED',
            'lead_score': 100
        }
        self.update_contact(email, updates)
    
    def get_campaign_stats(self):
        """Get campaign statistics"""
        stats = {
            'total_contacts': 0,
            'emails_sent': 0,
            'follow_ups_sent': 0,
            'replies': 0,
            'meetings_scheduled': 0,
            'unsubscribed': 0,
            'by_language': {'english': 0, 'arabic': 0, 'french': 0},
            'by_status': {'COLD': 0, 'WARM': 0, 'HOT': 0, 'QUALIFIED': 0}
        }
        
        try:
            with open(self.tracking_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    stats['total_contacts'] += 1
                    
                    if row['initial_email_sent'] == 'True':
                        stats['emails_sent'] += 1
                    
                    follow_ups = sum(1 for i in [1,2,3] if row[f'follow_up_{i}_sent'] == 'True')
                    stats['follow_ups_sent'] += follow_ups
                    
                    if row['replied'] == 'True':
                        stats['replies'] += 1
                    
                    if row['meeting_scheduled'] == 'True':
                        stats['meetings_scheduled'] += 1
                    
                    if row['unsubscribed'] == 'True':
                        stats['unsubscribed'] += 1
                    
                    # Language stats
                    lang = row.get('language', 'english')
                    if lang in stats['by_language']:
                        stats['by_language'][lang] += 1
                    
                    # Status stats
                    status = row.get('lead_status', 'COLD')
                    if status in stats['by_status']:
                        stats['by_status'][status] += 1
        
        except FileNotFoundError:
            pass
        
        return stats
    
    def print_campaign_stats(self):
        """Print formatted campaign statistics"""
        stats = self.get_campaign_stats()
        
        print("\n" + "="*60)
        print("📊 WRAKI COLD EMAIL CAMPAIGN STATISTICS")
        print("="*60)
        
        print(f"📧 Total Contacts: {stats['total_contacts']}")
        print(f"✉️  Initial Emails Sent: {stats['emails_sent']}")
        print(f"🔄 Follow-ups Sent: {stats['follow_ups_sent']}")
        print(f"💬 Replies Received: {stats['replies']}")
        print(f"📅 Meetings Scheduled: {stats['meetings_scheduled']}")
        print(f"🚫 Unsubscribed: {stats['unsubscribed']}")
        
        print(f"\n🌍 By Language:")
        for lang, count in stats['by_language'].items():
            print(f"   {lang.title()}: {count}")
        
        print(f"\n🎯 By Lead Status:")
        for status, count in stats['by_status'].items():
            print(f"   {status}: {count}")
        
        # Calculate rates
        if stats['emails_sent'] > 0:
            reply_rate = (stats['replies'] / stats['emails_sent']) * 100
            meeting_rate = (stats['meetings_scheduled'] / stats['emails_sent']) * 100
            print(f"\n📈 Performance Metrics:")
            print(f"   Reply Rate: {reply_rate:.1f}%")
            print(f"   Meeting Rate: {meeting_rate:.1f}%")
        
        print("="*60 + "\n")
