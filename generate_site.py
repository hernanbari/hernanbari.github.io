"""
FastHTML Website Generator for Hernán Barijhoff Personal Site
Run this to generate all HTML files
"""

from fasthtml.common import *
import re



def format_text(text):
    """
    Convert markdown-style formatting to FastHTML components
    Single:
    _word_ -> italic (Em)
    *word* -> bold (Strong)  
    /word/ -> underline (U)
    
    Double (nested):
    _*word*_ -> italic + bold
    *_word_* -> bold + italic
    /_word_/ -> underline + italic
    /*word*/ -> underline + bold
    _/word/_ -> italic + underline
    */word/* -> bold + underline
    
    Triple (all three):
    _*/word/*_ -> italic + bold + underline
    _/*word*/_ -> italic + underline + bold
    *_/word/_* -> bold + italic + underline
    */_word_/* -> bold + underline + italic
    /_*word*_/ -> underline + italic + bold
    /*_word_*/ -> underline + bold + italic
    """
    if not text or not isinstance(text, str):
        return [text] if text else []
    
    # Pattern matches: triple nesting (3 chars), double nesting (2 chars), then single (1 char)
    # Order matters: check longest patterns first
    pattern = r'(_\*/[^/]+/\*_|_/\*[^*]+\*/_|\*_/[^/]+/_\*|\*/_[^_]+_/\*|/_\*[^*]+\*_/|/\*_[^_]+_\*/|_\*[^*]+\*_|\*_[^_]+_\*|/_[^_]+_/|/\*[^*]+\*/|_/[^/]+/_|\*/[^/]+/\*|_[^_]+_|\*[^*]+\*|/[^/]+/)'
    parts = re.split(pattern, text)
    
    result = []
    for part in parts:
        if not part:
            continue
        
        # Triple nesting (3 markers)
        if part.startswith('_*/') and part.endswith('/*_'):
            # _*/text/*_ -> italic + bold + underline
            result.append(Em(Strong(U(part[3:-3]))))
        elif part.startswith('_/*') and part.endswith('*/_'):
            # _/*text*/_ -> italic + underline + bold
            result.append(Em(U(Strong(part[3:-3]))))
        elif part.startswith('*_/') and part.endswith('/_*'):
            # *_/text/_* -> bold + italic + underline
            result.append(Strong(Em(U(part[3:-3]))))
        elif part.startswith('*/_') and part.endswith('_/*'):
            # */_text_/* -> bold + underline + italic
            result.append(Strong(U(Em(part[3:-3]))))
        elif part.startswith('/_*') and part.endswith('*_/'):
            # /_*text*_/ -> underline + italic + bold
            result.append(U(Em(Strong(part[3:-3]))))
        elif part.startswith('/*_') and part.endswith('_*/'):
            # /*_text_*/ -> underline + bold + italic
            result.append(U(Strong(Em(part[3:-3]))))
        # Double nesting (2 markers)
        elif part.startswith('_*') and part.endswith('*_'):
            # _*text*_ -> italic + bold
            result.append(Em(Strong(part[2:-2])))
        elif part.startswith('*_') and part.endswith('_*'):
            # *_text_* -> bold + italic
            result.append(Strong(Em(part[2:-2])))
        elif part.startswith('/_') and part.endswith('_/'):
            # /_text_/ -> underline + italic
            result.append(U(Em(part[2:-2])))
        elif part.startswith('/*') and part.endswith('*/'):
            # /*text*/ -> underline + bold
            result.append(U(Strong(part[2:-2])))
        elif part.startswith('_/') and part.endswith('/_'):
            # _/text/_ -> italic + underline
            result.append(Em(U(part[2:-2])))
        elif part.startswith('*/') and part.endswith('/*'):
            # */text/* -> bold + underline
            result.append(Strong(U(part[2:-2])))
        # Single markers
        elif part.startswith('_') and part.endswith('_'):
            # _text_ -> italic
            result.append(Em(part[1:-1]))
        elif part.startswith('*') and part.endswith('*'):
            # *text* -> bold
            result.append(Strong(part[1:-1]))
        elif part.startswith('/') and part.endswith('/'):
            # /text/ -> underline
            result.append(U(part[1:-1]))
        else:
            # Plain text
            result.append(part)
    
    return result



# Color themes with pastel colors and different dark backgrounds
THEMES = {
    # "lavender": {
    #     "name": "Lavender Dream",
    #     "bg_dark": "#1a1625",
    #     "bg_secondary_dark": "#241d30",
    #     "accent_dark": "#b8a4d4",
    #     "accent_hover_dark": "#9d84c2",
    #     "bg_light": "#faf9fc",
    #     "accent_light": "#7c5fb8",
    # },
    # "sage": {
    #     "name": "Sage Garden",
    #     "bg_dark": "#1a1f1a",
    #     "bg_secondary_dark": "#242b24",
    #     "accent_dark": "#a8c9a8",
    #     "accent_hover_dark": "#8eb38e",
    #     "bg_light": "#f8faf8",
    #     "accent_light": "#5a8c5a",
    # },
    # "peach": {
    #     "name": "Warm Peach",
    #     "bg_dark": "#221a18",
    #     "bg_secondary_dark": "#2d2320",
    #     "accent_dark": "#e8b4a0",
    #     "accent_hover_dark": "#d49980",
    #     "bg_light": "#fdf9f7",
    #     "accent_light": "#c17a5a",
    # },
    "slate_blue": {
        "name": "Midnight Slate",
        "bg_dark": "#1a1d24",
        "bg_secondary_dark": "#242831",
        "accent_dark": "#a8b8d4",
        "accent_hover_dark": "#8fa3c2",
        "bg_light": "#f8f9fb",
        "accent_light": "#5a7099",
    },
}

# Page content - centralized to avoid duplication
CONTENT = {
    "name": "HERNÁN BARIJHOFF",
    "subtitle": "MS CS | MLE | EA | Founder",
    "tagline": "Building Mental Health tech that ",
    "tagline_emphasis": "scales",
    "email": "my_fullname@gmail.com",
    "linkedin_url": "https://www.linkedin.com/in/hernanbarijhoff/",
    "website_url": "https://mindappterapia.com",
    
    "about": {
        "title": "What I Think",
        "paragraphs": [

            "I've experienced first hand the transformative power of therapy, but I've known so many people who didn't have the same experience, or didn't even try it because of bias or stigma. This frustrated me, and I started to wonder, what was wrong? The therapists' abilities? The process itself? Access? Society?",
            "While researching societal problems, I came across the EA movement, and in particular, the work of a philosopher, Michael Plant, who proposes that /_*happiness*_/ should be the metric we should strive for, not 'years-lived' or 'lives-saved'. _What's the point of a life saved but riddled with suffering?_",
            "At the same time, I've always wanted to build a startup, because I think it has the biggest impact of any endeavor you could pursue, if you can actually pull it off. ",
            "My gut feeling was that it was worth diving deep into Mental Health, specifically /*facilitating access to quality therapy*/. That's how my current project MindApp started. I've learned things you can only learn by doing: how to balance patient needs with business sustainability, how edge cases reveal gaps in your initial thinking, when automated systems should escalate to human judgment. Being a founder taught me many different things — *about people, product, frustration, and purpose*. Invaluable learnings.  The most meaningful moments for me have been when a patient says *'thank you, you’ve helped me a lot .'*",
            "Technology for me was always a means to an end. I studied and worked in AI because I understood early on that it was *one of the most powerful tools for creating real change in people's lives*. Before MindApp, I spent years in the startup ecosystem, learning as much as I could, including time at an early-stage YC company (EmiLabsYC19) building NLP chatbots to improve job access for frontline workers.",
            "That's also why /I'm following AGI progress closely/ and participating in AI safety community events in Buenos Aires. *The timeline for world-changing AI is shorter than most people assume*, and Mental Health will be among the domains deeply reshaped—whether through AI-assisted therapy, companionship relationships, or risks we're only beginning to understand. I want to help ensure that transformation improves rather than undermines human wellbeing."
            
        ]
    },
    
    "experience": [
        {
            "company": "MindApp Therapy",
            "title": "Founder & CEO",
            "date": "Jan 2023 — Present",
            "bullets": [
                "Founded and built bootstrapped, profitable online therapy platform serving 380 patients/month at peak across Spain, USA, and Latin America with network of 22 therapists",
                "Designed evidence-based protocols and policies through iterative real-world testing",
                "Balanced therapy access, clinical quality, therapist autonomy, and business sustainability while growing therapist network through structured vetting and patient retention monitoring",
                "Hired and managed 4-person customer service team",
                "Built platform end-to-end using AWS, FastAPI, WhatsApp Platform, and Google/Meta ads"
            ]
        },
        {
            "company": "Startup Exploration",
            "title": "Independent Research",
            "date": "2022",
            "bullets": [
                "WeSex (SexEdTech): Ran structured 2-month cofounder trial; identified product was pre-PMF",
                "Adopted EA cause prioritization framework, pivoted to mental health based on tractability and personal fit",
                "Stenox (Blockchain): Built bot and investment data analytics product; reached YC interview stage"
            ]
        },
        {
            "company": "Emi Labs (YC19)",
            "title": "Sr. Machine Learning Engineer",
            "date": "Oct 2019 — Jan 2022",
            "bullets": [
                "Led NLP pipeline design and implementation for Chatbot (Rasa), with the mission of improving employment access for frontline workers",
                "Coordinated company-wide knowledge-sharing talks with both internal and external speakers",
                "Shaped product direction as fifth employee, including pragmatic scope decisions (e.g., eliminating unnecessary NLP classification when simpler solutions existed)"
            ]
        },
        {
            "company": "Mercado Libre (AMZ of Latam)",
            "title": "Data Scientist (Jr → Sr)",
            "date": "Dec 2016 — Oct 2019",
            "bullets": [
                "Developed Collaborative Filtering Recommendation Models for millions of users (meta-prod2vec)",
                "Built ETL pipelines processing billions of events daily and implemented monitoring infra",
                "Built Sales KPIs reporting for CTR, conversion, attribution and coverage metrics",
                "Developed deployment infra at scale"
            ]
        }
    ],
    
    "academia": [
        {
            "title": "NeurIPS Presentation",
            "subtitle": "ML Open Source Software Workshop",
            "date": "2018",
            "description": "Presented Ms. Thesis"
        },
        {
            "title": "Universidad de Buenos Aires",
            "subtitle": "Master's in Computer Science",
            "date": "2013 — 2018",
            "description": "Thesis: PyLissom - A tool for modeling computational maps of the visual cortex in PyTorch"
        },
        {
            "title": "Data Science Argentina",
            "subtitle": "Meetup Speaker",
            "date": "",
            "description": ""
        },
        {
            "title": "EA @ Buenos Aires",
            "subtitle": "Regular Participant",
            "date": "",
            "description": ""
        },
        {
            "title": "Patch Adams Volunteer",
            "subtitle": "Hospital Clown",
            "date": "",
            "description": ""
        }
    ]
}


def create_style(theme_key):
    """Generate CSS with theme colors"""
    theme = THEMES[theme_key]
    
    return Style(f"""
        :root[data-theme="light"] {{
            --bg-color: {theme['bg_light']};
            --bg-secondary: {theme['bg_light']};
            --text-color: #1a1a1a;
            --text-secondary: #666666;
            --border-color: #e0e0e0;
            --accent-color: {theme['accent_light']};
            --accent-hover: {theme['accent_light']};
            --card-bg: #ffffff;
            --card-border: #e5e7eb;
        }}

        :root[data-theme="dark"] {{
            --bg-color: {theme['bg_dark']};
            --bg-secondary: {theme['bg_secondary_dark']};
            --text-color: #f0f0f0;
            --text-secondary: #a0a0a0;
            --border-color: #333333;
            --accent-color: {theme['accent_dark']};
            --accent-hover: {theme['accent_hover_dark']};
            --card-bg: {theme['bg_secondary_dark']};
            --card-border: #2a2a2a;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: var(--bg-color);
            color: var(--text-color);
            line-height: 1.7;
            transition: background-color 0.3s ease, color 0.3s ease;
        }}

        .container {{
            max-width: 1100px;
            margin: 0 auto;
            padding: 40px 24px;
        }}

        /* Header */
        header {{
            margin-bottom: 40px;
            display: grid;
            grid-template-columns: 25% 1fr;
            align-items: start;
            gap: 40px;
        }}

        .header-left {{
            justify-self: start;
        }}

        .header-box {{
            display: inline-block;
            border: 2px solid var(--accent-color);
            padding: 12px 24px;
            border-radius: 8px;
            background: var(--bg-secondary);
        }}

        h1 {{
            font-size: 28px;
            font-weight: 800;
            letter-spacing: -0.5px;
        }}

        .header-center {{
            display: flex;
            justify-content: space-between;
            align-items: start;
            gap: 20px;
        }}

        .hero-content {{
            flex: 1;
        }}

        .contact-links {{
            display: flex;
            flex-direction: row;
            gap: 12px;
            align-items: center;
            margin-top: 8px;
            flex-wrap: wrap;
        }}

        .contact-links a {{
            color: var(--accent-color);
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
            transition: opacity 0.2s;
        }}

        .contact-links a:hover {{
            opacity: 0.7;
        }}

        .tagline {{
            font-size: 17px;
            color: var(--text-secondary);
            margin-bottom: 0;
            font-weight: 500;
        }}

        .tagline-emphasis {{
            color: var(--accent-color);
            font-weight: 700;
        }}

        .subtitle {{
            font-size: 12px;
            color: var(--text-secondary);
            margin-top: 6px;
            font-weight: 500;
            letter-spacing: 0.5px;
        }}

        .hero-link {{
            display: inline-block;
            margin-top: 8px;
            padding: 10px 20px;
            background: var(--accent-color);
            color: var(--bg-color);
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            font-size: 17px;
            transition: all 0.2s;
        }}

        .hero-link:hover {{
            background: var(--accent-hover);
            transform: translateY(-2px);
        }}

        /* Toggle Switch */
        .toggle-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 6px;
        }}

        .toggle-label-top {{
            font-size: 11px;
            color: var(--text-secondary);
            font-weight: 500;
        }}

        .toggle-switch {{
            position: relative;
            width: 60px;
            height: 30px;
            background: var(--border-color);
            border-radius: 15px;
            cursor: pointer;
            transition: background 0.3s;
        }}

        .toggle-switch::after {{
            content: '';
            position: absolute;
            width: 24px;
            height: 24px;
            background: white;
            border-radius: 50%;
            top: 3px;
            left: 3px;
            transition: transform 0.3s;
        }}

        .toggle-switch.active {{
            background: var(--accent-color);
        }}

        .toggle-switch.active::after {{
            transform: translateX(30px);
        }}

        section {{
            margin-bottom: 40px;
        }}

        #about {{
            display: block;
        }}

        .section-header {{
            font-size: 22px;
            font-weight: 800;
            margin-bottom: 20px;
            color: var(--text-color);
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .section-header::before {{
            content: "→";
            color: var(--accent-color);
            font-size: 24px;
        }}

        /* About Section */
        .about-content p {{
            font-size: 15px;
            margin-bottom: 12px;
            line-height: 1.6;
        }}

        .about-content p:first-child {{
            font-size: 16px;
            font-weight: 600;
            color: var(--accent-color);
        }}

        /* Mobile Tabs */
        .mobile-tabs {{
            display: none;
            margin-bottom: 20px;
        }}

        .tab-buttons {{
            display: flex;
            gap: 10px;
            border-bottom: 2px solid var(--border-color);
        }}

        .tab-button {{
            flex: 1;
            padding: 12px;
            background: none;
            border: none;
            border-bottom: 3px solid transparent;
            color: var(--text-secondary);
            cursor: pointer;
            font-size: 16px;
            font-weight: 600;
            transition: all 0.2s;
        }}

        .tab-button.active {{
            color: var(--accent-color);
            border-bottom-color: var(--accent-color);
        }}

        .tab-content {{
            display: none;
        }}

        .tab-content.active {{
            display: block;
        }}

        @media (min-width: 901px) {{
            .tab-content {{
                display: none !important;
            }}
        }}

        /* Two Column Layout */
        .two-column {{
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 30px;
        }}

        .column h3 {{
            font-size: 18px;
            font-weight: 800;
            margin-bottom: 16px;
            color: var(--text-color);
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .column h3::before {{
            content: "→";
            color: var(--accent-color);
            font-size: 20px;
        }}

        /* Job Cards */
        .job {{
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-left: 3px solid var(--accent-color);
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 16px;
            transition: all 0.3s;
        }}

        .job:hover {{
            border-color: var(--accent-color);
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            transform: translateX(2px);
        }}

        .job-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
            flex-wrap: wrap;
            gap: 8px;
        }}

        .job-title-row {{
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }}

        .academia-title-col {{
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}

        .job h4 {{
            font-size: 17px;
            font-weight: 700;
            margin-bottom: 0;
            color: var(--text-color);
            display: inline;
        }}

        .job-separator {{
            color: var(--text-secondary);
            font-weight: 400;
        }}

        .job-title {{
            font-size: 14px;
            color: var(--accent-color);
            font-weight: 600;
            margin-bottom: 0;
            display: inline;
        }}

        .job-date {{
            font-size: 13px;
            color: var(--text-secondary);
            white-space: nowrap;
            margin-bottom: 0;
            font-weight: 500;
        }}

        .job-bullets {{
            list-style: none;
            padding: 0;
        }}

        .job-bullets li {{
            padding-left: 20px;
            position: relative;
            margin-bottom: 8px;
            font-size: 14px;
            line-height: 1.6;
        }}

        .job-bullets li::before {{
            content: "▸";
            position: absolute;
            left: 0;
            color: var(--accent-color);
            font-weight: bold;
            font-size: 16px;
        }}

        .job-description {{
            font-size: 14px;
            line-height: 1.6;
            color: var(--text-secondary);
            margin-top: 6px;
        }}

        /* Nerdy Timeline */
        .nerdy-timeline {{
            background: linear-gradient(135deg, var(--card-bg) 0%, var(--bg-secondary) 100%);
            border: 2px solid var(--accent-color);
            border-radius: 12px;
            padding: 28px;
            margin-bottom: 24px;
            position: relative;
            overflow: hidden;
        }}

        .nerdy-timeline::before {{
            content: "";
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 6px;
            background: var(--accent-color);
        }}

        .nerdy-timeline h4 {{
            font-size: 24px;
            font-weight: 800;
            color: var(--accent-color);
            margin-bottom: 16px;
        }}

        .timeline-description {{
            margin-top: 12px;
            font-size: 17px;
            line-height: 1.7;
            color: var(--text-secondary);
        }}

        /* Footer with toggles */
        footer {{
            border-top: 2px solid var(--border-color);
            padding-top: 40px;
            margin-top: 80px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 20px;
        }}

        .footer-toggles {{
            display: flex;
            gap: 30px;
            align-items: center;
        }}

        .toggle-label {{
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 14px;
            color: var(--text-secondary);
        }}

        /* Responsive */
        @media (max-width: 900px) {{
            .two-column {{
                display: none;
            }}

            .column {{
                display: none;
            }}

            .mobile-tabs {{
                display: block;
            }}

            #about {{
                display: none;
            }}

            footer {{
                flex-direction: column;
                text-align: center;
            }}
        }}

        @media (max-width: 768px) {{
            .container {{
                padding: 30px 20px;
            }}

            header {{
                display: flex;
                flex-direction: column;
                align-items: stretch;
                margin-bottom: 30px;
                gap: 15px;
            }}

            .header-left {{
                justify-self: auto;
                display: flex;
                justify-content: center;
                width: 100%;
            }}

            .header-box {{
                padding: 10px 20px;
                flex: 1;
            }}

            h1 {{
                font-size: 24px;
            }}

            .header-center {{
                order: 2;
            }}

            .hero-content {{
                text-align: center;
            }}

            .toggle-container {{
                display: none;
            }}

            .contact-links {{
                flex-direction: row;
                justify-content: center;
                gap: 8px;
            }}

            .tagline {{
                font-size: 15px;
            }}

            .section-header {{
                font-size: 20px;
            }}

            .job {{
                padding: 14px;
            }}

            .job h4 {{
                font-size: 16px;
            }}

            .two-column {{
                grid-template-columns: 1fr;
            }}

            /* Make experience cards vertical on mobile */
            .experience-card .job-title-row {{
                flex-direction: column;
                align-items: flex-start;
                gap: 4px;
            }}

            .experience-card .job-separator {{
                display: none;
            }}

            .experience-card .job-title {{
                display: block;
            }}

            .experience-card .job-header {{
                align-items: flex-start;
            }}
        }}
    """)


def create_script():
    """JavaScript for dark mode, nerdy mode, and mobile tabs"""
    return Script("""
        // Dark Mode Toggle
        function initDarkMode() {
            const darkModeToggle = document.getElementById('darkModeToggle');
            const html = document.documentElement;
            
            const savedTheme = localStorage.getItem('theme') || 'dark';
            html.setAttribute('data-theme', savedTheme);
            if (darkModeToggle) {
                darkModeToggle.classList.toggle('active', savedTheme === 'dark');
            }
            
            if (darkModeToggle) {
                darkModeToggle.addEventListener('click', () => {
                    const currentTheme = html.getAttribute('data-theme');
                    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                    
                    html.setAttribute('data-theme', newTheme);
                    localStorage.setItem('theme', newTheme);
                    darkModeToggle.classList.toggle('active', newTheme === 'dark');
                });
            }
        }

        // Nerdy Mode Toggle
        function initNerdyMode() {
            const toggle = document.getElementById('nerdyToggle');
            const aboutDiv = document.querySelector('.about-content'); // Changed to class selector
            const expColumn = document.querySelector('.two-column');
            
            // Mobile tabs
            const mobileAbout = document.getElementById('tab-about');
            const mobileExp = document.getElementById('tab-experience');
            const mobileAcad = document.getElementById('tab-academia');
            
            if (!toggle) return;
            
            // Store originals
            const origAbout = aboutDiv ? aboutDiv.innerHTML : '';
            const origExp = expColumn ? expColumn.innerHTML : '';
            const origMobileAbout = mobileAbout ? mobileAbout.innerHTML : '';
            const origMobileExp = mobileExp ? mobileExp.innerHTML : '';
            let isNerdy = false;
            
            // Fun content
            const nerdyAboutHTML = '<h3 style="margin-bottom: 15px;">→ BEHIND THE SCIENTIST</h3><p>I\\'m obsessed with worlds—both real and imagined.</p><p><strong>Middle Earth shaped my worldview.</strong> LOTR taught me that small people can change history, that fellowship matters more than individual glory, and that the best adventures come from saying yes to the unexpected.</p><p><strong>Music taught me about the joy of everyday life.</strong> Music is my lifeline, daft punk my mantra. It’s what keeps me connected to people</p><p><strong>Meditation revealed the gap between map and territory.</strong> Sitting still for hours showed me that consciousness is weirder than any system we built, maybe AI can help us with that. Also: most of what we think is “I” is just noise.</p><p><strong>Science is what reminds me to keep wondering.</strong> Space, stars, physics, are the fields that I would love to study in an infinite-time universe.</p>';
            
            const nerdyTimelineHTML = '<div class="job" style="border-left: 3px solid var(--accent-color); padding-left: 20px; margin-bottom: 20px;"><h4 style="color: var(--accent-color); margin-bottom: 8px;">1990—2010: LOTR Dreaming</h4><p>Fell in love with world-building, epic quests, and the idea that hobbits—the smallest, most overlooked people—could save the world.</p></div>' +
                '<div class="job" style="border-left: 3px solid var(--accent-color); padding-left: 20px; margin-bottom: 20px;"><h4 style="color: var(--accent-color); margin-bottom: 8px;">2010—2020: Science & Meditation Obsession</h4><p>Discovered computational neuroscience could explain consciousness. Meanwhile, sat still for hours trying to understand it from the inside.</p></div>' +
                '<div class="job" style="border-left: 3px solid var(--accent-color); padding-left: 20px; margin-bottom: 20px;"><h4 style="color: var(--accent-color); margin-bottom: 8px;">2015—2018: Daft Punk Phase</h4><p>Random Access Memories changed everything. Realized electronic music isn\\'t cold—it\\'s the most human thing we\\'ve made.</p></div>' +
                '<div class="job" style="border-left: 3px solid var(--accent-color); padding-left: 20px;"><h4 style="color: var(--accent-color); margin-bottom: 8px;">2020—Present: Building for Impact</h4><p>Turned the existential angst into action. If reality is broken, let\\'s fix it.</p></div>';
            
            toggle.addEventListener('click', () => {
                isNerdy = !isNerdy;
                
                if (isNerdy) {
                    // Nerdy mode ON
                    // Desktop
                    if (aboutDiv) aboutDiv.innerHTML = nerdyAboutHTML;
                    if (expColumn) expColumn.innerHTML = '<div class="column" style="grid-column: 1 / -1;"><h3>→ A DIFFERENT TIMELINE</h3>' + nerdyTimelineHTML + '</div>';
                    
                    // Mobile
                    if (mobileAbout) mobileAbout.innerHTML = nerdyAboutHTML;
                    if (mobileExp) mobileExp.innerHTML = nerdyTimelineHTML;
                    if (mobileAcad) mobileAcad.style.display = 'none';
                    
                    toggle.classList.add('active');
                } else {
                    // Nerdy mode OFF - restore
                    // Desktop
                    if (aboutDiv) aboutDiv.innerHTML = origAbout;
                    if (expColumn) expColumn.innerHTML = origExp;
                    
                    // Mobile
                    if (mobileAbout) mobileAbout.innerHTML = origMobileAbout;
                    if (mobileExp) mobileExp.innerHTML = origMobileExp;
                    if (mobileAcad) mobileAcad.style.display = '';
                    
                    toggle.classList.remove('active');
                }
                
                document.getElementById('about').scrollIntoView({ behavior: 'smooth' });
            });
        }

        // Mobile Tabs
        function initMobileTabs() {
            const tabButtons = document.querySelectorAll('.tab-button');
            const tabContents = document.querySelectorAll('.tab-content');
            
            tabButtons.forEach(button => {
                button.addEventListener('click', () => {
                    const targetTab = button.dataset.tab;
                    
                    tabButtons.forEach(btn => btn.classList.remove('active'));
                    tabContents.forEach(content => content.classList.remove('active'));
                    
                    button.classList.add('active');
                    document.getElementById(targetTab).classList.add('active');
                });
            });
        }

        document.addEventListener('DOMContentLoaded', () => {
            initDarkMode();
            initNerdyMode();
            initMobileTabs();
        });
    """)


def create_job_card(job):
    """Create a job card from job data"""
    if "bullets" in job:
        # Job with bullet points
        return Div(
            Div(
                Div(
                    H4(job["company"]),
                    Span(" • ", cls="job-separator"),
                    Span(job["title"], cls="job-title"),
                    cls="job-title-row"
                ),
                P(job["date"], cls="job-date"),
                cls="job-header"
            ),
            Ul(
                *[Li(bullet) for bullet in job["bullets"]],
                cls="job-bullets"
            ),
            cls="job experience-card"
        )
    else:
        # Job with description
        return Div(
            Div(
                Div(
                    H4(job["company"]),
                    Span(" • ", cls="job-separator"),
                    Span(job["title"], cls="job-title"),
                    cls="job-title-row"
                ),
                P(job["date"], cls="job-date"),
                cls="job-header"
            ),
            P(job["description"], cls="job-description"),
            cls="job experience-card"
        )


def create_academia_card(item):
    """Create an academia/community card from item data"""
    return Div(
        Div(
            Div(
                H4(item["title"]),
                P(item["subtitle"], cls="job-title"),
                cls="academia-title-col"
            ),
            P(item["date"], cls="job-date") if item["date"] else None,
            cls="job-header"
        ),
        P(item["description"], cls="job-description"),
        cls="job"
    )


def generate_page(theme_key):
    """Generate a complete HTML page for a theme"""
    
    return Html(
        Head(
            Meta(charset="UTF-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Title("Hernán Barijhoff"),
            create_style(theme_key),
        ),
        Body(
            Div(
                # Header
                Header(
                    # Left: Name box (25%)
                    Div(
                        Div(
                            H1(CONTENT["name"]),
                            P(CONTENT["subtitle"], cls="subtitle"),
                            cls="header-box"
                        ),
                        cls="header-left"
                    ),
                    # Right: Hero content + Toggle (75%)
                    Div(
                        # Hero content (tagline + contact)
                        Div(
                            P(
                                CONTENT["tagline"],
                                Span(CONTENT["tagline_emphasis"], cls="tagline-emphasis"),
                                cls="tagline"
                            ),
                            Div(
                                A(CONTENT["email"], href=f"mailto:{CONTENT['email']}"),
                                A("LinkedIn", href=CONTENT["linkedin_url"], target="_blank"),
                                A("mindappterapia.com", href=CONTENT["website_url"], target="_blank"),
                                cls="contact-links"
                            ),
                            cls="hero-content"
                        ),
                        # Dark mode toggle
                        Div(
                            Span("Dark Mode", cls="toggle-label-top"),
                            Div(cls="toggle-switch", id="darkModeToggle"),
                            cls="toggle-container"
                        ),
                        cls="header-center"
                    ),
                ),
                
                # Main Content
                Main(
                    # Who I Am Section
                    Section(
                        H2(CONTENT["about"]["title"], cls="section-header"),
                        Div(
                            *[P(*format_text(para)) for para in CONTENT["about"]["paragraphs"]],
                            cls="about-content"
                        ),
                        id="about"
                    ),
                    
                    # Experience Section (no section header, just tabs and columns)
                    Section(
                        # Mobile Tabs
                        Div(
                            Div(
                                Button("What I Think", cls="tab-button active", **{"data-tab": "tab-about"}),
                                Button("What I've Built", cls="tab-button", **{"data-tab": "tab-experience"}),
                                Button("Academia & Community", cls="tab-button", **{"data-tab": "tab-academia"}),
                                cls="tab-buttons"
                            ),
                            cls="mobile-tabs"
                        ),
                        
                        Div(
                            # Mobile Tab Content - Who I Am
                            Div(
                                *[P(*format_text(para)) for para in CONTENT["about"]["paragraphs"]],
                                cls="tab-content active about-content",
                                id="tab-about"
                            ),
                            
                            # Mobile Tab Content - Experience
                            Div(
                                *[create_job_card(job) for job in CONTENT["experience"]],
                                cls="tab-content",
                                id="tab-experience"
                            ),
                            
                            # Mobile Tab Content - Academia
                            Div(
                                *[create_academia_card(item) for item in CONTENT["academia"]],
                                cls="tab-content",
                                id="tab-academia"
                            ),
                            
                            # Desktop Two-Column Layout
                            Div(
                                # Left Column - What I've Built
                                Div(
                                    H3("What I've Built"),
                                    *[create_job_card(job) for job in CONTENT["experience"]],
                                    cls="column"
                                ),
                                # Right Column - Academia & Community
                                Div(
                                    H3("Academia & Community"),
                                    *[create_academia_card(item) for item in CONTENT["academia"]],
                                    cls="column"
                                ),
                                cls="two-column",
                                id="experienceContent"
                            ),
                        ),
                        id="experience"
                    ),
                ),
                
                # Footer with toggles
                Footer(
                    P(f"Theme: {THEMES[theme_key]['name']}", style="color: var(--text-secondary); font-size: 14px;"),
                    Div(
                        Div(
                            Span("Nerdy Mode", cls="toggle-label"),
                            Div(cls="toggle-switch", id="nerdyToggle"),
                            style="display: flex; align-items: center; gap: 12px;"
                        ),
                        cls="footer-toggles"
                    ),
                ),
                
                cls="container"
            ),
            create_script()
        )
    )


# Generate all theme pages
if __name__ == "__main__":
    for theme_key in THEMES.keys():
        html_content = to_xml(generate_page(theme_key))
        # Use index.html for slate_blue (main theme for GitHub Pages)
        if theme_key == "slate_blue":
            filename = "index.html"
        else:
            filename = f"design-{theme_key}.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"<!DOCTYPE html>\n{html_content}")
        print(f"✅ Generated {filename}")
        