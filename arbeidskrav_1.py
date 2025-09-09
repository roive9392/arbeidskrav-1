# For å sammelingne årlige totalkostnadene mellom elbil og bensinbil

# Felles
km_per_år = 10_000
trafikkforsikringsavgift = 8.38 * 365

# For elbil
forsikring_elbil = 5000
kWh_brukt = km_per_år * 0.2
drivstoffbruk_elbil = kWh_brukt * 2
bomavgift_elbil = km_per_år * 0.1
total_kostnad_elbil = forsikring_elbil + drivstoffbruk_elbil + bomavgift_elbil + trafikkforsikringsavgift
print(f"Årlige totalkostnadene for elbil: {total_kostnad_elbil} kr".replace(".", ","))

# For bensinbil
forsikring_bensinbil = 7500
drivstoffbruk_bensinbil = km_per_år * 1
bomavgift_bensinbil = km_per_år * 0.3
total_kostnad_bensinbil = forsikring_bensinbil + drivstoffbruk_bensinbil + bomavgift_bensinbil + trafikkforsikringsavgift
print(f"Årlige totalkostnadene for bensinbil: {total_kostnad_bensinbil} kr".replace(".", ","))

# Kostnadsdifferanse
print(f"Kostnadsdifferanse: {total_kostnad_bensinbil - total_kostnad_elbil} kr".replace(".", ","))
      
      
