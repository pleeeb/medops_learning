"""
Dosage Master Pro - Utility Functions
Helper functions for generating practice problems and formatting solutions.
EXPANDED VERSION: ~20+ unique scenarios per module
"""

import random
from typing import Dict, Tuple, List, Any


# ============================================================================
# EXPANDED DRUG DATABASE - More realistic variety
# ============================================================================

DRUGS = {
    "antibiotics": [
        "Amoxicillin", "Cephalexin", "Azithromycin", "Ciprofloxacin", 
        "Metronidazole", "Clarithromycin", "Doxycycline", "Flucloxacillin",
        "Co-amoxiclav", "Trimethoprim"
    ],
    "analgesics": [
        "Paracetamol", "Ibuprofen", "Codeine", "Tramadol", 
        "Morphine", "Diclofenac", "Naproxen", "Co-codamol"
    ],
    "cardiovascular": [
        "Atenolol", "Bisoprolol", "Amlodipine", "Lisinopril", 
        "Ramipril", "Losartan", "Furosemide", "Digoxin"
    ],
    "psychiatric": [
        "Sertraline", "Fluoxetine", "Citalopram", "Amitriptyline",
        "Diazepam", "Lorazepam", "Olanzapine", "Risperidone"
    ],
    "pediatric_common": [
        "Amoxicillin", "Ibuprofen", "Paracetamol", "Cefalexin",
        "Azithromycin", "Clarithromycin", "Phenoxymethylpenicillin"
    ],
    "iv_fluids": [
        "Normal Saline (0.9%)", "Dextrose 5%", "Hartmann's Solution",
        "Dextrose Saline", "Potassium Chloride Infusion", "Plasma-Lyte"
    ]
}

def get_random_drug(category: str = None) -> str:
    """Get a random drug name, optionally from a specific category."""
    if category and category in DRUGS:
        return random.choice(DRUGS[category])
    all_drugs = [drug for drugs in DRUGS.values() for drug in drugs]
    return random.choice(all_drugs)


# ============================================================================
# EXPANDED CLINICAL SENTENCE TEMPLATES (20+ variations)
# ============================================================================

SENTENCE_TEMPLATES_TABLET = [
    "The doctor orders {desired}mg of {drug}. Each tablet contains {have}mg.",
    "Prescribe {desired}mg of {drug} stat. Available: {have}mg tablets.",
    "Give {drug} {desired}mg PO. You have {have}mg tablets on the ward.",
    "Patient requires {desired}mg {drug}. Stock shows {have}mg tablets available.",
    "Administer {desired}mg of {drug} orally. Tablets on hand: {have}mg each.",
    "{drug} {desired}mg is ordered for pain relief. Available strength: {have}mg per tablet.",
    "The prescription reads: {drug} {desired}mg. The pharmacy supplies {have}mg tablets.",
    "Morning medication round: {drug} {desired}mg needed. Ward stock: {have}mg tablets.",
    "Post-operative order: {drug} {desired}mg. Available: {have}mg tablets.",
    "PRN medication: Give {desired}mg of {drug}. Each tablet is {have}mg.",
]

SENTENCE_TEMPLATES_LIQUID = [
    "Administer {desired}mg of {drug} orally. The suspension contains {have}mg per {vehicle}mL.",
    "Give {drug} {desired}mg. Available as liquid: {have}mg/{vehicle}mL.",
    "Prescribe {desired}mg {drug} syrup. Concentration: {have}mg in {vehicle}mL.",
    "The patient needs {desired}mg of {drug} elixir. Stock: {have}mg per {vehicle}mL.",
    "Order: {drug} {desired}mg oral solution. Available: {have}mg/{vehicle}mL.",
    "Give {desired}mg of {drug} liquid. The bottle states {have}mg per {vehicle}mL.",
    "Administer {drug} suspension {desired}mg. Label reads: {have}mg/{vehicle}mL.",
    "{drug} oral solution {desired}mg is required. You have {have}mg/{vehicle}mL in stock.",
    "The child needs {drug} {desired}mg. Liquid available: {have}mg per {vehicle}mL.",
    "Medication order: {drug} {desired}mg PO as liquid. Strength: {have}mg/{vehicle}mL.",
]

SENTENCE_TEMPLATES_PEDIATRIC = [
    "A child weighing {weight}kg is prescribed {dose_per_kg}mg/kg of {drug}. You have {have}mg/{have_vol}mL available.",
    "Pediatric patient, {weight}kg, requires {drug} at {dose_per_kg}mg/kg. Stock: {have}mg/{have_vol}mL.",
    "Calculate dose for a {weight}kg child. Order: {drug} {dose_per_kg}mg/kg. Available: {have}mg/{have_vol}mL.",
    "A baby weighing {weight}kg needs {drug}. Dose: {dose_per_kg}mg/kg. Suspension: {have}mg/{have_vol}mL.",
    "Child's weight: {weight}kg. Prescribe {drug} at {dose_per_kg}mg/kg. You have {have}mg/{have_vol}mL.",
    "The pediatrician orders {drug} {dose_per_kg}mg/kg for a {weight}kg toddler. Available: {have}mg/{have_vol}mL.",
    "Infant weight: {weight}kg. Required: {drug} {dose_per_kg}mg/kg. Stock suspension: {have}mg/{have_vol}mL.",
    "A {weight}kg child presents with infection. Prescribe {drug} {dose_per_kg}mg/kg. Have: {have}mg/{have_vol}mL.",
    "Pediatric dosing: {weight}kg patient, {drug} at {dose_per_kg}mg/kg/day. Liquid: {have}mg/{have_vol}mL.",
    "Young patient weighs {weight}kg. Order: {drug} {dose_per_kg}mg/kg. Available liquid: {have}mg/{have_vol}mL.",
]


# ============================================================================
# MODULE A: EXPANDED SENTENCE DECIPHER PROBLEMS (20+ unique)
# ============================================================================

def generate_sentence_problem() -> Dict[str, Any]:
    """Generate a clinical sentence problem for the Sentence Decipher module."""
    problem_type = random.choice(["tablet", "tablet", "liquid", "liquid", "pediatric"])
    
    if problem_type == "tablet":
        # Expanded tablet strengths and doses for variety
        tablet_combos = [
            (50, 25), (100, 25), (100, 50), (150, 50), (200, 100),
            (250, 125), (300, 100), (500, 250), (750, 250), (1000, 500),
            (75, 25), (125, 125), (200, 50), (375, 125), (625, 125),
            (400, 200), (600, 300), (800, 400), (150, 75), (225, 75),
        ]
        desired, have = random.choice(tablet_combos)
        drug = get_random_drug()
        template = random.choice(SENTENCE_TEMPLATES_TABLET)
        sentence = template.format(desired=desired, drug=drug, have=have)
        
        return {
            "sentence": sentence,
            "desired": desired,
            "desired_unit": "mg",
            "have": have,
            "have_unit": "mg",
            "vehicle": 1,
            "vehicle_unit": "tablet",
            "answer": desired / have,
            "answer_unit": "tablets",
            "formula": "tablets",
            "drug": drug
        }
    
    elif problem_type == "liquid":
        # Expanded liquid concentrations
        liquid_combos = [
            # (desired, have, vehicle)
            (100, 100, 5), (125, 125, 5), (150, 100, 5), (200, 100, 5),
            (250, 125, 5), (250, 250, 5), (300, 250, 5), (375, 125, 5),
            (400, 200, 5), (500, 250, 5), (500, 500, 10), (600, 200, 5),
            (750, 250, 5), (100, 200, 10), (150, 250, 5), (200, 250, 10),
            (80, 160, 5), (120, 240, 5), (180, 120, 5), (225, 150, 5),
        ]
        desired, have, vehicle = random.choice(liquid_combos)
        drug = get_random_drug()
        template = random.choice(SENTENCE_TEMPLATES_LIQUID)
        sentence = template.format(desired=desired, drug=drug, have=have, vehicle=vehicle)
        answer = (desired / have) * vehicle
        
        return {
            "sentence": sentence,
            "desired": desired,
            "desired_unit": "mg",
            "have": have,
            "have_unit": "mg",
            "vehicle": vehicle,
            "vehicle_unit": "mL",
            "answer": round(answer, 2),
            "answer_unit": "mL",
            "formula": "liquid",
            "drug": drug
        }
    
    else:  # pediatric
        weight = random.choice([5, 6, 7, 8, 9, 10, 12, 14, 15, 18, 20, 22, 25, 28, 30, 32, 35, 38, 40])
        dose_per_kg = random.choice([5, 7.5, 10, 12.5, 15, 20, 25, 30, 40, 50])
        have = random.choice([100, 125, 200, 250])
        have_vol = random.choice([5, 10])
        drug = get_random_drug("pediatric_common")
        
        total_dose = weight * dose_per_kg
        answer = (total_dose / have) * have_vol
        
        template = random.choice(SENTENCE_TEMPLATES_PEDIATRIC)
        sentence = template.format(weight=weight, dose_per_kg=dose_per_kg, drug=drug, have=have, have_vol=have_vol)
        
        return {
            "sentence": sentence,
            "weight": weight,
            "dose_per_kg": dose_per_kg,
            "desired": total_dose,
            "desired_unit": "mg",
            "have": have,
            "have_unit": "mg",
            "vehicle": have_vol,
            "vehicle_unit": "mL",
            "answer": round(answer, 2),
            "answer_unit": "mL",
            "formula": "pediatric",
            "drug": drug
        }


# ============================================================================
# MODULE B: EXPANDED UNIT CONVERSION PROBLEMS (20+ unique)
# ============================================================================

# Expanded value sets for conversions
CONVERSION_VALUES = {
    "mcg": [100, 200, 250, 400, 500, 750, 800, 1000, 1200, 1500, 2000, 2500, 3000, 4000, 5000, 6000, 7500, 8000, 10000],
    "mg": [50, 100, 125, 150, 200, 250, 300, 400, 500, 600, 750, 800, 1000, 1250, 1500, 2000, 2500, 3000],
    "g": [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7.5, 10],
    "kg": [0.1, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 2, 2.5, 3, 3.5, 4, 5],
    "mL": [50, 100, 150, 200, 250, 300, 400, 500, 600, 750, 800, 1000, 1250, 1500, 2000, 2500, 3000],
    "L": [0.1, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 2, 2.5, 3, 4, 5],
}

CONVERSION_MNEMONICS = {
    "small_to_large": "SOLD: Small to Large = Divide",
    "large_to_small": "LOST: Large to Small = Times (Multiply)"
}

HOUSEHOLD_CONVERSIONS = {
    "teaspoon": 5,
    "tablespoon": 15,
    "ounce": 30,
    "cup": 240,
}


def generate_conversion_problem() -> Dict[str, Any]:
    """Generate a unit conversion problem with expanded variety."""
    conversion_type = random.choice(["metric", "metric", "metric", "household"])
    
    if conversion_type == "metric":
        conversions = [
            ("mcg", "mg", 1000, "divide"),
            ("mg", "mcg", 1000, "multiply"),
            ("mg", "g", 1000, "divide"),
            ("g", "mg", 1000, "multiply"),
            ("g", "kg", 1000, "divide"),
            ("kg", "g", 1000, "multiply"),
            ("mL", "L", 1000, "divide"),
            ("L", "mL", 1000, "multiply"),
        ]
        
        from_unit, to_unit, factor, operation = random.choice(conversions)
        value = random.choice(CONVERSION_VALUES[from_unit])
        
        if operation == "divide":
            answer = value / factor
            mnemonic = CONVERSION_MNEMONICS["small_to_large"]
        else:
            answer = value * factor
            mnemonic = CONVERSION_MNEMONICS["large_to_small"]
        
        return {
            "type": "metric",
            "value": value,
            "from_unit": from_unit,
            "to_unit": to_unit,
            "factor": factor,
            "operation": operation,
            "answer": round(answer, 4),
            "mnemonic": mnemonic
        }
    
    else:  # household
        conversions = [
            ("teaspoons", "mL", 5, "multiply"),
            ("tablespoons", "mL", 15, "multiply"),
            ("mL", "teaspoons", 5, "divide"),
            ("mL", "tablespoons", 15, "divide"),
            ("ounces", "mL", 30, "multiply"),
            ("mL", "ounces", 30, "divide"),
            ("cups", "mL", 240, "multiply"),
            ("mL", "cups", 240, "divide"),
        ]
        
        from_unit, to_unit, factor, operation = random.choice(conversions)
        
        if from_unit in ["teaspoons", "tablespoons"]:
            value = random.choice([0.5, 1, 1.5, 2, 2.5, 3, 4, 5])
        elif from_unit == "ounces":
            value = random.choice([0.5, 1, 2, 3, 4, 6, 8])
        elif from_unit == "cups":
            value = random.choice([0.25, 0.5, 0.75, 1, 1.5, 2])
        else:  # mL
            value = random.choice([2.5, 5, 7.5, 10, 15, 20, 30, 45, 60, 90, 120, 240])
        
        if operation == "divide":
            answer = value / factor
        else:
            answer = value * factor
        
        return {
            "type": "household",
            "value": value,
            "from_unit": from_unit,
            "to_unit": to_unit,
            "factor": factor,
            "operation": operation,
            "answer": round(answer, 2),
            "mnemonic": "Common conversions: 1 tsp = 5mL, 1 tbsp = 15mL, 1 oz ≈ 30mL, 1 cup ≈ 240mL"
        }


# ============================================================================
# MODULE C: EXPANDED TABLET & LIQUID DOSAGES (20+ unique each)
# ============================================================================

TABLET_SCENARIOS = [
    "A patient is prescribed {desired}mg of {drug}. You have {have}mg tablets available.",
    "The doctor orders {drug} {desired}mg stat. Each tablet contains {have}mg.",
    "Give {desired}mg of {drug} for pain relief. Available tablets: {have}mg each.",
    "Post-surgery order: {drug} {desired}mg. Ward stock: {have}mg tablets.",
    "The patient needs {drug} {desired}mg for their morning dose. Tablets available: {have}mg.",
    "Prescribe {desired}mg {drug} now. You have {have}mg scored tablets.",
    "Medication round: {drug} {desired}mg required. Each tablet is {have}mg.",
    "PRN order: {drug} {desired}mg for anxiety. Stock shows {have}mg tablets.",
    "Evening medication: {desired}mg of {drug}. Available strength: {have}mg per tablet.",
    "The prescription states {drug} {desired}mg orally. The pharmacy sent {have}mg tablets.",
]

LIQUID_SCENARIOS = [
    "Prescribe {desired}mg of {drug} oral suspension. Available: {have}mg/{vehicle}mL.",
    "Give {drug} {desired}mg. The elixir concentration is {have}mg per {vehicle}mL.",
    "A child requires {drug} {desired}mg. Syrup available: {have}mg/{vehicle}mL.",
    "Administer {desired}mg {drug} solution. The bottle states {have}mg in {vehicle}mL.",
    "The patient cannot swallow tablets. Give {drug} {desired}mg as liquid ({have}mg/{vehicle}mL).",
    "Pediatric order: {drug} {desired}mg. Suspension strength: {have}mg per {vehicle}mL.",
    "Calculate volume for {drug} {desired}mg. Solution concentration: {have}mg/{vehicle}mL.",
    "The nurse needs to give {desired}mg of {drug}. Liquid available: {have}mg/{vehicle}mL.",
    "Medication order: {drug} {desired}mg as oral liquid. Stock: {have}mg/{vehicle}mL.",
    "For easier administration, give {drug} {desired}mg as syrup ({have}mg per {vehicle}mL).",
]


def generate_tablet_problem() -> Dict[str, Any]:
    """Generate a tablet dosage calculation problem with expanded variety."""
    drug = get_random_drug()
    
    # Expanded tablet combinations
    tablet_combos = [
        (50, 25), (100, 50), (150, 50), (200, 100), (250, 125),
        (300, 100), (400, 200), (500, 250), (600, 200), (750, 250),
        (1000, 500), (75, 25), (125, 125), (375, 125), (625, 125),
        (100, 25), (200, 50), (300, 150), (400, 100), (500, 100),
        (150, 75), (225, 75), (450, 150), (600, 300), (900, 300),
    ]
    desired, have = random.choice(tablet_combos)
    answer = desired / have
    
    scenario = random.choice(TABLET_SCENARIOS).format(desired=desired, drug=drug, have=have)
    
    return {
        "drug": drug,
        "desired": desired,
        "have": have,
        "answer": answer,
        "scenario": scenario + " How many tablets should you give?",
    }


def generate_liquid_problem() -> Dict[str, Any]:
    """Generate a liquid dosage calculation problem with expanded variety."""
    drug = get_random_drug()
    
    # Expanded liquid combinations
    liquid_combos = [
        (100, 100, 5), (125, 125, 5), (150, 100, 5), (200, 100, 5),
        (250, 125, 5), (250, 250, 5), (300, 200, 5), (375, 125, 5),
        (400, 200, 5), (500, 250, 5), (600, 200, 5), (750, 250, 5),
        (100, 200, 10), (200, 400, 10), (500, 500, 10), (300, 150, 5),
        (180, 120, 5), (240, 160, 5), (360, 240, 5), (80, 80, 5),
        (50, 100, 5), (75, 150, 5), (175, 350, 10), (225, 450, 10),
    ]
    desired, have, vehicle = random.choice(liquid_combos)
    answer = (desired / have) * vehicle
    
    scenario = random.choice(LIQUID_SCENARIOS).format(desired=desired, drug=drug, have=have, vehicle=vehicle)
    
    return {
        "drug": drug,
        "desired": desired,
        "have": have,
        "vehicle": vehicle,
        "answer": round(answer, 2),
        "scenario": scenario + " Calculate the volume to administer.",
    }


# ============================================================================
# MODULE D: EXPANDED PEDIATRIC WEIGHT-BASED DOSING (20+ unique)
# ============================================================================

PEDIATRIC_SCENARIOS = [
    "A child weighing {weight}kg is prescribed {drug} at {dose_per_kg}mg/kg/day, given {freq_text}. Available: {have}mg/{vehicle}mL suspension.",
    "Pediatric patient ({weight}kg) requires {drug}. Dose: {dose_per_kg}mg/kg/day {freq_text}. Stock: {have}mg/{vehicle}mL.",
    "Calculate the dose for a {weight}kg child. Order: {drug} {dose_per_kg}mg/kg/day in {freq_text} doses. Have: {have}mg/{vehicle}mL.",
    "The pediatrician prescribes {drug} {dose_per_kg}mg/kg/day for a {weight}kg patient. Give {freq_text}. Liquid: {have}mg/{vehicle}mL.",
    "Infant weight: {weight}kg. Order: {drug} {dose_per_kg}mg/kg/day divided {freq_text}. Available: {have}mg/{vehicle}mL.",
    "A {weight}kg toddler needs {drug}. Recommended dose: {dose_per_kg}mg/kg/day ({freq_text}). Suspension: {have}mg/{vehicle}mL.",
    "Child's weight: {weight}kg. Prescribe {drug} {dose_per_kg}mg/kg/day in {freq_text} divided doses. Stock: {have}mg/{vehicle}mL.",
    "For this {weight}kg pediatric patient, give {drug} {dose_per_kg}mg/kg/day. Frequency: {freq_text}. Liquid: {have}mg/{vehicle}mL.",
    "The child weighs {weight}kg and needs {drug} at {dose_per_kg}mg/kg daily. Divide into {freq_text} doses. Have: {have}mg/{vehicle}mL.",
    "Young patient: {weight}kg. Drug: {drug} {dose_per_kg}mg/kg/day. Administration: {freq_text}. Available: {have}mg/{vehicle}mL.",
]


def generate_pediatric_problem() -> Dict[str, Any]:
    """Generate a pediatric weight-based dosing problem with expanded variety."""
    drug = get_random_drug("pediatric_common")
    
    # Expanded weight range with realistic pediatric values
    weights = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 22, 24, 25, 28, 30, 32, 35, 38, 40]
    weight = random.choice(weights)
    
    # Expanded dose per kg values
    doses_per_kg = [5, 7.5, 10, 12.5, 15, 20, 25, 30, 40, 50, 60]
    dose_per_kg = random.choice(doses_per_kg)
    
    # Frequency options
    frequencies = [
        (1, "once daily"),
        (2, "twice daily (BD)"),
        (3, "three times daily (TDS)"),
        (4, "four times daily (QDS)"),
        (2, "every 12 hours"),
        (3, "every 8 hours"),
        (4, "every 6 hours"),
    ]
    freq_num, freq_text = random.choice(frequencies)
    
    # Calculate
    total_daily = weight * dose_per_kg
    per_dose = total_daily / freq_num
    
    # Expanded concentrations
    concentrations = [(100, 5), (125, 5), (200, 5), (250, 5), (125, 10), (250, 10)]
    have, vehicle = random.choice(concentrations)
    
    volume_per_dose = (per_dose / have) * vehicle
    
    scenario = random.choice(PEDIATRIC_SCENARIOS).format(
        weight=weight, drug=drug, dose_per_kg=dose_per_kg, 
        freq_text=freq_text, have=have, vehicle=vehicle
    )
    
    return {
        "drug": drug,
        "weight": weight,
        "dose_per_kg": dose_per_kg,
        "frequency": freq_num,
        "frequency_text": freq_text,
        "total_daily": total_daily,
        "per_dose": round(per_dose, 2),
        "have": have,
        "vehicle": vehicle,
        "volume_per_dose": round(volume_per_dose, 2),
        "scenario": scenario,
    }


# ============================================================================
# MODULE E: EXPANDED INFUSIONS & DILUTIONS (20+ unique each)
# ============================================================================

INFUSION_SCENARIOS = [
    "Infuse {volume}mL of {drug} over {time_hours} hour(s). The giving set delivers {drop_factor} drops/mL.",
    "Set up an IV infusion of {drug} ({volume}mL) to run over {time_hours} hours. Drop factor: {drop_factor} gtts/mL.",
    "The patient needs {volume}mL of {drug} infused in {time_hours} hour(s). Using a {drop_factor} drops/mL giving set.",
    "Prepare {drug} {volume}mL IV over {time_hours} hours. The administration set has a drop factor of {drop_factor}.",
    "Run {volume}mL {drug} over {time_hours} hours. Drip set delivers {drop_factor} drops per mL.",
    "Doctor orders: {drug} {volume}mL IV to infuse over {time_hours} hours. Drop factor = {drop_factor} gtts/mL.",
    "Calculate drip rate for {volume}mL of {drug} over {time_hours} hours. Set: {drop_factor} drops/mL.",
    "IV order: {drug} {volume}mL. Time: {time_hours} hours. Administration set: {drop_factor} gtts/mL.",
    "Patient requires {drug} infusion. Volume: {volume}mL. Duration: {time_hours} hours. Set: {drop_factor} drops/mL.",
    "Infusion needed: {volume}mL {drug} over {time_hours} hours using a {drop_factor} drop/mL giving set.",
]

DILUTION_SCENARIOS = [
    "You have a stock solution of {c1}mg/mL. You need to prepare {v2}mL of a {c2}mg/mL solution.",
    "Prepare {v2}mL of {c2}mg/mL solution from {c1}mg/mL stock.",
    "A {c2}mg/mL solution ({v2}mL) is required. You have {c1}mg/mL concentrate available.",
    "Dilute {c1}mg/mL stock to make {v2}mL of {c2}mg/mL concentration.",
    "The order calls for {v2}mL of a {c2}mg/mL solution. Stock concentration: {c1}mg/mL.",
    "From {c1}mg/mL stock, prepare {v2}mL at {c2}mg/mL concentration.",
    "You need {v2}mL of {c2}mg/mL solution. Available: {c1}mg/mL concentrated stock.",
    "Calculate dilution: Need {v2}mL of {c2}mg/mL from {c1}mg/mL stock solution.",
    "Prepare a {c2}mg/mL dilution. Final volume: {v2}mL. Stock: {c1}mg/mL.",
    "Mix {c1}mg/mL stock solution to get {v2}mL at {c2}mg/mL final concentration.",
]


def generate_infusion_problem() -> Dict[str, Any]:
    """Generate an IV infusion drip rate problem with expanded variety."""
    drug = get_random_drug("iv_fluids")
    
    # Expanded volume/time combinations
    infusion_combos = [
        (100, 1), (100, 2), (250, 2), (250, 4), (500, 4),
        (500, 6), (500, 8), (1000, 6), (1000, 8), (1000, 12),
        (1000, 24), (500, 3), (250, 3), (100, 0.5), (50, 0.5),
        (250, 1), (500, 2), (750, 6), (1500, 12), (2000, 24),
    ]
    volume, time_hours = random.choice(infusion_combos)
    time_minutes = int(time_hours * 60)
    
    # Drop factors
    drop_factors = [10, 15, 20, 60]
    drop_factor = random.choice(drop_factors)
    
    drops_per_min = (volume / time_minutes) * drop_factor
    
    scenario = random.choice(INFUSION_SCENARIOS).format(
        volume=volume, drug=drug, time_hours=time_hours, drop_factor=drop_factor
    )
    
    return {
        "drug": drug,
        "volume": volume,
        "time_hours": time_hours,
        "time_minutes": time_minutes,
        "drop_factor": drop_factor,
        "drops_per_min": round(drops_per_min, 1),
        "scenario": scenario + " Calculate the drip rate in drops/minute.",
    }


def generate_dilution_problem() -> Dict[str, Any]:
    """Generate a dilution problem with expanded variety."""
    # Expanded concentration combinations
    dilution_combos = [
        # (c1, c2, v2)
        (10, 1, 100), (10, 2, 100), (10, 5, 100), (20, 2, 100),
        (20, 4, 100), (20, 5, 100), (50, 5, 100), (50, 10, 100),
        (100, 10, 100), (100, 20, 100), (100, 25, 100), (50, 5, 250),
        (50, 10, 250), (100, 10, 250), (100, 25, 250), (20, 4, 500),
        (50, 10, 500), (100, 20, 500), (200, 50, 100), (40, 8, 250),
    ]
    c1, c2, v2 = random.choice(dilution_combos)
    
    v1 = (c2 * v2) / c1
    diluent = v2 - v1
    
    scenario = random.choice(DILUTION_SCENARIOS).format(c1=c1, c2=c2, v2=v2)
    
    return {
        "c1": c1,
        "v1": round(v1, 2),
        "c2": c2,
        "v2": v2,
        "diluent": round(diluent, 2),
        "scenario": scenario + " How much stock solution and diluent do you need?",
    }


# ============================================================================
# MODULE F: EXPANDED PHARMACOECONOMICS (20+ unique)
# ============================================================================

DRUG_COST_PAIRS = [
    ("Lipitor (Atorvastatin)", "Generic Atorvastatin"),
    ("Nexium (Esomeprazole)", "Generic Esomeprazole"),
    ("Crestor (Rosuvastatin)", "Generic Rosuvastatin"),
    ("Zocor (Simvastatin)", "Generic Simvastatin"),
    ("Plavix (Clopidogrel)", "Generic Clopidogrel"),
    ("Singulair (Montelukast)", "Generic Montelukast"),
    ("Zyrtec (Cetirizine)", "Generic Cetirizine"),
    ("Prilosec (Omeprazole)", "Generic Omeprazole"),
    ("Prozac (Fluoxetine)", "Generic Fluoxetine"),
    ("Zoloft (Sertraline)", "Generic Sertraline"),
    ("Brand Medication A", "Generic Alternative A"),
    ("Branded Drug B", "Off-Patent Drug B"),
    ("Original Medicine C", "Biosimilar C"),
    ("Innovator Drug D", "Generic Equivalent D"),
    ("Premium Brand E", "Budget Alternative E"),
]

COST_SCENARIOS = [
    "{brand} costs £{brand_cost} for {pack_size} tablets. {generic} costs £{generic_cost} for the same quantity.",
    "Compare: {brand} at £{brand_cost}/{pack_size} tablets vs {generic} at £{generic_cost}/{pack_size} tablets.",
    "The pharmacist offers a switch from {brand} (£{brand_cost}) to {generic} (£{generic_cost}) per {pack_size} tablets.",
    "{brand}: £{brand_cost} per pack of {pack_size}. Alternative: {generic} at £{generic_cost} per {pack_size}.",
    "Monthly medication costs: {brand} £{brand_cost} vs {generic} £{generic_cost} (both for {pack_size} tablets).",
    "Patient currently on {brand} (£{brand_cost}/{pack_size}). GP suggests switching to {generic} (£{generic_cost}/{pack_size}).",
    "Drug costs comparison: {pack_size} tablets of {brand} = £{brand_cost}, {generic} = £{generic_cost}.",
    "Calculate savings when switching from {brand} (£{brand_cost}) to {generic} (£{generic_cost}) for {pack_size} tablets.",
    "NHS cost review: {brand} £{brand_cost} per {pack_size} tabs, {generic} £{generic_cost} per {pack_size} tabs.",
    "Prescription swap: {brand} currently £{brand_cost}, switch to {generic} at £{generic_cost} ({pack_size} tablets).",
]


def generate_cost_problem() -> Dict[str, Any]:
    """Generate a pharmacoeconomics cost comparison problem with expanded variety."""
    brand_name, generic_name = random.choice(DRUG_COST_PAIRS)
    
    # Pack sizes
    pack_sizes = [7, 14, 28, 30, 56, 60, 84, 90, 100]
    pack_size = random.choice(pack_sizes)
    
    # Brand cost (expanded range)
    brand_cost = round(random.uniform(8, 120), 2)
    
    # Generic cost (20-75% of brand for variety)
    discount = random.uniform(0.25, 0.75)
    generic_cost = round(brand_cost * discount, 2)
    
    # Calculate savings
    saving_per_pack = round(brand_cost - generic_cost, 2)
    
    # Daily dosing (expanded)
    doses_per_day = random.choice([1, 2, 3])
    days_supply = pack_size // doses_per_day
    
    # Weekly saving
    weekly_saving = round((saving_per_pack / days_supply) * 7, 2) if days_supply > 0 else 0
    
    # Percentage reduction
    percentage_reduction = round((saving_per_pack / brand_cost) * 100, 1) if brand_cost > 0 else 0
    
    # Annual saving
    annual_saving = round(saving_per_pack * (365 / days_supply), 2) if days_supply > 0 else 0
    
    scenario = random.choice(COST_SCENARIOS).format(
        brand=brand_name, generic=generic_name, 
        brand_cost=brand_cost, generic_cost=generic_cost, pack_size=pack_size
    )
    scenario += f" The patient takes {doses_per_day} tablet(s) daily."
    
    return {
        "brand_name": brand_name,
        "generic_name": generic_name,
        "pack_size": pack_size,
        "brand_cost": brand_cost,
        "generic_cost": generic_cost,
        "saving_per_pack": saving_per_pack,
        "doses_per_day": doses_per_day,
        "days_supply": days_supply,
        "weekly_saving": weekly_saving,
        "percentage_reduction": percentage_reduction,
        "annual_saving": annual_saving,
        "scenario": scenario,
    }


# ============================================================================
# FORMATTING HELPERS
# ============================================================================

def format_working_tablet(problem: Dict) -> str:
    """Format the working for a tablet problem."""
    return f"""
**Formula:**
$$X = \\frac{{\\text{{Desired}}}}{{\\text{{Have}}}} \\times \\text{{Vehicle}}$$

**Substitution:**
$$X = \\frac{{{problem['desired']}\\text{{mg}}}}{{{problem['have']}\\text{{mg}}}} \\times 1\\text{{ tablet}}$$

**Calculation:**
$$X = {problem['desired'] / problem['have']} \\times 1$$

**Answer:** {problem['answer']} tablet(s)
"""


def format_working_liquid(problem: Dict) -> str:
    """Format the working for a liquid problem."""
    return f"""
**Formula:**
$$\\text{{Volume}} = \\frac{{\\text{{Desired}}}}{{\\text{{Have}}}} \\times \\text{{Vehicle}}$$

**Substitution:**
$$\\text{{Volume}} = \\frac{{{problem['desired']}\\text{{mg}}}}{{{problem['have']}\\text{{mg}}}} \\times {problem['vehicle']}\\text{{mL}}$$

**Calculation:**
$$\\text{{Volume}} = {problem['desired'] / problem['have']} \\times {problem['vehicle']}$$

**Answer:** {problem['answer']}mL
"""


def format_working_pediatric(problem: Dict) -> str:
    """Format the working for a pediatric problem."""
    return f"""
**Step 1: Calculate total daily dose**
$$\\text{{Total daily dose}} = \\text{{dose/kg}} \\times \\text{{weight}}$$
$$= {problem['dose_per_kg']}\\text{{mg/kg}} \\times {problem['weight']}\\text{{kg}} = {problem['total_daily']}\\text{{mg}}$$

**Step 2: Calculate dose per administration**
$$\\text{{Per dose}} = \\frac{{\\text{{Total daily}}}}{{{problem['frequency']}}}$$
$$= \\frac{{{problem['total_daily']}\\text{{mg}}}}{{{problem['frequency']}}} = {problem['per_dose']}\\text{{mg}}$$

**Step 3: Calculate volume**
$$\\text{{Volume}} = \\frac{{{problem['per_dose']}\\text{{mg}}}}{{{problem['have']}\\text{{mg}}}} \\times {problem['vehicle']}\\text{{mL}}$$

**Answer:** {problem['volume_per_dose']}mL per dose
"""


def format_working_infusion(problem: Dict) -> str:
    """Format the working for an infusion problem."""
    return f"""
**Formula:**
$$\\text{{Drops/min}} = \\frac{{\\text{{Volume (mL)}}}}{{\\text{{Time (min)}}}} \\times \\text{{Drop Factor}}$$

**Substitution:**
$$\\text{{Drops/min}} = \\frac{{{problem['volume']}\\text{{mL}}}}{{{problem['time_minutes']}\\text{{min}}}} \\times {problem['drop_factor']}\\text{{ gtts/mL}}$$

**Calculation:**
$$\\text{{Drops/min}} = {problem['volume'] / problem['time_minutes']:.4f} \\times {problem['drop_factor']}$$

**Answer:** {problem['drops_per_min']} drops/minute
"""


def format_working_dilution(problem: Dict) -> str:
    """Format the working for a dilution problem."""
    return f"""
**Formula:**
$$C_1V_1 = C_2V_2$$

**Rearranged to find V₁:**
$$V_1 = \\frac{{C_2 \\times V_2}}{{C_1}}$$

**Substitution:**
$$V_1 = \\frac{{{problem['c2']}\\text{{mg/mL}} \\times {problem['v2']}\\text{{mL}}}}{{{problem['c1']}\\text{{mg/mL}}}}$$

**Calculation:**
$$V_1 = \\frac{{{problem['c2'] * problem['v2']}}}{{{problem['c1']}}} = {problem['v1']}\\text{{mL}}$$

**Diluent needed:**
$${problem['v2']}\\text{{mL}} - {problem['v1']}\\text{{mL}} = {problem['diluent']}\\text{{mL}}$$

**Answer:** Use {problem['v1']}mL of stock solution + {problem['diluent']}mL of diluent
"""


def format_working_conversion(problem: Dict) -> str:
    """Format the working for a conversion problem."""
    if problem['operation'] == 'divide':
        op_symbol = '÷'
        mnemonic = "**SOLD:** Small to Large = Divide"
    else:
        op_symbol = '×'
        mnemonic = "**LOST:** Large to Small = Times (Multiply)"
    
    return f"""
**Mnemonic:**
{mnemonic}

**Conversion:**
$${problem['value']}\\text{{{problem['from_unit']}}} {op_symbol} {problem['factor']} = {problem['answer']}\\text{{{problem['to_unit']}}}$$

**Answer:** {problem['answer']} {problem['to_unit']}
"""


def format_working_cost(problem: Dict) -> str:
    """Format the working for a cost problem."""
    return f"""
**Saving per pack:**
$$\\text{{Saving}} = £{problem['brand_cost']} - £{problem['generic_cost']} = £{problem['saving_per_pack']}$$

**Percentage reduction:**
$$\\text{{Reduction}} = \\frac{{£{problem['saving_per_pack']}}}{{£{problem['brand_cost']}}} \\times 100 = {problem['percentage_reduction']}\\%$$

**Days supply:** {problem['pack_size']} tablets ÷ {problem['doses_per_day']} per day = {problem['days_supply']} days

**Weekly saving:**
$$\\text{{Weekly}} = \\frac{{£{problem['saving_per_pack']}}}{{{problem['days_supply']}}} \\times 7 = £{problem['weekly_saving']}$$

**Annual saving:**
$$\\text{{Annual}} \\approx £{problem['annual_saving']}$$
"""


# ============================================================================
# EXPANDED SANITY CHECKS (More tips per category)
# ============================================================================

SANITY_CHECKS = {
    "tablet": [
        "Does the number of tablets seem reasonable? Most single doses are 1-4 tablets.",
        "If your answer is more than 4 tablets, double-check your calculation.",
        "A fraction like 0.5 tablets is common (split tablet), but 0.3 tablets isn't practical.",
        "Did you accidentally divide when you should multiply, or vice versa?",
        "Check the units match - both the order and stock should be in mg (or the same unit).",
        "Remember: you can only give whole or half tablets, not arbitrary fractions.",
        "If your answer is less than 0.5 tablets, recheck - perhaps units need converting.",
        "80 tablets for one dose? That's a red flag! Check your decimal point.",
        "Ask yourself: could a patient realistically swallow this many tablets at once?",
        "Double-check: did you divide dose by strength, not the other way around?",
    ],
    "liquid": [
        "Liquid doses are typically 2.5mL to 20mL for oral medications.",
        "If your answer is more than 30mL, that's a large volume - double-check!",
        "Did you use the correct concentration from the label?",
        "Remember: the concentration tells you mg PER the volume stated.",
        "Children's liquid doses are usually 2.5-10mL for ease of administration.",
        "If your answer seems very small (less than 1mL), verify your calculation.",
        "Check: did you multiply by the vehicle volume (what it's dissolved in)?",
        "Always label liquid syringes clearly with the volume in mL.",
        "Round to a practical measurement - most syringes measure to 0.5mL.",
        "50mL as a single oral dose? That's a lot of liquid - recheck!",
    ],
    "pediatric": [
        "Children's doses should always be smaller than adult doses.",
        "Always double-check the weight - using kg instead of lb is a common error.",
        "Verify the frequency: TDS (3x daily) vs BD (2x daily) makes a big difference.",
        "The volume per dose for children is usually 2.5-15mL.",
        "Pediatric doses are calculated per kg - always verify the child's current weight.",
        "If the calculated dose exceeds the adult dose, stop and verify!",
        "Remember to divide the DAILY total by the number of doses per day.",
        "Infant doses (under 1 year) require extra caution - always verify.",
        "For children under 12, always use weight-based dosing, not age.",
        "A dose of 50mL for a toddler? That's too much - recheck calculations.",
    ],
    "infusion": [
        "Typical drip rates range from 20-150 drops/minute.",
        "Microdrop sets (60 gtts/mL) give smaller drops, so more drops per minute.",
        "Always convert hours to minutes before calculating!",
        "If your rate seems extremely high or low, recheck your time conversion.",
        "Remember: faster infusion = more drops per minute.",
        "60 drops/mL sets are often used for pediatrics or when precision is critical.",
        "Standard adult sets are usually 15 or 20 drops/mL.",
        "A rate of 300 drops/min is too fast to count - recheck your math.",
        "Less than 10 drops/min is very slow - verify this is appropriate.",
        "For 24-hour infusions, rates are usually quite slow (around 40-60 gtts/min).",
    ],
    "dilution": [
        "The volume of stock solution must always be LESS than the final volume.",
        "C₁V₁ = C₂V₂ only works when concentrations are in the same units.",
        "Final concentration should always be LESS than stock concentration.",
        "Diluent volume = Final volume - Stock volume used.",
        "If you need more stock than final volume, something is wrong!",
        "Check: the diluted solution should be weaker, not stronger.",
        "Always add the diluent to the stock solution, not vice versa (usually).",
        "Verify your final volume by adding: stock volume + diluent volume.",
        "Common diluents: sterile water, normal saline, or specific solvents.",
        "If stock = final concentration, no dilution is needed - check the question!",
    ],
    "conversion": [
        "Going from smaller to larger units? Your number should get SMALLER.",
        "Going from larger to smaller units? Your number should get BIGGER.",
        "Remember: 1000mcg = 1mg, 1000mg = 1g, 1000g = 1kg",
        "For volume: 1000mL = 1L",
        "SOLD: Small → Large = Divide (1000mcg ÷ 1000 = 1mg)",
        "LOST: Large → Small = Times (1mg × 1000 = 1000mcg)",
        "Household tip: 1 teaspoon = 5mL, 1 tablespoon = 15mL",
        "Converting mg to mcg? Your number gets 1000 times BIGGER.",
        "Converting mL to L? Your number gets 1000 times SMALLER.",
        "Double-check: did you move the decimal point the right direction?",
    ],
    "cost": [
        "Generic medications should always cost less than branded versions.",
        "Percentage savings should be between 0% and 100%.",
        "Annual savings = (saving per pack) × (number of packs per year).",
        "Double-check: days supply = pack size ÷ tablets per day.",
        "Weekly saving should be proportional to the pack saving.",
        "If generic costs more than brand, something is wrong!",
        "Consider: higher daily doses = faster pack consumption = more packs/year.",
        "Savings percentage = (Brand - Generic) ÷ Brand × 100",
        "For annual calculations, remember there are ~52 weeks or ~365 days.",
        "NHS often switches patients to generics for exactly these savings!",
    ],
}


def get_sanity_check(problem_type: str) -> str:
    """Get a random sanity check tip for the given problem type."""
    checks = SANITY_CHECKS.get(problem_type, SANITY_CHECKS["tablet"])
    return random.choice(checks)
