def check_flood_risk(water_cm, rain_strength, tide_level):
    score = 0

    # Points for water height
    if water_cm > 30:
        score += 3
    elif water_cm > 15:
        score += 2
    else:
        score += 1

    # Points for rainfall
    rain = rain_strength.lower().strip()
    if rain == "heavy":
        score += 3
    elif rain == "moderate":
        score += 2

    # Points for tide
    if tide_level.lower().strip() == "high":
        score += 2

    # Figure out the warning level based on total points
    if score >= 7:
        level = "SEVERE"
        action = "Evacuate to higher ground immediately."
        contacts = "Emergency Hotline: 911 | Local Response: (02) 8911-1406"
    elif score >= 4:
        level = "MODERATE"
        action = "Move cars to higher ground and get emergency supplies ready."
        contacts = None
    else:
        level = "LOW"
        action = "Conditions look fine. Keep an eye on local weather updates."
        contacts = None

    return level, action, contacts


def main():
    print("--- AquaSense Local Flood Risk Tool ---")
    
    try:
        water_cm = float(input("Current water level (in cm): "))
        rain_strength = input("Rainfall (Light, Moderate, Heavy): ")
        tide_level = input("Tide status (Low or High): ")

        risk_level, action_plan, hotlines = check_flood_risk(water_cm, rain_strength, tide_level)

        print("\n--- RESULTS ---")
        print(f"Risk Rating: {risk_level}")
        print(f"What to do: {action_plan}")
        if hotlines:
            print(f"Hotlines: {hotlines}")

    except ValueError:
        print("Please enter a valid number for water level.")


if __name__ == "__main__":
    main()