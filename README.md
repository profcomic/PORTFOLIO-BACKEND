# ANTHONNEY MWANZAH - Portfolio Website

A modern, backend part of the full-stack portfolio website built with Django REST API.

## Project Structure

```
Portfolio-Backend/            # Django REST API
├── professor/               # Django app
├── requirements.txt         # Python dependencies
├── manage.py               # Django management script
└── ...                     # Other Django files
```

## Utilize it

1. Navigate to backend directory:
```bash
cd Portfolio-Backend
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Start development server:
```bash
python manage.py runserver
```

Backend will be available at: `http://127.0.0.1:8000`


## The Tech stacks used to compile it

### Backend
- **Django 5.2.2** - Web framework
- **Django REST Framework** - API development
- **SQLite** - Database
- **Pillow** - Image handling
- **django-cors-headers** - CORS support


## What you will interact with

- **Project Management**: Add, edit, delete projects
- **Image Upload**: Project images with fallbacks
- **Custom Admin**: Modern admin interface
- **Responsive Design**: Works on all devices


## Get to the Django Admin panel

### Django Admin (Default)
- URL: `http://127.0.0.1:8000/admin`
- Use superuser credentials

### I have customized an Admin dashboard
- URL: `http://127.0.0.1:8000/admin-dashboard/admin/`
- Modern UI with Bootstrap 5
- Enhanced project management

## Get the features connected // API Endpoints

- `GET /api/projects/` - List all projects
- `POST /api/projects/` - Create project

## Tailor it according to your taste

### Adding Projects
1. Access admin panel
2. Navigate to Projects section
3. Fill in project details:
   - Title & Description
   - Tech Stack (comma-separated)
   - GitHub URL & Live Demo
   - Project Image
   - Project Date

### Styling
- Edit `Portfolio-Backend/professor/templates/admin/`

## Ready to Go live🥳🥳🥳..Deploy it buddie

1. Set environment variables
2. Run `python manage.py collectstatic`
3. Configure web server (Nginx + Gunicorn)

## The Other Stacks can be  Accessed through

- **Github**: [Frontend repo](https://github.com/profcomic/PORTFOLIO-FRONTEND)
- **Github**: [Fullstack repo](https://github.com/profcomic/MY-PORTFOLIO)



## Lets LinkUp and share those insights

- **Email**: professorcomic1@gmail.com
- **Phone**: +254 113 088 424
- **LinkedIn**: [LinkedIn Profile](https://www.linkedin.com/in/anthony-mwanzah-432977354)
- **GitHub**: [GitHub Profile](https://github.com/profcomic)
- **Instagram**: [Instagram Profile](https://www.instagram.com/professor_comic/)
- **Location**: Anywhere, Space

## License

This project is open source and available under the MIT License.
