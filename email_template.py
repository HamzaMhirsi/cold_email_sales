"""
Professional email templates for Wraki cold outreach - Multi-language support
"""

def get_email_template(first_name, company_name, job_title, booking_link, language="english"):
    """
    Generate a personalized cold email template for Wraki outreach in specified language
    """
    
    # Multi-language content
    if language == "arabic":
        subject = f"سؤال سريع حول أتمتة المستندات في {company_name}"
        greeting = f"عزيزي {first_name}،"
        intro = "اسمي حمزة وأنا الرئيس التنفيذي لشركة وراقي."
        value_prop = f"لقد طورت شركتي طريقة جديدة تقلل الوقت المستغرق في تحويل الأوراق والصور إلى مستندات بنسبة <span style='background: #000000; color: #ffffff; padding: 4px 10px; font-weight: bold; border-radius: 3px;'>80%</span> وتقدم حلول أتمتة مخصصة في أيام وليس شهور."
        relevance = f"اعتقدت أن هذا قد يهمك نظراً لتركيز {company_name} على الأتمتة والذكاء الاصطناعي وتسريع عمليات سلسلة التوريد."
        cta_text = "أود الحصول على رأيك حتى لو لم تكن تبحث عن حلول في الوقت الحالي. هل لديك 20 دقيقة هذا الأسبوع للمحادثة؟"
        button_text = "📅 حجز مكالمة 20 دقيقة"
        calendly_text = "استخدم رابط Calendly أعلاه للحجز في الوقت المناسب لك"
        signature = "حمزة مهيرسي"
        title = "الرئيس التنفيذي والمؤسس، وراقي"
        platform_text = "منصة أتمتة المستندات"
        header_text = "نظام مستندات وراقي"
        
    elif language == "french":
        subject = f"Question rapide sur l'automatisation documentaire de {company_name}"
        greeting = f"Cher {first_name},"
        intro = "Je m'appelle Hamza et je suis le PDG de Wraki."
        value_prop = f"Mon entreprise a développé une nouvelle approche qui réduit le temps de traitement des documents de <span style='background: #000000; color: #ffffff; padding: 4px 10px; font-weight: bold; border-radius: 3px;'>80%</span> et livre des solutions d'automatisation personnalisées en jours, pas en mois."
        relevance = f"J'ai pensé que cela pourrait vous intéresser étant donné l'orientation de {company_name} vers l'automatisation et l'IA pour optimiser la chaîne d'approvisionnement."
        cta_text = "J'aimerais avoir votre avis, même si vous ne cherchez pas activement de solutions en ce moment. Auriez-vous 20 minutes cette semaine pour une brève conversation ?"
        button_text = "📅 PLANIFIER UN APPEL DE 20 MINUTES"
        calendly_text = "Utilisez mon lien Calendly ci-dessus pour réserver à votre convenance"
        signature = "Hamza Mhirsi"
        title = "PDG et Fondateur, Wraki"
        platform_text = "Plateforme d'Automatisation Documentaire"
        header_text = "SYSTÈME DOCUMENTAIRE WRAKI"
        
    else:  # Default to English
        subject = f"Quick question about {company_name}'s document automation"
        greeting = f"Dear {first_name},"
        intro = "My name is Hamza and I'm the CEO of Wraki."
        value_prop = f"We've developed a revolutionary approach that reduces document processing time by <span style='background: #000000; color: #ffffff; padding: 4px 10px; font-weight: bold; border-radius: 3px;'>80%</span> and delivers custom automation solutions in days, not months."
        relevance = f"Given your focus on supply chain automation and AI optimization, I thought this might be of significant interest to <strong>{company_name}</strong>."
        cta_text = "I'd love to get your feedback, even if you're not actively looking for solutions right now. Would you have 20 minutes this week for a brief conversation?"
        button_text = "📅 SCHEDULE 20-MINUTE CALL"
        calendly_text = "Use my Calendly link above to book at your convenience"
        signature = "Hamza Mhirsi"
        title = "CEO & Founder, Wraki"
        platform_text = "Document Automation Platform"
        header_text = "WRAKI DOCUMENT SYSTEM"
    
    # Set direction and alignment based on language
    body_direction = "rtl" if language == "arabic" else "ltr"
    text_align = "right" if language == "arabic" else "left"
    
    # Fax machine design with minimal blue and clear readability
    html_body = f"""
    <!DOCTYPE html>
    <html dir="{body_direction}">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Wraki - Document Automation</title>
    </head>
    <body style="margin: 0; padding: 0; font-family: 'Courier New', monospace; background-color: #e8e8e8; line-height: 1.5; direction: {body_direction}; text-align: {text_align};">
        <!-- Fax Machine Container -->
        <div style="max-width: 650px; margin: 30px auto; position: relative;">
            
            <!-- Fax Machine Top -->
            <div style="background: #333333; height: 50px; border-radius: 6px 6px 0 0; position: relative; box-shadow: 0 2px 8px rgba(0,0,0,0.15); margin: 0 15px; text-align: center; line-height: 50px;">
                <div style="color: #ffffff; font-size: 14px; font-weight: bold;">{header_text}</div>
            </div>
            
            <!-- Paper Coming Out -->
            <div style="background: #ffffff; margin: 0 15px; position: relative; box-shadow: 0 4px 15px rgba(0,0,0,0.15); border: 2px solid #cccccc; border-top: none;">
                
                <!-- Document Header -->
                <div style="background: #ffffff; padding: 20px 30px; border-bottom: 1px solid #cccccc;">
                    <div style="text-align: center; margin-bottom: 15px;">
                        <div style="font-size: 18px; font-weight: bold; color: #000000; margin-bottom: 8px;">WRAKI</div>
                        <div style="font-size: 12px; color: #666666; text-transform: uppercase;">{platform_text}</div>
                    </div>
                </div>
                
                <!-- Main Document -->
                <div style="padding: 40px 35px; background: #ffffff; position: relative;">
                    
                    <!-- Content -->
                    <div style="position: relative;">
                        <p style="color: #000000; font-size: 16px; line-height: 1.7; margin: 0 0 20px 0; text-align: {text_align};">
                            {greeting}
                        </p>
                        
                        <p style="color: #000000; font-size: 16px; line-height: 1.7; margin: 0 0 20px 0; text-align: {text_align};">
                            {intro}
                        </p>
                        
                        <p style="color: #000000; font-size: 16px; line-height: 1.7; margin: 0 0 20px 0; text-align: {text_align};">
                            {value_prop}
                        </p>
                        
                        <div style="border: 2px solid #333333; padding: 20px; margin: 25px 0; background: #f8f8f8;">
                            <p style="color: #000000; font-size: 16px; margin: 0; text-align: center; font-style: italic;">
                                "{relevance}"
                            </p>
                        </div>
                        
                        <p style="color: #000000; font-size: 16px; line-height: 1.7; margin: 0 0 30px 0; text-align: {text_align};">
                            {cta_text}
                        </p>
                        
                        <!-- CTA Button -->
                        <div style="text-align: center; margin: 35px 0;">
                            <a href="{booking_link}" style="display: inline-block; background: #000000; color: #ffffff; text-decoration: none; padding: 15px 30px; font-weight: bold; font-size: 16px; text-transform: uppercase; letter-spacing: 1px; border-radius: 4px;">
                                {button_text}
                            </a>
                        </div>
                        
                        <p style="color: #666666; font-size: 14px; text-align: center; margin: 25px 0 0 0;">
                            {calendly_text}
                        </p>
                    </div>
                </div>
                
                <!-- Fax Footer -->
                <div style="background: #f5f5f5; padding: 20px 35px; border-top: 2px solid #cccccc; text-align: center;">
                    <p style="color: #000000; font-size: 14px; font-weight: bold; margin: 0 0 3px 0; text-transform: uppercase;">{signature}</p>
                    <p style="color: #666666; font-size: 12px; margin: 0 0 8px 0; text-transform: uppercase;">{title}</p>
                    <p style="color: #000000; font-size: 12px; margin: 0; font-weight: bold;">WRAKI.MA</p>
                </div>
                
                <!-- Paper Tear Effect -->
                <div style="height: 6px; background: repeating-linear-gradient(90deg, #cccccc 0px, #cccccc 3px, transparent 3px, transparent 6px);"></div>
            </div>
            
            <!-- Fax Machine Bottom -->
            <div style="background: #333333; height: 15px; border-radius: 0 0 6px 6px; box-shadow: 0 4px 10px rgba(0,0,0,0.2); margin: 0 15px;"></div>
        </div>
    </body>
    </html>
    """
    
    # Clean text versions (remove HTML tags)
    def clean_html_tags(text):
        import re
        return re.sub(r'<[^>]+>', '', text)
    
    # Plain text version
    if language == "arabic":
        text_body = f"""
{greeting}

{intro}

{clean_html_tags(value_prop)}

{relevance}

{cta_text}

رابط الحجز: {booking_link}

مع أطيب التحيات،
{signature}
{title}
wraki.ma
"""
    elif language == "french":
        text_body = f"""
{greeting}

{intro}

{clean_html_tags(value_prop)}

{relevance}

{cta_text}

Lien de réservation: {booking_link}

Cordialement,
{signature}
{title}
wraki.ma
"""
    else:  # English
        text_body = f"""
{greeting}

{intro}

{clean_html_tags(value_prop)}

{clean_html_tags(relevance)}

{cta_text}

Book a call: {booking_link}

Best regards,
{signature}
{title}
wraki.ma
"""

    return subject, html_body, text_body

def get_follow_up_template(first_name, company_name):
    """
    Generate a follow-up email template
    """
    subject = f"Following up - {company_name} supply chain optimization"
    
    body = f"""Hi {first_name},

I wanted to follow up on my previous email about document automation for {company_name}.

We've helped similar companies in your industry reduce document processing time by 80% and eliminate manual data entry errors.

Would you be interested in a quick 15-minute call to see how this could benefit {company_name}?

Best regards,
Hamza Mhirsi
CEO, Wraki
"""
    
    return subject, body
