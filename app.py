"""
Dosage Master Pro
An interactive educational application for nursing students to master drug dosage calculations.
"""

import streamlit as st
import random
from utils import (
    generate_sentence_problem,
    generate_conversion_problem,
    generate_tablet_problem,
    generate_liquid_problem,
    generate_pediatric_problem,
    generate_infusion_problem,
    generate_dilution_problem,
    generate_cost_problem,
    format_working_tablet,
    format_working_liquid,
    format_working_pediatric,
    format_working_infusion,
    format_working_dilution,
    format_working_conversion,
    format_working_cost,
    get_sanity_check,
)

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Dosage Master Pro",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS - Clinical High-Contrast Theme
# ============================================================================

st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary-blue: #1e40af;
        --primary-light: #3b82f6;
        --success-green: #059669;
        --warning-amber: #d97706;
        --danger-red: #dc2626;
        --background-dark: #0f172a;
        --surface-dark: #1e293b;
        --text-primary: #f8fafc;
        --text-secondary: #94a3b8;
    }
    
    /* Global styling */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #f8fafc !important;
        font-weight: 600;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
        border-right: 1px solid #334155;
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {
        color: #f8fafc !important;
    }
    
    /* Cards/Containers */
    .problem-card {
        background: linear-gradient(145deg, #1e293b 0%, #334155 100%);
        border: 1px solid #475569;
        border-radius: 16px;
        padding: 24px;
        margin: 16px 0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
    }
    
    .success-card {
        background: linear-gradient(145deg, #064e3b 0%, #065f46 100%);
        border: 1px solid #059669;
        border-radius: 16px;
        padding: 24px;
        margin: 16px 0;
    }
    
    .error-card {
        background: linear-gradient(145deg, #7f1d1d 0%, #991b1b 100%);
        border: 1px solid #dc2626;
        border-radius: 16px;
        padding: 24px;
        margin: 16px 0;
    }
    
    .info-card {
        background: linear-gradient(145deg, #1e3a5f 0%, #1e40af 100%);
        border: 1px solid #3b82f6;
        border-radius: 16px;
        padding: 24px;
        margin: 16px 0;
    }
    
    /* Clinical scenario text */
    .scenario-text {
        font-size: 1.2rem;
        line-height: 1.8;
        color: #f8fafc;
        background: #334155;
        padding: 20px;
        border-radius: 12px;
        border-left: 4px solid #3b82f6;
        margin: 16px 0;
    }
    
    /* Highlight styles for sentence decipher */
    .highlight-desired {
        background: linear-gradient(90deg, #059669 0%, #10b981 100%);
        padding: 2px 8px;
        border-radius: 4px;
        font-weight: 600;
        color: white;
    }
    
    .highlight-have {
        background: linear-gradient(90deg, #d97706 0%, #f59e0b 100%);
        padding: 2px 8px;
        border-radius: 4px;
        font-weight: 600;
        color: white;
    }
    
    .highlight-vehicle {
        background: linear-gradient(90deg, #7c3aed 0%, #8b5cf6 100%);
        padding: 2px 8px;
        border-radius: 4px;
        font-weight: 600;
        color: white;
    }
    
    /* Score display */
    .score-display {
        background: linear-gradient(90deg, #1e40af 0%, #3b82f6 100%);
        padding: 12px 24px;
        border-radius: 12px;
        text-align: center;
        font-size: 1.3rem;
        font-weight: 600;
        color: white;
        margin: 10px 0;
    }
    
    /* Formula box */
    .formula-box {
        background: #0f172a;
        border: 2px solid #3b82f6;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        margin: 16px 0;
    }
    
    /* Mnemonic box */
    .mnemonic-box {
        background: linear-gradient(145deg, #7c3aed 0%, #6d28d9 100%);
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        font-weight: 600;
        color: white;
        margin: 16px 0;
    }
    
    /* Input styling */
    .stNumberInput input, .stTextInput input {
        background: #334155 !important;
        border: 1px solid #475569 !important;
        color: #f8fafc !important;
        border-radius: 8px !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(90deg, #1e40af 0%, #3b82f6 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(90deg, #1d4ed8 0%, #60a5fa 100%);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: #334155 !important;
        border-radius: 8px !important;
        color: #f8fafc !important;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: #1e293b;
        padding: 8px;
        border-radius: 12px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: #334155;
        border-radius: 8px;
        color: #94a3b8;
        padding: 12px 20px;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #1e40af 0%, #3b82f6 100%);
        color: white;
    }
    
    /* Radio button styling */
    .stRadio > div {
        background: #334155;
        padding: 16px;
        border-radius: 12px;
    }
    
    /* Sanity check box */
    .sanity-check {
        background: linear-gradient(145deg, #7f1d1d 0%, #991b1b 50%, #7f1d1d 100%);
        border: 1px solid #ef4444;
        border-radius: 12px;
        padding: 16px;
        margin: 16px 0;
    }
    
    .sanity-check::before {
        content: "⚠️ Common Sense Check: ";
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================

def init_session_state():
    """Initialize all session state variables."""
    defaults = {
        # Scores
        'total_correct': 0,
        'total_attempted': 0,
        
        # Module A - Sentence Decipher
        'sentence_problem': None,
        'sentence_submitted': False,
        'sentence_correct': False,
        
        # Module B - Conversions  
        'conversion_problem': None,
        'conversion_submitted': False,
        'conversion_correct': False,
        
        # Module C - Tablet/Liquid
        'tablet_problem': None,
        'tablet_submitted': False,
        'liquid_problem': None,
        'liquid_submitted': False,
        
        # Module D - Pediatric
        'pediatric_problem': None,
        'pediatric_submitted': False,
        
        # Module E - Infusions/Dilutions
        'infusion_problem': None,
        'infusion_submitted': False,
        'dilution_problem': None,
        'dilution_submitted': False,
        
        # Module F - Cost
        'cost_problem': None,
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_session_state()


# ============================================================================
# SIDEBAR
# ============================================================================

with st.sidebar:
    st.markdown("# 💊 Dosage Master Pro")
    st.markdown("---")
    
    # Score display
    if st.session_state.total_attempted > 0:
        accuracy = (st.session_state.total_correct / st.session_state.total_attempted) * 100
        st.markdown(f"""
        <div class="score-display">
            📊 Score: {st.session_state.total_correct}/{st.session_state.total_attempted} ({accuracy:.0f}%)
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="score-display">
            📊 Score: 0/0
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 📚 Quick Reference")
    
    with st.expander("📐 Core Formula"):
        st.latex(r"X = \frac{\text{Desired}}{\text{Have}} \times \text{Vehicle}")
    
    with st.expander("📏 Unit Conversions"):
        st.markdown("""
        **Weight:**
        - 1000 mcg = 1 mg
        - 1000 mg = 1 g  
        - 1000 g = 1 kg
        
        **Volume:**
        - 1000 mL = 1 L
        - 1 tsp = 5 mL
        - 1 tbsp = 15 mL
        """)
    
    with st.expander("💡 SOLD & LOST"):
        st.markdown("""
        <div class="mnemonic-box">
            <strong>SOLD</strong>: Small to Large = Divide<br>
            <strong>LOST</strong>: Large to Small = Times
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    if st.button("🔄 Reset Score", use_container_width=True):
        st.session_state.total_correct = 0
        st.session_state.total_attempted = 0
        st.rerun()


# ============================================================================
# MAIN CONTENT - TABS
# ============================================================================

st.markdown("# 💊 Dosage Master Pro")
st.markdown("*Master drug calculations through interactive practice*")

tabs = st.tabs([
    "🔍 A: Sentence Decipher",
    "📏 B: Unit Bootcamp", 
    "💊 C: Tablet & Liquid",
    "👶 D: Pediatric Dosing",
    "💉 E: Infusions",
    "💰 F: Cost Savings"
])


# ============================================================================
# MODULE A: SENTENCE DECIPHER
# ============================================================================

with tabs[0]:
    st.markdown("## 🔍 Module A: Sentence Decipher")
    st.markdown("""
    <div class="info-card">
        <h3>🎯 Goal: Learn to Extract Variables from Clinical Text</h3>
        <p>The hardest part of drug calculations isn't the math—it's identifying WHAT numbers to use!</p>
        <ul>
            <li><span class="highlight-desired">Desired (D)</span> = What the patient NEEDS (the order/prescription)</li>
            <li><span class="highlight-have">Have (H)</span> = What concentration/strength you HAVE on hand</li>
            <li><span class="highlight-vehicle">Vehicle (V)</span> = The form it comes in (tablet, mL, etc.)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    
    with col2:
        if st.button("🎲 New Problem", key="new_sentence", use_container_width=True):
            st.session_state.sentence_problem = generate_sentence_problem()
            st.session_state.sentence_submitted = False
            st.session_state.sentence_correct = False
            st.rerun()
    
    # Generate initial problem if none exists
    if st.session_state.sentence_problem is None:
        st.session_state.sentence_problem = generate_sentence_problem()
    
    problem = st.session_state.sentence_problem
    
    # Display the clinical scenario
    st.markdown(f"""
    <div class="scenario-text">
        📋 <strong>Clinical Scenario:</strong><br><br>
        {problem['sentence']}
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Identify the Variables")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<p style="color: #10b981; font-weight: 600;">Desired (D) - What patient needs:</p>', unsafe_allow_html=True)
        user_desired = st.number_input("Enter value:", key="inp_desired", min_value=0.0, step=0.1, format="%.2f")
    
    with col2:
        st.markdown('<p style="color: #f59e0b; font-weight: 600;">Have (H) - Strength on hand:</p>', unsafe_allow_html=True)
        user_have = st.number_input("Enter value:", key="inp_have", min_value=0.0, step=0.1, format="%.2f")
    
    with col3:
        st.markdown('<p style="color: #8b5cf6; font-weight: 600;">Vehicle (V) - Form/Volume:</p>', unsafe_allow_html=True)
        user_vehicle = st.number_input("Enter value:", key="inp_vehicle", min_value=0.0, step=0.1, format="%.2f")
    
    if st.button("✅ Check My Answers", key="check_sentence", use_container_width=True):
        st.session_state.sentence_submitted = True
        
        # Check answers (allow small tolerance for floating point)
        desired_correct = abs(user_desired - problem['desired']) < 0.01
        have_correct = abs(user_have - problem['have']) < 0.01
        vehicle_correct = abs(user_vehicle - problem['vehicle']) < 0.01
        
        all_correct = desired_correct and have_correct and vehicle_correct
        st.session_state.sentence_correct = all_correct
        
        if all_correct:
            st.session_state.total_correct += 1
        st.session_state.total_attempted += 1
    
    if st.session_state.sentence_submitted:
        if st.session_state.sentence_correct:
            st.markdown("""
            <div class="success-card">
                <h3>✅ Excellent! You correctly identified all variables!</h3>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="error-card">
                <h3>❌ Not quite right. Let's review the correct values:</h3>
            </div>
            """, unsafe_allow_html=True)
        
        # Show the formula mapping
        st.markdown("### 📐 Formula Mapping")
        
        st.markdown(f"""
        <div class="formula-box">
            <p style="font-size: 1.1rem; color: #94a3b8; margin-bottom: 12px;">Plugging in the values:</p>
            <div style="font-size: 1.5rem; color: #f8fafc;">
                X = <span class="highlight-desired">{problem['desired']}{problem['desired_unit']}</span> ÷ 
                <span class="highlight-have">{problem['have']}{problem['have_unit']}</span> × 
                <span class="highlight-vehicle">{problem['vehicle']} {problem['vehicle_unit']}</span>
            </div>
            <p style="font-size: 1.3rem; color: #10b981; margin-top: 16px; font-weight: 600;">
                = {problem['answer']} {problem['answer_unit']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("📝 Show Full Working"):
            if problem['formula'] == 'tablets':
                st.markdown(format_working_tablet({
                    'desired': problem['desired'],
                    'have': problem['have'],
                    'answer': problem['answer']
                }))
            elif problem['formula'] == 'liquid':
                st.markdown(format_working_liquid({
                    'desired': problem['desired'],
                    'have': problem['have'],
                    'vehicle': problem['vehicle'],
                    'answer': problem['answer']
                }))
            else:
                st.markdown(format_working_pediatric({
                    'weight': problem.get('weight', 0),
                    'dose_per_kg': problem.get('dose_per_kg', 0),
                    'total_daily': problem['desired'],
                    'frequency': 1,
                    'per_dose': problem['desired'],
                    'have': problem['have'],
                    'vehicle': problem['vehicle'],
                    'volume_per_dose': problem['answer']
                }))
        
        st.markdown(f"""
        <div class="sanity-check">
            {get_sanity_check('tablet' if problem['formula'] == 'tablets' else 'liquid')}
        </div>
        """, unsafe_allow_html=True)


# ============================================================================
# MODULE B: UNIT BOOTCAMP
# ============================================================================

with tabs[1]:
    st.markdown("## 📏 Module B: Unit Bootcamp")
    
    st.markdown("""
    <div class="info-card">
        <h3>🎯 Master Unit Conversions</h3>
        <p>Before you can calculate doses, you MUST be able to convert between units!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Mnemonic display
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="mnemonic-box">
            <h3>📉 SOLD</h3>
            <p>Small to Large = Divide</p>
            <p style="font-size: 0.9rem;">mcg → mg → g → kg</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="mnemonic-box">
            <h3>📈 LOST</h3>
            <p>Large to Small = Times</p>
            <p style="font-size: 0.9rem;">kg → g → mg → mcg</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🎲 New Conversion", key="new_conversion", use_container_width=True):
            st.session_state.conversion_problem = generate_conversion_problem()
            st.session_state.conversion_submitted = False
            st.session_state.conversion_correct = False
            st.rerun()
    
    if st.session_state.conversion_problem is None:
        st.session_state.conversion_problem = generate_conversion_problem()
    
    conv = st.session_state.conversion_problem
    
    st.markdown(f"""
    <div class="scenario-text">
        🔄 Convert: <strong>{conv['value']} {conv['from_unit']}</strong> to <strong>{conv['to_unit']}</strong>
    </div>
    """, unsafe_allow_html=True)
    
    user_answer = st.number_input(
        f"Your answer in {conv['to_unit']}:",
        key="conv_answer",
        min_value=0.0,
        step=0.0001,
        format="%.4f"
    )
    
    if st.button("✅ Check Answer", key="check_conversion", use_container_width=True):
        st.session_state.conversion_submitted = True
        
        # Check with tolerance
        tolerance = abs(conv['answer'] * 0.01)  # 1% tolerance
        is_correct = abs(user_answer - conv['answer']) <= max(tolerance, 0.001)
        st.session_state.conversion_correct = is_correct
        
        if is_correct:
            st.session_state.total_correct += 1
        st.session_state.total_attempted += 1
    
    if st.session_state.conversion_submitted:
        if st.session_state.conversion_correct:
            st.markdown("""
            <div class="success-card">
                <h3>✅ Correct!</h3>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="error-card">
                <h3>❌ Not quite. The correct answer is {conv['answer']} {conv['to_unit']}</h3>
            </div>
            """, unsafe_allow_html=True)
        
        with st.expander("📝 Show Working"):
            st.markdown(format_working_conversion(conv))
        
        st.markdown(f"""
        <div class="sanity-check">
            {get_sanity_check('conversion')}
        </div>
        """, unsafe_allow_html=True)


# ============================================================================
# MODULE C: TABLET & LIQUID DOSAGES
# ============================================================================

with tabs[2]:
    st.markdown("## 💊 Module C: Tablet & Liquid Dosages")
    
    sub_tabs = st.tabs(["💊 Tablets", "🧴 Liquids"])
    
    # TABLETS
    with sub_tabs[0]:
        st.markdown("""
        <div class="info-card">
            <h3>💊 Tablet Calculations</h3>
            <p>Formula: Tablets = Desired ÷ Have</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([3, 1])
        with col2:
            if st.button("🎲 New Problem", key="new_tablet", use_container_width=True):
                st.session_state.tablet_problem = generate_tablet_problem()
                st.session_state.tablet_submitted = False
                st.rerun()
        
        if st.session_state.tablet_problem is None:
            st.session_state.tablet_problem = generate_tablet_problem()
        
        prob = st.session_state.tablet_problem
        
        st.markdown(f"""
        <div class="scenario-text">
            {prob['scenario']}
        </div>
        """, unsafe_allow_html=True)
        
        user_tablets = st.number_input(
            "Number of tablets to give:",
            key="tablet_answer",
            min_value=0.0,
            step=0.5,
            format="%.1f"
        )
        
        if st.button("✅ Check Answer", key="check_tablet", use_container_width=True):
            st.session_state.tablet_submitted = True
            is_correct = abs(user_tablets - prob['answer']) < 0.01
            
            if is_correct:
                st.session_state.total_correct += 1
                st.markdown("""
                <div class="success-card"><h3>✅ Correct!</h3></div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="error-card"><h3>❌ The correct answer is {prob['answer']} tablet(s)</h3></div>
                """, unsafe_allow_html=True)
            
            st.session_state.total_attempted += 1
            
            with st.expander("📝 Show Working"):
                st.markdown(format_working_tablet(prob))
            
            st.markdown(f"""
            <div class="sanity-check">
                {get_sanity_check('tablet')}
            </div>
            """, unsafe_allow_html=True)
    
    # LIQUIDS
    with sub_tabs[1]:
        st.markdown("""
        <div class="info-card">
            <h3>🧴 Liquid Calculations</h3>
            <p>Formula: Volume = (Desired ÷ Have) × Vehicle</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([3, 1])
        with col2:
            if st.button("🎲 New Problem", key="new_liquid", use_container_width=True):
                st.session_state.liquid_problem = generate_liquid_problem()
                st.session_state.liquid_submitted = False
                st.rerun()
        
        if st.session_state.liquid_problem is None:
            st.session_state.liquid_problem = generate_liquid_problem()
        
        prob = st.session_state.liquid_problem
        
        st.markdown(f"""
        <div class="scenario-text">
            {prob['scenario']}
        </div>
        """, unsafe_allow_html=True)
        
        user_volume = st.number_input(
            "Volume to administer (mL):",
            key="liquid_answer",
            min_value=0.0,
            step=0.1,
            format="%.2f"
        )
        
        if st.button("✅ Check Answer", key="check_liquid", use_container_width=True):
            st.session_state.liquid_submitted = True
            is_correct = abs(user_volume - prob['answer']) < 0.1
            
            if is_correct:
                st.session_state.total_correct += 1
                st.markdown("""
                <div class="success-card"><h3>✅ Correct!</h3></div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="error-card"><h3>❌ The correct answer is {prob['answer']}mL</h3></div>
                """, unsafe_allow_html=True)
            
            st.session_state.total_attempted += 1
            
            with st.expander("📝 Show Working"):
                st.markdown(format_working_liquid(prob))
            
            st.markdown(f"""
            <div class="sanity-check">
                {get_sanity_check('liquid')}
            </div>
            """, unsafe_allow_html=True)


# ============================================================================
# MODULE D: PEDIATRIC WEIGHT-BASED DOSING
# ============================================================================

with tabs[3]:
    st.markdown("## 👶 Module D: Pediatric Weight-Based Dosing")
    
    st.markdown("""
    <div class="info-card">
        <h3>🎯 Weight-Based Calculations (mg/kg)</h3>
        <p>Pediatric doses are calculated based on the child's weight. This requires multiple steps!</p>
        <ol>
            <li>Calculate total daily dose: mg/kg × weight</li>
            <li>Divide by frequency (how many times per day)</li>
            <li>Convert to volume if using liquid</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🎲 New Problem", key="new_pediatric", use_container_width=True):
            st.session_state.pediatric_problem = generate_pediatric_problem()
            st.session_state.pediatric_submitted = False
            st.rerun()
    
    if st.session_state.pediatric_problem is None:
        st.session_state.pediatric_problem = generate_pediatric_problem()
    
    prob = st.session_state.pediatric_problem
    
    st.markdown(f"""
    <div class="scenario-text">
        {prob['scenario']}
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 Step-by-Step Entry")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Step 1: Total Daily Dose (mg)**")
        user_daily = st.number_input("Daily dose:", key="ped_daily", min_value=0.0, step=1.0, format="%.1f")
    
    with col2:
        st.markdown("**Step 2: Dose Per Administration (mg)**")
        user_per_dose = st.number_input("Per dose:", key="ped_perdose", min_value=0.0, step=0.1, format="%.2f")
    
    with col3:
        st.markdown("**Step 3: Volume Per Dose (mL)**")
        user_volume = st.number_input("Volume:", key="ped_volume", min_value=0.0, step=0.1, format="%.2f")
    
    if st.button("✅ Check All Steps", key="check_pediatric", use_container_width=True):
        st.session_state.pediatric_submitted = True
        
        daily_correct = abs(user_daily - prob['total_daily']) < 1
        per_dose_correct = abs(user_per_dose - prob['per_dose']) < 0.5
        volume_correct = abs(user_volume - prob['volume_per_dose']) < 0.5
        
        all_correct = daily_correct and per_dose_correct and volume_correct
        
        if all_correct:
            st.session_state.total_correct += 1
            st.markdown("""
            <div class="success-card"><h3>✅ All steps correct! Excellent work!</h3></div>
            """, unsafe_allow_html=True)
        else:
            results = []
            if not daily_correct:
                results.append(f"Step 1: Should be {prob['total_daily']}mg")
            if not per_dose_correct:
                results.append(f"Step 2: Should be {prob['per_dose']}mg")
            if not volume_correct:
                results.append(f"Step 3: Should be {prob['volume_per_dose']}mL")
            
            st.markdown(f"""
            <div class="error-card">
                <h3>❌ Some steps need correction:</h3>
                <ul>{''.join(f'<li>{r}</li>' for r in results)}</ul>
            </div>
            """, unsafe_allow_html=True)
        
        st.session_state.total_attempted += 1
        
        with st.expander("📝 Show Full Working"):
            st.markdown(format_working_pediatric(prob))
        
        st.markdown(f"""
        <div class="sanity-check">
            {get_sanity_check('pediatric')}
        </div>
        """, unsafe_allow_html=True)


# ============================================================================
# MODULE E: INFUSIONS & DILUTIONS
# ============================================================================

with tabs[4]:
    st.markdown("## 💉 Module E: Infusions & Dilutions")
    
    sub_tabs = st.tabs(["💧 IV Drip Rates", "🧪 Dilutions (C₁V₁=C₂V₂)"])
    
    # IV DRIP RATES
    with sub_tabs[0]:
        st.markdown("""
        <div class="info-card">
            <h3>💧 IV Drip Rate Formula</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.latex(r"\text{Drops/min} = \frac{\text{Volume (mL)}}{\text{Time (min)}} \times \text{Drop Factor (gtts/mL)}")
        
        col1, col2 = st.columns([3, 1])
        with col2:
            if st.button("🎲 New Problem", key="new_infusion", use_container_width=True):
                st.session_state.infusion_problem = generate_infusion_problem()
                st.session_state.infusion_submitted = False
                st.rerun()
        
        if st.session_state.infusion_problem is None:
            st.session_state.infusion_problem = generate_infusion_problem()
        
        prob = st.session_state.infusion_problem
        
        st.markdown(f"""
        <div class="scenario-text">
            {prob['scenario']}
        </div>
        """, unsafe_allow_html=True)
        
        user_rate = st.number_input(
            "Drip rate (drops/minute):",
            key="infusion_answer",
            min_value=0.0,
            step=0.5,
            format="%.1f"
        )
        
        if st.button("✅ Check Answer", key="check_infusion", use_container_width=True):
            st.session_state.infusion_submitted = True
            is_correct = abs(user_rate - prob['drops_per_min']) < 1
            
            if is_correct:
                st.session_state.total_correct += 1
                st.markdown("""
                <div class="success-card"><h3>✅ Correct!</h3></div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="error-card"><h3>❌ The correct answer is {prob['drops_per_min']} drops/min</h3></div>
                """, unsafe_allow_html=True)
            
            st.session_state.total_attempted += 1
            
            with st.expander("📝 Show Working"):
                st.markdown(format_working_infusion(prob))
            
            st.markdown(f"""
            <div class="sanity-check">
                {get_sanity_check('infusion')}
            </div>
            """, unsafe_allow_html=True)
    
    # DILUTIONS
    with sub_tabs[1]:
        st.markdown("""
        <div class="info-card">
            <h3>🧪 Dilution Formula</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.latex(r"C_1V_1 = C_2V_2")
        st.markdown("""
        Where:
        - **C₁** = Concentration of stock solution
        - **V₁** = Volume of stock solution needed
        - **C₂** = Desired final concentration
        - **V₂** = Desired final volume
        """)
        
        col1, col2 = st.columns([3, 1])
        with col2:
            if st.button("🎲 New Problem", key="new_dilution", use_container_width=True):
                st.session_state.dilution_problem = generate_dilution_problem()
                st.session_state.dilution_submitted = False
                st.rerun()
        
        if st.session_state.dilution_problem is None:
            st.session_state.dilution_problem = generate_dilution_problem()
        
        prob = st.session_state.dilution_problem
        
        st.markdown(f"""
        <div class="scenario-text">
            {prob['scenario']}
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            user_stock = st.number_input(
                "Stock solution volume (mL):",
                key="dilution_stock",
                min_value=0.0,
                step=0.1,
                format="%.2f"
            )
        with col2:
            user_diluent = st.number_input(
                "Diluent volume (mL):",
                key="dilution_diluent",
                min_value=0.0,
                step=0.1,
                format="%.2f"
            )
        
        if st.button("✅ Check Answer", key="check_dilution", use_container_width=True):
            st.session_state.dilution_submitted = True
            
            stock_correct = abs(user_stock - prob['v1']) < 0.5
            diluent_correct = abs(user_diluent - prob['diluent']) < 0.5
            
            if stock_correct and diluent_correct:
                st.session_state.total_correct += 1
                st.markdown("""
                <div class="success-card"><h3>✅ Both values correct!</h3></div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="error-card">
                    <h3>❌ Correct values:</h3>
                    <p>Stock: {prob['v1']}mL | Diluent: {prob['diluent']}mL</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.session_state.total_attempted += 1
            
            with st.expander("📝 Show Working"):
                st.markdown(format_working_dilution(prob))
            
            st.markdown(f"""
            <div class="sanity-check">
                {get_sanity_check('dilution')}
            </div>
            """, unsafe_allow_html=True)


# ============================================================================
# MODULE F: PHARMACOECONOMICS
# ============================================================================

with tabs[5]:
    st.markdown("## 💰 Module F: Pharmacoeconomics - Cost Savings")
    
    st.markdown("""
    <div class="info-card">
        <h3>🎯 Calculate Medication Cost Savings</h3>
        <p>Switching from branded to generic medications can save significant money. Learn to calculate these savings!</p>
    </div>
    """, unsafe_allow_html=True)
    
    mode = st.radio(
        "Choose mode:",
        ["📝 Practice Problem", "🧮 Custom Calculator"],
        horizontal=True
    )
    
    if mode == "📝 Practice Problem":
        col1, col2 = st.columns([3, 1])
        with col2:
            if st.button("🎲 New Problem", key="new_cost", use_container_width=True):
                st.session_state.cost_problem = generate_cost_problem()
                st.rerun()
        
        if st.session_state.cost_problem is None:
            st.session_state.cost_problem = generate_cost_problem()
        
        prob = st.session_state.cost_problem
        
        st.markdown(f"""
        <div class="scenario-text">
            {prob['scenario']}
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### Calculate the following:")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            user_saving = st.number_input("Saving per pack (£):", key="cost_saving", min_value=0.0, step=0.01, format="%.2f")
        
        with col2:
            user_percent = st.number_input("Percentage reduction (%):", key="cost_percent", min_value=0.0, max_value=100.0, step=0.1, format="%.1f")
        
        with col3:
            user_weekly = st.number_input("Weekly saving (£):", key="cost_weekly", min_value=0.0, step=0.01, format="%.2f")
        
        if st.button("✅ Check Answers", key="check_cost", use_container_width=True):
            saving_correct = abs(user_saving - prob['saving_per_pack']) < 0.05
            percent_correct = abs(user_percent - prob['percentage_reduction']) < 1
            weekly_correct = abs(user_weekly - prob['weekly_saving']) < 0.1
            
            all_correct = saving_correct and percent_correct and weekly_correct
            
            if all_correct:
                st.session_state.total_correct += 1
                st.markdown("""
                <div class="success-card"><h3>✅ All calculations correct!</h3></div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="error-card">
                    <h3>❌ Correct values:</h3>
                    <p>Saving: £{prob['saving_per_pack']} | Reduction: {prob['percentage_reduction']}% | Weekly: £{prob['weekly_saving']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.session_state.total_attempted += 1
            
            with st.expander("📝 Show Working"):
                st.markdown(format_working_cost(prob))
            
            st.markdown(f"""
            <div class="sanity-check">
                {get_sanity_check('cost')}
            </div>
            """, unsafe_allow_html=True)
    
    else:  # Custom Calculator
        st.markdown("### 🧮 Enter Your Own Values")
        
        col1, col2 = st.columns(2)
        
        with col1:
            brand_cost = st.number_input("Brand cost (£):", min_value=0.01, value=30.00, step=0.01, format="%.2f")
            pack_size = st.number_input("Tablets per pack:", min_value=1, value=28, step=1)
        
        with col2:
            generic_cost = st.number_input("Generic cost (£):", min_value=0.01, value=10.00, step=0.01, format="%.2f")
            doses_per_day = st.number_input("Doses per day:", min_value=1, value=1, step=1)
        
        if st.button("📊 Calculate Savings", use_container_width=True):
            saving_per_pack = brand_cost - generic_cost
            percentage = (saving_per_pack / brand_cost) * 100 if brand_cost > 0 else 0
            days_supply = pack_size // doses_per_day
            weekly = (saving_per_pack / days_supply) * 7 if days_supply > 0 else 0
            annual = saving_per_pack * (365 / days_supply) if days_supply > 0 else 0
            
            st.markdown(f"""
            <div class="success-card">
                <h3>📊 Cost Analysis Results</h3>
                <table style="width:100%; color: white;">
                    <tr><td>Saving per pack:</td><td><strong>£{saving_per_pack:.2f}</strong></td></tr>
                    <tr><td>Percentage reduction:</td><td><strong>{percentage:.1f}%</strong></td></tr>
                    <tr><td>Days supply per pack:</td><td><strong>{days_supply} days</strong></td></tr>
                    <tr><td>Weekly saving:</td><td><strong>£{weekly:.2f}</strong></td></tr>
                    <tr><td>Annual saving:</td><td><strong>£{annual:.2f}</strong></td></tr>
                </table>
            </div>
            """, unsafe_allow_html=True)


# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; padding: 20px;">
    <p>💊 <strong>Dosage Master Pro</strong> | Educational Tool for Clinical Calculations</p>
    <p style="font-size: 0.8rem;">Always double-check calculations in clinical practice. This tool is for educational purposes only.</p>
</div>
""", unsafe_allow_html=True)
