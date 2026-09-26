# -AquaSense-Localized-Flood-Risk-Predictor
AquaSense is a quick flood risk calculator for coastal neighborhoods. It takes simple local details like current water levels, rain intensity, and high/low tide and tells residents how high their flood risk is right now.

## Why it matters
When heavy rain hits during high tide, streets flood fast. General city weather reports cover big areas, so they often miss sudden water rises on specific streets until it's too late. This leaves families with damaged property and flooded cars. Having a simple tool focused on local numbers gives people enough warning to act before water creeps into their homes.

## Goals
1. *Specific:* Build a simple program that sorts flood risk into Low, Moderate, or Severe using water level, rainfall, and tide inputs.
2. *Measurable:* Make sure the calculation logic outputs the correct risk level for 100% of test scenarios.
3. *Time-Bound:* Finish the core logic, documentation, and GitHub setup before tonight's submission deadline.

## What it will do
- *Risk Calculator:* Runs local inputs through a simple point system to show immediate flood risk.
- *Safety Tips:* Gives short, clear advice on what actions to take based on the risk level.
- *Emergency Hotlines:* Automatically pulls up local rescue numbers during severe warnings.

## Inputs & Outputs
- *User Inputs:* Water Level (in cm), Rainfall (Light / Moderate / Heavy), Tide Status (Low / High).
- *System Outputs:* Risk Rating (Low / Moderate / Severe), Recommended Steps, Local Emergency Contacts.

## Logic Plan (Pseudocode)
```text
START
    GET water_level, rainfall_intensity, tide_status

    risk_score = 0

    // Check water height
    IF water_level > 30 THEN 
        risk_score = risk_score + 3 
    ELSE IF water_level > 15 THEN 
        risk_score = risk_score + 2 
    ELSE 
        risk_score = risk_score + 1

    // Check rain
    IF rainfall_intensity == "Heavy" THEN 
        risk_score = risk_score + 3 
    ELSE IF rainfall_intensity == "Moderate" THEN 
        risk_score = risk_score + 2

    // Check tide
    IF tide_status == "High" THEN 
        risk_score = risk_score + 2

    // Show output
    IF risk_score >= 7 THEN
        SHOW "SEVERE RISK - Evacuate to higher ground."
        SHOW Emergency Hotlines
    ELSE IF risk_score >= 4 THEN
        SHOW "MODERATE RISK - Move vehicles and prepare supplies."
    ELSE
        SHOW "LOW RISK - Conditions normal."
    ENDIF
END

