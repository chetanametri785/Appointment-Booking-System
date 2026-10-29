# 🏥 ApexCare Appointments - Modern Healthcare & Specialist Booking System

A modern, attractive, and responsive appointment booking and status tracking website built with a clean **Blue & White** color palette, smooth micro-interactions, real-time slot checking, and patient management features.

---

## 🌟 Key Features

### 1. 🎨 Modern Blue & White Design System
- **Color Scheme**: Deep royal blue (`#1E3A8A`), vibrant electric blue (`#2563EB`), sky blue accents (`#0284C7`), crisp pure white (`#FFFFFF`), and soft ice-blue tint surfaces (`#F0F7FF`, `#F8FAFC`).
- **Typography & UI**: Google Font *Plus Jakarta Sans*, sleek rounded cards with glassmorphism, glowing ambient accents, smooth hover transitions, and clean high-contrast text.

### 2. 🗓️ Interactive 4-Step Booking Wizard
- **Step 1 - Specialist & Department Selection**:
  - Filter by departments: Cardiology, General Medicine, Dermatology, Dental Care, Pediatrics, and Orthopedics.
  - Doctor profile cards displaying photo, rating, experience, room/suite location, and consultation fee.
- **Step 2 - Date & Time Slot Selection**:
  - Intuitive calendar picker and quick date selector buttons (*Today*, *Tomorrow*, *In 2 Days*, *In 3 Days*, *Next Week*).
  - Categorized time slots (*Morning*, *Afternoon*, *Evening*) with live status (Available vs. Booked).
- **Step 3 - Patient Contact & Visit Details**:
  - Patient Full Name, Email, Phone Number.
  - Visit Type: In-Person Clinic Visit or HD Video Consultation.
  - Primary symptoms or reason for appointment.
- **Step 4 - Review & Confirmation**:
  - Complete schedule breakdown and transparent fee summary.
- **Step 5 - Digital Appointment Pass**:
  - Unique booking reference code (e.g., `APT-2026-XXXXX`) with 1-click clipboard copy.
  - Print/Save PDF pass with fast check-in QR code.
  - Direct 1-click "Add to Google Calendar" link.

### 3. 🔍 Live Booking Status Tracker
- Instant search by **Booking Reference Code** (e.g. `APT-2026-101`), **Phone Number**, or **Email**.
- Quick sample buttons for instant testing.
- Visual status badges:
  - `Confirmed` (Active verified consultation)
  - `Pending Approval` (Awaiting review)
  - `Completed` (Finished session)
  - `Cancelled` (Cancelled booking)
- **Interactive Patient Management Actions**:
  - 🔄 **Reschedule**: Select a new date and live available slot.
  - ❌ **Cancel Appointment**: Cancel with confirmation dialog.
  - 🖨️ **Print Slip**: Clean, printable clinic pass.
  - 📅 **Add to Calendar**: Export to Google Calendar.

### 4. 👩‍⚕️ Staff & Receptionist Portal
- Overview analytics cards: Total Bookings, Confirmed, Pending Review, and Today's Sessions.
- Filter by status, filter by specific date, and search by patient name/phone.
- Quick staff action triggers: **Approve/Confirm**, **Mark Completed**, **Cancel**, and **Add Walk-in**.

### 5. ⚡ Dual-Mode Resilience (Zero-Config)
- **Backend Mode**: Powered by **FastAPI** + **SQLite** (`appointments.db`) with complete REST API.
- **Standalone Offline Mode**: If opened directly as `index.html` via browser without the backend running, the application automatically operates using **LocalStorage** with pre-seeded sample records!

---

## 🚀 How to Run the Website

### Option A: Launch with Python FastAPI Server (Recommended)

1. Open PowerShell or Terminal in this folder:
   ```powershell
   python server.py
   ```
2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

### Option B: Standalone Direct Launch
Simply double-click `index.html` or open it with Google Chrome / Microsoft Edge / Firefox. It will load instantly in Standalone Mode.

---

## 🧪 Sample Pre-Seeded Booking References

You can immediately test the **Track Status** feature using these sample reference numbers:

| Reference Code | Patient Name | Department / Doctor | Status |
| :--- | :--- | :--- | :--- |
| `APT-2026-101` | Alex Morgan | Cardiology (Dr. Sarah Jenkins) | **Confirmed** |
| `APT-2026-102` | Sophia Bennett | Dermatology (Dr. Elena Rostova) | **Confirmed** |
| `APT-2026-103` | Liam Chen | General Medicine (Dr. Marcus Vance) | **Pending Approval** |
| `APT-2026-104` | Emma Watson | Dental & Orthodontics (Dr. Jonathan Hayes) | **Completed** |

---

## 📁 Project Structure

```
Appointment Booking System/
├── backend/
│   ├── app.py              # FastAPI REST endpoints & static file hosting
│   ├── database.py         # SQLite database schema, seeding, & CRUD operations
│   └── appointments.db     # SQLite database (auto-generated on launch)
├── static/
│   ├── css/
│   │   └── style.css       # Blue and white design system, glassmorphism, animations, print rules
│   └── js/
│       ├── api.js          # Hybrid REST & LocalStorage API client
│       └── app.js          # Wizard flow, status tracking, modals, staff portal logic
├── index.html              # Main Single Page Application interface
├── server.py               # Launcher script for FastAPI server
└── README.md               # Documentation & User Guide
```
