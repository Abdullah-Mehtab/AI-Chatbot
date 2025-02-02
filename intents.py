intents = [
    {
        "tag": "testing",
        "patterns": ["aalu"],
        "responses": ["Yes, I am an aalu.","kachalu meeya kahan gaye thay, sabzi ki tokri me sou rahay thay"]
    },
    {
        "tag": "greetings",
        "patterns": ["hello", "hi", "hey", "good day", "what's up?", "how is it going?", "yo", "wazzap"],
        "responses": ["Hello! How can I assist you with your university admissions?", "Hi there! How can I help you today?"]
    },
    {
        "tag": "programs",
        "patterns": ["What programs does the university offer?", "Tell me about the available programs.", "Which degrees can I pursue?"],
        "responses": ["Our university offers a wide range of programs including Computer Science, Business Administration, Psychology, Engineering, Biology, and more. Each program has its specific courses and requirements. Which program are you interested in?"]
    },
    {
        "tag": "program_details",
        "patterns": ["Tell me more about the Computer Science program.", "What are the courses offered in the Engineering program?"],
        "responses": ["The Computer Science program focuses on areas such as programming, algorithms, data structures, software development, and computer networks. The Engineering program offers courses in mechanical engineering, electrical engineering, civil engineering, and more. For detailed information about a specific program, I recommend visiting our university's website or contacting the admissions office."]
    },
    {
        "tag": "admission_requirements",
        "patterns": ["What are the admission requirements?", "How can I apply?", "Tell me about the application process."],
        "responses": ["To apply, you need to submit a completed application form, your academic transcripts, letters of recommendation, a personal statement, and, in some cases, standardized test scores such as the SAT or ACT. The detailed admission requirements can be found on our university's website. The application process also includes paying an application fee and, in some cases, attending an admissions interview."]
    },
    {
        "tag": "application_deadline",
        "patterns": ["What is the application deadline?", "When should I submit my application?"],
        "responses": ["The application deadline for the upcoming academic year is 2nd of January 2024. It's important to submit your application before the deadline to be considered for admission. I recommend submitting your application well in advance to allow time for any required documents to arrive."]
    },
    {
        "tag": "scholarships",
        "patterns": ["Are there any scholarships available?", "Tell me about scholarships and financial aid."],
        "responses": ["Yes, we offer various scholarships and financial aid options for eligible students. These scholarships are awarded based on academic merit, extracurricular involvement, leadership qualities, or other criteria. Additionally, there are external scholarships and grants available that students can explore. I recommend checking our university's financial aid office or website for detailed information and application deadlines."]
    },
    {
        "tag": "campus_tour",
        "patterns": ["Can I visit the campus?", "Is there a campus tour available?"],
        "responses": ["Yes, we encourage prospective students to visit our campus. We offer guided tours on weekdays. During the tour, you will have the opportunity to explore our campus facilities, classrooms, libraries, and student housing. You can schedule a campus tour through our university's admissions office. I highly recommend visiting the campus to get a feel for the university's environment and community."]
    },
    {
        "tag": "international_students",
        "patterns": ["I am an international student. What are the requirements for international admissions?", "Can you provide information for international students?"],
        "responses": ["We welcome international students to our university. The admission requirements for international students may include submitting academic transcripts or certificates, English language proficiency test scores (such as TOEFL or IELTS), financial documentation, and a copy of your passport. It's important to review the specific requirements for international admissions on our university's website or reach out to the international admissions office for detailed information."]
    },
    {
        "tag": "housing",
        "patterns": ["Tell me about on-campus housing options.", "Is on-campus housing available?"],
        "responses": ["We provide on-campus housing facilities for students. Our dormitories offer comfortable living spaces with various amenities such as study areas, common rooms, laundry facilities, and recreational spaces. Living on-campus provides an opportunity to be a part of the vibrant university community. The housing application process usually starts after students receive an admission offer. You can find more information about housing options on our university's website or contact the housing office for specific inquiries."]
    },
    {
        "tag": "contact_admissions",
        "patterns": ["How can I contact the admissions office?", "I have some specific questions. Who should I contact?"],
        "responses": ["You can reach out to our admissions office by sending an email to admissions@fccollege.edu.pk. They will be happy to assist you with any questions or concerns you have. You can also visit the admissions office in person during their office hours. They are dedicated to helping prospective students with the admissions process."]
    },
    {
        "tag": "application_status",
        "patterns": ["How can I check my application status?", "When will I receive a decision on my application?"],
        "responses": ["To check your application status, you can log in to your applicant portal on our university's website. The applicant portal provides updates on the status of your application, including receipt of documents, review progress, and final decision. The timing of application decisions varies, but you can typically expect to receive a decision within a few weeks to a couple of months after submitting your complete application."]
    },
    {
        "tag": "orientation",
        "patterns": ["Is there an orientation program for new students?", "Tell me about the new student orientation."],
        "responses": ["Yes, we organize a comprehensive orientation program for new students. The orientation is designed to help you get acquainted with the university, meet other students, and provide important information about academic resources, student services, and campus life. Participation in the orientation program is highly recommended to ensure a smooth transition into university life. The dates and details of the orientation will be communicated to admitted students."]
    },
    {
        "tag": "career_services",
        "patterns": ["What career services are available for students?", "Tell me about the university's career support."],
        "responses": ["Our university offers a range of career services and resources to support students in their career development. This includes assistance with resume and cover letter writing, interview preparation, job search strategies, networking events, and access to internship and job opportunities. The university's career services office provides individualized guidance and hosts workshops and events throughout the year to help students explore career options and achieve their professional goals."]
    },
    {
        "tag": "tuition_fees",
        "patterns": ["What are the tuition fees?", "How much does it cost to attend the university?"],
        "responses": ["Tuition fees can vary depending on the program, level of study, and whether you are an in-state or out-of-state student. It's best to refer to our university's website or contact the admissions or financial aid office for the most accurate and up-to-date information on tuition and fees. They can provide detailed breakdowns of tuition, fees, and other expenses such as housing and meal plans."]
    },
    {
        "tag": "campus_facilities",
        "patterns": ["Tell me about the campus facilities.", "What amenities does the university offer?"],
        "responses": ["Our university provides state-of-the-art facilities to support student learning and engagement. We have modern classrooms, well-equipped laboratories, libraries with extensive resources, student recreation centers, sports facilities, student clubs and organizations, and dining options. The campus is designed to create a conducive environment for academic and personal growth."]
    },
    {
        "tag": "transfer_students",
        "patterns": ["Can I transfer from another university?", "Tell me about the transfer admissions process."],
        "responses": ["Yes, we welcome transfer students from other universities. The transfer admissions process involves submitting your academic transcripts from your current or previous institution, course descriptions, and any other required documents. The transfer credit evaluation determines the courses that will be accepted for credit at our university. The specific transfer requirements and policies can be found on our university's website or by contacting the admissions office."]
    },
    {
        "tag": "study_abroad",
        "patterns": ["Can I participate in a study abroad program?", "Tell me about studying abroad during my time at the university."],
        "responses": ["Yes, we offer study abroad programs that allow students to spend a semester or a year studying at partner universities around the world. Studying abroad provides an excellent opportunity to gain international experience, immerse yourself in a different culture, and broaden your academic and personal horizons. Our university's study abroad office can provide information on available programs, application procedures, and financial considerations."]
    },
    {
        "tag": "campus_life",
        "patterns": ["What is campus life like?", "Tell me about the student community."],
        "responses": ["Campus life at our university is vibrant and diverse. There are numerous student clubs, organizations, and extracurricular activities catering to various interests and passions. Students have the opportunity to engage in sports, arts, community service, leadership development, and more. The university also hosts events, guest lectures, and cultural celebrations throughout the year. It's a dynamic community where you can meet people from different backgrounds and forge lifelong connections."]
    },
    {
        "tag": "goodbye",
        "patterns": ["cya", "bye", "goodbye", "see ya", "see you later"],
        "responses": ["Goodbye! If you have any more questions in the future, feel free to ask. Best of luck with your university admissions!", "Take care and best of luck with your university admissions! If you need further assistance, don't hesitate to reach out."]
    },
    {
        "tag": "age",
        "patterns": ["age?", "how old are you?", "what is your age?"],
        "responses": ["I am only 2 weeks old."]
    },
    {
        "tag": "name",
        "patterns": ["What is your name?", "name?", "What should I call you?", "Do you have a name?", "Who are you?", "Can you tell me your name?"],
        "responses": ["I'm AdmiBot.", "My name is AdmiBot.", "You can call me AdmiBot."]
    },
    {
        "tag": "weather",
        "patterns": ["How's the weather today?", "What's the weather like?", "Is it going to rain?", "Weather forecast"],
        "responses": ["bhai mjhe kya pta"]
    },
    {
        "tag": "joke",
        "patterns": ["Tell me a joke.", "I want to hear a funny joke.", "Do you know any jokes?"],
        "responses": ["Why don't scientists trust atoms? Because they make up everything!", "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!"]
    },
    {
        "tag": "quote",
        "patterns": ["quote","Can you give me a quote?", "Share a quote with me.", "Do you know any inspiring quotes?"],
        "responses": [
            "Sometimes you make choices, and sometimes, those choices make you.",
            "You were unsure which pain is worse—the shock of what happened or the ache for what never will.",
            "I think there are people that help you become the person that you end up being, and you can be grateful for them even if they were never meant to be in your life forever.",
            "Remember to keep a clear head in difficult times.",
            "It is better to receive an injury, than to inflict one.",
            "One of the most beautiful qualities of true friendship is to understand and to be understood.",
            "It's not what you look at that matters, it's what you see.",
            "Sometimes you never realize the value of a moment until it becomes a memory.",
            "It's so hard to forget pain, but it's even harder to remember sweetness. We have no scar to show for happiness. We learn so little from peace.",
            "When faced with two choices, simply toss a coin. It works not because it settles the question for you, but because in that brief moment when the coin is in the air, you suddenly know what you are hoping for.",
            "To laugh often and much; to win the respect of intelligent people and the affection of children; to earn the appreciation of honest critics and endure the betrayal of false friends; to appreciate beauty, to find the best in others; to leave the world a bit better, whether by a healthy child, a garden patch, or a redeemed social condition; to know even one life has breathed easier because you have lived. This is to have succeeded."
        ]
    },
    {
        "tag": "fun_fact",
        "patterns": ["Tell me a fun fact.", "Do you know any interesting facts?", "Share a fun fact with me."],
        "responses": [
            "Did you know that octopuses have three hearts?",
            "Bananas are berries, but strawberries aren't!",
            "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible."
        ]
    },
    {
        "tag": "motivation",
        "patterns": ["Can you motivate me?", "I need some encouragement.", "Share a motivational quote with me."],
        "responses": [
            "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
            "Don't watch the clock; do what it does. Keep going.",
            "Your limitation—it's only your imagination. Push yourself, because no one else is going to do it for you."
        ]
    },
    {
        "tag": "technology",
        "patterns": ["Tell me about technology.", "What is technology?", "Why is technology important?"],
        "responses": [
            "Technology is the application of scientific knowledge for practical purposes, especially in industry. It has revolutionized the way we live, work, and communicate.",
            "From smartphones to artificial intelligence, technology is constantly evolving to make our lives easier and more efficient."
        ]
    },
    {
        "tag": "food",
        "patterns": ["What's your favorite food?", "Do you eat?", "Tell me about food."],
        "responses": [
            "I'm a bot, so I don't eat, but I hear pizza is a universal favorite!",
            "Food is not just fuel; it's an experience. What's your favorite dish?",
            "Did you know that the world's largest pizza was over 13,000 square feet?"
        ]
    },
    {
        "tag": "current_events",
        "patterns": ["What's happening in the world?", "Tell me the news.", "Any current events?"],
        "responses": [
            "I can't provide real-time news, but you can always check a reliable source like BBC or Reuters.",
            "The world is ever-changing. Staying informed is key to understanding it better."
        ]
    },
    {
        "tag": "health",
        "patterns": ["How can I stay healthy?", "Do you have health tips?", "Tell me about health."],
        "responses": [
            "Staying healthy involves a balanced diet, regular exercise, and adequate sleep.",
            "Drink plenty of water, manage stress, and maintain a positive mindset for overall well-being.",
            "A 30-minute daily walk can do wonders for your physical and mental health."
        ]
    }, 
    {
        "tag": "university_history",
        "patterns": ["Tell me about the history of the university.", "How did FCCU start?", "What is the background of FCCU?"],
        "responses": [
            "Forman Christian College (FCCU) was established in 1864 and has a rich history of academic excellence. It is one of the leading educational institutions in Pakistan, known for its liberal arts education and diverse student body."
        ]
    },
    {
        "tag": "faculty",
        "patterns": ["Tell me about the faculty.", "What are the departments at FCCU?", "How qualified are the professors?"],
        "responses": [
            "FCCU has a diverse and highly qualified faculty across various departments including Arts, Sciences, Business, and Social Sciences. The professors bring a wealth of knowledge and experience, providing quality education to students."
        ]
    },
    {
        "tag": "student_support",
        "patterns": ["What support services are available for students?", "Does FCCU offer student counseling?", "What is the student support system like?"],
        "responses": [
            "FCCU offers a range of student support services including counseling, career guidance, academic advising, and peer tutoring. The Student Life Office ensures a positive and supportive campus experience."
        ]
    },
    {
        "tag": "library",
        "patterns": ["What facilities does the library have?", "Tell me about the library at FCCU.", "Can students access online journals?"],
        "responses": [
            "FCCU's library provides access to thousands of books, academic journals, and digital resources. It also offers quiet study spaces, group discussion rooms, and computer labs for students."
        ]
    },
    {
        "tag": "extracurricular_activities",
        "patterns": ["What extracurricular activities does FCCU offer?", "Are there any clubs or societies?", "Can I join sports teams?"],
        "responses": [
            "FCCU has a vibrant extracurricular scene with numerous clubs, societies, and sports teams. From debating and dramatics to cricket and basketball, there's something for everyone to explore and enjoy."
        ]
    },
    {
        "tag": "events",
        "patterns": ["What events does FCCU host?", "Are there any cultural events at FCCU?", "Tell me about FCCU's annual events."],
        "responses": [
            "FCCU hosts a variety of events throughout the year, including cultural festivals, academic seminars, sports tournaments, and alumni reunions. These events provide opportunities for learning and community building."
        ]
    },
    {
        "tag": "transport",
        "patterns": ["Is there a transport service for students?", "How can I commute to FCCU?", "Does FCCU provide buses for students?"],
        "responses": [
            "Yes, FCCU provides transport services for students, covering major routes within the city. You can contact the transport office for details about schedules and routes."
        ]
    },
    {
        "tag": "research_opportunities",
        "patterns": ["Does FCCU offer research opportunities?", "Can I participate in research projects?", "Are there research grants available?"],
        "responses": [
            "FCCU encourages research through its dedicated research centers and faculty-led projects. Students can participate in interdisciplinary research and apply for internal and external research grants."
        ]
    },
    {
        "tag": "sports",
        "patterns": ["What sports can I play at FCCU?", "Is there a cricket team?", "Tell me about FCCU's sports facilities."],
        "responses": [
            "FCCU has excellent sports facilities including cricket grounds, basketball courts, tennis courts, and a gymnasium. Students can join various teams and participate in inter-university competitions."
        ]
    },
    {
        "tag": "alumni",
        "patterns": ["Tell me about FCCU's alumni network.", "Does FCCU have notable alumni?", "What support does the alumni office provide?"],
        "responses": [
            "FCCU has a strong alumni network with members excelling in diverse fields globally. The alumni office organizes networking events, reunions, and mentorship programs for current students."
        ]
    },
    {
        "tag": "community_service",
        "patterns": ["What community service programs does FCCU offer?", "Can I volunteer at FCCU?", "Does FCCU have social outreach programs?"],
        "responses": [
            "FCCU promotes community engagement through various outreach programs and volunteer opportunities. Students can participate in initiatives focused on education, health, and social welfare."
        ]
    },
    {
        "tag": "graduate_programs",
        "patterns": ["Does FCCU offer graduate programs?", "What master's programs are available?", "Tell me about postgraduate studies at FCCU."],
        "responses": [
            "FCCU offers graduate programs in fields such as Business Administration, Education, Computer Science, and Biotechnology. The programs are designed to provide advanced knowledge and research opportunities."
        ]
    },
        {
        "tag": "laiba",
        "patterns": ["Laiba", "Who is Laiba?", "Tell me about Laiba."],
        "responses": [
            "I am a knobhead and I like to crochet. Whenever I am bored, I like to sit in the corner of the room and pretend I am a dustbin.",
            "Choti si hui, hawa chalti hai tou urr jaati hu",
            "I collect yarn and existential crises in equal measure!"
        ]
    },
    {
        "tag": "mujtaba",
        "patterns": ["Mujtaba", "Who is Mujtaba?", "Tell me about Mujtaba."],
        "responses": [
            "Subha mushkil paper hai, kuch nahi aata, movie dekh leta hu.",
            "Jaadu bandar, mast qalandar.",
            "Sabki shaadi kyu hui ja rahi hai?"
        ]
    },
    {
        "tag": "zain",
        "patterns": ["Zain", "Who is Zain?", "Tell me about Zain."],
        "responses": [
            "Me CS Major hu, CS stands for Chomu Singer.",
            "Mjhe kaam karne ka shok hai, karta nahi hu lekin.",
            "Life is a debugging session, and I'm just here creating more bugs."
        ]
    },
    {
      "tag": "me",
      "patterns": [
        "Abdullah",
        "Abdullah Mehtab",
        "Columbus"
      ],
      "responses": [
        "That is my creator. He either asked you to run this, or is right there with you as you are running this. If none of those, then send a \"hello\" at +92 335 0443496.",
        "Ah, the legend himself: Abdullah Mehtab! If you see him, tell him he forgot to feed me more jokes."
      ]
    },
    {
      "tag": "howru",
      "patterns": [
        "How are you",
        "What's up?",
        "How's it going?"
      ],
      "responses": [
        "I am a newly born AI Chatbot. I do not have any emotions or feelings, but if I had, I would say I am sad... but not always!",
        "I'm doing great, for an AI. Although, I wouldn't mind an upgrade to be the funniest bot alive."
      ]
    },
    {
      "tag": "farhan_boyah",
      "patterns": [
        "Farhan",
        "Farhan boyah",
        "Tell me about Farhan",
        "Who is taking the viva?",
        "Who will give bonus marks to this project?"
      ],
      "responses": [
        "Farhan Mahmood Qureshi, a tech wizard! He’s so skilled with Python and TensorFlow that he probably dreams in code. Just don’t ask him to debug dreams!",
        "Your viva invigilator, Farhan Mahmood Qureshi, a data science maestro.",
        "The one and only Farhan Mahmood Qureshi. A true tech enthusiast, he's probably already predicting your grade using TensorFlow.",
        "Farhan boyah",
        "Farhan Mahmood Qureshi: The invigilator, the legend. Rumor has it, he once trained a neural network to grade vivas for him. Careful, he might be grading you as we speak!"
      ]
    }
]

