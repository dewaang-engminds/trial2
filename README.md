# 🚕 CabRoute AI

**CabRoute AI** is a full-stack, AI-powered system to manage employee cab routing dynamically, reduce transport costs, and optimize cab operations using clustering, real-time tracking, and intelligent scheduling — all through browser-based dashboards.

---

## 🔍 Problem Statement

Companies spend huge amounts on static, inefficient cab systems. Cabs are often underutilized, fixed routes ignore actual demand, and employees lack flexibility. Admins struggle with manual reimbursements and tracking.

---

## 💡 Solution

CabRoute AI solves this by:

- Letting employees choose when they need cabs (AM, PM, Both)
- Locking bookings daily at 6 PM
- Clustering addresses using ML to group passengers efficiently
- Solving vehicle routing problem (VRP) to assign minimal cabs
- Providing drivers with live optimized maps via the browser
- Allowing employees to track their cab like Uber/Ola
- Giving admins ride logs + reimbursement insights

---

## 🎯 Core Features

| Role       | Key Functions |
|------------|----------------|
| 🧍 Employee | Daily ride opt-in (AM/PM/Both), live cab tracking, ETA |
| 🚐 Driver   | Optimized stop map, live tracking interface, GPS sharing |
| 👨‍💼 Admin   | View usage logs, reimbursement days, analytics dashboard |

---

## 🧠 AI & Data Science Modules

| Module                     | Description |
|---------------------------|-------------|
| 📍 Clustering              | KMeans/DBSCAN to group employees geographically |
| 🧭 Route Optimization      | Google OR-Tools for shortest multi-stop route |
| 🔄 ETA Predictor           | Custom model using traffic + weather history |
| 📅 Demand Prediction       | XGBoost to learn attendance/ride habits |
| 💰 Reimbursement Tracker   | Flags unused ride days for payouts |
| 📈 Analytics Dashboard     | Ride frequency, cost efficiency, fleet usage |

---

## 🧱 Tech Stack

| Layer         | Technology |
|---------------|------------|
| Frontend      | React.js, Tailwind CSS, Google Maps JS SDK |
| Backend       | FastAPI (Python), PostgreSQL, Redis |
| Real-Time     | WebSockets, HTML5 Geolocation |
| AI/ML         | scikit-learn (KMeans), Google OR-Tools, XGBoost |
| Maps/Routing  | Google Maps Directions API (optimize:true) |
| Deployment    | Vercel (frontend), Render (backend & DB), Docker |

---
