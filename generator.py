import string,random

class Genarator:
    def __init__(self):
        self._roll = 0
        self._name = ""
        self._email = ""
        self._gender = ""
        self._contact = ""
        self._dob = ""
        self._address = ""
    
    def roll_gen(self,lenth):
        self._roll=[i for i in range(1,lenth+1)]
        return self._roll
    
    def name_gen(self,lenth):
        alpha_low = list(string.ascii_lowercase)
        alpha_upp = list(string.ascii_uppercase)
        title = ["Roy","Saha","Kundu","Paul","Das"]
        self._name = [random.choices(alpha_upp)[0]+"".join(random.sample(alpha_low,random.randint(2,7)))+" "+random.choice(title) for i in range(lenth)]
        return self._name
    
    def email_gen(self,length):
        alpha_low = list(string.ascii_lowercase)
        digits = list(string.digits)
        self._email = ["".join(random.sample(alpha_low,random.randint(4,8)))+"".join(random.sample(digits,random.randint(3,6)))+"@gmail.com" for i in range(length)]
        return self._email
    
    def gender_gen(self,length):
        gender = ["Male","Female"]
        self._gender = [random.choices(gender) for i in range(length)]
        return self._gender
    
    def contect_gen(self,length):
        digits = list(string.digits)
        self._contact = [random.choices(['9','8','7'])[0]+"".join(random.sample(digits,9)) for i in range(length)]
        return self._contact
    
    def dob_gen(self,length):
        date_list = ["0"+str(i) if len(str(i))<2 else str(i) for i in range(1,13)] 
        month_list = ["0"+str(i) if len(str(i))<2 else str(i) for i in range(1,32)]
        year_list = [str(i) for i in range(1900,2011)]
        self._dob = [random.choices(date_list)[0]+"/"+random.choices(month_list)[0]+"/"+random.choices(year_list)[0] for i in range(length)]
        return self._dob

    def address_gen(self,length):
        alpha_low = list(string.ascii_lowercase)
        alpha_upp = list(string.ascii_uppercase)
        number_list = [str(i) for i in range(1,100)]
        pincode = [str(i) for i in range(700000,700150)]
        self._address = [random.choices(number_list)[0]+random.choices(alpha_low)[0]+", "+".".join(random.sample(alpha_upp,3))+" "+"Road, "+"kolkata = "+random.choices(pincode)[0] for i in range(length)]
        return self._address
    

if __name__ == "__main__":
    ob = Genarator()
    print(ob.roll_gen(10))
    print(ob.name_gen(10))
    print(ob.email_gen(10))
    print(ob.gender_gen(10))
    print(ob.contect_gen(10))
    print(ob.dob_gen(10))
    print(ob.address_gen(10))