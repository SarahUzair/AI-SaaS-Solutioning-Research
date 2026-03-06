 =================================================================
# STRATEGIC ICT SOLUTIONS PORTFOLIO for ANZSCO 225211
# Purpose: Automation of Key Account Management (KAM) and Logistics Logic
# Developer: Sarah Uzair 
# =================================================================

# PROJECT 1: SENTINEL 2026 - Structural Pattern Matching for Regulatory Risk Assessment
package_id = str(input("Insert package ID: "))
weight = float(input("Insert weight: "))
declared_value = int(input("Insert declared value: "))
destination = str(input("Insert destination: "))
match destination:
  case "USA"|"usa":
    if declared_value > 1000:
      print ("Risk Level: High - IRS Reporting Required.")
    elif weight > 50:
      print ("Risk Level: Medium - Heavy Cargo Surcharge.")
    else:
      print("Risk Level: Low - Standard Domestic Clearance.")
  case "UK":
    if declared_value > 5000:
      print ("Risk Level: High - Customs Bond Required.")
    else:
      print("Risk Level: Low - Brexit Protocol Applied.")
  case "Mars":
    if weight == 0:
      print ("Risk Level: Fraud - Weightless package detected.")
    elif declared_value > 1000000:
      print("Risk Level: Critical - Interplanetary Insurance Needed.")
    else:
      print("Risk Level: Medium - Standard SpaceX transport.")
  case _:
    print("Risk Level: CRITICAL - Destination Blacklisted or Unknown.")

# PROJECT 2: GLOBAL LOGISTICS MANIFEST - String Normalization & Data Parsing
# Code to input: $$$ID:AMZ-992-ORIGIN:Australia-VAL:15000-WEIGHT:45.5$$$
a = (input("Raw Manifest Data:"))
b = a.strip().replace("$$$","").replace(" " , "").lower()
c = b.split("-")
e = c[2][7:] # ORIGIN
g = int(c[3][4:]) # VALUE
i = float(c[4][7:]) # WEIGHT
if i > 100:
  print("HEAVY FREIGHT - SUBJECT TO INSPECTION")
if e == "australia" or e == "saudi arabia":
  if g > 10000:
    print("15% Trade tarriff charges applied:", 1.15*g)
  else:
    print ("5% Trade tarriff charges applied:", 1.05*g)
elif e == "pakistan":
  print ("STANDARD DOMESTIC PROCESSING")
else:
  print("SECURITY ALERT - UNKNOWN ORIGIN")

# PROJECT 3: STRATEGIC KAM PERFORMANCE TRACKER - Quantitative Analytics
Client_Name = input("Client Name: ")
Total_Monthly_Revenue = input ("Total Monthly Revenue in PKR: ")
Number_of_Active_SIMs = input ("Number of Active SIMs: ")
Customer_Satisfaction_Score = input ("Enter Satisfaction Score (1-10): ")
ARPU = int(Total_Monthly_Revenue)/int(Number_of_Active_SIMs)
Churn_Risk_Score = int(Customer_Satisfaction_Score) < 5
Flagship_Account = int(Total_Monthly_Revenue) > 100000
print(f"{Client_Name} ARPU = {ARPU} | High Risk: {Churn_Risk_Score} | Flagship: {Flagship_Account}")

# PROJECT 4: SMART CITY INFRASTRUCTURE AUDIT – Automated Grid Load Validation
building_id = str(input("Insert Building ID: ")).strip().lower()
sector = str(input("Insert Sector: ")).strip().lower()
usage_kWH = float(input("Insert Kilowatts Used: "))
peak_status = int(input("Insert Peak Status (0/1): "))
if usage_kWH < 0 or (peak_status != 0 and peak_status != 1):
  print ("DATA CORRUPTION: Technician required.")
match sector:
    case "industrial" if usage_kWH > 50000 and peak_status == 1:
        print ("GRID ALERT: High usage during peak. Applying 25% Surge Tax.")
    case "medical" if "er" in building_id:
        print("CRITICAL LOAD: Emergency Hospital. Billing Exempt.")
    case "residential" if usage_kWH < 500:
        print("Eco-Friendly Reward: 0% Billing.")
    case _:
        print("Standard Rate applied or Unauthorized connection.")

# PROJECT 5: REAL-TIME MARKET HEATMAP – Automated Sector Performance & Risk Analytics
market_data = ["NVDA:Tech:130.50:10", "JPM:Finance:210.00:5", "BRENT:Energy:82.00:100"]
tech_vol = 0
for data in market_data:
  b = data.split(":")
  vol = float(b[2]) * int(b[3])
  if "Tech" in b: tech_vol += vol
print(f"Total Tech Volume: ${tech_vol}")

# PROJECT 6: INSTITUTIONAL PROCUREMENT AUDITOR – Automated Grant Compliance
item = str(input("Enter Item: ")).strip().lower()
cost = float(input("Cost per Unit: "))
qty = int(input("Quantity: "))
dept = str(input("Dept Code: ")).strip().lower()
if qty <= 0 or cost <= 0:
  print("Invalid entry.")
match dept:
  case "eng" if item == "drone":
    print("Needs Safety Permit", (cost*qty*0.90)+500)
  case "sci":
    print("Lab Supply Total: ", (qty*cost))
  case _:
    print("Standard processing.")

# PROJECT 7: FINTECH RISK METRIC ENGINE – Automated DTI Stress Testing
income = float(input("Monthly Income: "))
payment = float(input("Mortgage Payment: "))
stress_payment = payment * 1.2
DTI_now = payment/income
DTI_stress = stress_payment/income
Pass_Test = DTI_now <= 0.30 and DTI_stress <= 0.40
print(f"Current DTI: {DTI_now} | Stressed DTI: {DTI_stress} | Pass: {Pass_Test}")

# PROJECT 8: CYBERSECURITY INFRASTRUCTURE AUDIT – Forensic Log Parsing
server_log = "[2025-12-28-20:15:01]-IP:192.168.1.1-STATUS:200-LOC:LHR-USER:SARAH"
print("Year:", server_log[1:5])
print("Status Code:", server_log[48:51])
print("User:", server_log[61:66])

# PROJECT 9: STRATEGIC ACV FORECASTING & ENTERPRISE REVENUE ENGINE
monthly_fee_DC = 50000.00
pilot_vehicles_Pepsi = 1000
ACV_Pepsi = 8500.25 * 12
total_rev_Pepsi = ACV_Pepsi * pilot_vehicles_Pepsi
Flagship_Status_Pepsi = total_rev_Pepsi > 10000000
print(f"PepsiCo Portfolio Revenue: ${total_rev_Pepsi} | Flagship: {Flagship_Status_Pepsi}")

# PROJECT 10: CREDIT RISK INFRASTRUCTURE – Automated Expected Loss (EL) Modeling
exposure = float(input("Exposure at Default (SAR): "))
pd = float(input("Probability of Default (0.02): "))
lgd = float(input("Loss Given Default (0.40): "))
el = exposure * pd * lgd
acceptable = el < 5000
print(f"Expected Loss: {el} SAR | Acceptable Risk: {acceptable}")
