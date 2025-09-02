#!/usr/bin/env python3
"""
Generate HTML preview of the email template
"""

from email_template import get_email_template
import webbrowser
import tempfile
import os

def create_html_preview():
    """Create an HTML file to preview the email design"""
    
    # Generate sample email
    subject, html_body, text_body = get_email_template(
        first_name="John",
        company_name="Sample Company",
        job_title="Supply Chain Manager", 
        booking_link="https://calendly.com/hamza-wraki"
    )
    
    # Create temporary HTML file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
        f.write(html_body)
        temp_file = f.name
    
    print(f"📧 Email Preview Generated!")
    print(f"Subject: {subject}")
    print(f"HTML file created at: {temp_file}")
    print(f"\nOpening preview in browser...")
    
    # Open in default browser
    webbrowser.open(f'file://{temp_file}')
    
    return temp_file

if __name__ == "__main__":
    create_html_preview()
