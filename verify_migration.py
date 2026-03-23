import os
import django
import sys

# Setup Django environment
sys.path.append('d:/linq-corporate-website/Backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'linq_backend.settings')
django.setup()

from content_api.models import CareerGrowthMember, MemberExperience

def verify():
    members = CareerGrowthMember.objects.all()
    print(f"Total Members: {members.count()}")
    for member in members:
        print(f"Member: {member.name} ({member.role})")
        print(f"  Experiences: {member.experiences.count()}")
        for exp in member.experiences.all():
            print(f"    - {exp.title} ({exp.year})")

if __name__ == '__main__':
    verify()
