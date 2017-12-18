import numpy as np

class Main():

    lambd = 0.4
    mu = 0.04
    t = float(input("введите время в секундах"))
    M=0
    N=0
    x = 0
    y = 0
    def get_ksi(self,i):
        ksi = np.random.uniform(0,1,i)
        return ksi

    def exp_rapr(self,i,j,t):
        ksi = self.get_ksi(self, t)
        delta_t = - (1/self.lambd) * np.log(1 - ksi[i])
        delta_tau = -(1/self.mu) * np.log(1 - ksi[j])
        return delta_t, delta_tau

    def get_time(self, N):
        time = 0
        for i in range(N):
            delta_t, delta_tau = self.exp_rapr(self, i ,i, N)
            time = time + delta_t
        return time

    def smo(self):
        timer=0
        moment_t=0
        self.N=1
        self.M=1
        while timer < self.t:
            delta_t, delta_tau = self.exp_rapr(self,self.N, self.M, int(self.t))
            timer = timer + delta_t
            self.N=self.N+1
            moment_t=moment_t+delta_t
            if moment_t>=delta_tau:
                self.M=self.M+1
                moment_t=0

        print("количество заявок = " +str(self.N))
        print("количество обработанных заявок = " + str(self.M))
        return self.M/self.N, self.N

    def pogr(self):
        eps = 0.01
        p, N = self.smo(self)
        alpha = 3
        eps_s = alpha*np.sqrt(p*(1 - p)/N)
        if eps_s>eps:
            NT = (alpha**2 * p*(1-p))/(eps**2)
            return int(NT), 1,eps_s
        else:
            NT = (alpha ** 2 * p * (1 - p)) / (eps ** 2)
            return int(NT), 0,eps_s

    def print_result(self):
        while True:
            NT, flag, eps_s = self.pogr(self)
            if flag == 1:
                time = self.get_time(self,NT)
                print("при полученном количестве заявок за время = " \
                      + str(int(self.t)) + " , погрешность будет больше 0.01 " \
                      + " рекомендуется провести моделирование в период = " + str(time) + " секунд")

            else:
                time = self.get_time(self, NT)
                print("при полученном количестве заявок за время = " \
                      + str(int(self.t)) + " , погрешность будет меньше 0.01 " \
                      + " рекомендуется провести моделирование в период = " + str(time) + " секунд")

            print("погрешность = " + str(eps_s))
            print("требуемое количество заявок = " + str(NT))
            print()

            qu = input( "если хотите закончить моделирование, введите q" )
            if qu == 'q':
                break

            self.t = float(input( "введите новый период времени моделирования" ))



Main.print_result(Main)
