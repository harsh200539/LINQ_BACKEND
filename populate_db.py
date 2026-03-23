import os
import django
import shutil

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'linq_backend.settings')
django.setup()

from content_api.models import GalleryImage, Stat, TimelineItem, AboutUsSection, VisionSection
from django.core.files import File

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_IMAGES_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'src', 'images'))

def copy_and_get_file(relative_path):
    # Frontend path is relative to src/components/
    # So '../images/...' means src/images/...
    if relative_path.startswith('../'):
        clean_path = relative_path.replace('../', '', 1)
        src_path = os.path.join(os.path.dirname(FRONTEND_IMAGES_DIR), clean_path)
    else:
        src_path = os.path.join(FRONTEND_IMAGES_DIR, relative_path)
    
    if os.path.exists(src_path):
        return File(open(src_path, 'rb'), name=os.path.basename(src_path))
    else:
        print(f"File not found: {src_path}")
        return None

def populate_gallery():
    print("Populating Gallery...")
    images = [
        ('LifeatLinq/Activity/John_Peter/Peter.webp', 'a'),
        ('LifeatLinq/Festival/DS/christmas.webp', 'b'),
        ('LifeatLinq/Cricket/WhatsApp Image 2025-07-25 at 7.57.55 PM (2).webp', 'c'),
        ('LifeatLinq/Cricket/WhatsApp Image 2025-07-25 at 7.58.18 PM (1).webp', 'c'),
        ('Img/WhatsApp Image 2025-04-01 at 1.42.29 AM (1).webp', 'c'),
        ('LifeatLinq/Festival/NS/WhatsApp Image 2025-04-01 at 1.42.23 AM.webp', 'b'),
        ('LifeatLinq/Activity/WhatsApp Image 2025-08-01 at 8.54.04 PM (1).webp', 'c'),
        ('LifeatLinq/Festival/NS/Wiilli.webp', 'c'),
        ('LifeatLinq/Birthday/Birthday_NS/WhatsApp Image 2025-10-31 at 7.25.29 PM (1).webp', 'c'),
        ('LifeatLinq/Festival/NS/WhatsApp Image 2025-04-01 at 1.42.26 AM.webp', 'c'),
        ('LifeatLinq/Festival/NS/Xmas.webp', 'a'),
        ('LifeatLinq/Movie/1.webp', 'b'),
        ('LifeatLinq/Festival/NS/WhatsApp Image 2025-08-15 at 2.39.16 AM.webp', 'b'),
        ('LifeatLinq/Festival/NS/Navratri25.webp', 'b'),
        ('LifeatLinq/Cricket/cricket1.webp', 'b'),
        ('LifeatLinq/Activity/WhatsApp Image 2025-08-01 at 8.54.10 PM (1).webp', 'c'),
        ('LifeatLinq/Birthday/Birthday_NS/WhatsApp Image 2025-07-25 at 12.48.40 AM (1).webp', 'c'),
        ('LifeatLinq/Festival/NS/15Aug.webp', 'b'),
        ('LifeatLinq/Festival/NS/wilson.webp', 'c'),
        ('LifeatLinq/Festival/NS/WhatsApp Image 2025-04-01 at 1.42.24 AM (2).webp', 'b'),
        ('LifeatLinq/Cricket/Cricket2.webp', 'a'),
        ('LifeatLinq/Festival/NS/Cake.webp', 'c'),
        ('LifeatLinq/Festival/DS/Ganpati.webp', 'b'),
        ('LifeatLinq/Activity/John_Peter/John.webp', 'c'),
        ('LifeatLinq/Festival/DS/Ganpati1.webp', 'a'),
        ('LifeatLinq/Festival/NS/NSGanpati.webp', 'c'),
        ('LifeatLinq/Festival/DS/Ganpati2.webp', 'b'),
        ('LifeatLinq/Festival/NS/Man_Day.webp', 'c'),
        ('LifeatLinq/Festival/DS/Ganpati3.webp', 'b'),
        ('LifeatLinq/Birthday/Birthday_NS/HBday.webp', 'c'),
        ('LifeatLinq/Activity/dnhuap8tjqbkzoi9ds0f.webp', 'c'),
        ('LifeatLinq/Activity/WhatsApp Image 2026-01-31 at 2.20.14 AM.webp', 'c'),
        ('LifeatLinq/Festival/NS/kbrzakj8dffpw6j1q3z6.webp', 'a'),
        ('LifeatLinq/Festival/NS/IMG_1637.webp', 'c'),
        ('LifeatLinq/Festival/NS/IMG_1791.webp', 'c'),
        ('LifeatLinq/Festival/NS/IMG_1858.webp', 'c'),
        ('LifeatLinq/Festival/NS/IMG_0693.webp', 'c'),
        ('LifeatLinq/Festival/NS/IMG_0713.webp', 'b'),
        ('LifeatLinq/Festival/NS/IMG_0831.webp', 'b'),
        ('LifeatLinq/Festival/NS/IMG_0886.webp', 'a'),
        ('LifeatLinq/Festival/NS/IMG_8750.webp', 'a'),
        ('LifeatLinq/Festival/NS/IMG_8754.webp', 'b'),
        ('LifeatLinq/Festival/NS/c12ahhtes4l3jwspcshv.webp', 'b'),
    ]
    for rel_path, img_type in images:
        f = copy_and_get_file(rel_path)
        if f:
            GalleryImage.objects.get_or_create(image=f, image_type=img_type)

def populate_stats():
    print("Populating Stats...")
    stats = [
        ("Completed Projects", 500, "+"),
        ("Satisfied Customers", 15000, "k+"),
        ("Worldwide Honors", 45, "+"),
    ]
    for label, value, suffix in stats:
        Stat.objects.get_or_create(label=label, value=value, suffix=suffix)

def populate_timeline():
    print("Populating Timeline...")
        {
            "year": "2024",
            "title": "Setting the Pace for Strategic Excellence",
            "headline": "Setting the Pace for <highlight>Strategic Excellence</highlight>.",
            "description": "LINQ Corporate Solutions Pvt. Ltd. commenced operations as a dynamic market research and strategic advisory firm with a defined global vision.",
            "thumbnail": "LifeatLinq/AboutUS/IMG_6441.webp",
            "order": 1
        },
        {
            "year": "2025",
            "title": "Expansion & Growth",
            "headline": "Expanding Influence. <highlight>Amplifying Impact.</highlight>",
            "description": "With a client base spanning 41 countries and experience across 8 core industries, LINQ strengthened its international presence.",
            "thumbnail": "LifeatLinq/AboutUS/IMG_6554.webp",
            "order": 2
        },
        {
            "year": "2026",
            "title": "Innovation & Technology",
            "headline": "From Insight to <highlight>Industry Momentum</highlight>",
            "description": "As cross-industry engagement increased, LINQ enhanced its analytical capabilities and advisory frameworks.",
            "thumbnail": "LifeatLinq/AboutUS/IMG_6469 (1).webp",
            "order": 3
        },
        {
            "year": "2027",
            "title": "Global Reach",
            "headline": "Engineering Enterprise <highlight>Advantage</highlight>",
            "description": "Operating across multiple geographies and industries, LINQ continues to deliver comprehensive market research and strategic advisory solutions.",
            "thumbnail": "LifeatLinq/AboutUS/IMG_6755.webp",
            "order": 4
        },
        {
            "year": "...",
            "title": "Future Forward",
            "headline": "Shaping What’s Next in <highlight>Strategy</highlight>",
            "description": "Looking ahead, LINQ remains committed to advancing its global capabilities and maintaining high standards in research and advisory services.",
            "thumbnail": "LifeatLinq/AboutUS/IMG_6526.webp",
            "order": 5
        }
    ]
    for item in timeline:
        thumbnail_file = copy_and_get_file(item.pop("thumbnail"))
        TimelineItem.objects.get_or_create(**item, thumbnail=thumbnail_file)

def populate_about_us():
    print("Populating About Us...")
    sections = [
        ("Who We Are", "Connecting industries, ideas, and opportunities worldwide", 1),
        ("What We Stand For", "We invest in your development with continuous learning opportunities and career advancement paths.", 2),
        ("Our Vision for the Future", "Shaping the industries of tomorrow through innovation", 3),
        ("Collaborative Culture", "Thrive in a supportive team where your ideas are valued and your contributions make a real difference.", 4),
    ]
    for title, content, order in sections:
        AboutUsSection.objects.get_or_create(title=title, content=content, order=order)

    VisionSection.objects.get_or_create(
        title="Our Vision",
        subtitle="Connecting global industries through ideas that drive opportunity",
        description="Our vision is to connect global industries through ideas that drive opportunity and deliver measurable business value. We are committed to empowering organizations with accurate, timely, and actionable insights that support confident and informed decision-making.",
        description_extended="Through strong partnerships and a truly global perspective, we work closely with clients to understand their unique challenges and objectives. Our approach is centered on collaboration, innovation, and long-term value creation, enabling organizations to achieve sustainable growth.",
        image=copy_and_get_file("AboutUs/Vision.webp")
    )

if __name__ == '__main__':
    populate_gallery()
    populate_stats()
    populate_timeline()
    populate_about_us()
    print("Done!")
