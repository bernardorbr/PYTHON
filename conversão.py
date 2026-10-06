seg = int(input("Informe os segundos: \n"))

horas = seg // 3600
restseg = seg % 3600

minutos = restseg // 60
segundos = restseg % 60

print(f"{seg} segundos, equivalem a {horas}h, {minutos}m, {segundos}s.w")