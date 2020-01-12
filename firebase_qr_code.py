import pyrebase

class firebase:
    def __init__(self):
        self.config = {
            "apiKey": "AIzaSyBjyd-StJuZrHJ_fvx93NR3FwZ1D-DNHH4",
            "authDomain": "mcgill-aero-firebase.firebaseapp.com",
            "databaseURL": "https://mcgill-aero-firebase.firebaseio.com",
            "storageBucket": "mcgill-aero-firebase.appspot.com",
            "serviceAccount": "./mcgill-aero-firebase-firebase-adminsdk-ix65x-008d4163ab.json"
        }
        self.firebase = pyrebase.initialize_app(self.config)
        self.db = self.firebase.database()
        self.auth = self.firebase.auth()
        #authenticate a user
        self.user = self.auth.sign_in_with_email_and_password("yaredcyril@gmail.com", "mcgill-aero-on-fire")
    def readQRCode(self):
        return self.db.child("transfer-data").get(self.user['idToken']).val().get('qr_code')

    def updateQRCode(self, qr):
        self.db.child("transfer-data").update({"qr_code": qr}, self.user['idToken'])

    def createQRCode(self, qr):
        self.db.child("transfer-data").set({"qr_code":qr}, self.user['idToken'])




if __name__ == "__main__":
    
    fire = firebase()
    #fire.updateQRCode("aero")
    print(fire.readQRCode())