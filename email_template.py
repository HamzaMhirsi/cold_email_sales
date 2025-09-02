"""
Professional email templates for Wraki cold outreach
"""

def get_email_template(first_name, company_name, job_title, booking_link):
    """
    Generate a personalized cold email template for Wraki outreach
    """
    subject = f"Quick question about {company_name}'s document automation"
    
    # HTML email template with lighter blue design and document-like styling
    html_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Wraki - Document Automation</title>
    </head>
    <body style="margin: 0; padding: 0; font-family: 'Courier New', monospace; background-color: #e8eaf0;">
        <div style="max-width: 600px; margin: 20px auto; background-color: #f9f9f9; border-radius: 8px; overflow: hidden; box-shadow: 0 6px 25px rgba(0,0,0,0.15);">
            
            <!-- Header -->
            <div style="background: linear-gradient(135deg, #37474f 0%, #546e7a 100%); padding: 20px 40px; text-align: center; border-bottom: 4px solid #455a64;">
                <h1 style="color: #ffffff; margin: 0; font-size: 24px; font-weight: 700; letter-spacing: 2px;">WRAKI</h1>
                <p style="color: #b0bec5; margin: 6px 0 0 0; font-size: 12px; font-weight: 600; text-transform: uppercase;">Document Automation Platform</p>
            </div>
            
            <!-- Main Content -->
            <div style="padding: 30px 40px;">
                <!-- Fax-like document container -->
                <div style="background: #ffffff; border: 3px solid #37474f; border-radius: 4px; padding: 30px; margin: 15px 0; position: relative; box-shadow: inset 0 0 20px rgba(55, 71, 79, 0.1), 0 4px 15px rgba(0,0,0,0.1);">
                    <!-- Fax header lines -->
                    <div style="position: absolute; top: 8px; left: 15px; right: 15px; height: 2px; background: repeating-linear-gradient(90deg, #37474f 0px, #37474f 10px, transparent 10px, transparent 15px); opacity: 0.6;"></div>
                    <div style="position: absolute; top: 12px; left: 15px; right: 15px; height: 1px; background: repeating-linear-gradient(90deg, #37474f 0px, #37474f 8px, transparent 8px, transparent 12px); opacity: 0.4;"></div>
                    
                    <!-- Fax transmission effect -->
                    <div style="position: absolute; top: 0; left: 0; right: 0; height: 100%; background: repeating-linear-gradient(0deg, transparent 0px, transparent 18px, rgba(55, 71, 79, 0.03) 18px, rgba(55, 71, 79, 0.03) 20px); pointer-events: none;"></div>
                    
                    <p style="color: #1a1a1a; font-size: 15px; line-height: 1.6; margin: 0 0 16px 0; font-weight: 600; font-family: 'Courier New', monospace;">
                        Dear <strong style="color: #37474f; background: #f5f5f5; padding: 1px 4px; border-radius: 2px;">{first_name}</strong>, my name is Hamza and I'm the CEO of Wraki.
                    </p>
                    
                    <p style="color: #2c2c2c; font-size: 15px; line-height: 1.6; margin: 0 0 16px 0; font-family: 'Courier New', monospace;">
                        My company has developed a new way that reduces the time spent moving from papers and pictures to documents by <span style="background: #37474f; color: #ffffff; padding: 2px 6px; border-radius: 3px; font-weight: 700;">80%</span>, and ships custom document automation in days, not months.
                    </p>
                    
                    <p style="color: #2c2c2c; font-size: 15px; line-height: 1.6; margin: 0 0 16px 0; font-family: 'Courier New', monospace;">
                        I figured this might be of interest to you given moving to all automation with AI and speeding the supply chain process.
                    </p>
                    
                    <p style="color: #2c2c2c; font-size: 15px; line-height: 1.6; margin: 0; font-family: 'Courier New', monospace;">
                        I'd love to get your feedback even if you're not in the market for this right now. Do you have 20 min this week?
                    </p>
                </div>
                
                <!-- CTA Button -->
                <div style="text-align: center; margin: 25px 0;">
                    <a href="{booking_link}" style="display: inline-block; background: linear-gradient(135deg, #37474f 0%, #455a64 100%); color: #ffffff; text-decoration: none; padding: 12px 24px; border-radius: 4px; font-weight: 700; font-size: 14px; box-shadow: 0 4px 15px rgba(55, 71, 79, 0.4); font-family: 'Courier New', monospace; text-transform: uppercase; letter-spacing: 1px;">
                        📠 Book a 20-minute call
                    </a>
                </div>
                
                <p style="color: #607d8b; font-size: 12px; line-height: 1.4; margin: 20px 0 0 0; text-align: center; font-family: 'Courier New', monospace; text-transform: uppercase; letter-spacing: 0.5px;">
                    Use my Calendly to schedule at your convenience
                </p>
            </div>
            
            <!-- Footer -->
            <div style="background: linear-gradient(135deg, #37474f 0%, #455a64 100%); padding: 20px 40px; border-top: 3px solid #263238;">
                <div style="text-align: center;">
                    <p style="color: #ffffff; font-size: 16px; font-weight: 700; margin: 0 0 3px 0; font-family: 'Courier New', monospace; text-transform: uppercase; letter-spacing: 1px;">Hamza Mhirsi</p>
                    <p style="color: #b0bec5; font-size: 11px; margin: 0 0 8px 0; font-family: 'Courier New', monospace; text-transform: uppercase; letter-spacing: 0.5px;">CEO & Founder, Wraki</p>
                    <a href="https://wraki.ma" style="color: #81c784; text-decoration: none; font-size: 12px; font-weight: 600; font-family: 'Courier New', monospace; text-transform: uppercase;">wraki.ma</a>
                </div>
            </div>
            
        </div>
    </body>
    </html>
    """
    
    # Plain text version for fallback
    text_body = f"""Dear {first_name}, my name is Hamza and I'm the CEO of Wraki.

My company has developed a new way that reduces the time spent moving from papers and pictures to documents by 80%, and ships custom document automation in days, not months.

I figured this might be of interest to you given moving to all automation with AI and speeding the supply chain process.

I'd love to get your feedback even if you're not in the market for this right now. Do you have 20 min this week? You can use my Calendly to book a meeting: {booking_link}

Best regards,
Hamza Mhirsi
CEO & Founder, Wraki
wraki.ma"""

    return subject, html_body, text_body

def get_follow_up_template(first_name, company_name):
    """
    Generate a follow-up email template
    """
    subject = f"Following up - {company_name} supply chain optimization"
    
    body = f"""Hi {first_name},

I wanted to follow up on my previous email about supply chain optimization solutions for {company_name}.

I understand you're likely busy, so I'll keep this brief. Many supply chain leaders I speak with are dealing with similar challenges:

• Lack of real-time visibility across operations
• Manual processes that slow down decision-making
• Difficulty tracking KPIs and performance metrics

If any of these resonate with your current situation, I'd be happy to share some quick wins that have worked for similar companies.

Even if you're not interested in our solution, I'd value your perspective on the biggest challenges facing supply chain professionals today.

Would a brief 10-minute call work for you this week?

Best regards,
Hamza Mhirsi
Founder, Wraki"""

    return subject, body
