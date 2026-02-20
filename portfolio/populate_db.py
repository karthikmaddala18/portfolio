import os
import django
from datetime import date

def populate_data():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
    from django.apps import apps
    if not apps.ready:
        django.setup()

    from projects_app.models import Project, Certification
    projects_data = [
        {
            'title': 'Smart Parking Management System',
            'description': 'An ML-driven system that detects parking slot availability and predicts occupancy using real-time sensor data. Built with Python and Scikit-learn for high-accuracy detection, featuring a live interactive Streamlit dashboard.',
            'technology': 'Python, ML, Computer Vision, Streamlit',
            'github_link': 'https://github.com/karthikmaddala18/Smark-Parking-Management-System',
            'live_demo_link': '',
            'image_url': 'img/smart_parking.png'
        },
        {
            'title': 'An AI-Powered Diet Assistant',
            'description': 'An intelligent diet guidance system featuring an AI chatbot, BMI analyzer, and dynamic meal planner. Engineered with an optimized Python backend to deliver personalized health support through a seamless UI.',
            'technology': 'Python, AI Tools, UI Design',
            'github_link': 'https://github.com/karthikmaddala18/BLOGGING-PLATFORM-FOR-TRAVEL-ENTHUSIASTS',
            'live_demo_link': '',
            'image_url': 'img/diet_assistant.png'
        },
        {
            'title': 'Memory Management Simulator',
            'description': 'A Python-based simulator visualizing OS paging (FIFO, LRU) and segmentation techniques. Features Matplotlib-driven visualizations allowing users to test and compare the performance of different memory replacement algorithms.',
            'technology': 'Python, Matplotlib',
            'github_link': 'https://github.com/karthikmaddala18/Memory-Management-Simulator-',
            'live_demo_link': '',
            'image_url': 'img/memory_simulator.png'
        }
    ]

    print("Populating the database with Karthikeya's CV projects...")
    
    Project.objects.all().delete()
    
    added_count = 0
    for data in reversed(projects_data):
        project, created = Project.objects.get_or_create(
            title=data['title'],
            defaults={
                'description': data['description'],
                'tech_stack': data['technology'],
                'github_link': data['github_link'],
                'live_demo_link': data['live_demo_link'],
                'image_url': data['image_url']
            }
        )
        if created:
            print(f"Added project: {project.title}")
            added_count += 1
        else:
            print(f"Project already exists: {project.title}")
            
    print(f"Successfully added {added_count} projects!")

    certifications_data = [
        {
            'title': 'Mental Health Simulator | Java, Core-DSA',
            'issuer': 'Cipher Schools | GitHub (Jun ’25 – Jul ’25)',
            'description': 'Developed a console-based “Mental Health Stimulator” in Java using Core DSA. Implemented mood tracking, negative-thought management, and positive affirmations using HashMaps, Stacks, and Queues for an interactive mental-wellbeing companion.',
            'date_earned': date(2025, 7, 1),
            'github_link': 'https://github.com/karthikmaddala18/Mental-Health-Stimulator',
            'certificate_link': ''
        },
        {
            'title': 'ChatGPT-4 Prompt Engineering: ChatGPT, Generative AI & LLM',
            'issuer': 'Infosys | Springboard | Certificate Aug ’25',
            'description': '',
            'date_earned': date(2025, 8, 1),
            'github_link': '',
            'certificate_link': 'http://drive.google.com/file/d/1Q4KVTvtFzHPXPvclImuWWfmZkYLGiPr0/view'
        },
        {
            'title': 'Artificial Intelligence with Python',
            'issuer': 'Coincent | Certificate Jan ’25',
            'description': '',
            'date_earned': date(2025, 1, 1),
            'github_link': '',
            'certificate_link': 'https://drive.google.com/file/d/1Kj6UQ1nLxYfpmox85h0h013jEaa0CmTx/view'
        },
        {
            'title': 'Python Programming',
            'issuer': 'CSE Pathshala | Certificate Mar ‘24',
            'description': '',
            'date_earned': date(2024, 3, 1),
            'github_link': '',
            'certificate_link': 'https://drive.google.com/file/d/16CgF9YS5FxlptqOkq5QhmW2QAEORzR70/view'
        }
    ]

    print("Populating the database with Karthikeya's Trainings and Certifications...")
    Certification.objects.all().delete()
    
    added_certs = 0
    for data in certifications_data:
        cert, created = Certification.objects.get_or_create(
            title=data['title'],
            defaults={
                'issuer': data['issuer'],
                'description': data['description'],
                'date_earned': data['date_earned'],
                'github_link': data.get('github_link', ''),
                'certificate_link': data.get('certificate_link', '')
            }
        )
        if created:
            print(f"Added certification: {cert.title}")
            added_certs += 1
        else:
            print(f"Certification already exists: {cert.title}")
            
    print(f"Successfully added {added_certs} certifications!")

if __name__ == '__main__':
    populate_data()
