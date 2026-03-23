import os
import django
import sys
from django.core.files import File

# Setup Django environment
sys.path.append('d:/linq-corporate-website/Backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'linq_backend.settings')
django.setup()

from content_api.models import CareerGrowthMember, MemberExperience

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_IMAGES_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'src', 'images'))

def get_local_file(relative_path):
    # Map frontend style paths to actual filesystem paths
    clean_path = relative_path.replace('../images/', '')
    src_path = os.path.join(FRONTEND_IMAGES_DIR, clean_path)
    
    if os.path.exists(src_path):
        return File(open(src_path, 'rb'), name=os.path.basename(src_path))
    else:
        print(f"File not found: {src_path}")
        return None

TEAM_MEMBERS_DATA = [
    {
        "role": "Team Manager",
        "name": "Sam Razura",
        "description": "Visionary leader with a focus on strategic planning and operational excellence.",
        "detailed_description": "Sam is a visionary leader with over 10 years of experience in managing high-performance teams. He specializes in strategic planning and operational excellence, ensuring that every project is delivered with the highest standards of quality. His commitment to innovation and team growth has been a cornerstone of our success.",
        "image_path": "career-growth/career-growth-1.png",
        "member_bg_class": 'member-bg-primary',
        "experiences": [
            { "title": 'Operations Lead', "year": '2015', "duration": '2 years', "description": 'Optimized internal processes and workflow efficiency.', "exp_type": 'hollow' },
            { "title": 'Project Manager', "year": '2017', "duration": '3 years', "description": 'Led cross-functional teams for large-scale enterprise projects.', "exp_type": 'hollow' },
            { "title": 'Senior Operations Director', "year": '2020', "duration": '3 years', "description": 'Scaled company operations across multiple regions.', "exp_type": 'hollow' },
            { "title": 'Team Manager', "year": '2023', "duration": 'Present', "description": 'Shaping organizational culture and long-term strategy.', "exp_type": 'filled' },
        ]
    },
    {
        "role": "Lead Developer",
        "name": "Alex Smith",
        "description": "Expert in building scalable web applications and high-performance systems.",
        "detailed_description": "Alex is a technical powerhouse with a deep passion for clean code and scalable architecture. Leading our development efforts, he has successfully delivered numerous complex systems, always prioritizing performance and user experience. When not coding, Alex mentors junior developers and contributes to open-source projects.",
        "image_path": "career-growth/career-growth-1.png",
        "member_bg_class": 'member-bg-primary',
        "experiences": [
            { "title": 'Junior Web Developer', "year": '2016', "duration": '2 years', "description": 'Focused on frontend responsiveness and API integrations.', "exp_type": 'hollow' },
            { "title": 'Software Engineer', "year": '2018', "duration": '3 years', "description": 'Full-stack development using React and Node.js.', "exp_type": 'hollow' },
            { "title": 'Senior Developer', "year": '2021', "duration": '2.5 years', "description": 'Architected microservices and high-availability systems.', "exp_type": 'hollow' },
            { "title": 'Lead Developer', "year": '2024', "duration": 'Present', "description": 'Directing technical vision and engineering best practices.', "exp_type": 'filled' },
        ]
    },
    {
        "role": "UI Designer",
        "name": "Jane Doe",
        "description": "Creating beautiful and intuitive user experiences with modern design principles.",
        "detailed_description": "Jane brings a unique blend of creativity and analytical thinking to her designs. Her focus on user-centric design ensures that our interfaces are not only visually stunning but also highly functional. She stays at the forefront of design trends, incorporating modern principles to create memorable experiences for our users.",
        "image_path": "career-growth/career-growth-1.png",
        "member_bg_class": 'member-bg-primary',
        "experiences": [
            { "title": 'Graphic Designer', "year": '2017', "duration": '1 year', "description": 'Created visual assets and marketing materials.', "exp_type": 'hollow' },
            { "title": 'Junior UI Designer', "year": '2018', "duration": '2 years', "description": 'Supported design systems and prototyping efforts.', "exp_type": 'hollow' },
            { "title": 'UI/UX Designer', "year": '2020', "duration": '3.5 years', "description": 'Led user research and end-to-end feature design.', "exp_type": 'hollow' },
            { "title": 'Lead UI Designer', "year": '2024', "duration": 'Present', "description": 'Defining design systems and product aesthetics.', "exp_type": 'filled' },
        ]
    },
    {
        "role": "Product Owner",
        "name": "John Wilson",
        "description": "Driving product strategy and ensuring alignment with user needs and business goals.",
        "detailed_description": "John is the bridge between our technical teams and our business objectives. With a keen eye for market trends and user needs, he defines product roadmaps that drive growth and deliver value. His collaborative approach ensures that every feature we build aligns perfectly with our overarching vision.",
        "image_path": "career-growth/career-growth-1.png",
        "member_bg_class": 'member-bg-primary',
        "experiences": [
            { "title": 'Business Analyst', "year": '2016', "duration": '2 years', "description": 'Market research and requirement gathering.', "exp_type": 'hollow' },
            { "title": 'Associate Product Manager', "year": '2018', "duration": '3 years', "description": 'Assisted in feature prioritization and backlog management.', "exp_type": 'hollow' },
            { "title": 'Product Manager', "year": '2021', "duration": '2.5 years', "description": 'Owned product lifecycle for core software modules.', "exp_type": 'hollow' },
            { "title": 'Product Owner', "year": '2024', "duration": 'Present', "description": 'Driving overall product strategy and stakeholder alignment.', "exp_type": 'filled' },
        ]
    }
]

def seed():
    print("Clearing existing Career Growth data...")
    MemberExperience.objects.all().delete()
    CareerGrowthMember.objects.all().delete()

    for idx, member_data in enumerate(TEAM_MEMBERS_DATA):
        print(f"Adding member: {member_data['name']}")
        
        experiences_data = member_data.pop('experiences')
        image_path = member_data.pop('image_path')
        
        member = CareerGrowthMember(**member_data)
        member.order = idx + 1
        
        f = get_local_file(image_path)
        if f:
            member.image.save(os.path.basename(image_path), f, save=False)
        
        member.save()

        for exp_idx, exp_data in enumerate(experiences_data):
            exp = MemberExperience(member=member, **exp_data)
            exp.order = exp_idx + 1
            exp.save()

    print("Successfully seeded Career Growth data.")

if __name__ == '__main__':
    seed()
