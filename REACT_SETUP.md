# AgriCorp React Frontend Setup Guide

## Overview

Your AgriCorp project now includes a modern React frontend built with Vite. The frontend maintains your original teal/green color scheme (#007B5E) while providing an engaging, modern user interface. All of the previous Django templates have been migrated to React pages and the backend now functions solely as an API server; the two are completely separated.

## Project Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── Navigation.jsx    # Sticky navigation bar
│   │   ├── Navigation.css
│   │   ├── Footer.jsx        # Footer component
│   │   └── Footer.css
│   ├── pages/
│   │   ├── Home.jsx          # Landing page with features
│   │   ├── Home.css
│   │   ├── Login.jsx         # User login
│   │   ├── Register.jsx      # User registration
│   │   ├── Auth.css          # Auth pages styling
│   │   ├── Dashboard.jsx     # User dashboard
│   │   ├── Dashboard.css
│   │   ├── Expenses.jsx      # Expense management
│   │   ├── Expenses.css
│   │   ├── Products.jsx      # Product listing
│   │   └── Products.css
│   ├── App.jsx               # Main app component with routing
│   ├── App.css
│   ├── index.css             # Global styles with color variables
│   └── main.jsx              # Entry point
├── index.html
├── vite.config.js
├── package.json
└── .gitignore
```

## Color Scheme

The following CSS variables are used throughout the project:

- **Primary**: `#007B5E` - Teal/Green main color
- **Primary Dark**: `#005f47` - Darker variant
- **Primary Light**: `#00a383` - Lighter variant
- **Background**: `#f9f9f9` - Light background
- **Surface**: `#ffffff` - Card/surface color
- **Text**: `#333333` - Main text color
- **Text Light**: `#666666` - Secondary text
- **Border**: `#e0e0e0` - Border color

## Setup Instructions

### 1. Install Dependencies

Navigate to the frontend directory and install packages:

```bash
cd frontend
npm install
```

### 2. Start Development Server

```bash
npm run dev
```

The app will be available at `http://localhost:5173`

### 3. Build for Production

```bash
npm run build
```

This creates an optimized build in the `dist` folder.

## Features

### 🏠 Home Page
- Beautiful hero section with animated emoji
- Feature showcase (6 feature cards)
- Statistics section with key metrics
- Call-to-action section for sign-up

### 🔐 Authentication
- Login page with form validation
- Registration page with password matching
- JWT token storage in localStorage
- Automatic redirect to login if not authenticated

### 📊 Dashboard
- Overview statistics (expenses, products, orders)
- Recent expenses table
- Key metrics at a glance
- Responsive dashboard layout

### 💰 Expense Management
- Add new expense entries
- View all expenses in card format
- Filter by date and category
- Expense categorization
- Form validation

### 🛒 Products
- Browse all products
- Product cards with images
- Price display
- Quick order button
- Responsive product grid

### 📱 Responsive Design
- Mobile-first approach
- Hamburger menu for mobile navigation
- Responsive grid layouts
- Touch-friendly buttons and inputs

## API Integration

The frontend communicates with Django backend via REST API:

### Authentication Endpoints
- `POST /api/token/` - Obtain JWT tokens
- `POST /api/token/refresh/` - Refresh token
- `POST /api/register/` - User registration

### Data Endpoints
- `GET /api/dashboard/` - Dashboard data
- `GET /api/expenses/` - Get user expenses
- `POST /api/expenses/` - Create expense
- `GET /api/products/` - Get all products
- `GET /api/categories/` - Get product categories

## Environment Configuration

The frontend is configured to proxy API requests to `http://localhost:8000` (your Django server).

To change the backend URL, edit `vite.config.js`:

```javascript
proxy: {
  '/api': {
    target: 'http://localhost:8000', // Change this URL
    changeOrigin: true,
    rewrite: (path) => path.replace(/^\/api/, '')
  }
}
```

## CORS Configuration

Django is configured to accept requests from:
- `http://localhost:3000`
- `http://localhost:5173`
- `http://127.0.0.1:3000`
- `http://127.0.0.1:5173`

To add more origins, edit `agricorp/settings.py`:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
    # Add your production URLs here
]
```

## Running Both Server and Frontend

### Terminal 1 - Django Server
```bash
cd agricorp
python manage.py runserver
```

### Terminal 2 - React Frontend
```bash
cd frontend
npm run dev
```

Now your app is available at `http://localhost:5173`

## Key Technologies

- **React 18** - UI framework
- **Vite 5** - Build tool
- **React Router 6** - Client-side routing
- **Axios** - HTTP client for API calls
- **CSS3** - Modern styling with CSS variables

## Customization

### Adding New Components

```javascript
// src/components/MyComponent.jsx
import './MyComponent.css'

export default function MyComponent() {
  return (
    <div className="my-component">
      <h2>My Component</h2>
    </div>
  )
}
```

### Using Color Variables

```css
/* Apply primary color */
.my-element {
  background-color: var(--primary);
  color: white;
  border: 1px solid var(--border);
}

.my-element:hover {
  background-color: var(--primary-dark);
}
```

### Adding New Pages

1. Create a new file in `src/pages/`
2. Add the route in `src/App.jsx`:

```javascript
<Route path="/my-page" element={<MyPage />} />
```

## Troubleshooting

### API Connection Issues
- Ensure Django server is running on port 8000
- Check CORS settings in Django
- Verify proxy configuration in `vite.config.js`

### Build Issues
- Clear `node_modules` and reinstall: `rm -rf node_modules && npm install`
- Clear Vite cache: `rm -rf dist && npm run build`

### Authentication Issues
- Check that tokens are saved in localStorage
- Verify JWT settings in Django settings.py
- Check token expiration time

## Production Deployment

### Build the Frontend
```bash
npm run build
```

### Deploy Options

1. **Vercel** (Recommended)
   - Connect your GitHub repo
   - Set build command: `npm run build`
   - Output directory: `dist`

2. **Netlify**
   - Deploy `frontend` folder
   - Build command: `npm run build`
   - Public directory: `dist`

3. **Static Hosting (S3, etc.)**
   - Build the frontend
   - Upload `dist` folder to your host
   - Configure web server to serve index.html for all routes

## Performance Tips

- Images are lazy-loaded
- CSS is minified in production
- JavaScript is bundled and optimized
- Use the production build for deployment

## Support & Next Steps

1. **Add More Features**:
   - Create detailed expense reports
   - Add data visualization charts
   - Implement inventory management

2. **Enhance UI**:
   - Add animations using Framer Motion
   - Implement dark mode toggle
   - Add toast notifications

3. **Optimize Performance**:
   - Add code splitting
   - Implement virtual scrolling for large lists
   - Add service workers for offline support

---

Enjoy your new AgriCorp React frontend! 🚀🌾
