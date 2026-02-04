import json
from datetime import datetime,timedelta,date
    
def cargar_eventos()->list:
    with open("DataBase.json",'r',encoding='utf-8') as file:
        data_events=json.load(file)
    return data_events["eventos"]

def planes()->list:
    with open("DataBase.json",'r',encoding='utf-8') as file:
        data_plan=json.load(file)
    return data_plan["planes"]

            
def cargar_recursos()->dict:
    with open("DataBase.json",'r',encoding='utf-8') as file:
        data_recursos=json.load(file)
    return data_recursos["recursos"]

recursos=cargar_recursos()
planeados=planes()


class Eventos:
    def __init__(self,id:int,nombre:str,inicio:date,duracion:int,lugar:str,recursos:dict):
        self.id=id
        self.nombre=nombre
        self.inicio=inicio
        self.duracion=duracion
        self.fin=inicio+timedelta(days=duracion)
        self.lugar=lugar
        self.recursos=recursos    
    
    # Para revisar si el evento esta en el mismo periodo que otro.
    def choque_fecha(self,evento_2)->bool:
        fecha_inicio1=self.inicio
        fecha_fin1=self.fin
        fecha_ini2=datetime.strptime(evento_2["Fecha de inicio"],"%Y-%m-%d")
        fecha_fi2=datetime.strptime(evento_2["Fecha de fin"],"%Y-%m-%d")
        # Si el or da verdadero es xq no hay choques, por tanto retorna falso (razón: la funcion se llama choque_fecha, si hay choques retorna verdadero.)
        return not (fecha_fin1<=fecha_ini2.date() or fecha_inicio1>=fecha_fi2.date())

    def choque_lugar(self,evento_2):
        lugar1=self.lugar
        lugar2=evento_2["Lugar"]
        return lugar1==lugar2

    # Para revisar si el evento tiene recursos en comun con otro.
    def choque_recurso(self,evento_2,usados):
        if not self.choque_fecha(evento_2):
            return False,{}
        choque={}
        for recurso,cantidad in self.recursos.items():
            if recurso in usados:
                if recursos[recurso]-(cantidad + usados[f"{recurso}"])<0:
                    choque[recurso]=cantidad + usados[f"{recurso}"]
        return len(choque)>0,choque
    
    def check_resources(self,fecha_inicio,fecha_fin,recursos_necesarios):
        eventos_solapados=[]
        for evento in planeados:
            if fecha_inicio>datetime.strptime(evento["Fecha de fin"],"%Y-%m-%d").date():
                continue
            inicio_de_evento=datetime.strptime(evento["Fecha de inicio"],"%Y-%m-%d")
            fin_de_evento=datetime.strptime(evento["Fecha de fin"],"%Y-%m-%d")
            if not (fecha_fin<=inicio_de_evento.date() or fecha_inicio>=fin_de_evento.date()):
                eventos_solapados.append(evento)
        
        uso_recursos={}
        for evento in eventos_solapados:
            for recurso,cantidad in evento["Recursos utilizados"].items():
                uso_recursos[recurso]=uso_recursos.get(recurso,0)+cantidad
        
        for recurso, cantidad_necesaria in recursos_necesarios.items():
            cantidad_usada=uso_recursos.get(recurso,0)
            cantidad_total_necesaria=cantidad_usada+cantidad_necesaria
            if cantidad_total_necesaria>recursos[recurso]:
                return False,uso_recursos
        return True,uso_recursos

    
    def find_hole(self):
        duracion=timedelta(days=self.duracion)
        intervalo=timedelta(days=1)
        max_search=self.inicio+timedelta(days=30)
        first_search=self.inicio
        while first_search<=max_search:
            final_search=first_search+duracion
            disponible,_=self.check_resources(first_search,final_search,self.recursos)
            if disponible:
                def_start=first_search+timedelta(days=1)
                def_end=def_start+duracion
                return {"start suggest":def_start,"end suggest":def_end,"disponible":True,"mensaje":f"del {def_start} al {def_end}","recursos":_}
            first_search+=intervalo
        return {"start suggest":None,"end suggest":None,"disponible":False,"mensaje":f"No se encontró un intervalo disponible en los próximos {max_search} días"}

    def detalles(self)->dict:
        return {"ID":self.id,
                "Nombre":self.nombre,
                "Fecha de inicio":self.inicio.strftime("%Y-%m-%d"),
                "Fecha de fin":self.fin.strftime("%Y-%m-%d"),
                "Lugar":self.lugar,
                "Recursos utilizados":self.recursos}
    
    

# Para agregar eventos al json.
def añadir_evento(nombre:str,duracion:int,lugar:str):
    with open("DataBase.json",'r',encoding='utf-8') as file:
        datos=json.load(file)
    new_event={"Nombre":nombre,"Duracion":duracion,"Lugar":lugar}
    with open("DataBase.json",'w',encoding='utf-8') as file:
        datos["eventos"].append(new_event)
        json.dump(datos,file)

def añadir_plan(evento):
    with open("DataBase.json", 'r',encoding='utf-8') as file:
        plans=json.load(file)
    plans["planes"].append(evento)
    with open("DataBase.json",'w',encoding='utf-8') as file:
        json.dump(plans,file)


# Para aumentar la cantidad de los recursos en el json.
def aumentar_recurso(nombre:str,cantidad:int):
    with open ("DataBase.json",'r',encoding='utf-8') as file:
        data=json.load(file)
        data['recursos'][f"{nombre}"]+=cantidad
    with open("DataBase.json",'w',encoding='utf-8') as file:
        json.dump(data,file)

def calendario():
    datos=planes()
    final=[]
    for evento in datos:
        final.append({'ID':evento["ID"],
                      'title':evento["Nombre"],
                      'start':evento["Fecha de inicio"],
                      'end':evento["Fecha de fin"],
                      'lugar':evento["Lugar"],
                      'recursos':evento["Recursos utilizados"]})
    return final

def b_s(list:list,l:int,r:int,id:int):
    mid=(l+r)//2
    if list[mid]["ID"]==id:
        return mid
    if id>list[mid]["ID"]:
        return b_s(list,mid+1,r,id)
    else:
        return b_s(list,l,mid,id)
    

def delete_by_ID(ID:int):
    with open("DataBase.json","r",encoding="utf-8") as file:
        data=json.load(file)
    data["planes"].pop(b_s(data["planes"],0,len(data["planes"]),ID))
    with open("DataBase.json","w",encoding="utf-8") as file:
        json.dump(data,file)