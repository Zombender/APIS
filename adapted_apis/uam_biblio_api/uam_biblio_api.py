from api_base import APIBase
from adapted_apis.uam_biblio_api.student import StudentAPI,StudentLoginRequest,StudentResponse
from constants import UAM_BIBLIO_API,STUDENT_CIF,STUDENT_PIN,get_uam_biblio_get_header,UAM_BIBLIO_POST_HEADER

class UAMBiblioAPI(APIBase):
    def __init__(self,base_url:str):
        super().__init__(base_url)

    def log_in_student(self, cif:str, pin:str)->None | StudentAPI:
        login_request = StudentLoginRequest(cif,pin)
        response = self.post_response(login_request.__dict__,UAM_BIBLIO_POST_HEADER,f'{self.base_url}login')
        if response is None: return None
        
        token = f'Bearer {response.text}'
        data_url = f"{self.base_url}GetStudentInformation?cif={cif}"
        response = self.get_response(get_uam_biblio_get_header(token),data_url)

        if response is None: return None

        json_data = response.json()
        student_response = StudentResponse(success=json_data.get('success'),
                                       message=json_data.get('message'),
                                       data = json_data.get('data',[]))

        if not student_response.success:
            print(f'Error al traer datos. {student_response.message}')

        student_instance = StudentAPI(student_response.data)
        return student_instance
    
if __name__ == '__main__':
    uam_api = UAMBiblioAPI(UAM_BIBLIO_API)
    student_instance = uam_api.log_in_student(STUDENT_CIF,STUDENT_PIN)
    print(repr(student_instance))
