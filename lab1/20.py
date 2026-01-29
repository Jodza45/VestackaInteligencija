def boje(hex_zapis):
   
    keys = ["Red", "Green", "Blue"]
    
    values = [int(hex_zapis[i:i+2], 16) for i in range(1, 7, 2)]
    
    return dict(zip(keys, values))