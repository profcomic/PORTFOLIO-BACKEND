from django.core.management.base import BaseCommand
from projects.models import Project
from datetime import datetime

class Command(BaseCommand):
    help = 'Create sample projects for the portfolio'

    def handle(self, *args, **options):
        # Clear existing projects
        Project.objects.all().delete()
        
        sample_projects = [
            {
                'title': 'E-Commerce Platform',
                'description': 'A full-featured e-commerce platform with user authentication, payment processing, inventory management, and admin dashboard. Built with Django REST API and React frontend.',
                'tech_stack': ['Django', 'React', 'PostgreSQL', 'Stripe', 'Redis'],
                'github_url': 'https://github.com/yourusername/ecommerce-platform',
                'live_demo': 'https://ecommerce-demo.com',
            },
            {
                'title': 'Task Management System',
                'description': 'A collaborative task management application with real-time updates, drag-and-drop functionality, team collaboration features, and advanced analytics dashboard.',
                'tech_stack': ['Next.js', 'TypeScript', 'Tailwind CSS', 'PostgreSQL', 'Socket.io'],
                'github_url': 'https://github.com/yourusername/task-manager',
                'live_demo': 'https://taskmanager-demo.com',
            },
            {
                'title': 'Weather Dashboard',
                'description': 'A beautiful weather dashboard with location-based forecasts, interactive maps, detailed meteorological data visualization, and severe weather alerts.',
                'tech_stack': ['Angular', 'TypeScript', 'Chart.js', 'OpenWeather API', 'Mapbox'],
                'github_url': 'https://github.com/yourusername/weather-dashboard',
                'live_demo': 'https://weather-demo.com',
            },
            {
                'title': 'Brand Identity Design',
                'description': 'Complete brand identity package including logo design, color palette, typography guidelines, business cards, and marketing materials for a tech startup.',
                'tech_stack': ['Graphic Design', 'Photoshop', 'Illustrator', 'Figma', 'Brand Design'],
                'github_url': 'https://github.com/yourusername/brand-identity',
                'live_demo': 'https://brand-demo.com',
            },
            {
                'title': 'Product Photography Portfolio',
                'description': 'Professional product photography series for e-commerce clients, featuring lighting techniques, retouching, and creative composition for commercial products.',
                'tech_stack': ['Photography', 'Photoshop', 'Lightroom', 'Product Design', 'Visual Arts'],
                'github_url': 'https://github.com/yourusername/product-photography',
                'live_demo': 'https://photography-demo.com',
            },
            {
                'title': 'Corporate Video Production',
                'description': 'Complete video production for corporate clients including concept development, filming, editing, motion graphics, and post-production for marketing campaigns.',
                'tech_stack': ['Video Production', 'Motion Graphics', 'After Effects', 'Premiere Pro', 'Storytelling'],
                'github_url': 'https://github.com/yourusername/corporate-video',
                'live_demo': 'https://video-demo.com',
            },
            {
                'title': 'Social Media Graphics',
                'description': 'Engaging social media graphics and templates for various platforms including Instagram, Facebook, Twitter, and LinkedIn with consistent branding.',
                'tech_stack': ['Graphic Design', 'Social Media', 'Canva', 'Adobe Creative Suite', 'Marketing Design'],
                'github_url': 'https://github.com/yourusername/social-media-graphics',
                'live_demo': 'https://social-media-demo.com',
            },
            {
                'title': 'Fashion Photography Series',
                'description': 'Creative fashion photography editorial featuring artistic lighting, composition, and post-processing techniques for fashion brands and magazines.',
                'tech_stack': ['Fashion Photography', 'Photoshop', 'Lightroom', 'Creative Direction', 'Visual Storytelling'],
                'github_url': 'https://github.com/yourusername/fashion-photography',
                'live_demo': 'https://fashion-demo.com',
            },
            {
                'title': 'Documentary Video Project',
                'description': 'Short documentary film project covering social impact stories, including interviews, B-roll footage, sound design, and narrative editing.',
                'tech_stack': ['Documentary', 'Video Editing', 'Storytelling', 'Sound Design', 'Film Production'],
                'github_url': 'https://github.com/yourusername/documentary-video',
                'live_demo': 'https://documentary-demo.com',
            },
            {
                'title': 'UI/UX Design System',
                'description': 'Comprehensive design system for mobile applications including component library, design tokens, user flows, and interactive prototypes.',
                'tech_stack': ['UI/UX Design', 'Figma', 'Design Systems', 'Prototyping', 'User Research'],
                'github_url': 'https://github.com/yourusername/uiux-design-system',
                'live_demo': 'https://design-system-demo.com',
            },
        ]

        created_count = 0
        for project_data in sample_projects:
            project = Project.objects.create(**project_data)
            created_count += 1
            self.stdout.write(
                self.style.SUCCESS(f'Created project: {project.title}')
            )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} sample projects!')
        )
