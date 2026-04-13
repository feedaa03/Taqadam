"""
data.py
-------
Team fills this file with real model output.
The UI in app.py reads from here — do not modify app.py.
"""

# ── Fill STUDENTS with your model output ──────────────────────────────────────
#
# Each student is a dict with these keys:
#
#   id            : int
#   name          : str
#   major         : str
#   level         : str   e.g. "Level 4"
#   risk          : str   "high" | "medium" | "low"
#   risk_label    : str   e.g. "High Risk"
#   support_index : int   0–100  (lower = needs more support)
#   avg_grade     : int   average grade %
#   avg_delay     : float average submission delay in days
#   grades        : list[int]   weekly grades  e.g. [82, 76, 69, 63, 51]
#   engagement    : list[int]   weekly login sessions e.g. [18, 14, 10, 7, 4]
#   delays        : list        weekly delay in days, None = not submitted
#   xai_factors   : list[dict]  [{"name": str, "importance": int 0-100}, ...]
#   xai_reasons   : list[dict]  [{"title": str, "desc": str}, ...]
#
# Example with real model output:
#   import pandas as pd
#   df = pd.read_csv("model_output.csv")
#   STUDENTS = df.to_dict("records")

STUDENTS = [
    # paste your model output here
]


# ── Week labels — update if your semester has more/fewer weeks ─────────────────
WEEKS = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]


# ── Intervention actions per risk level — edit text if needed ─────────────────
ACTIONS = {
    "high": {
        "priority":       ("Very High",                  "#A32D2D"),
        "hours":          "24",
        "recommendation": "Urgent one-on-one advising session",
        "rec_desc":       "Review study plan and identify personal and academic obstacles",
        "support_type":   "Academic advising + psychological support",
        "support_desc":   "Coordinate with the mental health unit if needed",
        "followup":       ("Yes — within 48 hours",      "#185FA5"),
        "followup_desc":  "Confidential to advisor only. Student is not labeled.",
    },
    "medium": {
        "priority":       ("Medium",                     "#854F0B"),
        "hours":          "72",
        "recommendation": "Optional advising session this week",
        "rec_desc":       "Monitor student performance and provide improvement guidance",
        "support_type":   "Preventive academic advising",
        "support_desc":   "Strengthen study habits before the issue escalates",
        "followup":       ("Recommended — within a week", "#3B6D11"),
        "followup_desc":  "Periodic check-ins without pressure",
    },
    "low": {
        "priority":       ("Low",                        "#3B6D11"),
        "hours":          "168",
        "recommendation": "Routine periodic follow-up",
        "rec_desc":       "No immediate intervention needed",
        "support_type":   "Preventive support",
        "support_desc":   "Check in during the next scheduled session",
        "followup":       ("Not necessary at this time",  "#3B6D11"),
        "followup_desc":  "Review in the next routine session",
    },
}
