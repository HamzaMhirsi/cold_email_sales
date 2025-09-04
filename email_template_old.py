"""
Professional email templates for Wraki cold outreach
"""

def get_email_template(first_name, company_name, job_title, booking_link):
    """
    Generate a personalized cold email template for Wraki outreach
    """
    subject = f"Quick question about {company_name}'s document automation"
    
    # HTML email template with blue fax machine design - paper coming out effect
    html_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Wraki - Document Automation</title>
    </head>
    <body style="margin: 0; padding: 0; font-family: 'Segoe UI', Arial, sans-serif; background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); min-height: 100vh;">
        <!-- Fax Machine Container -->
        <div style="max-width: 650px; margin: 30px auto; position: relative;">
            
            <!-- Fax Machine Top -->
            <div style="background: linear-gradient(135deg, #1565c0 0%, #0d47a1 100%); height: 80px; border-radius: 12px 12px 0 0; position: relative; box-shadow: 0 -4px 20px rgba(21, 101, 192, 0.3);">
                <!-- Fax Machine Details -->
                <div style="position: absolute; top: 15px; left: 30px; right: 30px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div style="color: #ffffff; font-size: 18px; font-weight: 700; letter-spacing: 1px;">WRAKI FAX</div>
                        <div style="background: #4fc3f7; color: #0d47a1; padding: 4px 12px; border-radius: 20px; font-size: 10px; font-weight: 600; text-transform: uppercase;">TRANSMITTING</div>
                    </div>
                    <div style="color: #90caf9; font-size: 11px; margin-top: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Document Automation Platform</div>
                </div>
                
                <!-- Fax Machine Buttons -->
                <div style="position: absolute; bottom: 8px; right: 30px;">
                    <div style="display: inline-block; width: 8px; height: 8px; background: #4caf50; border-radius: 50%; margin: 0 3px;"></div>
                    <div style="display: inline-block; width: 8px; height: 8px; background: #ff9800; border-radius: 50%; margin: 0 3px;"></div>
                    <div style="display: inline-block; width: 8px; height: 8px; background: #f44336; border-radius: 50%; margin: 0 3px;"></div>
                </div>
            </div>
            
            <!-- Paper Coming Out Effect -->
            <div style="background: #ffffff; margin: 0 20px; position: relative; box-shadow: 0 8px 32px rgba(21, 101, 192, 0.2); transform: perspective(1000px) rotateX(-2deg); transform-origin: top;">
                
                <!-- Paper Perforation Edge -->
                <div style="height: 8px; background: repeating-linear-gradient(90deg, #1565c0 0px, #1565c0 4px, transparent 4px, transparent 8px); opacity: 0.3;"></div>
                
                <!-- Document Header -->
                <div style="background: linear-gradient(135deg, #e1f5fe 0%, #b3e5fc 100%); padding: 20px 40px; border-bottom: 3px solid #29b6f6;">
                    <div style="text-align: center;">
                        <div style="color: #0277bd; font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px;">FAX TRANSMISSION</div>
                        <div style="color: #0288d1; font-size: 12px;">FROM: WRAKI AUTOMATION SYSTEM</div>
                    </div>
                </div>
                
                <!-- Main Document Content -->
                <div style="padding: 35px 40px; background: #ffffff; position: relative;">
                    
                    <!-- Transmission Lines Effect -->
                    <div style="position: absolute; top: 0; left: 0; right: 0; height: 100%; background: repeating-linear-gradient(0deg, transparent 0px, transparent 22px, rgba(33, 150, 243, 0.04) 22px, rgba(33, 150, 243, 0.04) 24px); pointer-events: none;"></div>
                    
                    <!-- Message Content -->
                    <div style="position: relative; z-index: 2;">
                        <p style="color: #1a1a1a; font-size: 16px; line-height: 1.7; margin: 0 0 20px 0; font-weight: 600;">
                            Dear <span style="background: linear-gradient(120deg, #e3f2fd 0%, #bbdefb 100%); color: #0d47a1; padding: 3px 8px; border-radius: 4px; font-weight: 700;">{first_name}</span>, my name is Hamza and I'm the CEO of Wraki.
                        </p>
                        
                        <p style="color: #2c2c2c; font-size: 16px; line-height: 1.7; margin: 0 0 20px 0;">
                            My company has developed a new way that reduces the time spent moving from papers and pictures to documents by <span style="background: linear-gradient(135deg, #2196f3 0%, #1976d2 100%); color: #ffffff; padding: 4px 10px; border-radius: 6px; font-weight: 700; box-shadow: 0 2px 8px rgba(33, 150, 243, 0.3);">80%</span>, and ships custom document automation in days, not months.
                        </p>
                        
                        <p style="color: #2c2c2c; font-size: 16px; line-height: 1.7; margin: 0 0 20px 0;">
                            I figured this might be of interest to you given moving to all automation with AI and speeding the supply chain process.
                        </p>
                        
                        <p style="color: #2c2c2c; font-size: 16px; line-height: 1.7; margin: 0 0 30px 0;">
                            I'd love to get your feedback even if you're not in the market for this right now. Do you have 20 min this week?
                        </p>
                        
                        <!-- CTA Button -->
                        <div style="text-align: center; margin: 35px 0;">
                            <a href="{booking_link}" style="display: inline-block; background: linear-gradient(135deg, #2196f3 0%, #1565c0 100%); color: #ffffff; text-decoration: none; padding: 16px 32px; border-radius: 8px; font-weight: 700; font-size: 16px; box-shadow: 0 6px 20px rgba(33, 150, 243, 0.4); text-transform: uppercase; letter-spacing: 1px; transition: all 0.3s ease;">
                                📠 Schedule 20-Minute Call
                            </a>
                        </div>
                        
                        <p style="color: #64b5f6; font-size: 14px; line-height: 1.5; margin: 25px 0 0 0; text-align: center; font-style: italic;">
                            Use my Calendly to book a meeting at your convenience
                        </p>
                    </div>
                </div>
                
                <!-- Document Footer -->
                <div style="background: linear-gradient(135deg, #1976d2 0%, #1565c0 100%); padding: 25px 40px; color: #ffffff;">
                    <div style="text-align: center;">
                        <p style="color: #ffffff; font-size: 18px; font-weight: 700; margin: 0 0 5px 0; text-transform: uppercase; letter-spacing: 1px;">Hamza Mhirsi</p>
                        <p style="color: #90caf9; font-size: 13px; margin: 0 0 10px 0; text-transform: uppercase; letter-spacing: 0.5px;">CEO & Founder, Wraki</p>
                        <a href="https://wraki.ma" style="color: #4fc3f7; text-decoration: none; font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">wraki.ma</a>
                    </div>
                </div>
                
                <!-- Paper Bottom Perforation -->
                <div style="height: 8px; background: repeating-linear-gradient(90deg, #1565c0 0px, #1565c0 4px, transparent 4px, transparent 8px); opacity: 0.3;"></div>
            </div>
            
            <!-- Fax Machine Bottom Shadow -->
            <div style="background: linear-gradient(135deg, #0d47a1 0%, #1565c0 100%); height: 20px; border-radius: 0 0 12px 12px; box-shadow: 0 8px 25px rgba(13, 71, 161, 0.3);"></div>
        </div>
    </body>
    </html>
    """
                    
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

I'd love to get your feedback even if you're not in the market for this right now. Do you have 20 min this week?

You can use my Calendly to book a meeting at your convenience: {booking_link}

Best regards,
Hamza Mhirsi
CEO & Founder, Wraki
wraki.ma
"""

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
