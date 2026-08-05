from Cannon_Simulator import CannonSimulator
import buckets # Bucket maps and codes to try
import math
import numpy as np

# Constraints
VMIN = 5
VMAX = 30

# Selected code and map
bucket_map = buckets.BUCKET_MAP_A
code = buckets.CODE_A

# Solves for the angle, only possible with no air resistance
def analytical_solution(dx, dy, v, ay) -> float:
    A = (ay * dx) / (2* v**2)
    inside = 1 - 4 * A * (A - (dy/dx))
    
    if inside <= 0: 
        return 0.0
    
    tana = (-1 + math.sqrt(inside)) / (2 * A)
    alpha = math.atan(tana)
    if dx <= 0: alpha += np.pi
    return np.rad2deg(alpha)

def brute_force_solution(dx, dy, ax, ay, velo):
    for alpha in range(0, 3600, 10):
        alpha = alpha / 10
        
        vx = velo * np.cos(np.deg2rad(alpha))
        vy = velo * np.sin(np.deg2rad(alpha))
        
        if vx == 0: continue
        
        inside = vx**2 + 2 * ax * dx
        if inside < 0: continue # imaginary number
        solns = [-vx/ax + np.sqrt(inside)/ax, -vx/ax - np.sqrt(inside)/ax]
        for soln in solns:
            if soln < 0: continue # negative time
            solved_dy = vy * soln + (1/2) * ay * soln**2
            if np.isclose(solved_dy, dy, atol=0.1):
                return alpha
            
    return None
        

# Find a solution to hitting each bucket in the playable area 
# If a code cannot be done, return a list of numbers that cannot
# be hit in the code 
def cannon_code_breaker(bucket_map: dict[str, tuple[float, float]],
                        code: str) -> list[str]:
    
    ay = -9.8
    ax = 0
    
    simulator = CannonSimulator(bucket_map, ax=ax)

    launches = []
    impossible_shots = []
    added_launch = False
    
    for idx in code:
        dx = bucket_map[idx][0]
        dy = bucket_map[idx][1]
        
        for velo100x in range(VMIN * 100, VMAX * 100 + 1, 1):
            velo = velo100x/100

            if ax == 0:
                alpha = analytical_solution(dx, dy, velo, ay)
                if alpha != 0:
                    launches.append((velo, alpha))
                    added_launch=True
                    break # Found a solution
            else:
                alpha = brute_force_solution(dx, dy, ax, ay, velo)
                if alpha:
                    launches.append((velo, alpha))
                    added_launch=True
                    break
        
        if not added_launch:
            impossible_shots.append(idx)
            launches.append((VMIN, 0)) # Keep the animation rolling
        
        added_launch=False
        
    
    simulator.run_sim(launches, code)
    
    return impossible_shots

def main():
    
    # Fire in the hole
    out_of_range_buckets = cannon_code_breaker(bucket_map, code)
    
    if len(out_of_range_buckets) != 0:
        print("Some buckets could not be reached: ")
        for bucket in out_of_range_buckets:
            print(f"\t{bucket}")
    

if __name__ == "__main__":
    main()