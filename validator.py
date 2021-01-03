class Validator():
    """docstring for .
    - is it xml file"""

    def validate_xml(self,file_to_validate):
        if file_to_validate == "":
            error_msg = "File Not Detected"
            return error_msg,False
        else:
            return None,True
