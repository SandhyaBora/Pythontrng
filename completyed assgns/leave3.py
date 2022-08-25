from leave import Leave
class BasketofLeave(Leave):
    def __init__(self,employeeid,name,LeaveBalance,ReasonForApplyingLeave):
        super().__init__(employeeid,name,LeaveBalance)
        self.reason=ReasonForApplyingLeave
    def applyLeave(self):
        return str(self.id)+' ' +self.name+' has the reason'+' '+self.reason.upper()
