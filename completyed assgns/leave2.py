from leave import Leave
class RestrictedLeave(Leave):
    def _init_(self,employeeid,name,LeaveBalance,DateofBirth):
        super()._init_(employeeid, name, LeaveBalance)
        self.dob=DateofBirth
    def applyLeave(self):
        return self.name,self.dob

