# Du kan selv velge antall kjørte km/år ut fra din typiske bilbruk. Ev. (hvis du ikke har bil) kan du anta 10.000 km.
# Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.
# Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.
# Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. Bensinbil: 1,0 kr/km.
# Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km.

# Felles
km_per_år = 10_000
Trafikkforsikringsavgift = 8.38 * 365

# For elbil
Forsikring_elbil = 5000
kWh_brukt = km_per_år * 0.2
drivstoffbruk_elbil = kWh_brukt * 2
bomavgift_elbil = km_per_år * 0.1
total_kostnad_elbil = Forsikring_elbil + drivstoffbruk_elbil + bomavgift_elbil + Trafikkforsikringsavgift
print(f"Årlige totalkostnadene for elbil: {total_kostnad_elbil} kr".replace(".", ","))

# For bensinbil
Forsikring_bensinbil = 7500
drivstoffbruk_bensinbil = km_per_år * 1
bomavgift_bensinbil = km_per_år * 0.1
total_kostnad_bensinbil = Forsikring_bensinbil + drivstoffbruk_bensinbil + bomavgift_bensinbil + Trafikkforsikringsavgift
print(f"Årlige totalkostnadene for bensinbil: {total_kostnad_bensinbil} kr".replace(".", ","))

# Kostnadsdifferanse
print(f"Kostnadsdifferanse: {total_kostnad_bensinbil - total_kostnad_elbil} kr".replace(".", ","))
      
      