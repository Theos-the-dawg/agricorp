# AgriCorp React + Django Integration

## Quick Start Summary

### Prerequisites
- Python 3.8+
- Node.js 16+
- pip & npm

### Installation

### 1. **Django Backend Setup**
This backend now operates purely as an API server. All previous HTML
templates have been replaced by a separate React frontend; Django views
no longer render pages. The old template files live under `store/templates/`
and are no longer used—feel free to remove or archive them once you're
happy with the React app. During development Django will redirect any
non-API request to `http://localhost:5173`, and in production the
compiled React build should be served from static files.

```bash
# Create virtual environment
python -m venv .venv
source .venv/Scripts/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start Django server
python manage.py runserver
```

#### 2. React Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Accessing the Application

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **Django Admin**: http://localhost:8000/admin

---

## What's New in your AgriCorp Project

✅ **Complete React Frontend** with:
- Modern UI with your teal/green color scheme (#007B5E)
- Responsive design for all devices
- Client-side routing with React Router
- JWT authentication integration
- API integration with Axios

✅ **Django REST Backend** configured with:
- JWT token authentication
- CORS support for frontend
- User registration endpoint
- API endpoints for:
  - Dashboard data
  - Expense management
  - Product listing
  - User authentication

✅ **Engaging Features**:
- Beautiful landing page with hero section
- User authentication system
- Dashboard with statistics
- Expense management interface
- Product showcase
- Responsive navigation with mobile hamburger menu

---

## File Structure

```
agricorp/
├── agricorp/              # Django settings
│   ├── settings.py       # ✨ Updated with CORS & REST framework
│   ├── urls.py          # ✨ Added API endpoints
│   └── ...
├── store/
│   ├── api_views.py     # ✨ NEW - API views
│   ├── serializers.py   # ✨ Updated with API serializers
│   ├── models.py
│   ├── views.py
│   └── ...
├── frontend/            # ✨ NEW - React app
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
├── requirements.txt
├── REACT_SETUP.md       # ✨ NEW - React setup guide
├── README.md
└── ...
```

---

## Django Settings Updates

Your Django settings now include:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```

---

## Available API Endpoints

### Authentication
- `POST /api/token/` - Get JWT tokens
- `POST /api/token/refresh/` - Refresh token
- `POST /api/register/` - Register new user

### User Data
- `GET /api/dashboard/` - Dashboard statistics
- `GET /api/expenses/` - User's expenses
- `POST /api/expenses/` - Create expense
- `GET /api/products/` - All products
- `GET /api/categories/` - Product categories

---

## Key Technologies Added

- **Vite 5** - Modern build tool
- **React 18** - UI framework
- **React Router 6** - Client routing
- **Axios** - HTTP client
- **djangorestframework** - DRF for APIs
- **djangorestframework-simplejwt** - JWT auth
- **django-cors-headers** - CORS support

---

## Next Steps

1. **Test the Application**:
   - Start both servers (Django on 8000, React on 5173)
   - Navigate to http://localhost:5173
   - Register a new account
   - Test the dashboard and features

2. **Customize the Theme**:
   - Edit color variables in `frontend/src/index.css`
   - Modify component styles in respective CSS files
   - The color scheme automatically updates everywhere

3. **Add More Features**:
   - Extend API endpoints in `store/api_views.py`
   - Create new React components in `frontend/src/components/`
   - Add new pages in `frontend/src/pages/`

4. **Deploy**:
   - Frontend: Deploy to Vercel, Netlify, or your host
   - Backend: Deploy Django to Heroku, PythonAnywhere, or your server

---

## Important Notes

⚠️ **SECRET KEY**: Change the SECRET_KEY in `agricorp/settings.py` before production!

⚠️ **DEBUG MODE**: Set `DEBUG = False` in production!

⚠️ **ALLOWED_HOSTS**: Update with your production domain!

---

## Support & Documentation

- **React Setup**: See [REACT_SETUP.md](REACT_SETUP.md)
- **Django Docs**: https://docs.djangoproject.com/
- **Vite Docs**: https://vitejs.dev/
- **React Router**: https://reactrouter.com/

---

Happy coding! 🚀🌾
