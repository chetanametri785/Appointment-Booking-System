import uvicorn
import os
import sys

# Ensure backend directory is in sys.path
backend_dir = os.path.join(os.path.dirname(__file__), "backend")
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

if __name__ == "__main__":
    print("=" * 60)
    print(" ApexCare Appointment Booking System ")
    print(" Blue & White Modern Health & Consultation Portal")
    print("=" * 60)
    print(" Starting server on http://127.0.0.1:8000 ...")
    print(" Open http://127.0.0.1:8000 in your browser to view.")
    print(" Press CTRL+C to stop.")
    print("=" * 60)
    
    uvicorn.run("backend.app:app", host="127.0.0.1", port=8000, reload=True)
