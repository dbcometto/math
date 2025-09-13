import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from datetime import datetime, timezone, timedelta

# Current UTC time
gps_epoch = datetime(1980, 1, 6, tzinfo=timezone.utc)

plt.ion()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

c = 3e8

my_pos = (1,0)

sat_pos = [(35e6,0),
           (0,37e6),
           (-39e6,0),
           (0,-22e6)]


clock_bias = 0.25
mx_st_dev = 10e-9



class receiver():

    def __init__(self, x0, y0, b0, var, _true_bias):
        self._true_bias = _true_bias

        self.x = np.array([x0,y0,b0])
        self.F = np.eye(3)
        self.P = np.diag([3.0, 3.0, 1.0])
        self.Q = np.zeros((3,3))
        self.R = np.diag([var]*3)
        self.H = np.eye(3)

    def calc_position(self,sat_pos,sat_times,max_iter=100,tol=1e-6):
        S = np.array(sat_pos)
        n = len(sat_pos)

        x = self.x[0]
        y = self.x[1]
        b = self.x[2]
        
        current_time = 0
        my_time = (current_time+self._true_bias) # faking bias
    
        

        for i in range(max_iter):
            pseudoranges = np.array([(my_time-t)*c for t in sat_times])
            dists = np.hypot(x-S[:,0],y-S[:,1])
            r = pseudoranges - (dists+b*c)

            H = np.zeros((n,3))
            H[:,0] = (x-S[:,0])/dists
            H[:,1] = (y-S[:,1])/dists
            H[:,2] = 1

            delta, *_ = np.linalg.lstsq(H,r,rcond=None)

            x += + delta[0]
            y += + delta[1]
            b += + delta[2]/c

            if np.linalg.norm(delta) < tol:
                return (x,y,b), True
            
        return (x,y,b), False

    def update_kf(self,sat_pos,sat_times):
        # Predict
        x_pred = self.F @ self.x
        P_pred = self.F @ self.P @ self.F.T + self.Q

        # Measure
        (x_meas,y_meas,b_meas), success = self.calc_position(sat_pos,sat_times)
        z = np.array([x_meas,y_meas,b_meas])

        if not success:
            print("Failed to converge!")

        # Update
        S = self.H @ P_pred @ self.H.T + self.R
        K = P_pred @ self.H.T @ np.linalg.inv(S)
        self.x = x_pred + K @ (z-x_pred)
        self.P = (np.eye(3) - K @ self.H) @ P_pred




x = 0
y = 0
b = 0


if __name__=="__main__":

    my_rx = receiver(0,0,0,(20e-9*c)**2,clock_bias)

    try:
        while True:
            # Set up (fake noise)

            current_time = 0
            sat_distance = [np.hypot(my_pos[0]-p[0],my_pos[1]-p[1]) for p in sat_pos]
            sat_times = [current_time-d/c + mx_st_dev*random.uniform(-1,1) for d in sat_distance]

            # calculation
            my_rx.update_kf(sat_pos,sat_times)

            print(f"Pos ({my_rx.x[0]:12.4f},{my_rx.x[1]:12.4f}) and bias {my_rx.x[2]:8.4f}")
            

            # Plotting
            ax1.cla()
            ax2.cla()

            # for d,p in zip(my_distances,sat_pos):
            #     circle = plt.Circle(p, d, fill=False, color='blue', linewidth=2)
            #     ax1.add_patch(circle)
            #     zcircle = plt.Circle(p, d, fill=False, color='blue', linewidth=2)
            #     ax2.add_patch(zcircle)

            ax1.plot(my_pos[0],my_pos[1],'o',color="#FF0000")
            ax1.plot(my_rx.x[0],my_rx.x[1],'x',color="#FF8800")
            ax1.add_patch(plt.Circle((my_rx.x[0],my_rx.x[1]), my_rx.P[1][1], fill=False, color='#FF8800', linewidth=2))


            lim = 5
            ax1.set_xlim(-lim, lim)
            ax1.set_ylim(-lim, lim)
            ax1.set_aspect('equal', adjustable='box')  # Keep it circular

            # zlim = 10
            # ax2.set_xlim(-zlim, zlim)   # Zoomed-in window
            # ax2.set_ylim(-zlim, zlim)
            # ax2.set_aspect('equal')

            plt.pause(0.01)

    except KeyboardInterrupt:
        print("Exiting")