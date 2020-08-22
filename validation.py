import re

class validations:

    def validatemob(self,mob):
        pattern = re.compile(r'\d{10}')
        if(pattern.match(mob)):
            return True
        else:
            print("Re-enter Mobile Number")
            return False