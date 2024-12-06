UAM_BIBLIO_API = 'https://uvirtual.uam.edu.ni:442/uambiblioapi/User/'
UAM_BIBLIO_POST_HEADER = {
    "Content-Type": "application/json",
    "X-Uam-Secure-Api": "version-1.0"
}
def get_uam_biblio_get_header(token:str):
    return {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "X-Uam-Secure-Api": "version-1.0",
    "Authorization": token
    }

STUDENT_CIF = ''
STUDENT_PIN = ''

