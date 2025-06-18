import streamlit as st

# Page setup
st.set_page_config(page_title="AI Career Advisor", layout="centered", page_icon="🎯")

# Dark theme
st.markdown("""
    <style>
        body { background-color: #121212; color: #FFFFFF; }
        .stButton>button { background-color: #1f77b4; color: white; }
        .stCheckbox>div>label { color: white; }
        .stMarkdown h2 { color: #FFDD57; }
    </style>
""", unsafe_allow_html=True)

# --- Career Data ---
career_data = {
    "creative": {
        "career": "Creative Artist / Designer",
        "roles": [
            "Artist", "Painter", "Illustrator", "Graphic Designer", "Animator",
            "Interior Designer", "Fashion Designer", "Photographer", "Musician",
            "Writer", "Author", "Dancer", "Actor", "Director", "Makeup Artist"
        ],
        "courses": [
            {"name": "Graphic Design Basics", "link": "https://www.coursera.org/specializations/graphic-design"},
            {"name": "Interior Design Fundamentals", "link": "https://www.udemy.com/course/interior-design-fundamentals/"},
            {"name": "Fashion Design Course", "link": "https://www.skillshare.com/browse/fashion-design"},
            {"name": "Photography Masterclass", "link": "https://www.udemy.com/course/photography-masterclass-complete-guide-to-photography/"},
            {"name": "Creative Writing", "link": "https://www.edx.org/course/how-to-write-a-novel"}
        ]
    },
    "stem": {
        "career": "STEM Professional",
        "roles": [
            "Scientist", "Mathematician", "Astronomer", "Software Developer", "AI Engineer",
            "Cybersecurity Analyst", "Web Developer", "Game Developer", "Aerospace Engineer",
            "Mechanical Engineer", "Civil Engineer", "Electrical Engineer", "Robotics Engineer",
            "Doctor", "Psychologist", "Dentist", "Pharmacist", "Laser Technician", "Veterinarian"
        ],
        "courses": [
            {"name": "AI for Everyone", "link": "https://www.coursera.org/learn/ai-for-everyone"},
            {"name": "Python for Data Science", "link": "https://www.edx.org/course/python-for-data-science"},
            {"name": "Cybersecurity Basics", "link": "https://www.ibm.com/training/path/cybersecurity"},
            {"name": "Intro to Robotics", "link": "https://online.stanford.edu/courses/soe-ycscs0007-robotics"}
        ]
    },
    "business": {
        "career": "Business and Finance Professional",
        "roles": [
            "Entrepreneur", "CEO", "Marketing Manager", "Sales Executive", "Financial Analyst",
            "Investment Banker", "Stock Trader", "Accountant", "Business Analyst"
        ],
        "courses": [
            {"name": "Financial Markets by Yale", "link": "https://www.coursera.org/learn/financial-markets-global"},
            {"name": "Excel for Business", "link": "https://www.coursera.org/specializations/excel"},
            {"name": "Digital Marketing", "link": "https://www.google.com/intl/en_in/digitalgarage/"}
        ]
    },
    "education": {
        "career": "Educator / Researcher",
        "roles": [
            "School Teacher", "Lecturer", "Educational Counselor", "Principal", "Research Scientist", "Librarian"
        ],
        "courses": [
            {"name": "Becoming a Teacher", "link": "https://www.coursera.org/learn/becoming-a-teacher"},
            {"name": "Instructional Design", "link": "https://www.edx.org/learn/instructional-design"}
        ]
    },
    "law": {
        "career": "Law & Public Service Professional",
        "roles": [
            "Lawyer", "Judge", "Police", "Civil Servant", "Politician", "Social Worker"
        ],
        "courses": [
            {"name": "Law for Non-Lawyers", "link": "https://www.edx.org/course/law-for-non-lawyers"},
            {"name": "Social Work Practice", "link": "https://www.coursera.org/specializations/social-work"}
        ]
    }
}

# Import all career descriptions
career_details = {
    # --- Creative & Arts Careers ---
    "Artist": {
        "about": "Artists create visual or performance-based works to express ideas and emotions.",
        "pros": ["Creative freedom", "Emotional expression", "Flexible working hours"],
        "cons": ["Irregular income", "Self-promotion needed", "High competition"]
    },
    "Painter": {
        "about": "Painters use paint to create artwork conveying ideas or emotions.",
        "pros": ["Artistic satisfaction", "Freelance and studio options", "Exhibit opportunities"],
        "cons": ["Art supplies can be expensive", "Difficult to get recognition", "Income not steady"]
    },
    "Illustrator": {
        "about": "Illustrators create drawings to explain, decorate, or narrate ideas.",
        "pros": ["Work in books, games, media", "High creativity", "Freelance options"],
        "cons": ["Client changes", "Deadlines", "Technology learning required"]
    },
    "Graphic Designer": {
        "about": "Designs visuals using digital tools for branding, ads, and media.",
        "pros": ["Widely needed", "Good remote opportunities", "Creative work"],
        "cons": ["Revisions", "Client feedback pressure", "Competitive"]
    },
    "Animator": {
        "about": "Animators make visuals come alive for film, games, or media.",
        "pros": ["Exciting visuals", "Popular industry", "Fun projects"],
        "cons": ["Long hours", "Stressful deadlines", "Needs high skill"]
    },
    "Interior Designer": {
        "about": "Designs aesthetically pleasing and functional interior spaces.",
        "pros": ["High demand", "Creativity with real impact", "Client interaction"],
        "cons": ["Client demands", "Budget limits", "Certifications often needed"]
    },
    "Fashion Designer": {
        "about": "Designs clothing and accessories reflecting style and trends.",
        "pros": ["Trendsetting", "Fame opportunity", "Global industry"],
        "cons": ["Competitive", "Hard to break in", "Unstable income"]
    },
    "Photographer": {
        "about": "Captures visuals for journalism, art, or commercial use.",
        "pros": ["Travel possible", "Freelance flexibility", "Creative fulfillment"],
        "cons": ["Expensive gear", "Unsteady income", "Heavy competition"]
    },
    "Musician": {
        "about": "Creates and performs music solo or with groups.",
        "pros": ["Artistic expression", "Performance thrill", "Growing digital scene"],
        "cons": ["Variable income", "Rehearsal-heavy", "Tough to stand out"]
    },
    "Writer": {
        "about": "Creates written content for books, blogs, ads, and more.",
        "pros": ["Work remotely", "Creative liberty", "Diverse niches"],
        "cons": ["Writer’s block", "Tough publishing scene", "Earnings vary"]
    },
    "Author": {
        "about": "Writes long-form books, fiction or nonfiction.",
        "pros": ["Long-lasting impact", "Full creative control", "Self-publishing options"],
        "cons": ["Time-consuming", "Uncertain sales", "Criticism risk"]
    },
    "Dancer": {
        "about": "Performs choreographed or improvised movements artistically.",
        "pros": ["Fitness benefit", "Live performance thrill", "Cultural representation"],
        "cons": ["Injury risk", "Shorter career span", "High practice needed"]
    },
    "Actor": {
        "about": "Performs in plays, movies, or TV portraying various characters.",
        "pros": ["Fame and glamour", "Role diversity", "Passion-driven"],
        "cons": ["Audition pressure", "Irregular jobs", "Public scrutiny"]
    },
    "Director": {
        "about": "Manages creative vision in film, theatre, or TV.",
        "pros": ["Creative control", "Influence big projects", "Prestige"],
        "cons": ["High responsibility", "Budget pressure", "Tight deadlines"]
    },
    "Makeup Artist": {
        "about": "Applies makeup for events, fashion, film, or clients.",
        "pros": ["Artistic and personal impact", "Events and celebrity work possible", "In demand"],
        "cons": ["Long hours", "Standing a lot", "Client expectations"]
    },

    # --- STEM Careers ---
    "Scientist": {
        "about": "Researches to discover new knowledge and solve problems.",
        "pros": ["Innovation-driven", "Grants and publishing", "Academia or industry"],
        "cons": ["Long education", "Funding issues", "Slow results"]
    },
    "Mathematician": {
        "about": "Solves problems using theoretical and applied mathematics.",
        "pros": ["Foundation for AI, finance, physics", "Academic recognition"],
        "cons": ["Abstract thinking", "Specialized knowledge", "Less public understanding"]
    },
    "Astronomer": {
        "about": "Studies planets, stars, galaxies, and space phenomena.",
        "pros": ["Exciting discoveries", "Research-based", "Space exploration"],
        "cons": ["Few job openings", "Heavy data work", "Requires PhD"]
    },
    "Software Developer": {
        "about": "Builds and maintains applications and systems software.",
        "pros": ["High salary", "Remote jobs", "Tech boom"],
        "cons": ["Long screen hours", "Debugging stress", "Constant updates"]
    },
    "AI Engineer": {
        "about": "Designs and develops artificial intelligence systems.",
        "pros": ["Hot industry", "Exciting challenges", "Well-paid"],
        "cons": ["Advanced math & coding", "Ethical risks", "Fast-changing tech"]
    },
    "Cybersecurity Analyst": {
        "about": "Protects networks and systems from digital threats.",
        "pros": ["Critical demand", "Remote work possible", "High pay"],
        "cons": ["Always learning", "24/7 responsibility", "Stressful attacks"]
    },
    "Web Developer": {
        "about": "Creates websites and web applications for users and clients.",
        "pros": ["Freelance options", "Creative logic", "Startups and corporates"],
        "cons": ["Browser issues", "Client demands", "Debugging pain"]
    },
    "Game Developer": {
        "about": "Designs and builds interactive video games.",
        "pros": ["Fun industry", "Art meets code", "Big global market"],
        "cons": ["Tight deadlines", "Crunch culture", "Low pay entry-level"]
    },
    "Aerospace Engineer": {
        "about": "Designs aircraft, satellites, and space vehicles.",
        "pros": ["High prestige", "Space & defense", "Great pay"],
        "cons": ["Hard to enter", "Long projects", "Team-heavy work"]
    },
    "Doctor": {
        "about": "Diagnoses and treats illnesses in patients.",
        "pros": ["Respectful job", "High income", "Life-saving impact"],
        "cons": ["Long education", "Night shifts", "Emotional stress"]
    },
    "Dentist": {
        "about": "Maintains oral hygiene and treats dental issues.",
        "pros": ["High-paying", "Clinic ownership", "Popular healthcare field"],
        "cons": ["Costly degree", "Manual precision needed", "Patient fear"]
    },
    "Psychologist": {
        "about": "Studies human behavior and mental health.",
        "pros": ["Helping others", "Research or clinical options", "Growing need"],
        "cons": ["Emotional fatigue", "Long study path", "Sensitive issues"]
    },

    # --- Business & Finance Careers ---
    "Entrepreneur": {
        "about": "Starts businesses based on ideas, products, or services.",
        "pros": ["Freedom and impact", "No limit on growth", "Personal pride"],
        "cons": ["Financial risk", "Failure rate", "No work-life balance initially"]
    },
    "CEO": {
        "about": "Heads the organization and makes strategic decisions.",
        "pros": ["Influence", "High income", "Leadership"],
        "cons": ["High pressure", "Hard to reach", "Public accountability"]
    },
    "Marketing Manager": {
        "about": "Plans campaigns to promote brands and increase sales.",
        "pros": ["Creative + strategic", "Data + design blend", "Digital growth"],
        "cons": ["Trend pressure", "Tight deadlines", "ROI expectations"]
    },
    "Sales Executive": {
        "about": "Sells products or services to customers and businesses.",
        "pros": ["Commission", "Networking", "Rapid growth"],
        "cons": ["Rejection", "Targets stress", "Travel often"]
    },
    "Financial Analyst": {
        "about": "Evaluates data to advise on finance and investment.",
        "pros": ["Stable sector", "Corporate or freelance", "High pay"],
        "cons": ["Numbers all day", "Market pressure", "Certifications"]
    },
    "Investment Banker": {
        "about": "Helps companies raise capital and conduct deals.",
        "pros": ["Prestige", "Huge salary", "Financial expertise"],
        "cons": ["Workaholic hours", "Burnout risk", "Cutthroat"]
    },
    "Stock Trader": {
        "about": "Buys and sells stocks to make profits.",
        "pros": ["Exciting", "Self-employed possible", "Lucrative"],
        "cons": ["Risky", "Unstable income", "Addictive"]
    },
    "Accountant": {
        "about": "Manages finances, taxes, and reports for firms or clients.",
        "pros": ["Secure job", "Many roles", "Scalable"],
        "cons": ["Seasonal stress", "Routine work", "Strict compliance"]
    },
    "Business Analyst": {
        "about": "Analyzes business needs and tech solutions.",
        "pros": ["Hybrid skillset", "In every industry", "Process improvement"],
        "cons": ["Jargon-heavy", "Stakeholder friction", "Ambiguous problems"]
    },

    # --- Education & Research Careers ---
    "School Teacher": {
        "about": "Educates children in schools in different subjects.",
        "pros": ["Impactful", "Holidays", "Respectful"],
        "cons": ["Admin load", "Discipline issues", "Underpaid sometimes"]
    },
    "Lecturer": {
        "about": "Teaches in universities and often conducts research.",
        "pros": ["Academic role", "Publish research", "Mentor students"],
        "cons": ["PhD often needed", "High workload", "Promotion slow"]
    },
    "Educational Counselor": {
        "about": "Guides students in career or academic decisions.",
        "pros": ["Helpful role", "Good demand", "School & college jobs"],
        "cons": ["Emotional issues", "Conflict resolution", "Credential needed"]
    },
    "Principal": {
        "about": "Leads a school and manages faculty and students.",
        "pros": ["Leadership", "Education reform impact", "Respected"],
        "cons": ["Heavy pressure", "Accountability", "Stakeholder conflict"]
    },
    "Research Scientist": {
        "about": "Performs research to develop knowledge and innovations.",
        "pros": ["Discovery", "Science advancement", "Cross-disciplinary"],
        "cons": ["Grants chasing", "Slow process", "Not always commercial"]
    },
    "Librarian": {
        "about": "Maintains books and resources, helps people find info.",
        "pros": ["Quiet job", "Academic or public options", "Information access"],
        "cons": ["Tech upgrades", "Limited roles", "Low pay in some areas"]
    },

    # --- Law, Government, and Public Service ---
    "Lawyer": {
        "about": "Advises or defends people in legal matters.",
        "pros": ["High respect", "Good income", "Variety of fields"],
        "cons": ["Stressful", "Time-intensive", "Law school needed"]
    },
    "Judge": {
        "about": "Presides over legal proceedings and ensures fair outcomes.",
        "pros": ["Authority", "Legal respect", "Stable"],
        "cons": ["Heavy decisions", "Years of experience needed", "Less flexible"]
    },
    "Police": {
        "about": "Enforces laws, investigates crimes, and maintains order.",
        "pros": ["Public servant", "Exciting at times", "Pension benefits"],
        "cons": ["Dangerous", "High stress", "Shifts"]
    },
    "Civil Servant": {
        "about": "Works for the government in administrative or policy roles.",
        "pros": ["Job security", "Country-building", "Respect"],
        "cons": ["Bureaucracy", "Promotion delays", "Exam needed"]
    },
    "Politician": {
        "about": "Represents people and creates policy in government.",
        "pros": ["Leadership", "Make change", "Powerful"],
        "cons": ["Public criticism", "Campaign pressure", "Job uncertainty"]
    },
    "Social Worker": {
        "about": "Supports vulnerable individuals or families in need.",
        "pros": ["Emotional impact", "Helping others", "Many roles"],
        "cons": ["Burnout risk", "Exposure to trauma", "Tough caseload"]
    }
}


# --- Input Section ---
st.title("🎓 Welcome to CareerPath AI")
name = st.text_input("👤 Enter your name:")
st.write("Tell us your interests:")

# --- Interest Options ---
interests = []
if st.checkbox("🎨 Creative Arts"): interests.append("creative")
if st.checkbox("🔬 STEM"): interests.append("stem")
if st.checkbox("💼 Business & Finance"): interests.append("business")
if st.checkbox("📚 Education & Research"): interests.append("education")
if st.checkbox("⚖️ Law & Public Service"): interests.append("law")

# --- Suggest Career Options ---
suggested_roles = []
if "career_suggested" not in st.session_state:
    st.session_state["career_suggested"] = False
    
if st.button("🚀 Suggest Careers"):
    if name and interests:
        st.session_state["career_suggested"] = True
    else:
        st.error("Please enter your name to continue.")
        st.stop()

if st.session_state["career_suggested"]:
    st.markdown(f"### 👋 Hi **{name}**, based on your interests here are some career options:")
    for interest in interests:
        data = career_data.get(interest)
        if data:
            st.markdown(f"#### 🔹 {data['career']}")
            st.write("**Possible Roles:**")
            for role in data["roles"]:
                st.markdown(f"- {role}")
                suggested_roles.append(role)
            st.write("**Courses to Explore:**")
            for course in data["courses"]:
                st.markdown(f"- [{course['name']}]({course['link']})")

    # --- Let user select one career to explore ---
    selected_career = st.selectbox("🔍 Select a career to learn more:", sorted(set(suggested_roles)))

    # --- Show Details if available ---
    if selected_career in career_details:
        details = career_details[selected_career]
        st.markdown(f"### 📌 About **{selected_career}**")
        st.write(details["about"])

        st.markdown("✅ **Why you should choose it:**")
        for point in details["pros"]:
            st.markdown(f"- {point}")

        st.markdown("❌ **Why you might not:**")
        for point in details["cons"]:
            st.markdown(f"- {point}")
    else:
        st.warning("We don’t have detailed info for this role yet. Coming soon!")


# --- Footer ---
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit | Project by Madiha")
st.markdown("📎 Connect on [LinkedIn](https://www.linkedin.com/in/madihanaz/") 
st.markdown("📎Connect on [GitHub](https://github.com/madiha3106)")
