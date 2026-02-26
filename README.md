# Dosage Master Pro

An interactive educational application for nursing students to practice drug dosage calculations, with emphasis on **translating clinical word problems into mathematical equations**.

## ✨ Features

| Module | Description | Questions |
|--------|-------------|-----------|
| **A: Sentence Decipher** | Extract D/H/V variables from clinical text | 20+ unique scenarios |
| **B: Unit Bootcamp** | Master conversions with SOLD/LOST mnemonics | 20+ combinations |
| **C: Tablet & Liquid** | Practice problems with step-by-step solutions | 25+ each type |
| **D: Pediatric Dosing** | Weight-based mg/kg calculations | 20+ scenarios |
| **E: Infusions/Dilutions** | IV drip rates and C₁V₁=C₂V₂ | 20+ each |
| **F: Pharmacoeconomics** | Cost comparison calculations | 15+ drug pairs |

---

## 🚀 Quick Start Options

### Option 1: One-Click Launch (Easiest if Python is installed)

```
Double-click: RUN_APP.bat
```

This will automatically install dependencies and start the app.

---

### Option 2: Streamlit Cloud (FREE - No Installation Required!)

**This is the easiest way to run the app on any computer without installing anything!**

1. Create a free account at [https://share.streamlit.io](https://share.streamlit.io)
2. Upload your files to a GitHub repository:
   - `app.py`
   - `utils.py`
   - `requirements.txt`
3. Connect your GitHub repo to Streamlit Cloud
4. Click **Deploy** - your app gets a public URL!
5. Share the link with anyone - they can use it from any browser.

**Benefits:**
- ✅ No Python installation needed
- ✅ No Docker needed
- ✅ Works on any device (laptop, tablet, phone)
- ✅ Free hosting
- ✅ Shareable link

---

### Option 3: Docker (Portable, works everywhere)

If you have Docker Desktop installed:

```bash
# Build and run
docker-compose up --build

# Access at http://localhost:8501

# To stop
docker-compose down
```

---

### Option 4: Manual Python Setup

```bash
# Install Python 3.11+ from python.org
# IMPORTANT: Check "Add Python to PATH" during installation!

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

# Access at http://localhost:8501
```

---

## 📖 Usage Tips

1. **Start with Module A** - The Sentence Decipher tool teaches you to identify key variables
2. **Use "Show Working" sections** - Every problem includes detailed step-by-step solutions
3. **Read the Sanity Check tips** - These help catch common calculation errors
4. **Track your progress** - Score is saved during each session

---

## 📐 Formulas Reference

| Calculation | Formula |
|-------------|---------|
| Basic Dose | `X = (Desired ÷ Have) × Vehicle` |
| Pediatric Dose | `Total = mg/kg × weight(kg)` |
| Drip Rate | `gtts/min = (Volume ÷ Time) × Drop Factor` |
| Dilution | `C₁V₁ = C₂V₂` |

---

## 📁 File Structure

```
medops_study/
├── app.py              # Main Streamlit application
├── utils.py            # Problem generators (20+ per module!)
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Docker Compose setup
├── RUN_APP.bat        # One-click Windows launcher
└── README.md          # This file
```

---

## 🆘 Troubleshooting

**"Python not found"**
- Install Python from [python.org](https://www.python.org/downloads/)
- ✓ Check "Add Python to PATH" during installation
- Restart your terminal/command prompt

**"Module not found"**
- Run: `pip install -r requirements.txt`

**"Port already in use"**
- Another app is using port 8501
- Run: `streamlit run app.py --server.port 8502`

---

## 📜 License

Educational use only.
