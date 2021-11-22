class Statistics():
    def __init__(self,extra_workers,simulations):
        self.simulations = simulations
        self.exceded_time_no_help = 0
        self.exceded_time_help = 0
        self.total_attended_no_help = 0
        self.total_attended_help = 0
        self.extra_workers = extra_workers
        self.attended_by_extra = 0

    def GetMedia(self):
        m1 = self.exceded_time_no_help/self.simulations
        m2 = self.exceded_time_help/self.simulations


        print(f'Mean clients waiting more than 5 minutes with only two workers = {m1}')
        print(f'Mean clients waiting more than 5 minutes with {self.extra_workers} extra workers = {m2}')

        m3 = round(m1-m2)
        if m3>=0:
            print(f'''Each day around {m3} more clients wait more than 5 minutes when there aren't extra workers''')
        else:
            print(f'''Each day around {-1*m3} more clients wait more than 5 minutes when there are extra workers''')

        

        print('')

    def GetPercent(self):
        p1 = (self.exceded_time_no_help*100)/self.total_attended_no_help
        p2 = (self.exceded_time_help*100)/self.total_attended_help
        p3 = (self.attended_by_extra*100)/self.total_attended_help

        print(f'% clients waiting more than 5 minutes with only two workers = {p1} %')
        print(f'% clients waiting more than 5 minutes with {self.extra_workers} extra workers = {p2} %')  
        if p3:
            print(f'% of clients attended by {self.extra_workers} extra workers = {p3} %')  

        p4 = p1-p2
        if p4>=0:
            print(f'''There are {p4} % less of the clients waiting more than 5 mins when employing extra workers.''')           
        else:
            print(f'''There are {-1*p4} % less of the clients waiting more than 5 mins when not employing extra workers.''')
        print('')

    def Data(self):
        print(f'Total clients attended with only two workers {self.total_attended_no_help}')
        print(f'Total clients attended with {self.extra_workers} more workers {self.total_attended_help}')
        print(f'Clients attended by {self.extra_workers} extra workers {self.attended_by_extra}')
        print('')