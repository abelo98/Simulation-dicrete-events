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
        print(f'''Each day around {round(m1-m2)} more clients wait more than 5 minutes when there aren't extra workers''')
        

        print('')

    def GetPercent(self):
        p1 = (self.exceded_time_no_help*100)/self.total_attended_no_help
        p2 = (self.exceded_time_help*100)/self.total_attended_help
        p3 = (self.attended_by_extra*100)/self.total_attended_help

        print(f'% clients waiting more than 5 minutes with only two workers = {p1} %')
        print(f'% clients waiting more than 5 minutes with {self.extra_workers} extra workers = {p2} %')  
        if p3:
            print(f'% of clients attended by {self.extra_workers} extra workers = {p3} %')  

        print(f'''There are {p1-p2} % less of the clients waiting more than 5 mins when employing extra workers.''')
        print('')

    def Data(self):
        print(f'Total clients attended with only two workers {self.total_attended_no_help}')
        print(f'Total clients attended with {self.extra_workers} more workers {self.total_attended_help}')
        print(f'Clients attended by {self.extra_workers} extra workers {self.attended_by_extra}')
        print('')