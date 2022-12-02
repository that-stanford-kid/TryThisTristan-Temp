<h2> Custom repo generated --> <i> <b>TryThisTristan-Temp</b></i>.</h2>

---
<h5>

Language: "R".

Author: "Patrick ONeil".(c)

Date: 12/2/2022

---	
  About: 
  - Synthetic Futures Pricing Per Driver for Spot requests.
	- Opportunity = Supply
		- Metric Quantity of loads(avalibility).
		- Metric in decimal repr --> Millions. i.e 45.21 = 45,210,000.00 ["m"]
		- Differentiate against opportunities from each other state(48) in c.reference.
		- Distance From Current (Ori) location to (Des), Destination by miles.
	
	- Vehicle Type = Van | Reef
	 	- Reef = Refrigerated(More expensive)
		- Van = Standard Carrier without perishables.
		
	- Location = US.[1]
		- States(48)
		- Citities(abb)
			- Abbreviated
			- Zip by e.unique (Origin | Destination) --> Distance in miles.
	
	- Demand = (Demand_atDest>Ori_location(Ori(state(zip)))
		- Reference(Supply)
	
	- Outliers
		- Road elevation.
		- Condition(s).
		- Season(s).
		- Temperature(F*).
		- Weather api in prod env.
		
	- Distance:
		- Miles
			- "m" = (abb)
		
	- Synopsis:
		- Predict "$" optimum min or max for delivery to suceed though with inclusion of outliers and current demand and supply.
		- Rate Per Mile basis for "$" value by mile.
		- First in queue by reponse time is accounted for by driver.
		- RPM recommended by the algorithmic model by_Region(Zip2Zip).(State(Ori|Des)2State(abb)).
		- Streaming.

	- Goal: "Maximize Accuracy and rofit through the custom Rate Paid Per Mile by what is accounted for and what cannot be accounted for _".
		- Ever-changing fluctuations.
--- 
