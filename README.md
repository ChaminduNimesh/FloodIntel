# FloodIntel

**AI-Based Flood Prediction and Residential Damage Risk Assessment System for the Lower Kelani River Basin**

FloodIntel is a rainfall-driven, AI-powered web GIS system that forecasts river water level and flood severity, estimates real per-building damage risk, and delivers automated multi-channel alerts for Hanwella, Kaduwela, and Angoda — three flood-prone areas in Sri Lanka's Lower Kelani River Basin.

Built as a final year undergraduate research project, FloodIntel integrates two trained LSTM deep learning models, a real per-building geospatial damage engine, an interactive GIS dashboard, and automated email/SMS alerting into a single, working full-stack system.

---

## Live Demo

🔗 https://lnkd.in/p/gusxKbfM

---

## The Problem

Existing flood monitoring in the region relies mostly on river sensors and manual checking. There is very little map-based risk information, and no way for a resident to know which specific buildings will be affected. FloodIntel was built to close that gap.

---

## Key Features

### 🧠 Dual-LSTM Forecasting
- Two independently trained LSTM networks: a water level regression model and a four-class severity classifier (Low / Medium / High / Severe)
- Trained on **10 years (2016–2025) of real hourly rainfall and water-level data** — 86,913 records — from the Nagalagam Street gauge and four real rainfall stations
- 13 engineered features including multi-window cumulative rainfall (6h/24h/72h), water-level rate of change, hour, and month
- Input window and prediction horizon justified by a real lag-correlation analysis (peak correlation r = 0.438 at a 36-hour lag)
- Evaluated on a chronologically held-out test set of 25,555 real records — achieving **0.286 ft RMSE** (68.1% improvement over baseline) and **0.47 Macro F1** (22% improvement over a Random Forest baseline trained on identical data)
- Validated directly against Sri Lanka's real, documented **November 2025 flood event**

### 🏢 Real Per-Building Damage Assessment
- Compares each prediction's water level against the **actual elevation of every individual building** — not an area-wide approximation
- Covers ~40,000 real OpenStreetMap building footprints across all three study areas
- Elevation and slope data sourced from Copernicus DEM satellite data
- Classifies each building into No Damage / Minor / Moderate / Severe categories

### 🗺️ Interactive GIS Dashboard
- Leaflet-based live risk map with a real 20×13 building-risk grid per area
- Compare mode to view all three areas side by side
- Role-appropriate views: Dashboard, GIS Map, Water Level Trend, Damage Assessment, Rainfall Prediction, Prediction History, Alerts, Model Performance, Shelters, Saved Locations

### 📡 Live Water Level Integration
- Automatically fetches the current real water level from a public monitoring source if no manual reading is supplied
- Falls back gracefully to manual entry if the live source is unavailable

### 🔔 Multi-Channel Automated Alerting
- Email and SMS (via Notify.lk, a Sri Lanka-specific SMS gateway) notifications
- Personalized messages for users with a registered home area; full area summaries for users without one
- Includes real flow-direction data and risk-appropriate action guidance in every alert
- PDF report generation with real comparison against the previous prediction

### 🔐 Three-Tier Role-Based Access Control
- **Admin** — full system access including user and shelter management
- **Officer** — full operational access (rainfall input, all dashboards) except user management
- **User** — read-only access to their own registered area, notification preferences, saved locations

### 🌙 Additional Features
- Dark mode
- Browser push notifications
- Risk trend indicators (rising/falling vs. previous prediction)
- Admin user activity audit log
- Real shelter and emergency contact directory, admin-editable
- One-click PDF report download

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React (Vite), Tailwind CSS, React Router, Leaflet.js |
| Backend | Flask (Python), Flask-SQLAlchemy, Flask-CORS |
| Authentication | JWT (PyJWT), Werkzeug password hashing |
| Database | PostgreSQL |
| Machine Learning | TensorFlow/Keras (dual LSTM), scikit-learn (Random Forest baseline — comparison only) |
| Geospatial | rasterio (Copernicus DEM elevation/slope analysis) |
| Live Data | Playwright (headless browser water level scraping) |
| Notifications | SMTP (email), Notify.lk (SMS) |
| Data Processing | pandas, NumPy |

---

## Dataset Sources

- Real hourly rainfall (2016–2025): Hanwella, Angoda Mental Hospital, Hanwella Group, and Oruwala rainfall stations
- Real hourly river water level (2016–2025): Kelani Ganga at Nagalagam Street
- Official flood thresholds: Disaster Management Centre Islandwide Water Level & Rainfall Situation report
- Residential building footprints: OpenStreetMap (GeoJSON)
- Digital Elevation Model: Copernicus DEM

---

## Project Structure

```
floodintel/
├── backend/
│   ├── app/
│   │   ├── models/        # SQLAlchemy database models
│   │   ├── routes/        # REST API endpoints
│   │   ├── services/      # Business logic (hydrology, damage, notifications)
│   │   ├── ml/             # LSTM model loading and prediction
│   │   └── utils/          # Auth decorators, helpers
│   ├── requirements.txt
│   └── run.py
├── frontend/
│   ├── src/
│   │   ├── pages/          # Route-level page components
│   │   ├── components/     # Reusable UI components
│   │   ├── services/       # API service modules
│   │   ├── context/        # React context (theme, etc.)
│   │   └── layouts/        # Shared layout wrappers
│   └── package.json
└── README.md
```

---

## Getting Started

### Prerequisites
- Python 3.10+
- Node.js 18+
- PostgreSQL

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\Activate.ps1
pip install -r requirements.txt --break-system-packages
```

Create a `.env` file in `backend/` with:
```
DATABASE_URL=postgresql://user:password@localhost:5432/floodintel_db
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret_key
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password
SMTP_FROM_EMAIL=your_email@gmail.com
NOTIFY_LK_USER_ID=your_notify_lk_user_id
NOTIFY_LK_API_KEY=your_notify_lk_api_key
NOTIFY_LK_SENDER_ID=NotifyDEMO
FRONTEND_BASE_URL=http://localhost:5173
```

```bash
python run.py
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## Model Performance Summary

| Model | Metric | Result |
|---|---|---|
| Water Level Regression (LSTM) | RMSE | 0.286 ft |
| Water Level Regression (LSTM) | MAE | 0.210 ft |
| Severity Classifier (LSTM) | Accuracy | 98.29% |
| Severity Classifier (LSTM) | Macro F1 | 0.47 |
| Severity Classifier (LSTM) vs. Random Forest | Improvement | +22% Macro F1 |

**Real-world validation (November 2025 flood event):** Predicted 3.38 ft vs. actual recorded 6.30–6.40 ft (official DMC report) — a specific, honestly reported limitation attributed to missing upstream catchment inflow data.

---

## Known Limitations

- Trained on a single gauge station (Nagalagam Street); Kaduwela and Angoda water levels are estimated via area-specific calibration, not independently gauged
- 0% recall on the rare Severe risk class (only 87 real hours of Severe conditions across the full 10-year training record)
- Does not incorporate upstream catchment inflow data — identified as the top priority for future work
- Research prototype — not field-tested or certified for operational deployment

---

## Future Work

- Incorporate upstream catchment inflow features (Kitulgala, Deraniyagala)
- Add independently gauged Kaduwela and Angoda stations
- Class-weighting or data augmentation to address the Severe-class recall gap
- Field validation with the Disaster Management Centre and Irrigation Department

---

## Team

| Name | Role |
|---|---|
| Nimesh A.C.R. | Machine Learning |
| Dilthusha K.S.N. | Backend & Database |
| Nawoda A.M.I. | Frontend & GIS Visualization |

**Supervisor:** Mr. Samarasinghe P. — **Co-Supervisor:** Ms. Lakchani B.
Faculty of Computing and IT, Sri Lanka Technology Campus

---

## License

*[Add your real license here, e.g. MIT, or "Academic project — all rights reserved"]*
