class producst_testing():


    def test_db_connection(self):
        db_string = ''
        self = self.test_db_connection()
        if self == True:
            return 'db properly connected'
        else:
            return 'db not connected'