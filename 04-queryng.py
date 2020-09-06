import urllib.request, json
with urllib.request.urlopen("https://mul14.github.io/data/employees.json") as url:
    data = json.loads(url.read().decode())

def salary(slr):
    return slr['first_name'] \
        if int(slr['salary']) > 15000000 \
            else False

def locJakarta(jkt):
    return jkt['first_name'] \
        if str(jkt['addresses'][0]['city']) == 'DKI Jakarta' \
            else False

def month(month):
    return month['first_name'] \
        if int(month['birthday'].split('-')[1]) == 4 \
            else False

def departement(dept):
    return dept['first_name'] \
        if str(dept['department']['name']) == 'Research and development' \
            else False

def absent(abs):
    def count(var): return int(var.split('-')[1]) == 10 and int(var.split('-')[0]) == 2019
    oktober = filter(count,abs['presence_list'])
    return {"name":abs['first_name'],"absent":len(list(oktober))}

Salary = filter(None, map(salary,data))
Jakarta = filter(None, map(locJakarta,data))
Brithday = filter(None, map(month,(data)))
Departement = filter(None, map(departement,(data)))
Absent = filter(None,map(absent,data))


print("salary up 15jt :", ", ".join(list(Salary)))
print("address Dki jakarta :", ", ".join(list(Jakarta)))
print("brithday on april :", ", ".join(list(Brithday)))
print("in departement research :", ", ".join(list(Departement)))
print("absent on oktober :",(list(Absent)))

