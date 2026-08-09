from Cannon_Simulator import CannonSimulator
import buckets # Bucket maps and codes to try

# Constraints
VMIN = 5
VMAX = 25

# Selected code and map
bucket_map_choice = buckets.BUCKET_MAP_A
code_choice = buckets.CODE_A

# Find a solution to hitting each bucket in the playable area 
# If a code cannot be done, return a list of numbers that cannot
# be hit in the code. run_sim is expecting a list of velocities and launch angles
# in degrees. Note that metric units are used (m, s)
# HINT: Look at the simluator parameters to determine the accelerations
def cannon_code_breaker(bucket_map: dict[str, tuple[float, float]],
                        code: str) -> list[str]:

    simluator = CannonSimulator(bucket_map)
    launches = [(0.0, 0.0)] # You will need to edit this in this function
    
    ## Your code goes here!
    
    simluator.run_sim(launches, code)
    return []

def main():
    
    # Fire in the hole
    out_of_range_buckets = cannon_code_breaker(bucket_map_choice, code_choice)
    
    if len(out_of_range_buckets) != 0:
        print("Some buckets could not be reached: ")
        for bucket in out_of_range_buckets:
            print(f"\t{bucket}")
    

if __name__ == "__main__":
    main()