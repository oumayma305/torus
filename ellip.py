 import math
    import pylab as pl
    import matplotlib.patches as pt
    class billiard_collision_ellipse:

        def __init__(self, x = 0.6, y = 0.8, vx = 2, vy = 4, a = 7, b = 1, total_time = 100):
            self.a = a
            self.b = b
            self.x = [x]
            self.y = [y]
            self.vx = vx
            self.vy = vy
            self.v = [vx, vy]
            self.ps_x = []
            self.ps_vx = []
            self.total_road = total_time * math.hypot(vx, vy)
            self.passed_road = [0]
            self.kr = 0

        def vdp(a, b):
            return(a[0] * b[0] + a[1] * b[1])

        def vsub(a, b):
            return([a[0] - b[0], a[1] - b[1]])
    
        def vsm(a, b):
            return([a * b[0], a * b[1]])

        def n_cal(self):
                if self.x[-1] > 0:
                    return([-1 / math.sqrt(self.kr**2 + 1), -self.kr / math.sqrt(self.kr**2 + 1)])
                else:
                    return([1 / math.sqrt(self.kr**2 + 1), self.kr / math.sqrt(self.kr**2 + 1)])

        def calculate(self):
                loop_calculate = True
                while(loop_calculate):#Ne considère pas le cas où la vitesse est perpendiculaire à l'axe des x
                k = self.v[1] / self.v[0]
                m = self.y[-1] - self.x[-1] * k
                temp_vx = self.v[0]
                while(True):
                    #Lorsque la composante latérale de la vitesse est supérieure à zéro
                    if self.v[0] > 0:
                        self.x.append((-k * m * self.a**2 + self.a * self.b * math.sqrt(k**2 * self.a**2 - m**2 + self.b**2)) / (self.a**2 * k**2 + self.b**2))
                        self.y.append((self.b**2 * m + k * self.a * self.b * math.sqrt(k**2 * self.a**2 - m**2 + self.b**2)) / (self.a**2 * k**2 + self.b**2))
                        break
                    #Lorsque la composante latérale de la vitesse est inférieure à zéro
                    else:
                        self.x.append((-k * m * self.a**2 - self.a * self.b * math.sqrt(k**2 * self.a**2 - m**2 + self.b**2)) / (self.a**2 * k**2 + self.b**2))
                        self.y.append((self.b**2 * m - k * self.a * self.b * math.sqrt(k**2 * self.a**2 - m**2 + self.b**2)) / (self.a**2 * k**2 + self.b**2))
                        break

                        def show_result(self):
            fig = pl.figure()
            pl.title('Trajectory of a billiard on a elliptic table', fontsize=20)
            pl.xlabel('x', fontsize=20)
            pl.ylabel('y', fontsize=20)
            ax = fig.add_subplot(111)
            ellipse1 = pt.Ellipse(xy = (0, 0), width=2*self.a, height=2*self.b, fill = False)#Le premier paramètre est les coordonnées du centre du cercle, le second est le rayon et le troisième est la transparence(0-1)
            ax.add_patch(ellipse1)
            pl.xlim(-self.a, self.a)
        pl.ylim(-self.b, self.b)
        pl.plot(self.x, self.y)
        pl.plot(self.x[0], self.y[0], 'o')
        pl.show()
        
        
    def show_result_ps(self):
    pl.title('Poincare section $v_x$ versus x', fontsize=20)
    pl.xlabel('x', fontsize=20)
    pl.ylabel('$v_x$', fontsize=20)
    pl.xlim(-self.a, self.a)
    pl.ylim(-math.hypot(self.vx, self.vy), math.hypot(self.vx, self.vy))
    pl.plot(self.ps_x, self.ps_vx, '.')
    pl.show()
    pl.savefig('graph.png')


    def my_plot():
        num_str_in = input("Veuillez saisir les coordonnées horizontales et verticales x, y de la position initiale de la balle, les composantes horizontale et verticale vx, vy de la vitesse initiale de la balle, les demi-axes a et b de la longueur de l'ellipse et la durée t du mouvement, séparés par des espaces:\n")
        num = [float(n) for n in num_str_in.split()]
        x = num[0]
        y = num[1]
        vx = num[2]
        vy = num[3]
        a = num[4]
        b = num[5]
        total_time = num[6]
        start = billiard_collision_ellipse(x, y, vx, vy, a, b, total_time)
        start.calculate()
        start.show_result()
        start.show_result_ps()

