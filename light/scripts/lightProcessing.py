
import lightFunctions as j



# Создание листов значений яркости для каждой из ламп
my = j.readIntensity("yellow-tungsten.png", "yellow-tungsten", "Лампа накаливания", "Жёлтый лист")
mb = j.readIntensity("blue-tungsten.png", "blue-tungsten", "Лампа накаливания", "Синий лист")
mw = j.readIntensity("white-tungsten.png", "white-tungsten", "Лампа накаливания", "Белый лист")
mr = j.readIntensity("red-tungsten.png", "red-tungsten", "Лампа накаливания", "Красный лист")
mg = j.readIntensity("green-tungsten.png", "green-tungsten", "Лампа накаливания", "Зелёный лист")
mc = j.readIntensity("white-mercury.png", "white-mercury", "Ртутная лампа", "Белый лист")
mn = j.calibration(mc, my)
n = len(mn)

albmy = j.albedo_znach(my, mw, n)
albmb = j.albedo_znach(mb, mw, n)
albmw = j.albedo_znach(mw, mw, n)
albmr = j.albedo_znach(mr, mw, n)
albmg = j.albedo_znach(mg, mw, n)

# Построение графика интенсивностей и альбедо
j.intensities(my, mb, mw, mr, mg, mn)
j.albedos(albmy, albmb, albmw, albmr, albmg, mn)