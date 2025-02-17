def update_arrival(h,m,d):
    total_minutes = h*60 + m + d
    new_h = (total_minutes //60)%24
    new_m = total_minutes %60
    return (new_h, new_m)

# Prueba del código
if __name__ == "__main__":
    h, m, d = 23, 50, 30  # Hora de llegada 23:50 con 30 min de retraso
    new_h, new_m = update_arrival(h, m, d)
    print(f"Nueva hora de llegada: {new_h:02d}:{new_m:02d}")