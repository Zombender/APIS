from dataclasses import dataclass

class StudentAPI():
    def __init__(self,student_api_response:list[dict]):
        parsed_api_response = self.parse_student_api_response(student_api_response)
        self.cif = parsed_api_response['cif']
        self.nombre_completo = f"{parsed_api_response['nombres']} {parsed_api_response['apellidos']}"
        self.tipo = parsed_api_response['tipo']
        self.correo = parsed_api_response['correo']
        self.sexo = parsed_api_response['sexo'] #Maybe we can modify this so it is clear what M and F means
        self.phone = parsed_api_response['telefono']
        self.carrera = parsed_api_response['carrera']
    
    def parse_student_api_response(self,student_api_response:list[dict]):
        base_response = student_api_response[0]
        base_response['carrera'] = [base_response['carrera']]
        #If student has an extra career
        if len(student_api_response) > 1:
            base_response['carrera'].append([career_response['carrera'] for career_response in student_api_response])
            print(base_response)
        del base_response['facultad']
        return base_response

    def __repr__(self):
       str_format:str 
       str_format = f'CIF: {self.cif}\n'
       str_format += f'Nombre completo: {self.nombre_completo}\n'
       str_format += f'Tipo: {self.tipo}\n'
       str_format += f'Correo: {self.correo}\n'
       str_format += f'Sexo: {self.sexo}\n'
       str_format += f'Teléfono: {self.phone}\n'
       str_format += f'{"Carrera" if len(self.carrera) == 1 else "Carreras"}: {self.carrera}\n'
       return str_format
    
@dataclass
class StudentLoginRequest:
    cif : str
    password: str

@dataclass
class StudentResponse:
    success: bool
    message : str
    data : dict