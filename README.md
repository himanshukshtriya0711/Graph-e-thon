# Brain Tumor Detection System

A web application for early detection of brain tumors using artificial intelligence.

## Features

- User registration and authentication
- Dashboard with 3D brain model visualization
- Medical status tracking
- Appointment scheduling
- MRI scan analysis using AI
- Prescription management

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Backend**: Django
- **Database**: SQLite (default)
- **3D Visualization**: Three.js
- **AI Integration**: Ready for integration with custom AI models

## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/brain_tumor_detection.git
cd brain_tumor_detection
```

2. Create a virtual environment:
```
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Apply migrations:
```
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:
```
python manage.py createsuperuser
```

6. Run the development server:
```
python manage.py runserver
```

7. Visit `http://127.0.0.1:8000/` in your browser

## Project Structure

- `brain_tumor_project/`: Django project settings
- `tumor_detection/`: Main application
  - `models.py`: Database models
  - `views.py`: View functions
  - `forms.py`: Form definitions
  - `urls.py`: URL patterns
  - `admin.py`: Admin panel configurations
- `templates/`: HTML templates
- `static/`: Static files (CSS, JS, images)
- `media/`: User-uploaded files
- `models/`: For AI model integration

## Usage

1. Register an account
2. Login with your credentials
3. Complete your medical profile
4. Upload MRI scans for analysis
5. Schedule appointments with doctors
6. Manage prescriptions and medical records

## Future Enhancements

- Mobile app integration
- Advanced AI model for more accurate tumor detection
- Real-time consultation with specialists
- Integration with hospital management systems
- Patient data analytics and reporting

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Bootstrap for the UI components
- Three.js for 3D brain visualization
- Django for the web framework 