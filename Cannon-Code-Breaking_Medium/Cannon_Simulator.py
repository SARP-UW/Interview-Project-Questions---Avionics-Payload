import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as ani
from matplotlib import style
from matplotlib.patches import Circle, Rectangle
import time

# Simulation Parameters
#########################
GRAVITY = -9.8 # m/s^2
DT = 0.0001 #s 
TARGET_RADIUS = 0.25 #m
CANNON_WIDTH = 0.25 #m
CANNON_HEIGHT = 0.5 #m
CANNON_BASE_RADIUS = CANNON_WIDTH/2 #m
TARGET_NUMBER_FONT_SIZE = 6 
CANNON_BALL_RADIUS = CANNON_BASE_RADIUS/2
RENDER_EVERY_N_STEPS =  40
#########################


class CannonSimulator():
    
    def __init__(self,
                bucket_map: dict[str, tuple[float, float]],
                play_back_multiplier: float = 1, 
                cannon_pos: tuple[float, float] = (0,0), 
                plot_trajectory: bool = True,
                ay: float = GRAVITY, 
                ax: float = 0,
                dt: float = DT,
                target_radius: float = TARGET_RADIUS
                ):
        
        self.pbm = play_back_multiplier
        self.cannon_pos = cannon_pos
        self.bucket_map = bucket_map
        self.plot_trajectory = plot_trajectory
        self.ay = ay
        self.ax = ax
        self.dt = dt
        self.target_radius = target_radius
        
        # Start with blank cannon ball and cannon
        self.cannon_patch = None
        self.cannon_ball_patch = None
        
        # Target mapping
        self.failed_targets: dict[str, Circle] = {}
        self.succeeded_targets: dict[str, Circle]= {}
    
    # Computes one step in the projectile motion path
    # Returns a tuple the form of (new pos, new velo)
    def _compute_1D_step(self, 
                     dt: float, 
                     pos: float ,
                     vel: float, 
                     accel: float, 
                    ) -> tuple[float, float]:
        
        return (pos + vel * dt, vel + accel * dt)
        
        
    # Returns a dictionary of { 'pos' : (new x, new y), 'vel' : (new vx, new vy) }
    def _compute_2D_step(self, 
                        state: dict[str, tuple[float, float]]
                        )-> dict[str, tuple[float, float]]:
        
        x_state = self._compute_1D_step(self.dt, state['pos'][0], state['vel'][0], self.ax)
        y_state = self._compute_1D_step(self.dt, state['pos'][1], state['vel'][1], self.ay)
        
        return {
            'pos' : (x_state[0], y_state[0]),
            'vel' : (x_state[1], y_state[1])
        }
    
    # retruns true if the ball is within the target range
    def _hit_target(self, 
                        pos: tuple[float, float],
                        target: tuple[float, float], 
                        target_radius: float
                        ) -> bool:
        
        pos_x = pos[0]
        pos_y = pos[1]
        tar_x = target[0]
        tar_y = target[1]
        return np.sqrt((pos_x - tar_x)**2 + (pos_y - tar_y)**2 ) <= target_radius

    # returns true if the ball is below the target and out of the target successful range
    def _missed_target(self,
                       pos: tuple[float,float],
                       target: tuple[float, float],
                       target_radius: float
                       )-> bool:
    
        pos_x = pos[0]
        pos_y = pos[1]
        tar_x = target[0]
        tar_y = target[1]
        
        return (abs(pos_x) > abs(tar_x) + target_radius) and (pos_y < tar_y - target_radius)
    
    # Creates the base graph that all targets will be overlayed on
    def _create_base_graph(self):
        fig, ax = plt.subplots()
        ax.set_title("Cannon Ball Bucket Map")
        ax.set_xlabel("x distance (m)")
        ax.set_ylabel("y distance (m)")
        ax.grid(visible=True, alpha=0.3)

        x_max = max([abs(p[0]) for p in self.bucket_map.values()])
        y_max = max([abs(p[1]) for p in self.bucket_map.values()])
    
        pad = TARGET_RADIUS * 4
        ax.set_xlim(-x_max - pad, x_max + pad)
        ax.set_ylim(-y_max - pad, y_max+ pad)
        ax.set_aspect('equal', adjustable='box')  # avoid circles looking like ellipses

        cannon_base = Circle(self.cannon_pos, CANNON_BASE_RADIUS, color="brown")
        ax.add_patch(cannon_base)
        for pos in self.bucket_map:
            ax.text(*self.bucket_map[pos], pos, fontsize=TARGET_NUMBER_FONT_SIZE)
            target = Circle(self.bucket_map[pos], TARGET_RADIUS, color="red")
            ax.add_patch(target)          # <-- also note: this was missing too!
            self.failed_targets[pos] = target

        return fig, ax
    
    def _tally_targets(self):
        print("Targets hit")
        for target in self.succeeded_targets:
            print(target, end=" ")
        print("")
        print("Targets missed")
        for target in self.failed_targets:
            print(target, end=" ")
    
    # Runs a full simulation given a code, expects the velocities and launch angles as a list of
    # [(velocity, launch angle (deg))]
    def run_sim(self, 
                launch_conditions: list[tuple[float, float]],
                code: str
                ):
        
        # Check for launch conditions quality
        if len(launch_conditions) != len(code): 
            raise ValueError("Launch Conditions must be same length as the code")
        
        if self.plot_trajectory:
            # Enable Live Plotting
            plt.ion()
    
        print(f"Starting simulation: Cannon location X: {self.cannon_pos[0]} Y: {self.cannon_pos[1]}")
        
        if self.plot_trajectory:
            fig, ax = self._create_base_graph()
            pass
    
        step_count = 0
        
        for i in range(0, len(code), 1): 
            bucket_num = code[i]
            bucket_loc = self.bucket_map[bucket_num]

            initial_velo = launch_conditions[i][0]
            launch_angle = launch_conditions[i][1]
            
            print(f'Firing Shot Number {i+1}: vi = {initial_velo} m/s, angle = {launch_angle} deg')
            
            # initial state
            state = {
                'vel' : (initial_velo * np.cos(np.deg2rad(launch_angle)), initial_velo * np.sin(np.deg2rad(launch_angle))),
                'pos' : self.cannon_pos
            } 
            
            if self.plot_trajectory:
                x, y = [], [] # type: ignore
                line, = ax.plot([], [], label=f'Shot {i+1}', linestyle='--', color='orange') # type: ignore
                

            if self.plot_trajectory:
                if self.cannon_patch:
                    self.cannon_patch.remove()

                cannon_origin = (self.cannon_pos[0] - CANNON_WIDTH / 2, self.cannon_pos[1])

                self.cannon_patch = Rectangle(cannon_origin, CANNON_WIDTH, CANNON_HEIGHT,
                                            rotation_point=self.cannon_pos,   # pivot at bottom-center
                                            angle= 270 + launch_angle,
                                            linewidth=2, edgecolor="black", facecolor="grey")

                ax.add_patch(self.cannon_patch) # type: ignore

            while True:

                # Check break conditions
                if self._hit_target(state['pos'], bucket_loc, self.target_radius):
                    print(f"Target {i+1} hit!")
                    if self.plot_trajectory:
                        self.failed_targets[bucket_num].remove()
                        del self.failed_targets[bucket_num]

                        green_target = Circle(self.bucket_map[bucket_num], self.target_radius, color="green")
                        ax.add_patch(green_target)# type:ignore
                        self.succeeded_targets[bucket_num] = green_target

                    break

                if self._missed_target(state['pos'], bucket_loc, self.target_radius):
                    print(f"Target {i+1} missed.")
                    break

                # Step forward in time
                state = self._compute_2D_step(state)
                step_count += 1

                # Only touch the plot every N physics steps
                if self.plot_trajectory and step_count % RENDER_EVERY_N_STEPS == 0:
                    x.append(state['pos'][0])# type:ignore
                    y.append(state['pos'][1])# type:ignore
                    line.set_xdata(x)# type:ignore
                    line.set_ydata(y)# type:ignore

                    if self.cannon_ball_patch:
                        self.cannon_ball_patch.remove()

                    self.cannon_ball_patch = Circle(state['pos'], CANNON_BALL_RADIUS,
                                                    facecolor="darkgrey", edgecolor="black", linewidth=2)
                    ax.add_patch(self.cannon_ball_patch) # type:ignore

                    plt.pause(self.dt * RENDER_EVERY_N_STEPS / self.pbm)
        
        
        if self.plot_trajectory:
            plt.ioff()
            plt.show()
            

                
        