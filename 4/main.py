import re

lines = []
with open('4/input', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

passports = []
bufstr = ""
for line in lines:
  if line == "":
    entries = [entry.strip() for entry in bufstr.strip().split(" ")]
    entry_dict = {entry.split(":")[0]:entry.split(":")[1] for entry in entries}
    passports.append(entry_dict)
    bufstr = ""
    continue

  bufstr += " " + line

val_passes = 0
keys = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
eycl = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
for passp in passports:
  #input()
  print(passp)
  if not all([key in passp.keys() for key in keys]):
    print('missing keys')
    continue

  if not (int(passp['byr']) >= 1920 and int(passp['byr']) <= 2002):
    print('bad byr')
    continue

  if not (int(passp['iyr']) >= 2010 and int(passp['iyr']) <= 2020):
    print('bad iyr')
    continue

  if not (int(passp['eyr']) >= 2020 and int(passp['eyr']) <= 2030):
    print('bad eyr')
    continue

  if not ('cm' in passp['hgt'] or 'in' in passp['hgt']):
    print('bad unit')
    continue

  height = int(passp['hgt'][:-2])
  unit = passp['hgt'][-2:]
  #print(height, unit)
  #input()
  if unit == 'cm' and not(height >= 150 and height <= 193):
    print('bad cm height')
    continue
  if unit == 'in' and not(height >= 59 and height <= 76):
    print('bad in height')
    continue

  #print(len(re.findall('^#[a-f0-9]\w{5}$', passp['hcl'])))

  if len(re.findall('^#[a-f0-9]\w{5}$', passp['hcl'])) == 0:
    print('bad hcl')
    continue



  if not (passp['ecl'] in eycl):
    print('bad ecl')
    continue

  if not len(passp['pid']) == 9:
    print('bad pid')
    continue

  print('valid')
  val_passes += 1

print(val_passes)
