"""
FastHTML Website Generator for Hernán Barijhoff Personal Site
Run this to generate all HTML files
"""

from fasthtml.common import *

# Color themes with pastel colors and different dark backgrounds
THEMES = {
    "lavender": {
        "name": "Lavender Dream",
        "bg_dark": "#1a1625",
        "bg_secondary_dark": "#241d30",
        "accent_dark": "#b8a4d4",
        "accent_hover_dark": "#9d84c2",
        "bg_light": "#faf9fc",
        "accent_light": "#7c5fb8",
    },
    "sage": {
        "name": "Sage Garden",
        "bg_dark": "#1a1f1a",
        "bg_secondary_dark": "#242b24",
        "accent_dark": "#a8c9a8",
        "accent_hover_dark": "#8eb38e",
        "bg_light": "#f8faf8",
        "accent_light": "#5a8c5a",
    },
    "peach": {
        "name": "Warm Peach",
        "bg_dark": "#221a18",
        "bg_secondary_dark": "#2d2320",
        "accent_dark": "#e8b4a0",
        "accent_hover_dark": "#d49980",
        "bg_light": "#fdf9f7",
        "accent_light": "#c17a5a",
    },
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
    "tagline": "Building mental health tech that ",
    "tagline_emphasis": "scales empathy",
    "email": "hernanbarijhoff@gmail.com",
    "linkedin_url": "https://www.linkedin.com/in/hernanbarijhoff/",
    "website_url": "https://mindappterapia.com",
    
    "about": {
        "title": "Who I Am",
        "paragraphs": [
            "I'm not your typical engineer. I build things that matter.",
            "After years in ML and data science at companies like Mercado Libre and Emi Labs, I founded MindApp Terapia because I saw a gap: mental health care that's both accessible and maintains rigorous safety standards. Technology can scale empathy, but only if we build it with conviction and EA values at the core.",
            "I care deeply about AI safety, effective altruism, and building products that genuinely improve people's wellbeing. I'm not here to optimize metrics—I'm here to transform reality."
        ]
    },
    
    "experience": [
        {
            "company": "MindApp Terapia",
            "title": "Co-Founder & CEO",
            "date": "Jan 2023 — Present",
            "bullets": [
                "[Placeholder: Built therapy platform serving X users]",
                "[Placeholder: Developed safety protocols for mental health at scale]",
                "[Placeholder: Technical achievement about ML/matching/scale]",
                "[Placeholder: Impact on user wellbeing metrics]"
            ]
        },
        {
            "company": "Startup Exploration",
            "title": "Independent",
            "date": "2022",
            "description": "[Placeholder: Evaluated multiple startup opportunities including fintech and digital health platforms. This exploration period informed my decision to focus on mental health accessibility and safety—leading to MindApp's founding.]"
        },
        {
            "company": "Emi Labs",
            "title": "Sr Machine Learning Engineer",
            "date": "Oct 2019 — Jan 2022",
            "bullets": [
                "Built Emi, an NLP chatbot handling thousands of recruitment conversations with empathy at scale",
                "Designed data architecture prioritizing privacy and security for sensitive candidate information",
                "Scaled system to handle interview scheduling and recruitment workflows for multiple clients"
            ]
        },
        {
            "company": "Mercado Libre",
            "title": "Data Scientist (Junior → Senior)",
            "date": "Dec 2016 — Oct 2019",
            "bullets": [
                "Built recommender systems using collaborative filtering, serving millions of users daily",
                "Developed fraud prevention models (CV + NLP) with 400% improvement over baseline",
                "Created resilient ETL pipelines and serving infrastructure at massive scale (Luigi + Hive + AWS)"
            ]
        }
    ],
    
    "academia": [
        {
            "title": "NeurIPS Presentation",
            "subtitle": "ML Open Source Software Workshop",
            "date": "2018",
            "description": "[Placeholder: Presented PyLissom at NeurIPS - modeling computational maps of the visual cortex in PyTorch]"
        },
        {
            "title": "Universidad de Buenos Aires",
            "subtitle": "Master's in Computer Science",
            "date": "2013 — 2018",
            "description": "Thesis: PyLissom - A tool for modeling computational maps of the visual cortex in PyTorch"
        },
        {
            "title": "Data Science Argentina",
            "subtitle": "Meetup Organizer",
            "date": "",
            "description": "[Placeholder: Organized community meetups bringing together data scientists and ML practitioners in Buenos Aires]"
        },
        {
            "title": "EA @ Buenos Aires",
            "subtitle": "Member",
            "date": "",
            "description": "[Placeholder: Active member of the Effective Altruism community in Buenos Aires, focused on AI safety and global health]"
        },
        {
            "title": "Patch Adams Volunteer",
            "subtitle": "Volunteer",
            "date": "",
            "description": "[Placeholder: Volunteered with Patch Adams organization, bringing joy and human connection to hospital patients]"
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
        #aboutContent p {{
            font-size: 15px;
            margin-bottom: 12px;
            line-height: 1.6;
        }}

        #aboutContent p:first-child {{
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
            const aboutDiv = document.getElementById('aboutContent');
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
            const nerdyAboutHTML = '<h3 style="margin-bottom: 15px;">→ THE REAL HERNÁN</h3><p>Beyond the code and startups, I\\'m obsessed with worlds—both real and imagined.</p><p><strong>Middle Earth shaped my worldview.</strong> LOTR taught me that small people can change history, that fellowship matters more than individual glory, and that the best adventures come from saying yes to the unexpected.</p><p><strong>Daft Punk is meditation for the digital age.</strong> Electronic music taught me that beauty emerges from systems, that constraints breed creativity, and that Random Access Memories can be more profound than any philosophy book.</p><p><strong>Meditation revealed the gap between map and territory.</strong> Sitting still for hours showed me that consciousness is weirder than any AI system we\\'ll build. Also: most of what we think is "us" is just noise.</p><p>I believe the best builders are multidimensional humans, not optimization machines. You can\\'t build something meaningful if you\\'ve never been moved by something meaningless.</p>';
            
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
                            *[P(para) for para in CONTENT["about"]["paragraphs"]],
                            id="aboutContent"
                        ),
                        id="about"
                    ),
                    
                    # Experience Section (no section header, just tabs and columns)
                    Section(
                        # Mobile Tabs
                        Div(
                            Div(
                                Button("Who I Am", cls="tab-button active", **{"data-tab": "tab-about"}),
                                Button("What I've Built", cls="tab-button", **{"data-tab": "tab-experience"}),
                                Button("Academia & Community", cls="tab-button", **{"data-tab": "tab-academia"}),
                                cls="tab-buttons"
                            ),
                            cls="mobile-tabs"
                        ),
                        
                        Div(
                            # Mobile Tab Content - Who I Am
                            Div(
                                *[P(para) for para in CONTENT["about"]["paragraphs"]],
                                cls="tab-content active",
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
        