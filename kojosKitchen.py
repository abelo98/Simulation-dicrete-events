import numpy as np
import sys
from numpy.random.mtrand import uniform
from fractions import Fraction
from Stats import Statistics
from Console import Show

class Kitchen:
    def __init__(self, extra_workers,lambda_arrive,lambda_rush):
        self.simulation_time = 11*60 # 11 hours open and 60 min per hour
        self.lambda_arrive = lambda_arrive
        self.lambda_rush = lambda_rush

        # extra workers for the rush time
        self.extra_workers = extra_workers
        self.exceded_time = 0
        self.attended_by_extra = 0

        self.__Initialization()


    def __Initialization(self):
        self.time_line = self.N_a = 0
        self.people_in_syst = 0
        self.N_d = 0 
        self.Arrivals = {}
        self.Departures = {}
        self.t_d = []
        
        # in the first pos. the number of free services, then the services.
        self.all_services = [] 
        for _ in range(2+self.extra_workers):
            self.all_services.append([])
            self.t_d.append(sys.maxsize)
        self.t_a = self.ExpGeneration(self.lambda_arrive)
      
    def __InRushHour(self):
       return 90 < self.t_a < 210 or 420 < self.t_a < 540
        

    def UnifGeneration(self,a,b):
        return a + (b - a) * uniform(0,1)

    def ExpGeneration(self,l):
        return -(1/l) * np.log(uniform(0,1))

    def Order(self):
        p = uniform(0,1)
        if p < 0.5:
            return 1
        
        return 0

    # The client selects the line where there is less people
    def __Selectline(self):
        r = 0 if len(self.all_services[0]) <= len(self.all_services[1]) else 1

        if self.__InRushHour() and self.extra_workers > 0:
            min_qty = sys.maxsize
            for i in range(len(self.all_services)):
                curr_qty = len(self.all_services[i])
                if curr_qty < min_qty:
                    min_qty = curr_qty
                    r = i
        if r > 1:
            self.attended_by_extra+=1
        return r
        
    def __UpdateQueue(self,service,id):
        l = self.__Selectline()
        if len(self.all_services[l]) == 0: 
            if service:
                self.t_d[l] = self.time_line + self.UnifGeneration(5,8)
            else:
                self.t_d[l] = self.time_line + self.UnifGeneration(3,5)              

        self.all_services[l].append((id,service)) 

    
    def __ClientArrival(self):
        if min(min(self.t_d),self.t_a) == self.t_a and \
                self.t_a <= self.simulation_time:

            self.time_line = self.t_a
            self.N_a += 1
            self.people_in_syst += 1

            self.Arrivals[self.N_a] = self.time_line
            lamb = self.lambda_rush if self.__InRushHour() else self.lambda_arrive
            self.t_a = self.time_line + self.ExpGeneration(lamb) 
            o = self.Order()    
            self.__UpdateQueue(o,self.N_a)
        
    def __NextOut(self):
        m = min(self.t_d)
        index = self.t_d.index(m)
        return index, m

    def __DispatchClient(self,line_client):
        if len(self.all_services[line_client]) == 1:
            self.t_d[line_client] = sys.maxsize 
        else:    
            _,next_service = self.all_services[line_client][1]
            if next_service:
                self.t_d[line_client] = self.UnifGeneration(5,8) + self.time_line
            else:
                self.t_d[line_client] = self.UnifGeneration(3,5) + self.time_line

        self.all_services[line_client].pop(0) # one client out
        time_waiting = self.Departures[self.N_d] - self.Arrivals[self.N_d]

        if time_waiting > 5:
            self.exceded_time += 1 

    def __ClientDeparture(self):
        line_number,td = self.__NextOut()

        if min(td,self.t_a) == td and td <= self.simulation_time:
            self.time_line = td
            self.people_in_syst-=1
            self.N_d += 1
            self.Departures[self.N_d] = self.time_line
            self.__DispatchClient(line_number)

    def __Closing(self):
        while self.people_in_syst > 0:
            line_number,td = self.__NextOut()
            self.time_line = td

            self.people_in_syst -= 1
            
            self.N_d += 1
            self.Departures[self.N_d] = self.time_line
            self.__DispatchClient(line_number)
        
    def SimulateEvents(self):
        while self.t_a < self.simulation_time:
            self.__ClientArrival()
            self.__ClientDeparture()
        self.__Closing()

        return self.exceded_time

def main(simulations,extra_workers,arrive_lambda,rush_lambda):
    oldstdout = sys.stdout
    sys.stdout = open('output.txt', 'w')

    print(f'******* Statistics after {simulations} simulations(days) *******\n')

    for l in range(len(arrive_lambda)):
        st = Statistics(extra_workers,simulations)
        for i in range(2):
            w = extra_workers if i else 0
            for j in range(simulations):
                sim_Kujos = Kitchen(w,arrive_lambda[l],rush_lambda[l])
                sim_Kujos.SimulateEvents()

                if i:
                    st.total_attended_help += sim_Kujos.N_a
                    st.exceded_time_help += sim_Kujos.exceded_time 
                    st.attended_by_extra += sim_Kujos.attended_by_extra
                   
                else:
                    st.total_attended_no_help += sim_Kujos.N_a
                    st.exceded_time_no_help += sim_Kujos.exceded_time 
                   
        
        la = Fraction(arrive_lambda[l]).limit_denominator()
        lr = Fraction(rush_lambda[l]).limit_denominator() 
        print(f'lambda of arrives = {la} and lambda of rush hour = {lr}\n')
        st.Data()
        st.GetMedia()
        st.GetPercent()
    t = 'output.txt'
    sys.stdout = oldstdout
    print(f'Finished simulations. See file:{t}')

if __name__=="__main__":
    c = Show()
    simulations,workers,la,lr =  c.start()
    main(simulations,workers,la,lr)



