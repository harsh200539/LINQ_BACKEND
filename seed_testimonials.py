import os
import django
import sys
import requests
from django.core.files.base import ContentFile

sys.path.append('d:/linq-corporate-website/Backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'linq_backend.settings')
django.setup()

from content_api.models import Testimonial

testimonials_data = [
    # Middle Cards (6)
    {
        "name": "Sarah Jenkins",
        "role": "Marketing Director",
        "quote": "LINQ transformed our approach to market analysis. The insights provided were actionable and directly contributed to our Q3 growth.",
        "category": "MIDDLE",
        "is_avatar_only": False,
        "img_url": "https://images.unsplash.com/photo-1655249493799-9cee4fe983bb?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=200"
    },
    {
        "name": "David Chen",
        "role": "CEO, TechFlow",
        "quote": "The strategic advisory services are second to none. They understand the intricacies of scaling a startup in a competitive landscape.",
        "category": "MIDDLE",
        "is_avatar_only": False,
        "img_url": "https://images.unsplash.com/photo-1752952952773-80378cefc23d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=200"
    },
    {
        "name": "Emily Rodriguez",
        "role": "Operations Manager",
        "quote": "Their data management solutions completely streamlined our reporting workflow. We save countless hours every week.",
        "category": "MIDDLE",
        "is_avatar_only": False,
        "img_url": "https://images.unsplash.com/photo-1613473350016-1fe047d6d360?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=200"
    },
    {
        "name": "Michael Chang",
        "role": "Head of Product",
        "quote": "The industry intelligence reports give us the competitive edge we need. Highly recommended for any product team.",
        "category": "MIDDLE",
        "is_avatar_only": False,
        "img_url": "https://images.unsplash.com/photo-1672685667592-0392f458f46f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=200"
    },
    {
        "name": "Jessica Taylor",
        "role": "VP of Sales",
        "quote": "Outstanding Web Development support. Our new platform is fast, responsive, and has significantly improved our conversion rates.",
        "category": "MIDDLE",
        "is_avatar_only": False,
        "img_url": "https://images.unsplash.com/photo-1765648763932-43a3e2f8f35c?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=200"
    },
    {
        "name": "Robert Wilson",
        "role": "Financial Analyst",
        "quote": "Reliable data and expert insights. LINQ has become an indispensable part of our strategic planning process.",
        "category": "MIDDLE",
        "is_avatar_only": False,
        "img_url": "https://images.unsplash.com/photo-1655249493799-9cee4fe983bb?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=200"
    },

    # Right Cards (6)
    {
        "name": "Amanda Lee",
        "role": "HR Director",
        "quote": "",
        "category": "RIGHT",
        "is_avatar_only": True,
        "img_url": "https://images.unsplash.com/photo-1765648763932-43a3e2f8f35c?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=200"
    },
    {
        "name": "Thomas Wright",
        "role": "CTO",
        "quote": "A seamless experience from start to finish. The technical expertise they brought to our project was exactly what we needed.",
        "category": "RIGHT",
        "is_avatar_only": False,
        "img_url": "https://images.unsplash.com/photo-1752952952773-80378cefc23d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=200"
    },
    {
        "name": "Sophia Garcia",
        "role": "Lead Designer",
        "quote": "Their attention to detail and commitment to quality is evident in everything they do.",
        "category": "RIGHT",
        "is_avatar_only": False,
        "img_url": "https://images.unsplash.com/photo-1613473350016-1fe047d6d360?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=200"
    },
    {
        "name": "Daniel Smith",
        "role": "Consultant",
        "quote": "",
        "category": "RIGHT",
        "is_avatar_only": True,
        "img_url": "https://images.unsplash.com/photo-1672685667592-0392f458f46f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=200"
    },
    {
        "name": "Olivia Brown",
        "role": "Marketing Specialist",
        "quote": "The operational support we received allowed us to focus on our core business objectives. Truly transformative.",
        "category": "RIGHT",
        "is_avatar_only": False,
        "img_url": "https://images.unsplash.com/photo-1655249493799-9cee4fe983bb?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=200"
    },
    {
        "name": "William Davis",
        "role": "Project Manager",
        "quote": "Highly professional and consistently exceeding expectations. I look forward to our continued partnership.",
        "category": "RIGHT",
        "is_avatar_only": False,
        "img_url": "https://images.unsplash.com/photo-1752952952773-80378cefc23d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=200"
    }
]

Testimonial.objects.all().delete()

for idx, data in enumerate(testimonials_data):
    try:
        response = requests.get(data['img_url'])
        img_content = response.content
        
        t = Testimonial(
            name=data['name'],
            role=data['role'],
            quote=data['quote'],
            category=data['category'],
            is_avatar_only=data['is_avatar_only'],
            highlight=""
        )
        
        filename = f"testimonial_{idx}.jpg"
        t.image.save(filename, ContentFile(img_content), save=False)
        t.save()
        print(f"Added {data['name']}")
    except Exception as e:
        print(f"Error adding {data['name']}: {e}")

print("Done adding testimonials.")
