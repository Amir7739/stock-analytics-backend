# Stock Analytics Backend

This is the backend for Stock Analytics built with FastAPI and Firebase Admin SDK.

---

## Prerequisites

- Python 3.8 or higher installed
- Git (optional, if you want to clone the repo)
- Firebase project and service account created

---

## Steps: Get the Code

# Step 1: Clone the code

If you want to clone from GitHub:

```bash
git clone https://github.com/Amir7739/stock-analytics-backend.git
cd stock-analytics-backend


# Step 2: Create Virtual Environment and Activate It

# On Windows (cmd or PowerShell):
python -m venv venv
venv\Scripts\activate

# On macOS/Linux:
# bash
# Copy
# Edit


python3 -m venv venv
source venv/bin/activate

# Step 3: Install Dependencies

fastapi
uvicorn
firebase-admin
python-dotenv

# then install
pip install -r requirements.txt


#  Step 4: Setup Firebase Environment Variables

FIREBASE_TYPE=service_account
FIREBASE_PROJECT_ID=your-project-id
FIREBASE_PRIVATE_KEY_ID=your-private-key-id
FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY_CONTENT\n-----END PRIVATE KEY-----\n"
FIREBASE_CLIENT_EMAIL=your-client-email@your-project-id.iam.gserviceaccount.com
FIREBASE_CLIENT_ID=your-client-id
FIREBASE_AUTH_URI=https://accounts.google.com/o/oauth2/auth
FIREBASE_TOKEN_URI=https://oauth2.googleapis.com/token
FIREBASE_AUTH_PROVIDER_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
FIREBASE_CLIENT_CERT_URL=https://www.googleapis.com/robot/v1/metadata/x509/your-client-email@your-project-id.iam.gserviceaccount.com

PORT=8000


# Step 5: Run the Backend Server

uvicorn app.main:app --reload


# Test your api
# In header [Bearer<Token>]
# in body {
#   "tickers": ["AAPL", "MSFT"],
#   "period": "1M"
# }

http://localhost:8000/api/stocks/data


```
