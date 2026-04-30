# ClimateModeling
ClimateModeling Repository contains the codework for the Climate Modeling Tool. 

This is a python backed project that will utilize many different API calls and resources from US Government based services to provide reliable, credible climate modeling. 

NEED:
What will go on each page, the math behind it, and the layout
https://1drv.ms/x/c/8f1716f510363a80/IQAhejFmv0MrQoOhppDMLCZ0AXGx0hFOQ6l1BQlUSC1BMhc?e=7pxVZx
Excell sheet with all data on it. Working to get equations 
Heres the link to the data points i got 
https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/


Climate Model Equations
Stressₜ = w_F * F′ₜ + w_P * P′ₜ + w_T * T′ₜ + w_C * C′ₜ + w_S * Sₜ
Fₜ₊₁ = Fₜ + k₁ * Stressₜ + k₂ * (Tₜ - Tₜ₋₁) + k₃ * (Pₜ - Pₜ₋₁)
Zₜ₊₁ = Zₜ + γ * F′ₜ * Sₜ
